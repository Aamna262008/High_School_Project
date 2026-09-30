from concurrent.futures import ThreadPoolExecutor, TimeoutError
import threading

release = threading.Event()

def held_download():
    release.wait()
    return "photo.jpg: DONE"

with ThreadPoolExecutor(max_workers=1) as pool:
    first = pool.submit(held_download)
    waiting = pool.submit(lambda: "second job")
    print("First done:", first.done())
    print("Cancel queued job:", waiting.cancel())
    print("Queued job cancelled:", waiting.cancelled())
    try:
        first.result(timeout=0.05)
    except TimeoutError:
        print("Result is not ready yet")
    finally:
        release.set()
    print(first.result())
    print("First done now:", first.done())
