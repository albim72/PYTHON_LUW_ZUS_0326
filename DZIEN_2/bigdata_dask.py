import dask.array as da
import time

N = 10_000_000

start = time.time()
data = [i for i in range(N)]
result = sum(data)
end = time.time()
print(f"Result: {result}")
print(f"Time: {end - start}")

print("_"*80)

start = time.time()
x = da.arange(N, chunks=1_000_000)
result = x.sum()
mid = time.time()
print(f"po definicji (bez compute): {mid - start}")

final = result.compute()
end = time.time()
print(f"Result: {final}")
print(f"Time: {end - start}")
