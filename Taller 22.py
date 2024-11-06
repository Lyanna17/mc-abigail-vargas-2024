x1 = [1, 1, 2, 3, 1, 2, 3, 3]
x2 = [0, 0.5, 0.5, 1, 1, 1.5, 1.5, 0.5]
y = [1.2, 4, 0.2, 0.6, 4.5, 4.6, 1.5, -2]


def mean(values):
    return sum(values) / len(values)


x1_mean = mean(x1)
x2_mean = mean(x2)
y_mean = mean(y)


sum_x1y = sum((x1[i] - x1_mean) * (y[i] - y_mean) for i in range(len(x1)))
sum_x2y = sum((x2[i] - x2_mean) * (y[i] - y_mean) for i in range(len(x2)))
sum_x1x2 = sum((x1[i] - x1_mean) * (x2[i] - x2_mean) for i in range(len(x1)))
sum_x1x1 = sum((x1[i] - x1_mean) ** 2 for i in range(len(x1)))
sum_x2x2 = sum((x2[i] - x2_mean) ** 2 for i in range(len(x2)))

b1 = (sum_x1y * sum_x2x2 - sum_x2y * sum_x1x2) / (sum_x1x1 * sum_x2x2 - sum_x1x2 ** 2)
b2 = (sum_x2y * sum_x1x1 - sum_x1y * sum_x1x2) / (sum_x1x1 * sum_x2x2 - sum_x1x2 ** 2)
b0 = y_mean - b1 * x1_mean - b2 * x2_mean


y_pred = [b0 + b1 * x1[i] + b2 * x2[i] for i in range(len(x1))]


SS_res = sum((y[i] - y_pred[i]) ** 2 for i in range(len(y)))
SS_tot = sum((y[i] - y_mean) ** 2 for i in range(len(y)))
r = (1 - SS_res / SS_tot) ** 0.5


print("Coeficientes de regresión:")
print("b0 =", b0)
print("b1 =", b1)
print("b2 =", b2)
print("Coeficiente de correlación múltiple (r):", r)