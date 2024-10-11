"""
API router for item-related operations.
"""

from fastapi import APIRouter, HTTPException
from app.models.items import ItemModel, ItemUpdateModel, ItemResponseModel, ItemAggregationResponseModel
from app.lib.db import DB
from datetime import datetime, date
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemResponseModel)
async def create_item(item: ItemModel):
    """
    Create a new item in the database.
    """
    if DB is None:
        raise HTTPException(status_code=500, detail="Database connection not established")
    item_data = item.dict()
    item_data['insert_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Automatically set the insert date
    result = DB["items"].insert_one(item_data)
    item_data['id'] = str(result.inserted_id)
    return ItemResponseModel(**item_data)

@router.get("/filter", response_model=List[ItemResponseModel])
async def filter_items(email: str = None, expiry_date: date = None, 
                        insert_date: date = None, quantity: int = None):
    """
    Filter items based on various criteria.
    """
    query = {}
    if email:
        query['email'] = email
    if expiry_date:
        query['expiry_date'] = {'$gt': expiry_date.strftime("%Y-%m-%d")}
    if insert_date:
        query['insert_date'] = {'$gt': insert_date.strftime("%Y-%m-%d")}
    if quantity:
        query['quantity'] = {'$gte': quantity}

    items = list(DB["items"].find(query))
    for item in items:
        item['id'] = str(item['_id'])
    return [ItemResponseModel(**item) for item in items]

@router.get("/aggregation", response_model=List[ItemAggregationResponseModel])
async def aggregate_items():
    """
    Aggregate items to count them grouped by email.
    """
    aggregation = DB["items"].aggregate([
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ])
    return [{"email": item["_id"], "count": item["count"]} for item in aggregation]

@router.get("/{id}", response_model=ItemResponseModel)
async def get_item(id: str):
    """
    Retrieve an item by its ID.
    """
    item = DB["items"].find_one({"_id": ObjectId(id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item['id'] = str(item['_id'])
    return ItemResponseModel(**item)

@router.put("/{id}", response_model=ItemResponseModel)
async def update_item(id: str, item: ItemUpdateModel):
    """
    Update an item's details by ID (excluding the Insert Date).
    """
    update_data = item.dict(exclude_unset=True)
    result = DB["items"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    # Get the updated item to return
    updated_item = DB["items"].find_one({"_id": ObjectId(id)})
    updated_item['id'] = str(updated_item['_id'])
    return ItemResponseModel(**updated_item)

@router.delete("/{id}", response_model=dict)
async def delete_item(id: str):
    """
    Delete an item based on its ID.
    """
    result = DB["items"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
