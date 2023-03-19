import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Definimos la variable independiente
x = sp.Symbol('x')

# Función que calcula el límite de una función dada en un punto dado
def calcular_limite(funcion, punto):
    return sp.limit(funcion, x, punto)

# Función que grafica una función dada, su límite en un punto y la línea vertical del punto
def graficar_limite(funcion, punto):
    # Convertimos la función en una expresión de SymPy
    expr_funcion = sp.sympify(funcion)
    
    # Calculamos el límite en el punto dado
    limite = calcular_limite(expr_funcion, punto)
    
    # Definimos un rango de valores de x para la gráfica
    x_vals = np.linspace(punto-10, punto+10, 1000)
    
    # Convertimos la función en una función de NumPy
    np_funcion = sp.lambdify(x, expr_funcion, 'numpy')
    
    # Evaluamos la función en el rango de valores de x
    y_vals = np_funcion(x_vals)
    
    # Creamos la figura y los ejes de la gráfica
    fig, ax = plt.subplots()
    
    # Graficamos la función
    ax.plot(x_vals, y_vals, label='Función')
    
    # Graficamos la línea vertical del punto
    ax.axvline(punto, linestyle='--', color='grey', label='Punto')
    
    # Graficamos el límite en el punto
    ax.axhline(limite, linestyle='--', color='red', label='Límite')
    
    # Agregamos leyendas y título a la gráfica
    ax.legend()
    ax.set_title('Gráfica de la función y su límite en el punto ' + str(punto))
    
    # Mostramos la gráfica
    plt.show()

# Función que permite al usuario introducir la función y el punto
def main():
    # Pedimos la función al usuario
    funcion = input("Introduce la función: ")
    
    # Pedimos el punto al usuario
    punto = float(input("Introduce el punto: "))
    
    # Llamamos a la función que grafica la función y el límite
    graficar_limite(funcion, punto)

# Ejecutamos el programa
if __name__ == '__main__':
    main()
