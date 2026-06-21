from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReportCreate(BaseModel):
    """Report creation schema"""
    prediction_id: int
    title: str = Field(..., max_length=200)
    recommendations: str

class ReportResponse(BaseModel):
    """Report response schema"""
    id: int
    patient_id: int
    prediction_id: int
    doctor_id: Optional[int]
    title: str
    content: str
    recommendations: str
    risk_assessment: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
