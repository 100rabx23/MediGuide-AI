from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class PredictionCreate(BaseModel):
    """Prediction creation schema"""
    symptoms_input: str = Field(..., min_length=3)
    language: str = Field(default="en", regex="^(en|hi|gu)$")

class PredictionResponse(BaseModel):
    """Prediction response schema"""
    id: int
    user_id: int
    symptoms_input: str
    top_5_predictions: List[str]
    confidence_scores: Dict[str, float]
    risk_level: str
    explanation: str
    language: str
    created_at: datetime
    
    class Config:
        from_attributes = True
