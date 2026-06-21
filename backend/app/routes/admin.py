from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import User, Doctor
import logging

router = APIRouter(prefix="/admin", tags=["Admin"])
logger = logging.getLogger(__name__)

@router.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
    """Get all users (admin only)"""
    users = db.query(User).all()
    return {
        "total": len(users),
        "users": users
    }

@router.get("/doctors")
async def get_all_doctors(db: Session = Depends(get_db)):
    """Get all doctors (admin only)"""
    doctors = db.query(Doctor).all()
    return {
        "total": len(doctors),
        "doctors": doctors
    }

@router.post("/doctors/{doctor_id}/verify")
async def verify_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """Verify doctor (admin only)"""
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )
    
    doctor.verified = True
    db.commit()
    
    logger.info(f"Doctor verified: {doctor_id}")
    return {"status": "success", "message": "Doctor verified successfully"}

@router.post("/users/{user_id}/deactivate")
async def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    """Deactivate user (admin only)"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user.is_active = False
    db.commit()
    
    logger.info(f"User deactivated: {user_id}")
    return {"status": "success", "message": "User deactivated successfully"}

@router.get("/analytics")
async def get_analytics(db: Session = Depends(get_db)):
    """Get system analytics (admin only)"""
    total_users = db.query(User).count()
    total_doctors = db.query(Doctor).count()
    
    return {
        "total_users": total_users,
        "total_doctors": total_doctors,
        "timestamp": "now()"
    }
