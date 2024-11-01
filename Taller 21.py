import matplotlib.pyplot as plt


x = [1, 3, 5, 7, 9, 11, 13]
y = [14.9, 3.6, -2, -3.6, -2.4, 4.4, 14.4]


n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum(xi**2 for xi in x)
sum_x3 = sum(xi**3 for xi in x)
sum_x4 = sum(xi**4 for xi in x)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2y = sum(x[i]**2 * y[i] for i in range(n))


A = [[sum_x4, sum_x3, sum_x2],
     [sum_x3, sum_x2, sum_x],
     [sum_x2, sum_x, n]]

B = [sum_x2y, sum_xy, sum_y]

def gauss_jordan(A, B):
    n = len(B)
    for i in range(n):
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        B[i] /= factor

        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x

a, b, c = gauss_jordan(A, B)


y_fit = [a * xi**2 + b * xi + c for xi in x]


ss_tot = sum((yi - sum(y) / n)**2 for yi in y)
ss_res = sum((y[i] - y_fit[i])**2 for i in range(n))
r_squared = 1 - (ss_res / ss_tot)


# Graficar
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_fit, color='red', label='Ajuste cuadrático')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Ajuste de polinomio de segundo grado\nCoeficiente de determinación $R^2 = {r_squared:.4f}$')
plt.legend()
plt.show()
