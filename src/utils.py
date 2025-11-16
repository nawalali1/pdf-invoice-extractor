"""
Utility functions for the PDF invoice extractor.
"""

import os


def ensure_directory_exists(directory_path):
    """
    Creates a directory if it doesn't already exist.
    
    Args:
        directory_path (str): Path to the directory
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")


def clean_currency_value(value):
    """
    Removes currency symbols and formatting from a price string.
    
    Args:
        value (str): Raw currency value (e.g., "£1,234.50")
    
    Returns:
        str: Cleaned value (e.g., "1234.50")
    """
    if not value:
        return ""
    
    # Remove common currency symbols and commas
    cleaned = value.replace('£', '').replace('$', '').replace('€', '')
    cleaned = cleaned.replace(',', '').strip()
    
    return cleaned
