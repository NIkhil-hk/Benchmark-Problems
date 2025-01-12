cimport cython
from cython.parallel import prange

@cython.boundscheck(False)
@cython.wraparound(False)
def sum_of_squares(int limit):
    cdef int n, total = 0
    for n in prange(limit, nogil=True):
        total += n * n
    return total
