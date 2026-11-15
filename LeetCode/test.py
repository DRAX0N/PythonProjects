#import asyncio
#
#async def fetch_data(name, delay):
#    print(f"Start {name}")
#    await asyncio.sleep(delay)  # symulacja I/O
#    print(f"Koniec {name}")
#
#async def main():
#    await asyncio.gather(
#        fetch_data("A", 2),
#        fetch_data("B", 1),
#        fetch_data("C", 3)
#    )
#
#asyncio.run(main())
#print("======================================")
#import threading
#import time
#
#def task(name, delay):
#    print(f"Start {name}")
#    time.sleep(delay)
#    print(f"Koniec {name}")
#
#threads = []
#for i in range(3):
#    t = threading.Thread(target=task, args=(f"Thread-{i}", 2))
#    t.start()
#    threads.append(t)
#
#for t in threads:
#    t.join()

#print("======================================")

import multiprocessing

def cpu_intensive(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    numbers = [10_000_000] * 4
    with multiprocessing.Pool() as pool:
        results = pool.map(cpu_intensive, numbers)
    print(results)