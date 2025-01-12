from multiprocessing import Pool
import time

def square(n):
    return n * n

if __name__ == '__main__':
    range_limit = 10_000_000
    start_time = time.time()

    with Pool(processes=4) as pool:
        result = sum(pool.map(square, range(range_limit)))

    end_time = time.time()
    print(f"Sum of squares completed in {end_time - start_time:.4f} seconds.")
