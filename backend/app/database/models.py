from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from backend.app.database.database import Base

class UserRole(str, enum.Enum):
    """User roles"""
    PATIENT = "patient"
    DOCTOR = "doctor"
    ADMIN = "admin"

class RiskLevel(str, enum.Enum):
    """Risk levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(Enum(UserRole), default=UserRole.PATIENT)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    patient = relationship("Patient", back_populates="user", uselist=False)
    doctor = relationship("Doctor", back_populates="user", uselist=False)
    predictions = relationship("Prediction", back_populates="user")

class Patient(Base):
    """Patient model"""
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(20))
    blood_group = Column(String(10))
    medical_history = Column(Text)
    allergies = Column(Text)
    current_medications = Column(Text)
    phone = Column(String(20))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="patient")
    reports = relationship("Report", back_populates="patient")

class Doctor(Base):
    """Doctor model"""
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    license_number = Column(String(100), unique=True)
    specialization = Column(String(100))
    phone = Column(String(20))
    clinic_name = Column(String(200))
    clinic_address = Column(Text)
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="doctor")
    reports = relationship("Report", back_populates="doctor")

class Symptom(Base):
    """Symptom model"""
    __tablename__ = "symptoms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(Text)
    category = Column(String(50))
    severity_levels = Column(JSON)  # Store as JSON
    related_symptoms = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

class Prediction(Base):
    """Prediction model"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symptoms_input = Column(Text)
    top_5_predictions = Column(JSON)
    confidence_scores = Column(JSON)
    risk_level = Column(Enum(RiskLevel), default=RiskLevel.LOW)
    explanation = Column(Text)
    language = Column(String(10), default="en")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="predictions")
    report = relationship("Report", back_populates="prediction", uselist=False)

class Report(Base):
    """Medical Report model"""
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"))
    title = Column(String(200))
    content = Column(Text)
    recommendations = Column(Text)
    risk_assessment = Column(Text)
    doctor_observations = Column(Text, nullable=True)
    pdf_path = Column(String(255), nullable=True)
    status = Column(String(20), default="pending")  # pending, reviewed, approved
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    reviewed_at = Column(DateTime, nullable=True)
    
    # Relationships
    patient = relationship("Patient", back_populates="reports")
    doctor = relationship("Doctor", back_populates="reports")
    prediction = relationship("Prediction", back_populates="report")
