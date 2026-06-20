import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.main import app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "MediGuide AI" in response.json()["message"]

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_api_info():
    """Test API info endpoint"""
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert "endpoints" in response.json()

def test_register():
    """Test user registration"""
    response = client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "full_name": "Test User",
        "password": "password123"
    })
    assert response.status_code == 201

def test_symptom_analysis():
    """Test symptom analysis"""
    response = client.post("/api/v1/symptoms/analyze", json={
        "symptoms": ["fever", "cough"],
        "duration": "3 days",
        "severity": "moderate"
    })
    assert response.status_code == 200
    assert "symptoms" in response.json()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
