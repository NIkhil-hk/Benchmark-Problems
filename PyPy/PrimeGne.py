import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start_time = time.time()
primes = [n for n in range(2, 1000000) if is_prime(n)]
end_time = time.time()

print(f"Prime number generation completed in {end_time - start_time:.4f} seconds.")
