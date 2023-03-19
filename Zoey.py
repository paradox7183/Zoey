import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from scipy.optimize import linprog

init_printing()

# Función para resolver derivadas
def resolver_derivadas():
    x = symbols('x')
    funcion = input('Function: ')
    derivada = diff(funcion, x)
    print('Diff:', derivada)
    graficar_funcion(funcion, derivada)

# Función para resolver integrales
def resolver_integrales():
    x = symbols('x')
    funcion = input('Function ')
    integral = integrate(funcion, x)
    print('Integral:', integral)
    graficar_funcion(funcion, integral)

# Función para graficar una función y su derivada o integral
def graficar_funcion(funcion, derivada_o_integral):
    x = symbols('x')
    funcion_lambdify = lambdify(x, funcion, 'numpy')
    derivada_o_integral_lambdify = lambdify(x, derivada_o_integral, 'numpy')
    x_vals = np.linspace(-10, 10, 1000)
    y_vals_funcion = funcion_lambdify(x_vals)
    y_vals_derivada_o_integral = derivada_o_integral_lambdify(x_vals)
    
    fig, axs = plt.subplots(2, sharex=True)
    fig.suptitle('Functions Graphic and the derivative or integral graph')
    axs[0].plot(x_vals, y_vals_funcion, label='Función')
    axs[1].plot(x_vals, y_vals_derivada_o_integral, label='Diff or Integral')
    axs[0].legend()
    axs[1].legend()
    
    # Establecer los límites de los ejes x e y para mostrar el plano cartesiano completo
    axs[0].set_xlim(x_vals[0], x_vals[-1])
    axs[0].set_ylim(y_vals_funcion.min() - abs(y_vals_funcion.min() * 0.1), y_vals_funcion.max() + abs(y_vals_funcion.max() * 0.1))
    axs[1].set_xlim(x_vals[0], x_vals[-1])
    axs[1].set_ylim(y_vals_derivada_o_integral.min() - abs(y_vals_derivada_o_integral.min() * 0.1), y_vals_derivada_o_integral.max() + abs(y_vals_derivada_o_integral.max() * 0.1))
    
    plt.show()

    # Función para resolver inecuaciones
def resolver_inecuaciones():
    x = symbols('x')
    inecuacion = input('Inequality: ')
    solucion = solve(inecuacion)
    print('Solution:', solucion)
    graficar_inecuacion(inecuacion)

# Función para graficar una inecuación
def graficar_inecuacion(inecuacion):
    x = symbols('x')
    inecuacion_lambdify = lambdify(x, inecuacion, 'numpy')
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = inecuacion_lambdify(x_vals)
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='Inequation')
    ax.fill_between(x_vals, y_vals, where=(y_vals>=0), color='green', alpha=0.3, label='Solución')
    ax.fill_between(x_vals, y_vals, where=(y_vals<0), color='red', alpha=0.3, label='No solución')
    ax.legend()
    
    # Establecer los límites de los ejes x e y para mostrar el plano cartesiano completo
    ax.set_xlim(x_vals[0], x_vals[-1])
    ax.set_ylim(y_vals.min() - abs(y_vals.min() * 0.1), y_vals.max() + abs(y_vals.max() * 0.1))
    
    plt.show()

# Menú principal
while True:
    print ("""
 ________                         __     
/\_____  \                       /\ \    
\/____//'/'    ___     __  __  __\ \ \   
     //'/'    / __`\ /'__`\\ \/\ \\ \ \  
    //'/'___ /\ \L\ \\  __/ \ \_\ \\ \_\ 
    /\_______\ \____/ \____\/`____ \\/\_\
    \/_______/\/___/ \/____/`/___/> \\/_/
                               /\___/    
                               \/__/     1.0
Mathematic python framework for engineers

    1.- Derivatives
    2.- Integral
    3.- Inequality
    4.- Dantzig's simplex algorithm  (Linear Programming)
    5.- Limits
    6.- Exit
    """)
    opcion = input('Chosse an option>>> ')
    if opcion == '1':
        resolver_derivadas()
    elif opcion == '2':
        resolver_integrales()
    elif opcion == '3':
        resolver_inecuaciones()
    elif opcion == '4':
        exec(open("Simplex.py").read())
    elif opcion == '5':
        exec(open("limit.py").read())
    elif opcion == '6':
        break
    else:
        print('No valid option, try again')
