from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from passlib.context import CryptContext

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    username: str
    full_name: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        os.getenv("JWT_SECRET_KEY", "your-secret-key"),
        algorithm="HS256"
    )
    return encoded_jwt

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=dict)
async def register(request: RegisterRequest):
    """User registration endpoint"""
    # Check if user already exists (in real app, query database)
    hashed_password = hash_password(request.password)
    
    return {
        "message": "User registered successfully",
        "email": request.email,
        "username": request.username,
        "user_id": 1  # Would be from database
    }

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """User login endpoint"""
    # In real app, verify credentials from database
    access_token = create_access_token(data={"sub": request.email, "user_id": 1})
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user_id=1
    )

@router.post("/logout")
async def logout():
    """User logout endpoint"""
    return {"message": "Logged out successfully"}

@router.post("/forgot-password")
async def forgot_password(email: str):
    """Request password reset"""
    return {"message": "Password reset email sent", "email": email}

@router.post("/reset-password")
async def reset_password(token: str, new_password: str):
    """Reset password with token"""
    return {"message": "Password reset successfully"}

@router.post("/verify-email")
async def verify_email(token: str):
    """Verify email address"""
    return {"message": "Email verified successfully"}
