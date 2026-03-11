import aiohttp
import asyncio
from scraper.parser import parse_title, parse_books
import random
import logging
from scraper.config import MAX_RETRIES, BASE_DELAY, DEFAULT_TIMEOUT, USER_AGENTS

logger = logging.getLogger(__name__)

async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore):
    max_retries = MAX_RETRIES
    base_delay = BASE_DELAY
    headers = {
    "User-Agent": random.choice(USER_AGENTS)
    }

    async with semaphore:
        for attempt in range(1, max_retries + 1):
            try:
                async with session.get(
                    url,
                    timeout=DEFAULT_TIMEOUT,
                    headers=headers
                ) as response:
                    response.raise_for_status()
                    html = await response.text()

                    parsed_data = parse_books(html)

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