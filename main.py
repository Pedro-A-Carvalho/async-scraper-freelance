import asyncio
import aiohttp
from scraper.fetcher import fetch

URLS = [
    "https://example.com",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/status/404",
]

CONCURRENCY_LIMIT = 3


async def run():
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, url, semaphore)
            for url in URLS
        ]

        results = await asyncio.gather(*tasks)

    print("\nFinal Results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(run())