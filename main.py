import asyncio
import aiohttp
from scraper.fetcher import fetch
import logging
import argparse
from scraper.exporter import export_to_json, export_to_csv
from scraper.input_reader import load_urls
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def parse_args():
    parser = argparse.ArgumentParser(description="Async Web Scraper")

    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of pages to scrape"
    )

    parser.add_argument(
        "--concurrency",
        type=int,
        default=5,
        help="Number of concurrent requests"
    )

    return parser.parse_args()


async def run():
    args = parse_args()

    urls = load_urls("urls.txt")
    concurrency = args.concurrency

    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, url, semaphore)
            for url in tqdm(urls, desc="Scraping pages")
        ]

        results = await asyncio.gather(*tasks)

    logger.info(f"SAVED")
    export_to_csv(results)
    export_to_json(results)


if __name__ == "__main__":
    asyncio.run(run())