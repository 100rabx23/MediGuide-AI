from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api/v1/admin", tags=["admin"])

class UserStats(BaseModel):
    total_users: int
    total_patients: int
    total_doctors: int
    total_admins: int

class AnalyticsData(BaseModel):
    daily_reports: int
    top_diseases: List[str]
    avg_confidence: float

@router.get("/dashboard")
async def get_admin_dashboard():
    """Get admin dashboard statistics"""
    return {
        "total_users": 0,
        "total_patients": 0,
        "total_doctors": 0,
        "total_reports": 0,
        "active_sessions": 0
    }

@router.get("/analytics")
async def get_analytics(days: Optional[int] = 7):
    """Get system analytics"""
    return {
        "message": "Analytics data",
        "period_days": days,
        "daily_reports": 0,
        "top_diseases": [],
        "user_growth": [],
        "system_health": "healthy"
    }

@router.get("/users")
async def list_users(skip: int = 0, limit: int = 100):
    """List all users"""
    return {
        "users": [],
        "total": 0,
        "skip": skip,
        "limit": limit
    }

@router.get("/users/{user_id}")
async def get_user_details(user_id: int):
    """Get user details"""
    return {
        "user_id": user_id,
        "user_data": {}
    }

@router.post("/users/{user_id}/activate")
async def activate_user(user_id: int):
    """Activate user account"""
    return {"message": "User activated successfully"}

@router.post("/users/{user_id}/deactivate")
async def deactivate_user(user_id: int):
    """Deactivate user account"""
    return {"message": "User deactivated successfully"}

@router.get("/disease-stats")
async def get_disease_statistics():
    """Get disease statistics"""
    return {
        "top_diseases": [],
        "disease_counts": {},
        "trend": []
    }

@router.get("/system-health")
async def get_system_health():
    """Get system health status"""
    return {
        "status": "healthy",
        "database": "connected",
        "api": "operational",
        "uptime": "100%"
    }
