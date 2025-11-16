"""
Main orchestration script for PDF invoice extraction.
"""

import os
import sys

# Add parent directory to path so imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.reader import get_pdf_files, extract_text_from_pdf
from src.extractor import parse_invoice
from src.writer import write_to_csv
from src.utils import ensure_directory_exists


def main():
    """
    Main function that coordinates the invoice extraction process.
    """
    # Define paths
    invoices_folder = "invoices"
    output_folder = "output"
    output_file = os.path.join(output_folder, "extracted.csv")
    
    # Ensure output directory exists
    ensure_directory_exists(output_folder)
    
    # Get list of PDF files
    print("Scanning for PDF invoices...")
    pdf_files = get_pdf_files(invoices_folder)
    
    if not pdf_files:
        print("No PDF files found in the invoices folder.")
        print(f"   Please add PDF files to: {invoices_folder}/")
        return
    
    print(f"✓ Found {len(pdf_files)} PDF file(s)")
    
    # Process each PDF
    extracted_data = []
    
    for pdf_file in pdf_files:
        print(f"\n Processing: {pdf_file}")
        
        # Full path to PDF
        pdf_path = os.path.join(invoices_folder, pdf_file)
        
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        
        if not text:
            print(f"   ⚠ Could not extract text from {pdf_file}")
            continue
        
        # Parse invoice fields
        invoice_data = parse_invoice(text, pdf_file)
        extracted_data.append(invoice_data)
        
        # Print summary
        print(f"   Invoice: {invoice_data['invoice_number']}")
        print(f"   Date: {invoice_data['date']}")
        print(f"   Total: {invoice_data['total']}")
        print(f"   Supplier: {invoice_data['supplier'][:50]}...")  # Truncate long names
    
    # Write results to CSV
    print("\n" + "="*60)
    if extracted_data:
        write_to_csv(extracted_data, output_file)
        print(f"\n Extraction complete! Results saved to: {output_file}")
    else:
        print("No data was extracted from any PDFs.")
    
    print("="*60)


if __name__ == "__main__":
    main()
