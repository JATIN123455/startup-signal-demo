# Startup Signal Demo Pipeline

This project demonstrates a reproducible data pipeline that processes
startup funding data and generates hiring signals.

## How it works
1. Reads startup data from CSV
2. Cleans and deduplicates records
3. Generates hiring and funding signals
4. Exports results to Google Sheets

## How to run
```bash
pip install -r requirements.txt
python src/main.py
