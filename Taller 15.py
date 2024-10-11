import numpy as np

A = np.array([[1, 0, 1, 5], 
              [3, 4, 3, 23], 
              [4, 1, 0, 30]], dtype=float)

def gauss_jordan(A):
    n = len(A)
    for i in range(n):
        # Hacer el pivote igual a 1
        A[i] = A[i] / A[i][i]
        for j in range(n):
            if i != j:
                A[j] = A[j] - A[j][i] * A[i]
    return A

solucion = gauss_jordan(A)

print(f"x1 = {solucion[0][-1]}")
print(f"x2 = {solucion[1][-1]}")
print(f"x3 = {solucion[2][-1]}")
