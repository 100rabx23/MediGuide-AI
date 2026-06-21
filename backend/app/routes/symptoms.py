from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import Symptom
from backend.app.schemas.symptom import SymptomCreate, SymptomResponse
from typing import List
import logging

router = APIRouter(prefix="/symptoms", tags=["Symptoms"])
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[SymptomResponse])
async def get_symptoms(db: Session = Depends(get_db)):
    """Get all symptoms"""
    symptoms = db.query(Symptom).all()
    return symptoms

@router.get("/{symptom_id}", response_model=SymptomResponse)
async def get_symptom(symptom_id: int, db: Session = Depends(get_db)):
    """Get symptom by ID"""
    symptom = db.query(Symptom).filter(Symptom.id == symptom_id).first()
    if not symptom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Symptom not found"
        )
    return symptom

@router.post("/", response_model=SymptomResponse, status_code=status.HTTP_201_CREATED)
async def create_symptom(symptom: SymptomCreate, db: Session = Depends(get_db)):
    """Create new symptom"""
    db_symptom = Symptom(**symptom.dict())
    db.add(db_symptom)
    db.commit()
    db.refresh(db_symptom)
    return db_symptom

@router.get("/search/{query}")
async def search_symptoms(query: str, db: Session = Depends(get_db)):
    """Search symptoms by name or description"""
    symptoms = db.query(Symptom).filter(
        (Symptom.name.ilike(f"%{query}%")) | 
        (Symptom.description.ilike(f"%{query}%"))
    ).all()
    return symptoms
