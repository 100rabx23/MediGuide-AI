from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import Doctor, Report, User
from backend.app.schemas.doctor import DoctorCreate, DoctorResponse
from typing import List
import logging

router = APIRouter(prefix="/doctor", tags=["Doctor"])
logger = logging.getLogger(__name__)

@router.post("/register", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
async def register_doctor(doctor: DoctorCreate, user_id: int, db: Session = Depends(get_db)):
    """Register doctor profile"""
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if doctor already exists
    db_doctor = db.query(Doctor).filter(Doctor.license_number == doctor.license_number).first()
    if db_doctor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Doctor with this license number already exists"
        )
    
    # Create doctor profile
    db_doctor = Doctor(**doctor.dict(), user_id=user_id)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    
    logger.info(f"Doctor registered: {doctor.license_number}")
    return db_doctor

@router.get("/profile/{doctor_id}", response_model=DoctorResponse)
async def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """Get doctor profile"""
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )
    return doctor

@router.get("/reports/{doctor_id}", response_model=List)
async def get_doctor_reports(doctor_id: int, db: Session = Depends(get_db)):
    """Get all reports assigned to doctor"""
    reports = db.query(Report).filter(Report.doctor_id == doctor_id).all()
    return reports

@router.put("/{report_id}/review")
async def review_report(report_id: int, observations: str, db: Session = Depends(get_db)):
    """Doctor reviews and adds observations to a report"""
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    
    report.doctor_observations = observations
    report.status = "reviewed"
    db.commit()
    
    logger.info(f"Report reviewed: {report_id}")
    return {"status": "success", "message": "Report reviewed successfully"}
