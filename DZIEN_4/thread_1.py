import threading
import time

def download(name):
    print(f"Start downloading {name}")
    time.sleep(2)
    print(f"Finish downloading {name}")

# ====================
# sekwencyjnie
# ====================

start = time.perf_counter()

for i in range(3):
    download(f"file{i}\n")
end = time.perf_counter()
print(f"Time(sekwencyjnie): {end - start}s")

threads = []
start = time.perf_counter()
for i in range(3):
    t = threading.Thread(target=download, args=(f"file{i}\n",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end = time.perf_counter()
print(f"Thread time: {end - start}s")

print("All done!")
