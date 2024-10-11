"""
API router for clock-in related operations.
"""

from fastapi import APIRouter, HTTPException
from app.models.clock_in import ClockInModel, ClockInResponseModel, ClockInUpdateModel
from app.lib.db import DB
from bson import ObjectId
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/clock-in", tags=["Clock In"])

@router.post("/", response_model=ClockInResponseModel)
async def create_clock_in(clock_in: ClockInModel):
    """
    Create a new clock-in record in the database.
    """
    if DB is None:
        raise HTTPException(status_code=500, detail="Database connection not established")
    clock_in_data = clock_in.dict()
    clock_in_data['insert_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = DB["clock_in"].insert_one(clock_in_data)
    clock_in_data['id'] = str(result.inserted_id)
    return ClockInResponseModel(**clock_in_data)

@router.get("/filter", response_model=List[ClockInResponseModel])
async def filter_clock_ins(email: Optional[str] = None, 
                            location: Optional[str] = None,
                            insert_datetime: Optional[datetime] = None):
    """
    Filter clock-in records based on various criteria.
    """
    query = {}
    if email:
        query['email'] = email
    if location:
        query['location'] = location
    if insert_datetime:
        query['insert_datetime'] = {'$gt': insert_datetime.strftime("%Y-%m-%d %H:%M:%S")}

    clock_ins = list(DB["clock_in"].find(query))
    for clock_in in clock_ins:
        clock_in['id'] = str(clock_in['_id'])

    return [ClockInResponseModel(**clock_in) for clock_in in clock_ins]

@router.get("/{id}", response_model=ClockInResponseModel)
async def get_clock_in(id: str):
    """
    Retrieve a clock-in record by its ID.
    """
    clock_in = DB["clock_in"].find_one({"_id": ObjectId(id)})
    if not clock_in:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    clock_in['id'] = str(clock_in['_id'])
    return ClockInResponseModel(**clock_in)

@router.put("/{id}", response_model=ClockInResponseModel)
async def update_clock_in(id: str, clock_in: ClockInUpdateModel):
    """
    Update a clock-in record by ID.
    """
    update_data = clock_in.dict(exclude_unset=True)
    result = DB["clock_in"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")

    # Get the updated clock-in to return
    updated_clock_in = DB["clock_in"].find_one({"_id": ObjectId(id)})
    updated_clock_in['id'] = str(updated_clock_in['_id'])
    return ClockInResponseModel(**updated_clock_in)

@router.delete("/{id}", response_model=dict)
async def delete_clock_in(id: str):
    """
    Delete a clock-in record based on its ID.
    """
    result = DB["clock_in"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"detail": "Clock-in record deleted"}
