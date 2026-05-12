# NBP Currency Tracker & ETL Pipeline

## Overview

This project demonstrates a professional ETL pipeline built in Python to track and analyze exchange rates. 

The goal is to automate the collection of financial data from the NBP API, compute technical indicators (SMA, Volatility), and provide a clear analytical dashboard.

## Architecture

NBP API → extraction → transformation → SQLite → analytical dashboard

## Technologies

- Python
- Pandas
- SQLite
- Seaborn
- Matplotlib
- NBP API

## Pipeline Steps

- Fetch currency rates (EUR, USD, GBP) from NBP API
- Calculate 7-day Simple Moving Average (SMA)
- Compute daily percentage change and market volatility
- Generate trend signals (increase/drop/stable)
- Store processed data in SQLite database
- Generate CLI performance report and financial charts

## Data Model

The project stores data in a `rates` table with the following structure:

- `date` – exchange rate date
- `currency` – currency code (EUR, USD, GBP)
- `rate` – mid exchange rate
- `sma7` – 7-day Simple Moving Average
- `pct_change` – daily percentage change
- `signal` – automated trend signal

## Example Analysis

The project includes a dashboard and reporting module:
- Monthly performance summary with MoM changes
- Indexed performance chart (Base 100)
- Daily exchange rate volatility tracking

## What I learned

- How to design a modular ETL pipeline in Python
- Implementing financial logic and rolling windows using pandas
- Professional logging and error handling in data scripts
- Managing configuration with environment variables
- Creating financial visualizations for data analysis

## Future Improvements

- Add more currencies and historical data range
- Implement automated unit tests for transformation logic
- Add email notification system for price signals
- Containerize pipeline using Docker

## Setup

Install dependencies:
```
pip install -r requirements.txt
```
Run ETL pipeline:
```
python src/main.py
```
Run analysis:
```
python src/analysis.py
```