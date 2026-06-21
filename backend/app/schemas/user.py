from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """User creation schema"""
    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: str = Field(default="patient", regex="^(patient|doctor|admin)$")

class UserLogin(BaseModel):
    """User login schema"""
    username: str
    password: str

class UserResponse(BaseModel):
    """User response schema"""
    id: int
    username: str
    email: str
    role: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
