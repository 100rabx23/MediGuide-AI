# 🏥 MediGuide AI - Intelligent Medical Pre-Diagnosis & Healthcare Decision Support Platform

## Overview

MediGuide AI is a comprehensive B.Tech final-year project that combines **Artificial Intelligence**, **Machine Learning**, **Natural Language Processing**, and **Computer Vision** to create an intelligent healthcare decision support system.

**IMPORTANT DISCLAIMER**: 

This system is designed as a pre-diagnosis and decision-support assistant. It does NOT provide medical diagnoses. Always consult with healthcare professionals for proper medical diagnosis and treatment.


*****
## 🎯 Key Features
*****
### Core Functionality
- ✅ **Symptom Analysis**: Text and voice input processing
- ✅ **Disease Prediction**: Top 5 most likely conditions with confidence scores
- ✅ **Explainable AI**: Clear reasoning behind predictions
- ✅ **Risk Assessment**: Comprehensive health risk evaluation
- ✅ **Healthcare Recommendations**: Preventive measures and lifestyle guidance
- ✅ **Medical Reports**: Downloadable PDF reports
- ✅ **Multi-Language Support**: English, Hindi, Gujarati
- ✅ **Voice Assistant**: Speech recognition and text-to-speech
- ✅ **Medical Image Analysis**: AI-powered image recognition (optional)

### User Roles
- **Patients**: Access symptom checker, reports, and healthcare guidance
- **Doctors**: Review patient reports, add observations, track history
- **Administrators**: Manage users, view analytics, system monitoring

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Server**: Uvicorn

### Database
- **Development**: SQLite
- **Production**: PostgreSQL
- **ORM**: SQLAlchemy

### Machine Learning & NLP
- **ML**: Scikit-learn, XGBoost, RandomForest
- **NLP**: spaCy, NLTK, Transformers, BERT
- **Deep Learning**: PyTorch, TensorFlow

### Frontend
- **HTML5**, **CSS3**, **Bootstrap 5**
- **JavaScript** (Vanilla & Async/Await)
- **API Integration**: Fetch API

### AI & APIs
- **Google Gemini API** for AI assistant
- **Google Cloud Vision API** for image analysis

### Additional Tools
- **Report Generation**: ReportLab, Matplotlib
- **Voice Processing**: SpeechRecognition, pyttsx3
- **Computer Vision**: OpenCV, YOLOv8 (optional)
- **Authentication**: JWT, bcrypt

## 📁 Project Structure

```
MediGuide-AI/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   ├── schemas/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── symptoms.py
│   │   │   ├── predictions.py
│   │   │   ├── reports.py
│   │   │   ├── doctor.py
│   │   │   └── admin.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── disease_predictor.py
│   │   │   ├── nlp_processor.py
│   │   │   ├── report_generator.py
│   │   │   └── gemini_assistant.py
│   │   └── middleware/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── main.py
│   └── wsgi.py
├── frontend/
│   ├── index.html
│   ├── templates/
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── ml_models/
│   ├── disease_prediction/
│   ├── nlp/
│   └── image_analysis/
├── tests/
├── docs/
├── logs/
├── uploads/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL (for production)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/100rabx23/MediGuide-AI.git
   cd MediGuide-AI
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Download NLP models**
   ```bash
   python3 -m spacy download en_core_web_sm
   python3 -m nltk.downloader punkt stopwords wordnet averaged_perceptron_tagger
   ```

6. **Run the server**
   ```bash
   cd backend
   python main.py
   ```

Server will run at: `http://localhost:8000`

## 📚 API Documentation

Once the server is running, access the interactive API docs:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Security Features

- ✅ JWT Authentication
- ✅ Password hashing (bcrypt)
- ✅ Input validation & sanitization
- ✅ SQL injection protection
- ✅ CORS configuration
- ✅ Rate limiting
- ✅ Audit logging

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_auth.py

# With coverage
pytest --cov=app tests/
```

## 📊 Core Modules

### 1. Authentication Module
- User registration and login
- JWT token management
- Role-based access control
- Password hashing with bcrypt

### 2. Symptom Collection
- Text symptom input
- Voice-to-text conversion
- Symptom extraction using NLP
- Symptom history tracking

### 3. Disease Prediction Engine
- ML model for disease prediction
- Top 5 predictions with confidence scores
- Risk level assessment
- Explainable predictions

### 4. AI Assistant
- Gemini API integration
- Healthcare Q&A
- Recommendation engine

### 5. Report Generator
- PDF report creation
- Patient information summary
- Prediction details
- Healthcare recommendations

### 6. Doctor Dashboard
- Patient report review
- Observation addition
- Patient history tracking
- Data export functionality

### 7. Admin Dashboard
- User management
- System analytics
- Usage statistics
- Disease analytics

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- **Developer**: 100rabx23
- **Institution**: B.Tech Final Year Project

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## ⚠️ Medical Disclaimer

**This system is NOT a medical diagnosis tool.** It is designed as an educational and informational platform for pre-diagnosis support only. Always consult with qualified healthcare professionals for proper medical diagnosis, treatment, and care. Do not delay seeking professional medical help based on results from this system.

---

**Built with ❤️ for healthcare innovation**
