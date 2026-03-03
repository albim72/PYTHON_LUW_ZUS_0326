import tracemalloc
import time

N = 1_000_000

def return_version(n):
    return [i for i in range(n)]

def yield_version(n):
    for i in range(n):
        yield i

tracemalloc.start()
start = time.time()
lst = sum(return_version(N))
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Return version: {end - start}")
print(f"Current memory: {current}")
print(f"Peak memory: {peak}")

tracemalloc.stop()

print("_"*80)

tracemalloc.start()
start = time.time()
gen= yield_version(N)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Yield version - czas utworzenia generatora: {end - start}")
print(f"Peak memory: {peak}")

tracemalloc.stop()

print("_"*80)

print("_"*80)

tracemalloc.start()
start = time.time()
total = sum(yield_version(N))
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Yield version - czas utworzenia generatora: {end - start}")
print(f"Peak memory: {peak}")

tracemalloc.stop()
