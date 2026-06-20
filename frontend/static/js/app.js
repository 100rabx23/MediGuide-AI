// MediGuide AI Frontend Application

const API_BASE_URL = 'http://localhost:8000/api/v1';
const API_ROOT = 'http://localhost:8000';

// DOM Elements
const appDiv = document.getElementById('app');
const statusAlert = document.getElementById('status-alert');
const featuresDiv = document.getElementById('features');

// Initialize app on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('🏥 MediGuide AI Application Loaded');
    initializeApp();
});

// Initialize Application
async function initializeApp() {
    try {
        console.log('📡 Connecting to backend...');
        const response = await fetch(`${API_ROOT}/`);
        const data = await response.json();
        console.log('✅ Backend Status:', data);
        updateUI(data);
    } catch (error) {
        console.error('❌ Backend connection error:', error);
        showErrorMessage('Unable to connect to backend server');
    }
}

// Update UI with backend response
function updateUI(data) {
    if (appDiv) {
        appDiv.innerHTML = `
            <div class="alert alert-success fade-in" role="alert">
                <h4 class="alert-heading">✅ System Online</h4>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Version:</strong> ${data.version}</p>
                <hr>
                <p><small>⚠️ <strong>Medical Disclaimer:</strong> This system provides pre-diagnosis support only. Always consult qualified healthcare professionals for proper medical diagnosis and treatment.</small></p>
            </div>
        `;
        if (featuresDiv) {
            featuresDiv.style.display = 'grid';
        }
    }
}

// Show error message
function showErrorMessage(message) {
    if (statusAlert) {
        statusAlert.innerHTML = `
            <div class="alert alert-danger fade-in" role="alert">
                <h4 class="alert-heading">❌ Connection Error</h4>
                <p>${message}</p>
                <p><small>Make sure the FastAPI backend server is running on http://localhost:8000</small></p>
            </div>
        `;
    }
    if (appDiv) {
        appDiv.innerHTML = '';
    }
}

// Show success message
function showSuccessMessage(message) {
    if (statusAlert) {
        statusAlert.innerHTML = `
            <div class="alert alert-success fade-in" role="alert">
                <strong>✅ Success!</strong> ${message}
            </div>
        `;
    }
}

// Show info message
function showInfoMessage(message) {
    if (statusAlert) {
        statusAlert.innerHTML = `
            <div class="alert alert-info fade-in" role="alert">
                <strong>ℹ️ Info:</strong> ${message}
            </div>
        `;
    }
}

// API Functions

/**
 * Analyze symptoms
 */
async function sendSymptoms(symptoms) {
    try {
        const response = await fetch(`${API_BASE_URL}/symptoms/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptoms })
        });
        return await response.json();
    } catch (error) {
        console.error('❌ Error analyzing symptoms:', error);
        return { error: error.message };
    }
}

/**
 * Predict diseases
 */
async function predictDiseases(symptoms) {
    try {
        const response = await fetch(`${API_BASE_URL}/predictions/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptoms })
        });
        return await response.json();
    } catch (error) {
        console.error('❌ Error predicting diseases:', error);
        return { error: error.message };
    }
}

/**
 * Generate report
 */
async function generateReport(patientId, symptomsSummary) {
    try {
        const response = await fetch(`${API_BASE_URL}/reports/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ patient_id: patientId, symptoms_summary: symptomsSummary })
        });
        return await response.json();
    } catch (error) {
        console.error('❌ Error generating report:', error);
        return { error: error.message };
    }
}

/**
 * Register user
 */
async function registerUser(email, username, fullName, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                username: username,
                full_name: fullName,
                password: password
            })
        });
        return await response.json();
    } catch (error) {
        console.error('❌ Error registering user:', error);
        return { error: error.message };
    }
}

/**
 * Login user
 */
async function loginUser(email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });
        return await response.json();
    } catch (error) {
        console.error('❌ Error logging in:', error);
        return { error: error.message };
    }
}

/**
 * Get health information
 */
async function getHealthInfo(diseaseId) {
    try {
        const response = await fetch(`${API_BASE_URL}/predictions/disease/${diseaseId}`);
        return await response.json();
    } catch (error) {
        console.error('❌ Error fetching health info:', error);
        return { error: error.message };
    }
}

// Navigation Functions

/**
 * Navigate to symptom checker
 */
function goToSymptomChecker() {
    console.log('📋 Navigating to Symptom Checker');
    showInfoMessage('Symptom Checker feature coming soon!');
    // TODO: Implement symptom checker UI
}

/**
 * Navigate to AI assistant
 */
function goToAIAssistant() {
    console.log('🤖 Navigating to AI Assistant');
    showInfoMessage('AI Assistant feature coming soon!');
    // TODO: Implement AI assistant UI
}

/**
 * Navigate to reports
 */
function goToReports() {
    console.log('📊 Navigating to Reports');
    showInfoMessage('Medical Reports feature coming soon!');
    // TODO: Implement reports UI
}

/**
 * Navigate to doctor dashboard
 */
function goToDoctorDashboard() {
    console.log('🏥 Navigating to Doctor Dashboard');
    showInfoMessage('Doctor Dashboard feature coming soon!');
    // TODO: Implement doctor dashboard UI
}

// Utility Functions

/**
 * Format date
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

/**
 * Generate UUID
 */
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

console.log('✅ MediGuide AI Frontend Ready');
