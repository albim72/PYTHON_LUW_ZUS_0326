import asyncio
import aiohttp


URLS = [
    "https://example.com",
    "https://www.python.org",
    "https://docs.aiohttp.org",
    "https://httpbin.org/get",
    "https://httpbin.org/html",
]


async def worker(name: str, queue: asyncio.Queue, session: aiohttp.ClientSession):
    while True:
        url = await queue.get()

        if url is None:
            queue.task_done()
            print(f"[{name}] koniec")
            break

        try:
            async with session.get(url) as response:
                text = await response.text()
                print(f"[{name}] {url} -> {response.status}, {len(text)} znaków")
        except Exception as e:
            print(f"[{name}] {url} -> ERROR: {e}")

        queue.task_done()


async def main():
    queue = asyncio.Queue()
    timeout = aiohttp.ClientTimeout(total=10)

    for url in URLS:
        await queue.put(url)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        workers = [
            asyncio.create_task(worker("W1", queue, session)),
            asyncio.create_task(worker("W2", queue, session)),
            asyncio.create_task(worker("W3", queue, session)),
        ]

        await queue.join()

        for _ in workers:
            await queue.put(None)

        await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())
