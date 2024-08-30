import math

es = (0.5 * 10**-8) * 100
ea = 100

x = float(input("Escriba un ángulo en radianes: "))
cosx = 1

iteraciones = 1
potencia= 2
signo = -1


while ea >= es:
    vant= cosx

    cosx += signo * (x**potencia / math.factorial(potencia))

    ea = abs((cosx - vant)/ cosx) * 100

    signo *= -1
    iteraciones += 1
    potencia +=2


print("El valor estimado es: ", cosx ,"El error aproximado relativo porcentual es de: ", ea, "el número de iteraciones realizadas fue de: ", iteraciones)



