"""
PDF reading functionality using pdfplumber.
"""

import os
import pdfplumber


def get_pdf_files(invoices_folder):
    """
    Lists all PDF files in the specified folder.
    
    Args:
        invoices_folder (str): Path to the folder containing PDF invoices
    
    Returns:
        list: List of PDF filenames
    """
    if not os.path.exists(invoices_folder):
        print(f"Warning: {invoices_folder} does not exist.")
        return []
    
    pdf_files = [f for f in os.listdir(invoices_folder) if f.lower().endswith('.pdf')]
    return pdf_files


def extract_text_from_pdf(pdf_path):
    """
    Extracts all text content from a PDF file.
    
    Args:
        pdf_path (str): Full path to the PDF file
    
    Returns:
        str: Extracted text from all pages
    """
    text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""
    
    return text
