import asyncio
import aiohttp
import re
from urllib.parse import urljoin, urlparse


START_URL = "https://example.com"
MAX_LINKS = 10


def extract_links(base_url: str, html: str) -> list[str]:
    pattern = r'href=["\'](.*?)["\']'
    raw_links = re.findall(pattern, html, flags=re.IGNORECASE)

    links = []
    base_domain = urlparse(base_url).netloc

    for link in raw_links:
        absolute = urljoin(base_url, link)
        parsed = urlparse(absolute)

        if parsed.scheme in ("http", "https") and parsed.netloc == base_domain:
            links.append(absolute)

    return list(dict.fromkeys(links))  # usuń duplikaty, zachowaj kolejność


async def fetch_html(url: str, session: aiohttp.ClientSession, sem: asyncio.Semaphore) -> tuple[str, str | None]:
    async with sem:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return url, await response.text()
                return url, None
        except Exception:
            return url, None


async def main():
    timeout = aiohttp.ClientTimeout(total=10)
    sem = asyncio.Semaphore(5)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        start_url, html = await fetch_html(START_URL, session, sem)

        if not html:
            print("Nie udało się pobrać strony startowej.")
            return

        links = extract_links(start_url, html)[:MAX_LINKS]

        print("Znalezione linki:")
        for link in links:
            print(" -", link)

        tasks = [fetch_html(link, session, sem) for link in links]
        results = await asyncio.gather(*tasks)

        print("\nPodsumowanie odwiedzin:")
        for url, page_html in results:
            if page_html is None:
                print(f"{url} -> ERROR")
            else:
                print(f"{url} -> {len(page_html)} znaków")


if __name__ == "__main__":
    asyncio.run(main())
