cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def is_prime(int n):
    if n <= 1:
        return False
    cdef int i
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(int limit):
    cdef int n
    cdef list primes = []
    for n in range(2, limit):
        if is_prime(n):
            primes.append(n)
    return primes
