import asyncio
import aiohttp
from scraper.fetcher import fetch
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def parse_args():
    parser = argparse.ArgumentParser(description="Async Web Scraper")

    parser.add_argument(
        "--pages",
        type=int,
        default=3,
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

    pages = args.pages
    concurrency = args.concurrency
    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, BASE_URL.format(page), semaphore)
            for page in range(1, pages + 1)
        ]

        results = await asyncio.gather(*tasks)

    print("\nFinal Results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(run())