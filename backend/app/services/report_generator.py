from typing import Dict
from datetime import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

class ReportGenerator:
    """Generate medical reports in PDF format"""
    
    def __init__(self):
        self.report_dir = "reports"
        os.makedirs(self.report_dir, exist_ok=True)
    
    def generate_pdf_report(self, patient_data: Dict) -> str:
        """Generate PDF report for patient"""
        report_name = f"report_{patient_data.get('patient_id')}_{datetime.now().timestamp()}.pdf"
        report_path = os.path.join(self.report_dir, report_name)
        
        try:
            # Create PDF document
            doc = SimpleDocTemplate(report_path, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#2563eb'),
                spaceAfter=30,
                alignment=1
            )
            story.append(Paragraph("MediGuide AI - Medical Report", title_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Patient Info
            story.append(Paragraph("Patient Information", styles['Heading2']))
            patient_info = [
                ["Patient ID:", str(patient_data.get('patient_id', 'N/A'))],
                ["Date:", datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                ["Age:", str(patient_data.get('age', 'N/A'))],
            ]
            patient_table = Table(patient_info)
            patient_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(patient_table)
            story.append(Spacer(1, 0.3*inch))
            
            # Disclaimer
            disclaimer_style = ParagraphStyle(
                'Disclaimer',
                parent=styles['Normal'],
                fontSize=9,
                textColor=colors.HexColor('#ef4444'),
                borderPadding=10,
                borderColor=colors.HexColor('#ef4444'),
                borderRadius=5
            )
            story.append(Paragraph(
                "⚠️ <b>MEDICAL DISCLAIMER:</b> This report is for informational purposes only and does not constitute medical diagnosis. Always consult with qualified healthcare professionals for proper diagnosis and treatment.",
                disclaimer_style
            ))
            
            # Build PDF
            doc.build(story)
            return report_path
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return ""
    
    def generate_text_report(self, patient_data: Dict) -> str:
        """Generate text report"""
        report = f"""
        ========================================
        MediGuide AI - Medical Report
        ========================================
        
        Patient Information:
        - Patient ID: {patient_data.get('patient_id', 'N/A')}
        - Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        - Age: {patient_data.get('age', 'N/A')}
        
        Symptoms:
        {', '.join(patient_data.get('symptoms', []))}
        
        Risk Assessment:
        {patient_data.get('risk_level', 'Unknown')}
        
        DISCLAIMER:
        This report is for informational purposes only.
        Always consult with healthcare professionals.
        
        ========================================
        """
        return report

report_generator = ReportGenerator()
