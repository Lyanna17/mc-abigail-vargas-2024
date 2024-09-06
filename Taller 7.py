import math

def exp_neg(x, tolerance=1e-8):
    term = 1
    result = 1
    n = 1
    while abs(term) > tolerance:
        term *= -x / n
        result += term
        n += 1
    exact_value = math.exp(-x)
    error = abs(exact_value - result) / exact_value * 100
    return result, error, n

x = 0.55
approximation, error, iterations = exp_neg(x)

print(f"Aproximación 1 (Taylor) para e^{-x} con x = {x}:")
print(f"Valor calculado: {approximation:.8f}")
print(f"Último error relativo porcentual: {error:.8f}%")
print(f"Número de iteraciones: {iterations}")

def exp_x(x, tolerance=1e-8):
    term = 1
    result = 1
    n = 1
    while abs(term) > tolerance:
        term *= x / n
        result += term
        n += 1
    exp_x = result
    exp_neg_x = 1 / exp_x
    exact_value = math.exp(-x)
    error = abs(exact_value - exp_neg_x) / exact_value * 100
    return exp_neg_x, error, n

x = 0.55
approximation, error, iterations = exp_x(x)

print(f"Aproximación 2 (Usando e^x) para e^{-x} con x = {x}:")
print(f"Valor calculado: {approximation:.8f}")
print(f"Último error relativo porcentual: {error:.8f}%")
print(f"Número de iteraciones: {iterations}")