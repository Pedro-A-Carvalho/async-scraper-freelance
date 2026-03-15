# Async Web Scraper (Python)

A high-performance asynchronous web scraper built with Python.

This project demonstrates modern scraping techniques such as:

- asynchronous requests
- concurrency control
- retry with exponential backoff
- user-agent rotation
- automatic pagination discovery
- CSV and JSON export
- progress tracking

The scraper collects book data from the practice website:
https://books.toscrape.com

---

## Features

- Async scraping using aiohttp
- Concurrency control with asyncio.Semaphore
- Retry logic with exponential backoff
- Random User-Agent rotation
- Automatic pagination detection
- Progress bar using tqdm
- CSV and JSON export
- Failed URL tracking

---

## Data Collected

For each book the scraper extracts:

- Title
- Price
- Rating
- Source URL

---

## Project Structure
```
 async-scraper-freelance/
 │
 ├── scraper/
 │   ├── config.py
 │   ├── fetcher.py
 │   ├── parser.py
 │   ├── exporter.py
 │   ├── pagination.py
 │   └── input_reader.py
 │
 ├── main.py
 ├── urls.txt
 ├── requirements.txt
 └── README.md
```
---

## Installation

Clone the repository:

git clone https://github.com/Pedro-A-Carvalho/async-scraper-freelance

cd async-scraper-freelance

Create virtual environment:

python -m venv venv

Activate environment:

Linux/ WSL:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Usage
 
Run the scraper:

python main.py

The scraper will:

1. Detect total pages automatically
2. Scrape all book listings
3. Export results to CSV and JSON

---

## Output

The scraper generates:

output.csv
output.json

Example CSV output:

url,title,price,rating
page1,A Light in the Attic,£51.77,Three
page1,Tipping the Velvet,£53.74,One

---

## Technologies Used

- Python
- asyncio
- aiohttp
- BeautifulSoup
- tqdm

---

## Disclaimer

This project is for educational purposes only.
The target website is intentionally designed for scraping practice.