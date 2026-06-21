from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import Prediction, User
from backend.app.schemas.prediction import PredictionCreate, PredictionResponse
from backend.app.services.disease_predictor import DiseasePredictor
from typing import List
import logging

router = APIRouter(prefix="/predictions", tags=["Predictions"])
logger = logging.getLogger(__name__)

predictor = DiseasePredictor()

@router.post("/", response_model=PredictionResponse, status_code=status.HTTP_201_CREATED)
async def create_prediction(
    prediction: PredictionCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    """Create new prediction"""
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Get predictions from ML model
    try:
        predictions_data = predictor.predict(prediction.symptoms_input)
        top_5 = predictions_data.get("top_5", [])
        confidence_scores = predictions_data.get("confidence_scores", {})
        risk_level = predictions_data.get("risk_level", "low")
        explanation = predictions_data.get("explanation", "")
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error generating predictions"
        )
    
    # Save prediction to database
    db_prediction = Prediction(
        user_id=user_id,
        symptoms_input=prediction.symptoms_input,
        top_5_predictions=top_5,
        confidence_scores=confidence_scores,
        risk_level=risk_level,
        explanation=explanation,
        language=prediction.language
    )
    
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    
    return db_prediction

@router.get("/user/{user_id}", response_model=List[PredictionResponse])
async def get_user_predictions(user_id: int, db: Session = Depends(get_db)):
    """Get all predictions for a user"""
    predictions = db.query(Prediction).filter(Prediction.user_id == user_id).all()
    return predictions

@router.get("/{prediction_id}", response_model=PredictionResponse)
async def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    """Get prediction by ID"""
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
    if not prediction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prediction not found"
        )
    return prediction
