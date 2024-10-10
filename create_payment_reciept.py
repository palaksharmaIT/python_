from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Function to generate receipt PDF
def generate_receipt(transaction_id, payer_name, amount, date):
    # Define the PDF file name
    file_name = f"receipt_{transaction_id}.pdf"
    
    # Create the PDF object
    pdf = canvas.Canvas(file_name, pagesize=letter)
    
    # Set PDF title
    pdf.setTitle(f"Receipt #{transaction_id}")
    
    # Start writing content to PDF
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(200, 750, "Payment Receipt")

    # Add payer information and transaction details
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Transaction ID: {transaction_id}")
    pdf.drawString(50, 680, f"Payer Name: {payer_name}")
    pdf.drawString(50, 660, f"Amount Paid: ${amount}")
    pdf.drawString(50, 640, f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Draw a line to separate header and details
    pdf.line(50, 620, 550, 620)
    
    # Add footer text
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, 100, "Thank you for your payment!")
    
    # Save the PDF
    pdf.save()
    
    print(f"Receipt saved as {file_name}")

# Example usage
if __name__ == "__main__":
    # Sample transaction details
    transaction_id = "TXN12345"
    payer_name = "John Doe"
    amount = 150.75
    date = datetime.now()
    
    # Generate the receipt
    generate_receipt(transaction_id, payer_name, amount, date)
