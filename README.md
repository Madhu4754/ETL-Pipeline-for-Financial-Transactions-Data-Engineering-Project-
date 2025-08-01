# ETL Pipeline for Financial Transactions

## Overview
Extract, transform, and load financial transaction data from varied formats into a structured SQLite database, simulating a production data engineering workflow.

## Tech Stack
- Python (Pandas), SQLite (fallback), CSV/JSON input  
- Logging, validation, duplicate handling

## Files
- `generate_transactions.py`: Creates synthetic transaction data in CSV/JSON.  
- `etl_pipeline.py`: Performs ETL: extract -> transform (clean, dedupe) -> load.  
- `config.yaml`: Basic configuration for input paths.  
- `notebook.ipynb`: Demonstration of pipeline execution.

## Quick Start
1. Run `python generate_transactions.py` to create sample data.  
2. Run `python etl_pipeline.py` to process and load into DB.  
