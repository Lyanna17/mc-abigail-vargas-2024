import matplotlib.pyplot as plt

# Datos
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [15, 11, 13, 7, 9, 6, 5, 2]

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

print("Pendiente (m):", m)
print("Intersección (b):", b)

regre_y = [m * x + b for x in X]

#Graficar
plt.scatter(X, Y, color='blue', label='Datos originales') 
plt.plot(X, regre_y, color='red', label='Línea de regresión') 
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()