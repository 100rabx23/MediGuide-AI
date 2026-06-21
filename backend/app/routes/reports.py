from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import Report, Prediction, Patient
from backend.app.schemas.report import ReportCreate, ReportResponse
from backend.app.services.report_generator import ReportGenerator
from typing import List
import logging

router = APIRouter(prefix="/reports", tags=["Reports"])
logger = logging.getLogger(__name__)

report_gen = ReportGenerator()

@router.post("/", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
async def create_report(report: ReportCreate, db: Session = Depends(get_db)):
    """Create new report"""
    # Verify prediction exists
    prediction = db.query(Prediction).filter(Prediction.id == report.prediction_id).first()
    if not prediction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prediction not found"
        )
    
    # Get patient
    patient = db.query(Patient).filter(Patient.user_id == prediction.user_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    
    # Create report in database
    db_report = Report(
        patient_id=patient.id,
        prediction_id=prediction.id,
        title=report.title,
        content=report.recommendations,
        recommendations=report.recommendations,
        risk_assessment=""
    )
    
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    
    logger.info(f"Report created: {db_report.id}")
    return db_report

@router.get("/patient/{patient_id}", response_model=List[ReportResponse])
async def get_patient_reports(patient_id: int, db: Session = Depends(get_db)):
    """Get all reports for a patient"""
    reports = db.query(Report).filter(Report.patient_id == patient_id).all()
    return reports

@router.get("/{report_id}", response_model=ReportResponse)
async def get_report(report_id: int, db: Session = Depends(get_db)):
    """Get report by ID"""
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    return report

@router.post("/{report_id}/download")
async def download_report(report_id: int, db: Session = Depends(get_db)):
    """Download report as PDF"""
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    
    try:
        pdf_path = report_gen.generate_pdf(report)
        return {"pdf_path": pdf_path, "status": "success"}
    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error generating PDF"
        )
