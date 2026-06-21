import logging
import os
from backend.config.settings import settings
from typing import Optional

logger = logging.getLogger(__name__)

class GeminiAssistant:
    """Gemini AI Assistant Service"""
    
    def __init__(self):
        """Initialize Gemini assistant"""
        self.api_key = settings.GEMINI_API_KEY
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize Gemini client"""
        try:
            if self.api_key:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.client = genai.GenerativeModel('gemini-pro')
                logger.info("Gemini client initialized")
        except Exception as e:
            logger.error(f"Error initializing Gemini: {str(e)}")
    
    def get_health_advice(self, symptoms: str) -> Optional[str]:
        """Get health advice from Gemini"""
        if not self.client:
            logger.warning("Gemini client not available")
            return None
        
        try:
            prompt = f"""
            Based on the following symptoms, provide general health advice and recommendations.
            Symptoms: {symptoms}
            
            IMPORTANT: This is for informational purposes only and not a medical diagnosis.
            Always recommend consulting with a healthcare professional.
            """
            
            response = self.client.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error getting health advice: {str(e)}")
            return None
    
    def answer_health_question(self, question: str) -> Optional[str]:
        """Answer health-related questions"""
        if not self.client:
            logger.warning("Gemini client not available")
            return None
        
        try:
            prompt = f"""
            Answer the following health-related question. 
            Provide accurate, helpful information.
            
            Question: {question}
            
            Note: This is for educational purposes. Always recommend consulting healthcare professionals.
            """
            
            response = self.client.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error answering question: {str(e)}")
            return None
