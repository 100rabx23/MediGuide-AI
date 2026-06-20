import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Base Configuration
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings:
    """Application Settings"""
    
    # App Configuration
    APP_NAME = os.getenv("APP_NAME", "MediGuide AI")
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    
    # Database Configuration
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR}/mediguide.db"
    )
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))
    
    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GOOGLE_CLOUD_KEY = os.getenv("GOOGLE_CLOUD_KEY", "")
    
    # Server Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    WORKERS = int(os.getenv("WORKERS", "4"))
    
    # File Upload Configuration
    MAX_UPLOAD_SIZE = int(os.getenv("MAX_UPLOAD_SIZE", "10485760"))  # 10MB
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".pdf"}
    
    # Language Support
    SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "en,hi,gu").split(",")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
    
    # Email Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    
    # ML Model Paths
    DISEASE_MODEL_PATH = os.getenv(
        "DISEASE_MODEL_PATH",
        str(BASE_DIR / "backend/ml_models/trained_models/disease_model.pkl")
    )
    VECTORIZER_PATH = os.getenv(
        "VECTORIZER_PATH",
        str(BASE_DIR / "backend/ml_models/trained_models/vectorizer.pkl")
    )
    
    # Disease Database
    DISEASES_FILE = os.getenv(
        "DISEASES_FILE",
        str(BASE_DIR / "backend/ml_models/diseases_database.json")
    )

settings = Settings()
