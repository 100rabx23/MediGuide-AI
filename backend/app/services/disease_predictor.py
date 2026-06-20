import joblib
import numpy as np
from typing import List, Dict, Optional
import os

class DiseasePredictor:
    """Disease prediction service using ML models"""
    
    def __init__(self, model_path: str, vectorizer_path: str):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model = None
        self.vectorizer = None
        self.load_models()
    
    def load_models(self):
        """Load ML model and vectorizer"""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            if os.path.exists(self.vectorizer_path):
                self.vectorizer = joblib.load(self.vectorizer_path)
        except Exception as e:
            print(f"Error loading models: {e}")
    
    def predict(self, symptoms: List[str]) -> Dict:
        """Predict diseases from symptoms"""
        if not self.model or not self.vectorizer:
            return {
                "status": "error",
                "message": "Models not loaded. Training required.",
                "predictions": []
            }
        
        try:
            text = " ".join(symptoms)
            features = self.vectorizer.transform([text])
            predictions = self.model.predict(features)
            
            return {
                "status": "success",
                "predictions": predictions.tolist()
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "predictions": []
            }

# Singleton instance
_predictor: Optional[DiseasePredictor] = None

def get_disease_predictor() -> DiseasePredictor:
    """Get disease predictor instance"""
    global _predictor
    if _predictor is None:
        _predictor = DiseasePredictor(
            "backend/ml_models/trained_models/disease_model.pkl",
            "backend/ml_models/trained_models/vectorizer.pkl"
        )
    return _predictor
