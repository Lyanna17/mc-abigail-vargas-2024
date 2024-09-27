import math
from math import e

x = 0,405
base = 0,4
h = (x - base)

valor_real = e**-x

resultado = 0


for i in range(16):
    valor_ant = resultado
    
    termino = (e**-base / math.factorial(i)) * (h**i)
    
    if i % 2 == 0:
        resultado +=termino
    else:
        resultado -=termino

    error=abs((resultado - valor_ant)/resultado)*100
    print(f"{i:<6} {resultado:<15.10f} {error}")



    






