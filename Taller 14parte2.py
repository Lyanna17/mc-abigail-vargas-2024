m=int(input("Ingrese el número de filas de las matrices: "))
n=int(input("Ingrese el número de las columnas de las matrices: "))

Matriz1=[]
Matriz2=[]

print("Ingrese los elementos de la matriz A: ")
for i in range(m):
    fila_a=[]
    for j in range(n):
        valor=float(input(f"Elemento ({i+1}, {i+1}): "))
        fila_a.append(valor)
    Matriz1.append(fila_a)

print(Matriz1)

print("Ingrese los elementos de la matriz B: ")
for i in range(m):
    fila_b=[]
    for j in range(n):
        valor=float(input(f"Elemento ({i+1}, {i+1}): "))
        fila_b.append(valor)
    Matriz2.append(fila_b)

print(Matriz2)

print("Operaciones: ")
print("2A: ")
A2=[]
for i in range(m):
    fila_a=[]
    for j in range(n):
        fila_a.append(2*Matriz1[i][j])
    A2.append(fila_a)

print(A2)
    
print("3B: ")
B3=[]
for i in range(m):
    fila_b=[]
    for j in range(n):
        fila_b.append(3*Matriz2[i][j])
    B3.append(fila_b)

print(B3)

print("A + B: ")
A_mas_B=[]
for i in range(m):
    suma=[]
    for j in range(n):
        suma.append(Matriz1[i][j]+Matriz2[i][j])
    A_mas_B.append(suma)

print(A_mas_B)

print("A x B: ")
A_por_B=[]
for i in range(m):
    producto=[]
    for j in range(n):
        Product=0
        for k in range(n):
            Product += Matriz1[i][k] * Matriz2[k][j]
        producto.append(Product)
    A_por_B.append(producto)

print(A_por_B)
