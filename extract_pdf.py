import pdfplumber
import pandas as pd

# Path to the PDF file
PDF_PATH = "Google Play Store Apps.pdf"

# Extract text from PDF
def extract_pdf_text(pdf_path):
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text.append(page.extract_text())
    return "\n".join(text)

if __name__ == "__main__":
    pdf_text = extract_pdf_text(PDF_PATH)
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(pdf_text)
    print("PDF text extracted to extracted_text.txt")
