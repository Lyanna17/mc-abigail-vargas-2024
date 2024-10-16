def gauss_jordan_inverse(matrix):
    n = len(matrix)
    
    augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    
    for i in range(n):
       
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError("La matriz es singular y no tiene inversa.")
        for j in range(2 * n):
            augmented[i][j] /= pivot

        
        for j in range(n):
            if j != i:
                factor = augmented[j][i]
                for k in range(2 * n):
                    augmented[j][k] -= factor * augmented[i][k]

    
    inverse = [row[n:] for row in augmented]
    return inverse

def multiply_matrices(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
                return False
    return True


matrices = [
    [[3, 2, 2], [3, 1, -3], [1, 0, -2]],
    [[1, 2, 0, 4], [2, 0, -1, -2], [1, 1, -1, 0], [0, 4, 1, 0]]
]

for i, matrix in enumerate(matrices):
    try:
        inverse = gauss_jordan_inverse(matrix)
        print(f"Inversa de la matriz {i + 1}:")
        for row in inverse:
            print(row)

        identity = multiply_matrices(matrix, inverse)
        print(f"Producto de matriz {i + 1} y su inversa:")
        for row in identity:
            print(row)

        if is_identity(identity):
            print("El producto es una matriz identidad.\n")
        else:
            print("El producto no es una matriz identidad.\n")
    except ValueError as e:
        print(e)