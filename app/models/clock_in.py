"""
Pydantic models for clock-in related operations.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClockInModel(BaseModel):
    """
    Pydantic model for a clock-in entity.
    """
    email: str
    location: str

class ClockInResponseModel(ClockInModel):
    """
    Response model for a clock-in entity.
    """
    id: str
    insert_datetime: datetime

class ClockInUpdateModel(ClockInModel):
    """
    Pydantic model for updating a clock-in entity.
    """
    email: Optional[str] = None
    location: Optional[str] = None