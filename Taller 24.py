def multiplicar(a, b):
    longitud = len(a) + len(b)-1
    resultado = [0] * longitud

    for i in range(len(a)):
        for j in range(len(b)):
            resultado[i+j] += a[i] * b[j]
    
    return resultado

def terminos(x , y):
    n = len(x)
    resultado = [0] * n

    for i in range(n):
        numerador = [1]
        denominador =1
        for j in range(n):
            if i != j:
                actual = [-x[j], 1]
                numerador = multiplicar(numerador, actual)
                denominador *= (x[i] - x [j])

        for j in range(len(numerador)):
            numerador[j] *= y [i]/denominador

        for j  in range(len(numerador)):
            if j < len(resultado):
                resultado[j] += numerador[j]

    return resultado

def polinomio(coeficientes, x):
    resultado = 0
    for i in range(len(coeficientes)):
        resultado += coeficientes[i] * (x ** i)

    return resultado

def main():
    x = [0, 1, 2, 3, 4]
    y = [0, 0.9, -1, -2.3, 1.8]

    coeficientes = terminos(x, y)
    print("Coeficientes del polinomio: ")
    for i in range(len(coeficientes)):
        print(f"Coeficiente x {i}: {coeficientes [i]}")

    print("Verificamos los puntos originales: ")
    for i in range(len(x)):
        y_calculado = polinomio(coeficientes, x[i])
        print(f"x = {x[i]}: y_original = {y[i]}, y_calculado = {y_calculado}") 


if __name__ == '__main__':
    main()