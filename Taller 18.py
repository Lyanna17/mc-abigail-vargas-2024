import matplotlib.pyplot as plt

# Datos
X = [1, 2, 3, 4, 5, 6, 7]
Y = [0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9]

n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

num = 0  # Numerador
denom = 0  # Denominador

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2

m = num / denom
b = mean_y - m * mean_x

st = sum((Yi - mean_y)**2 for Yi in Y)
sy = (st/(n-1)) ** 0.5

sr = sum((b + m * X[i] - mean_y) ** 2 for i in range (n))
se = st - sr

error= (se / (n -2)) ** 0.5

r2 = ((st - sr)/st)
r= ((r2) ** 0.5) * 100


print("Pendiente (m):", m)
print("Intersección (b):", b)
print("Desviación estandar: ", sy)
print("Error: ", error)
print("Coeficiente de determinación r2: ", r2)
print("Coeficiente de determinación r: ", r)

regre_y = [m * x + b for x in X]

#Graficar
plt.scatter(X, Y, color='blue', label='Datos originales') 
plt.plot(X, regre_y, color='red', label='Línea de regresión') 
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()