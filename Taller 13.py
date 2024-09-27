import math
from math import e

x = 0,405
h = 0,4

valor_real = e**-x

resultado = 0

error = []

for i in range(16):
    termino = (valor_real * ((x - h) ** i) / math.factorial(i)) * (-1) ** i
    valor_real += termino

    error_relativo = abs((valor_real - resultado) / valor_real) * 100
    error.append(error_relativo)

    print(f"Orden: {i} ", "Estimación: {resultado}", "Error: {error_relativo}")



    






