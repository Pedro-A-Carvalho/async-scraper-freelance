import aiohttp
import asyncio

DEFAULT_TIMEOUT = 10


async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=DEFAULT_TIMEOUT) as response:
                response.raise_for_status()
                html = await response.text()
                print(f"[SUCCESS] {url}")
                return {"url": url, "content": html}

        except asyncio.TimeoutError:
            print(f"[TIMEOUT] {url}")
            return {"url": url, "error": "timeout"}

        except aiohttp.ClientError as e:
            print(f"[ERROR] {url} -> {e}")
            return {"url": url, "error": str(e)}