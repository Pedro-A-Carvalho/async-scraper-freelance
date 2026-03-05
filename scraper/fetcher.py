import aiohttp
import asyncio
from scraper.parser import parse_title
import random
import logging

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10


async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore):
    max_retries = 3
    base_delay = 1

    async with semaphore:
        for attempt in range(1, max_retries + 1):
            try:
                async with session.get(url, timeout=DEFAULT_TIMEOUT) as response:
                    response.raise_for_status()
                    html = await response.text()

                    parsed_data = parse_title(html)

                    logger.info(f"SUCCESS: {url}")
                    return {
                        "url": url,
                        "data": parsed_data
                    }

            except (asyncio.TimeoutError, aiohttp.ClientError) as e:
                logger.warning(f"RETRY {attempt}: {url} -> {e}")

                if attempt == max_retries:
                    logger.error(f"FAILED: {url}")
                    return {
                        "url": url,
                        "error": str(e)
                    }

                delay = base_delay * (2 ** (attempt - 1))
                jitter = random.uniform(0, 0.5)
                await asyncio.sleep(delay + jitter)