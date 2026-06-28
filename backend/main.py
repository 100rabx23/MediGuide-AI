import logging
import os
import sys
from pathlib import Path



#1*2
# Add parent
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from backend.app.routes import health, auth, symptoms, predictions, reports, doctor, admin
from backend.app.database.database import Base, engine

# Load environment variables
load_dotenv()


#23222

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="MediGuide AI",
    description="Intelligent Medical Pre-Diagnosis & Healthcare Decision Support Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")

# Create necessary directories
for directory in ["logs", "uploads", "reports"]:
    Path(directory).mkdir(exist_ok=True)

# Include routers
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(symptoms.router)
app.include_router(predictions.router)
app.include_router(reports.router)
app.include_router(doctor.router)
app.include_router(admin.router)

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - Welcome message"""
    return {
        "message": "Welcome to MediGuide AI",
        "description": "Intelligent Medical Pre-Diagnosis & Healthcare Decision Support Platform",
        "status": "online",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
