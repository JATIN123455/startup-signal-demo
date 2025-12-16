# Startup Signal Demo Pipeline

This project demonstrates a reproducible data pipeline that processes
startup funding data and generates hiring signals.

## What it does
- Ingests startup data from CSV
- Cleans and deduplicates records
- Generates hiring and funding signals
- Exports structured output to Google Sheets

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
