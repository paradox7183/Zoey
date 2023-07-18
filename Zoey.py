import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

init_printing()

# Función para resolver derivadas
def resolver_derivadas(funcion):
    x = symbols('x')
    derivada = diff(funcion, x)
    solucion_text.set('Diff: ' + str(derivada))
    graficar_funcion(funcion, derivada)

# Función para resolver integrales
def resolver_integrales(funcion):
    x = symbols('x')
    integral = integrate(funcion, x)
    solucion_text.set('Integral: ' + str(integral))
    graficar_funcion(funcion, integral)

# Función para resolver inecuaciones
def resolver_inecuaciones(inecuacion):
    x = symbols('x')
    solucion = solve(inecuacion)
    solucion_text.set('Solution: ' + str(solucion))
    graficar_inecuacion(inecuacion)

# Función para resolver límites
def resolver_limites(funcion, valor):
    x = symbols('x')
    limite = limit(funcion, x, valor)
    solucion_text.set('Limit: ' + str(limite))

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

    # Set the x and y-axis limits to display the complete Cartesian plane
    axs[0].set_xlim(x_vals[0], x_vals[-1])
    axs[0].set_ylim(y_vals_funcion.min() - abs(y_vals_funcion.min() * 0.1), y_vals_funcion.max() + abs(y_vals_funcion.max() * 0.1))
    axs[1].set_xlim(x_vals[0], x_vals[-1])
    axs[1].set_ylim(y_vals_derivada_o_integral.min() - abs(y_vals_derivada_o_integral.min() * 0.1), y_vals_derivada_o_integral.max() + abs(y_vals_derivada_o_integral.max() * 0.1))

    plt.pause(0.001)  # Pause to allow the figure to be displayed

# Función para graficar una inecuación
def graficar_inecuacion(inecuacion):
    x = symbols('x')
    inecuacion_lambdify = lambdify(x, inecuacion, 'numpy')
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = inecuacion_lambdify(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='Inequation')
    ax.fill_between(x_vals, y_vals, where=(y_vals >= 0), color='green', alpha=0.3, label='Solución')
    ax.fill_between(x_vals, y_vals, where=(y_vals < 0), color='red', alpha=0.3, label='No solución')
    ax.legend()

    # Set the x and y-axis limits to display the complete Cartesian plane
    ax.set_xlim(x_vals[0], x_vals[-1])
    ax.set_ylim(y_vals.min() - abs(y_vals.min() * 0.1), y_vals.max() + abs(y_vals.max() * 0.1))

    plt.pause(0.001)  # Pause to allow the figure to be displayed

# Function to handle the button click event
def on_calculate_clicked():
    selected_option = combo_option.get()
    input_value = entry_function.get()

    if selected_option == 'Derivatives':
        resolver_derivadas(input_value)
    elif selected_option == 'Integral':
        resolver_integrales(input_value)
    elif selected_option == 'Inequality':
        resolver_inecuaciones(input_value)
    elif selected_option == 'Limits':
        value = entry_value.get()
        resolver_limites(input_value, float(value))

    # Update the solution label with the new result
    label_result.config(text=solucion_text.get())

# Create the main application window
root = tk.Tk()
root.title("Zoey calculator!")
root.geometry("650x700")

# ASCII Art for the title
ascii_art = r"""                                                                                   
ZZZZZZZZZZZZZZZZZZZ                                                             !!! 
Z:::::::::::::::::Z                                                            !!:!!
Z:::::::::::::::::Z                                                            !:::!
Z:::ZZZZZZZZ:::::Z                                                             !:::!
ZZZZZ     Z:::::Z     ooooooooooo       eeeeeeeeeeee  yyyyyyy           yyyyyyy!:::!
        Z:::::Z     oo:::::::::::oo   ee::::::::::::ee y:::::y         y:::::y !:::!
       Z:::::Z     o:::::::::::::::o e::::::eeeee:::::eey:::::y       y:::::y  !:::!
      Z:::::Z      o:::::ooooo:::::oe::::::e     e:::::e y:::::y     y:::::y   !:::!
     Z:::::Z       o::::o     o::::oe:::::::eeeee::::::e  y:::::y   y:::::y    !:::!
    Z:::::Z        o::::o     o::::oe:::::::::::::::::e    y:::::y y:::::y     !:::!
   Z:::::Z         o::::o     o::::oe::::::eeeeeeeeeee      y:::::y:::::y      !!:!!
ZZZ:::::Z     ZZZZZo::::o     o::::oe:::::::e                y:::::::::y        !!! 
Z::::::ZZZZZZZZ:::Zo:::::ooooo:::::oe::::::::e                y:::::::y             
Z:::::::::::::::::Zo:::::::::::::::o e::::::::eeeeeeee         y:::::y          !!! 
Z:::::::::::::::::Z oo:::::::::::oo   ee:::::::::::::e        y:::::y          !!:!!
ZZZZZZZZZZZZZZZZZZZ   ooooooooooo       eeeeeeeeeeeeee       y:::::y            !!! 
                                                            y:::::y                 
                                                           y:::::y                  
                                                          y:::::y                   
                                                         y:::::y                    
                                                        yyyyyyy                     
    2.0
Mathematic python framework for engineers
"""

# Function to get the ASCII art as an ImageTk object
def get_ascii_art_image():
    if not hasattr(get_ascii_art_image, "ascii_art_image"):
        ascii_art_image = Image.new("RGB", (550, 420), color="white")
        ascii_art_draw = ImageDraw.Draw(ascii_art_image)
        ascii_art_draw.text((10, 10), ascii_art, fill="black", font=ImageFont.load_default())
        get_ascii_art_image.ascii_art_image = ImageTk.PhotoImage(ascii_art_image)
    return get_ascii_art_image.ascii_art_image

# Label to display ASCII art
label_ascii_art = tk.Label(root, image=get_ascii_art_image())
label_ascii_art.pack(pady=10)

label_title = tk.Label(root, text="Choose an option:", font=("Arial", 14))
label_title.pack(pady=10)

combo_option = ttk.Combobox(root, values=["Derivatives", "Integral", "Inequality", "Limits"])
combo_option.pack(pady=5)

label_function = tk.Label(root, text="Function:")
label_function.pack(pady=5)

entry_function = tk.Entry(root)
entry_function.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate", command=on_calculate_clicked)
button_calculate.pack(pady=10)

label_solution = tk.Label(root, text="Solution:")
label_solution.pack(pady=5)

solucion_text = tk.StringVar()
label_result = tk.Label(root, textvariable=solucion_text)
label_result.pack(pady=5)

label_limit_value = tk.Label(root, text="Value (for Limits):")
label_limit_value.pack(pady=5)

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.pack(pady=5)

root.mainloop()
