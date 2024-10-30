import math
import matplotlib.pyplot as plt

# Datos de la tabla
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2.2, 3.3, 3.7, 4.0, 4.2, 4.4, 4.5, 4.7]


log_x = [math.log(xi) for xi in x]
log_y = [math.log(yi) for yi in y]


n = len(x)
sum_log_x = sum(log_x)
sum_log_y = sum(log_y)
sum_log_x2 = sum(xi ** 2 for xi in log_x)
sum_log_x_log_y = sum(log_x[i] * log_y[i] for i in range(n))


b_pot = (n * sum_log_x_log_y - sum_log_x * sum_log_y) / (n * sum_log_x2 - sum_log_x ** 2)
ln_a_pot = (sum_log_y - b_pot * sum_log_x) / n
a_pot = math.exp(ln_a_pot) 


y_potencia = [a_pot * (xi ** b_pot) for xi in x]


def calcular_error(alpha, B, x, y):
    error = 0
    for i in range(len(x)):
        y_pred = alpha * (x[i] / (B + x[i]))
        error += (y[i] - y_pred) ** 2
    return error

mejor_a = 0
mejor_B = 0
menor_error = float('inf')

for alpha in range(0, 100):
    for B in range(0, 100):
        alpha_val = alpha / 10  
        B_val = B / 10
        error = calcular_error(alpha_val, B_val, x, y)
        if error < menor_error:
            menor_error = error
            mejor_a = alpha_val
            mejor_B = B_val


y_crecimiento = [mejor_a * (xi / (mejor_B + xi)) for xi in x]


plt.scatter(x, y, label='Datos', color='black')
plt.plot(x, y_potencia, label=f'Ecuación de Potencias: y={a_pot:.2f}*x^{b_pot:.2f}', color='blue')
plt.plot(x, y_crecimiento, label=f'Razón de Crecimiento: y={mejor_a:.2f}*(x/({mejor_B:.2f}+x))', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de Modelos')
plt.show()