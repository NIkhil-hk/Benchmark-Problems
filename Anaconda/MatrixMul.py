import numpy as np
import time

# Generate two 300x300 matrices
matrix1 = np.random.rand(300, 300)
matrix2 = np.random.rand(300, 300)

start_time = time.time()
result = np.dot(matrix1, matrix2)
end_time = time.time()

print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds.")
