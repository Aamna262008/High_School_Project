import queue
import threading
import time

jobs = queue.Queue(maxsize=2)
results = []
results_lock = threading.Lock()


def download(label, chunks, delay=0.1):
    if chunks < 1:
        raise ValueError("chunks must be at least 1")
    for _ in range(chunks):
        time.sleep(delay)
    return f"{label}: DONE"


def worker():
    while True:
        item = jobs.get()
        try:
            if item is None:
                return
            label, chunks = item
            try:
                result = download(label, chunks)
            except Exception as error:
                result = f"{label}: FAILED ({error})"
            with results_lock:
                results.append(result)
            name = threading.current_thread().name
            print(f"{name} | {result}")
        finally:
            jobs.task_done()
downloads = [
    
]

workers = []
for number in range(1, 4):
    t = threading.Thread(target=worker, name=f"Worker-{number}")
    workers.append(t)
    t.start()

for item in downloads:
    jobs.put(item)
for _ in workers:
    jobs.put(None)

jobs.join()
for t in workers:
    t.join()

with open("download_report.txt", "w", encoding="utf-8") as report:
    for result in sorted(results):
        print(result, file=report)

print("Results:", len(results))
print("Workers alive:", sum(t.is_alive() for t in workers))
print("Saved download_report.txt")
