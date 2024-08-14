cantidadA = int(input("Cantidad de elementos del conjunto A: "))

conjuntoA = set()
for i in range(cantidadA):
    elemento= float(input(f"Elemento {i + 1}: "))
    conjuntoA.add(elemento)

print("A = ", conjuntoA)

cantidadB = int(input("Cantidad de elementos del conjunto B: "))

conjuntoB = set()
for i in range(cantidadB):
    elemento= float(input(f"Elemento {i + 1}: "))
    conjuntoB.add(elemento)

print("B = ", conjuntoB)

print("¿Qué operación deseas realizar? (1. Unión, 2. Intersección, 3. Diferencia, 4. Diferencia Simetrica)")
operacion= input("¿Cual desea?: ")

if operacion == "1" :
    resultado = conjuntoA.union(conjuntoB)
elif operacion == "2" :
    resultado = conjuntoA.intersection(conjuntoB)
elif operacion == "3" :
    resultado = conjuntoA.difference(conjuntoB)
elif operacion == "4" :
    resultado = conjuntoA.symmetric_difference(conjuntoB)

else:
    print("La operación no es valida")


print("El resultado es: ", resultado)



