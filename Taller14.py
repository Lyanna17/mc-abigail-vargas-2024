tamaño = int(input("Digite el tamaño de los vectores: "))

vector1 = []
vector2 = []

product= 0

for i in range (tamaño):
    num1 = float(input(f"Digite los valores del primer vector: "))
    vector1.append(num1)

for i in range (tamaño):
    num2 = float(input(f"Digite los valores del segundo vector: "))
    vector2.append(num2)

for i in range (tamaño):
    product += vector1[i] * vector2[i]

print("El producto escalar de los dos vectores es de: ", product)


