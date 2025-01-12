from random import random
import time

# Generate two 300x300 matrices
matrix1 = [[random() for _ in range(300)] for _ in range(300)]
matrix2 = [[random() for _ in range(300)] for _ in range(300)]
result = [[0] * 300 for _ in range(300)]

start_time = time.time()
for i in range(300):
    for j in range(300):
        for k in range(300):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
end_time = time.time()

print(f"Matrix multiplication completed in {end_time - start_time:.4f} seconds.")
