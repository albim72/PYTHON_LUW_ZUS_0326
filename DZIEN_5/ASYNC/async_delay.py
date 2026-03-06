import time
import asyncio

def task(name, delay):
    print(f"Starting {name} in {delay} seconds")
    time.sleep(delay)
    print(f"{name} finished")

async def atask(name, delay):
    print(f"Starting {name} in {delay} seconds")
    time.sleep(delay)
    print(f"{name} finished")

def main_():
    task("task1", 2)
    task("task2", 1)
    task("task3", 3)

async def main_a():
    await asyncio.gather(
        atask("task1", 2),
        atask("task2", 1),
        atask("task3", 3)
    )


if __name__ == '__main__':
    print("synchronicznie....")
    s = time.perf_counter()
    main_()
    e = time.perf_counter()
    print(f"Czas wykonania: {e-s} sekund")
    print("asynchronicznie....")
    sa = time.perf_counter()
    asyncio.run(main_a())
    ea = time.perf_counter()
    print(f"Czas wykonania: {ea-sa} sekund")
