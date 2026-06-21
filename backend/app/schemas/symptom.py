from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class SymptomCreate(BaseModel):
    """Symptom creation schema"""
    name: str = Field(..., max_length=100)
    description: str
    category: str
    severity_levels: Optional[List[str]] = None
    related_symptoms: Optional[List[str]] = None

class SymptomResponse(BaseModel):
    """Symptom response schema"""
    id: int
    name: str
    description: str
    category: str
    severity_levels: Optional[List[str]]
    related_symptoms: Optional[List[str]]
    created_at: datetime
    
    class Config:
        from_attributes = True
