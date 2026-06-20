from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api/v1/predictions", tags=["predictions"])

class PredictionRequest(BaseModel):
    symptoms: List[str]

class PredictionItem(BaseModel):
    rank: int
    disease_name: str
    confidence_score: float
    risk_level: str

class PredictionResponse(BaseModel):
    message: str
    predictions: List[PredictionItem]
    overall_risk_level: str
    disclaimer: str

@router.post("/predict", status_code=status.HTTP_200_OK, response_model=dict)
async def predict_diseases(request: PredictionRequest):
    """Predict possible diseases from symptoms"""
    return {
        "message": "Disease prediction completed",
        "predictions": [
            {
                "rank": 1,
                "disease_name": "Model Training Required",
                "confidence_score": 0.0,
                "risk_level": "pending"
            }
        ],
        "overall_risk_level": "unknown",
        "disclaimer": "⚠️ These are predictive estimates only, NOT medical diagnoses. Always consult a healthcare professional."
    }

@router.get("/explanation/{prediction_id}")
async def get_prediction_explanation(prediction_id: int):
    """Get explanation for a specific prediction"""
    return {
        "prediction_id": prediction_id,
        "explanation": "Awaiting model training",
        "symptoms_contributing": [],
        "confidence_details": {}
    }

@router.get("/disease/{disease_name}")
async def get_disease_info(disease_name: str):
    """Get detailed information about a disease"""
    return {
        "disease_name": disease_name,
        "symptoms": [],
        "treatments": [],
        "prevention": [],
        "when_to_see_doctor": ""
    }

@router.post("/batch-predict")
async def batch_predict(symptom_lists: List[List[str]]):
    """Batch predict for multiple symptom lists"""
    return {
        "message": "Batch prediction completed",
        "results": []
    }
