from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class UserRole(str, enum.Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(Enum(UserRole), default=UserRole.PATIENT)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    patient_profile = relationship("Patient", back_populates="user", uselist=False)
    doctor_profile = relationship("Doctor", back_populates="user", uselist=False)
    reports = relationship("Report", back_populates="user")
    chat_history = relationship("ChatHistory", back_populates="user")

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    age = Column(Integer)
    gender = Column(String)
    blood_type = Column(String)
    allergies = Column(Text)
    medical_history = Column(Text)
    emergency_contact = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="patient_profile")
    symptoms = relationship("Symptom", back_populates="patient")
    predictions = relationship("DiseasePrediction", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    license_number = Column(String, unique=True)
    specialization = Column(String)
    qualification = Column(String)
    experience_years = Column(Integer)
    hospital_affiliation = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="doctor_profile")
    observations = relationship("DoctorObservation", back_populates="doctor")

class Symptom(Base):
    __tablename__ = "symptoms"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    symptom_name = Column(String)
    description = Column(Text)
    duration = Column(String)
    severity = Column(String)  # mild, moderate, severe
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    patient = relationship("Patient", back_populates="symptoms")

class DiseasePrediction(Base):
    __tablename__ = "disease_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    disease_name = Column(String)
    confidence_score = Column(Float)
    rank = Column(Integer)  # 1-5
    risk_level = Column(String)  # low, medium, high
    explanation = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    patient = relationship("Patient", back_populates="predictions")

class Report(Base):
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    report_type = Column(String)  # symptom_analysis, full_report
    symptoms_summary = Column(Text)
    predictions_summary = Column(Text)
    recommendations = Column(Text)
    risk_assessment = Column(Text)
    pdf_path = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="reports")
    observations = relationship("DoctorObservation", back_populates="report")

class DoctorObservation(Base):
    __tablename__ = "doctor_observations"
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    report_id = Column(Integer, ForeignKey("reports.id"))
    observation_text = Column(Text)
    recommendation = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    doctor = relationship("Doctor", back_populates="observations")
    report = relationship("Report", back_populates="observations")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_message = Column(Text)
    assistant_response = Column(Text)
    topic = Column(String)  # health_question, recommendation, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="chat_history")

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    appointment_date = Column(DateTime)
    notes = Column(Text)
    status = Column(String)  # pending, confirmed, completed, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())
