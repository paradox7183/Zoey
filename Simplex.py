import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

# Solicitar al usuario los coeficientes de la función objetivo
c = []
n_variables = int(input("Ingrese el número de variables: "))
for i in range(n_variables):
    coef = float(input(f"Ingrese el coeficiente de la variable x{i}: "))
    c.append(-coef)

# Solicitar al usuario las restricciones
A = []
b = []
n_restricciones = int(input("Ingrese el número de restricciones: "))
for i in range(n_restricciones):
    restriccion = []
    print(f"Restricción {i+1}")
    for j in range(n_variables):
        coef = float(input(f"Ingrese el coeficiente de la variable x{j}: "))
        restriccion.append(coef)
    A.append(restriccion)
    b.append(float(input("Ingrese el lado derecho de la restricción: ")))

# Definir los límites de las variables
bounds = []
for i in range(n_variables):
    bounds.append((0, None))

# Resolver el problema utilizando el método simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Imprimir el resultado
print(res)

# Crear un gráfico
x = np.linspace(0, 10, 1000)
y = (c[0]*x + res.fun) / -c[1]

fig, ax = plt.subplots()
ax.plot(x, y, label='Función objetivo')
for i in range(n_restricciones):
    restriccion = A[i]
    rhs = b[i]
    x1 = np.linspace(0, 10, 1000)
    x2 = (rhs - restriccion[0]*x1) / restriccion[1]
    ax.fill_between(x1, x2, np.max(y), alpha=0.3, label=f'Restricción {i+1}')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.legend(loc='upper right')

plt.show()
