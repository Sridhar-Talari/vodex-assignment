"""
Pydantic models for item-related operations.
"""
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class ItemBase(BaseModel):
    """
    Base model for common item fields.
    """
    name: Optional[str] = None
    email: Optional[str] = None
    item_name: Optional[str] = None
    quantity: Optional[int] = Field(None, gt=0, description="Quantity must be greater than zero")
    expiry_date: Optional[str] = None

    @validator('expiry_date', pre=True, always=True)
    def validate_expiry_date(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d').date().strftime('%Y-%m-%d')
            except ValueError:
                raise ValueError("expiry_date must be in YYYY-MM-DD format")
        return value.strftime('%Y-%m-%d') if isinstance(value, datetime) else value

class ItemModel(ItemBase):
    """
    Pydantic model for creating a new item.
    """
    name: str
    email: str
    item_name: str
    expiry_date: str  # Ensure it's required in this model

class ItemResponseModel(ItemBase):
    """
    Response model for an item entity.
    """
    id: str
    insert_date: str

class ItemUpdateModel(ItemBase):
    """
    Pydantic model for updating an item entity.
    """
    pass

class ItemAggregationResponseModel(BaseModel):
    """
    Response model for item aggregation results.
    """
    email: str
    count: int