cantidadU = int(input("Cantidad de elementos del conjunto Universal: "))

conjuntoU = set()
for i in range(cantidadU):
    elemento= float(input(f"Elemento {i + 1}: "))
    conjuntoU.add(elemento)

print("U = ", conjuntoU)

cantidadA = int(input("Cantidad de elementos del conjunto A: "))

conjuntoA = set()
for i in range(cantidadA):
    elemento= float(input(f"Elemento {i + 1}: "))
    conjuntoA.add(elemento)

print("A = ", conjuntoA)

if conjuntoU >= conjuntoA:
    
    x = (conjuntoU.union(conjuntoA)).intersection(conjuntoA)

    y = (conjuntoU.intersection(conjuntoA)).symmetric_difference(conjuntoA)

    z = (conjuntoU.difference(conjuntoA)).symmetric_difference(conjuntoA)

    print("La primera respuesta es: ", x)
    print("La segunda respuesta es: ", y)
    print("La tercera respuesta es: ", z)

else:
    print ("El conjunto A no es un subconjunto del conjunto Universal")



