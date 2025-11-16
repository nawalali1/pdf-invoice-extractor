# PDF Invoice Extractor

A simple Python automation tool that extracts key information from PDF invoices and exports the data to CSV format.

## Features

- Automatically processes multiple PDF invoices from a folder
- Extracts four key fields: invoice number, date, total amount, and supplier
- Handles variations in field naming (e.g., "Total", "Amount Due", "Invoice Total")
- Outputs clean CSV data for further analysis
- No OCR required – works with text-based PDFs

## Project Structure
```
pdf-invoice-extractor/
├── src/
│   ├── reader.py      # Handles PDF loading and text extraction
│   ├── extractor.py   # Regex-based field extraction logic
│   ├── writer.py      # CSV output generation
│   ├── utils.py       # Helper functions
│   └── main.py        # Main orchestration script
├── invoices/          # Place your PDF invoices here
├── output/            # Generated CSV files appear here
├── requirements.txt
└── README.md
```

## Installation

1. Clone or download this project
2. Create a virtual environment (recommended):
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Usage

1. Place your PDF invoices in the `invoices/` folder
2. Run the extraction script:
```bash
   python src/main.py
```
3. Find your results in `output/extracted.csv`

## Example Output

The generated CSV will contain:

| invoice_number | date       | total   | supplier        | source_file    |
|----------------|------------|---------|-----------------|----------------|
| INV-001234     | 15/03/2024 | £450.00 | Acme Supplies   | invoice_01.pdf |
| INV-001235     | 16/03/2024 | £230.50 | Office Depot    | invoice_02.pdf |

## Limitations

- Works only with text-based PDFs (not scanned images)
- Extraction accuracy depends on consistent invoice formatting
- Designed for simple invoice structures

## Future Enhancements

- Add support for more invoice fields
- Implement fuzzy matching for better field detection
- Add configuration file for custom regex patterns
