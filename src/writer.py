"""
CSV writing functionality.
"""

import csv


def write_to_csv(data, output_path):
    """
    Writes extracted invoice data to a CSV file.
    
    Args:
        data (list): List of dictionaries containing invoice data
        output_path (str): Full path to output CSV file
    """
    if not data:
        print("No data to write.")
        return
    
    # Define CSV columns
    fieldnames = ["invoice_number", "date", "total", "supplier", "source_file"]
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data rows
            for row in data:
                writer.writerow(row)
        
        print(f"✓ Successfully wrote {len(data)} records to {output_path}")
        
    except Exception as e:
        print(f"Error writing CSV: {e}")
