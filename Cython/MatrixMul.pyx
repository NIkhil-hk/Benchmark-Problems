cimport cython
from cython.parallel import prange
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def matrix_multiply(np.ndarray[np.float64_t, ndim=2] matrix1, 
                    np.ndarray[np.float64_t, ndim=2] matrix2):
    cdef int i, j, k
    cdef int size = matrix1.shape[0]
    cdef np.ndarray[np.float64_t, ndim=2] result = np.zeros((size, size), dtype=np.float64)
    
    for i in prange(size, nogil=True):
        for j in range(size):
            for k in range(size):
                result[i, j] += matrix1[i, k] * matrix2[k, j]
    
    return result
