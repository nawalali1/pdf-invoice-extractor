"""
Field extraction logic using regex patterns.
"""

import re
from src.utils import clean_currency_value


def parse_invoice(text, filename):
    """
    Extracts invoice fields from text using regex patterns.
    
    Args:
        text (str): Extracted text from PDF
        filename (str): Name of the source PDF file
    
    Returns:
        dict: Dictionary containing extracted fields
    """
    result = {
        "invoice_number": extract_invoice_number(text),
        "date": extract_date(text),
        "total": extract_total(text),
        "supplier": extract_supplier(text),
        "source_file": filename
    }
    
    return result


def extract_invoice_number(text):
    """
    Extracts invoice number using various common patterns.
    """
    patterns = [
        r'Invoice\s*#?\s*:?\s*([A-Z0-9-]+)',
        r'Invoice\s*Number\s*:?\s*([A-Z0-9-]+)',
        r'INV\s*[:-]?\s*([A-Z0-9-]+)',
        r'#\s*([A-Z0-9-]{5,})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "Not found"


def extract_date(text):
    """
    Extracts invoice date using common date formats.
    """
    patterns = [
        r'Date\s*:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'Invoice\s*Date\s*:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "Not found"


def extract_total(text):
    """
    Extracts total amount from invoice.
    """
    patterns = [
        r'Total\s*:?\s*([£$€]?\s*\d+[,\d]*\.?\d*)',
        r'Amount\s*Due\s*:?\s*([£$€]?\s*\d+[,\d]*\.?\d*)',
        r'Invoice\s*Total\s*:?\s*([£$€]?\s*\d+[,\d]*\.?\d*)',
        r'Grand\s*Total\s*:?\s*([£$€]?\s*\d+[,\d]*\.?\d*)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            raw_value = match.group(1).strip()
            return clean_currency_value(raw_value)
    
    return "Not found"


def extract_supplier(text):
    """
    Extracts supplier/company name from the top of the invoice.
    Usually the first prominent line of text.
    """
    # Split text into lines and get first few non-empty lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    if len(lines) > 0:
        # Return first line as supplier (usually company name)
        return lines[0]
    
    return "Not found"
