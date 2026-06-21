from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class DoctorCreate(BaseModel):
    """Doctor creation schema"""
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    license_number: str = Field(..., max_length=100)
    specialization: str = Field(..., max_length=100)
    phone: str
    clinic_name: Optional[str] = None
    clinic_address: Optional[str] = None

class DoctorResponse(BaseModel):
    """Doctor response schema"""
    id: int
    user_id: int
    first_name: str
    last_name: str
    license_number: str
    specialization: str
    phone: str
    clinic_name: Optional[str]
    clinic_address: Optional[str]
    verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
