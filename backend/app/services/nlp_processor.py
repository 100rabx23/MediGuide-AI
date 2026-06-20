from typing import List, Dict
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class NLPProcessor:
    """Natural Language Processing for symptom extraction"""
    
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            self.stop_words = set()
    
    def extract_symptoms(self, text: str) -> List[str]:
        """Extract symptoms from text"""
        # Simple tokenization and symptom extraction
        tokens = word_tokenize(text.lower())
        symptoms = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        return symptoms
    
    def process_text(self, text: str) -> Dict:
        """Process user input text"""
        symptoms = self.extract_symptoms(text)
        return {
            "original_text": text,
            "extracted_symptoms": symptoms,
            "symptom_count": len(symptoms)
        }

nlp_processor = NLPProcessor()
