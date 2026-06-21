from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PatientCreate(BaseModel):
    """Patient creation schema"""
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0, le=150)
    gender: str = Field(..., regex="^(male|female|other)$")
    blood_group: Optional[str] = None
    medical_history: Optional[str] = None
    allergies: Optional[str] = None
    current_medications: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientUpdate(BaseModel):
    """Patient update schema"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    medical_history: Optional[str] = None
    allergies: Optional[str] = None
    current_medications: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientResponse(BaseModel):
    """Patient response schema"""
    id: int
    user_id: int
    first_name: str
    last_name: str
    age: int
    gender: str
    blood_group: Optional[str]
    medical_history: Optional[str]
    allergies: Optional[str]
    current_medications: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
