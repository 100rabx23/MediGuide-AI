import logging
from datetime import datetime
from typing import Optional
import os

logger = logging.getLogger(__name__)

class ReportGenerator:
    """Report Generation Service"""
    
    def __init__(self):
        """Initialize report generator"""
        self.output_dir = "reports"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_pdf(self, report):
        """Generate PDF report"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.units import inch
            
            filename = f"{self.output_dir}/report_{report.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            
            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()
            
            # Add title
            title = Paragraph(f"<b>Medical Report</b>", styles['Heading1'])
            elements.append(title)
            elements.append(Spacer(1, 0.3*inch))
            
            # Add content
            content = Paragraph(report.content if report.content else report.title, styles['Normal'])
            elements.append(content)
            
            # Build PDF
            doc.build(elements)
            
            logger.info(f"PDF report generated: {filename}")
            return filename
        except Exception as e:
            logger.error(f"Error generating PDF: {str(e)}")
            raise
    
    def generate_html_report(self, report) -> str:
        """Generate HTML report"""
        html_content = f"""
        <html>
            <head>
                <title>Medical Report - {report.title}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    .header {{ background-color: #2c3e50; color: white; padding: 20px; }}
                    .content {{ padding: 20px; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>{report.title}</h1>
                </div>
                <div class="content">
                    <p>{report.content}</p>
                    <h3>Recommendations</h3>
                    <p>{report.recommendations}</p>
                </div>
            </body>
        </html>
        """
        return html_content
