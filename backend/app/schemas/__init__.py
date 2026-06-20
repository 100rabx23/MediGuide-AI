"""Pydantic schemas for request/response validation"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: str
    username: str
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Symptom Schemas
class SymptomBase(BaseModel):
    symptom_name: str
    description: Optional[str] = None
    severity: str = "moderate"

class SymptomCreate(SymptomBase):
    patient_id: int
    duration: str

class SymptomResponse(SymptomBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Prediction Schemas
class PredictionResponse(BaseModel):
    disease_name: str
    confidence_score: float
    rank: int
    risk_level: str
    explanation: Optional[str] = None

# Report Schemas
class ReportBase(BaseModel):
    symptoms_summary: str
    predictions_summary: Optional[str] = None
    recommendations: Optional[str] = None
    risk_assessment: Optional[str] = None

class ReportCreate(ReportBase):
    patient_id: int

class ReportResponse(ReportBase):
    id: int
    user_id: int
    report_type: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Chat Schemas
class ChatMessage(BaseModel):
    user_message: str
    topic: Optional[str] = None

class ChatResponse(ChatMessage):
    assistant_response: str
    created_at: datetime
