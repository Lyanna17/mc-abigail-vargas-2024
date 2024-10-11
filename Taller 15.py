def gauss_jordan(A):
    n = len(A)
    
    for i in range(n):
        pivote = A[i][i]
        for k in range(n + 1):
            A[i][k] /= pivote
        
        for j in range(n):
            if i != j:
                factor = A[j][i]
                for k in range(n + 1):
                    A[j][k] -= factor * A[i][k]
    
    soluciones = [A[i][-1] for i in range(n)]
    return soluciones

A = [
    [1, 0, 1, 5],    # x1 + x3 = 5
    [3, 4, 3, 23],   # 3x1 + 4x2 + 3x3 = 23
    [4, 1, 0, 30]    # 4x1 + x2 = 30
]

solucion = gauss_jordan(A)

x1, x2, x3 = solucion
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")

