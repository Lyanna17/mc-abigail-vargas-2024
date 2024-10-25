import math
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]  
y = [0.8, 1.2, 1.7, 2.2, 3.2, 4.5]  

log_y = [math.log(yi) for yi in y]


n = len(x)
Sx = sum(x)
Sy = sum(log_y)
Sxy = sum(x[i] * log_y[i] for i in range(n))
Sxx = sum(xi ** 2 for xi in x)

b = (n * Sxy - Sx * Sy) / (n * Sxx - Sx ** 2)
a = math.exp((Sy - b * Sx) / n)

log_y_ = [math.log(a) + b * xi for xi in x]

res = [y[i] - log_y_[i] for i in range(n)]
suma_res_cuad = sum(res ** 2 for res in res)
est_error = (suma_res_cuad / (n - 2)) ** 0.5

#Graficar
plt.scatter(x, y, color='blue', label= "Datos originales") 
plt.plot(x, log_y_, color='red', label= "Ajuste exponencial") 
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Regresión Exponencial")
plt.legend()
plt.show()

print(f"Parámetros del modelo: a = {a}, b = {b}")
print(f"Error estándar de estimación: {est_error}")