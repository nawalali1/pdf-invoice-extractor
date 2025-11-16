# PDF Invoice Extractor

A small Python automation tool for extracting basic information from PDF invoices and exporting it to CSV.

## Features

* Processes multiple PDF files placed in the `invoices` folder
* Extracts four common invoice fields: invoice number, date, total amount, and supplier
* Handles simple variations in field naming such as "Total", "Invoice Total", and "Amount Due"
* Outputs clean CSV data to `output/extracted.csv`
* Works with standard text-based PDFs without OCR

## Project Structure
```
pdf-invoice-extractor/
├── src/
│   ├── reader.py       # PDF loading and text extraction
│   ├── extractor.py    # Regex-based field extraction
│   ├── writer.py       # CSV output functions
│   ├── utils.py        # Helper functions
│   └── main.py         # Main script
├── invoices/           # User-provided PDF invoices
├── output/             # Generated CSV file
├── requirements.txt
└── README.md
```

## Installation

1. Clone or download the repository
2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Add your PDF invoices to the `invoices` folder
2. Run the script:
```bash
python src/main.py
```

3. The extracted data will be saved in `output/extracted.csv`

## Example Output
```csv
invoice_number,date,total,supplier,source_file
INV-001234,15/03/2024,450.00,Acme Supplies,invoice_01.pdf
INV-001235,16/03/2024,230.50,Office Depot,invoice_02.pdf
```

## Limitations

* Supports text-based PDFs only
* Extraction relies on simple patterns, so very inconsistent invoice layouts may require adjustments

## Possible Enhancements

* Additional invoice fields
* More flexible matching rules
* Configurable regex patterns
