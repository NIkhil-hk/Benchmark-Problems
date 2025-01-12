from threading import Thread
import time

def square_range(start, end, result, index):
    result[index] = sum(n * n for n in range(start, end))

if __name__ == '__main__':
    range_limit = 10_000_000
    num_threads = 4
    step = range_limit // num_threads
    result = [0] * num_threads

    threads = []
    start_time = time.time()

    for i in range(num_threads):
        t = Thread(target=square_range, args=(i * step, (i + 1) * step, result, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_sum = sum(result)
    end_time = time.time()

    print(f"Sum of squares completed in {end_time - start_time:.4f} seconds.")
