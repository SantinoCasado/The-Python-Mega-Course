from tkinter import *                           # Tkinter es una biblioteca de interfaz gráfica de usuario para aplicaciones de escritorio

def convert_kg():                                                   # Define la función para convertir kilómetros a millas
    grams = float(e1_value.get()) * 1000                            # Obtiene el valor ingresado en el campo de entrada
    t1.delete('1.0', END)                                           # Limpia el área de texto antes de insertar nuevo valor
    t1.insert(END, grams)                                           # Inserta el resultado de la conversión en el área de texto

    pounds = float(e1_value.get()) * 2.20462                        # Obtiene el valor ingresado en el campo de entrada
    t2.delete('1.0', END)                                           # Limpia el área de texto antes de insertar nuevo valor
    t2.insert(END, pounds)                                          # Inserta el resultado de la conversión en el área de texto

    ounces = float(e1_value.get()) * 35.274                         # Obtiene el valor ingresado en el campo de entrada
    t3.delete('1.0', END)                                           # Limpia el área de texto antes de insertar nuevo valor
    t3.insert(END, ounces)                                          # Inserta el resultado de la conversión en el área de texto               

window = Tk()                                                       # Crea la ventana principal de la aplicación
window.geometry("500x100")                                          # Define el tamaño de la ventana (ancho x alto)

window.title("Conversor de kilogramos")                             # Establece el título de la ventana


b1 = Button(window, text="Convertir", command=convert_kg)           # Crea un botón con el texto "Convertir" en la ventana principal
b1.grid(row=0, column=2)                                            # Ubica el botón en la posición (0,1) de una cuadrícula dentro de la ventana

l1 = Label(window, text="Kilogramos")                               # Crea una etiqueta con el texto "Ingresa kilómetros" en la ventana principal
l1.grid(row=0, column=0)                                            # Ubica la etiqueta en la posición (1,0) de una cuadrícula dentro de la ventana
l2 = Label(window, text="Gramos")                                   # Crea una etiqueta con el texto "Ingresa kilómetros" en la ventana principal
l2.grid(row=2, column=0)                                            # Ubica la etiqueta en la posición (1,0) de una cuadrícula dentro de la ventana
l3 = Label(window, text="Pounds")                                   # Crea una etiqueta con el texto "Ingresa kilómetros" en la ventana principal
l3.grid(row=2, column=1)                                            # Ubica la etiqueta en la
l4 = Label(window, text="Ounces")                                   # Crea una etiqueta con el texto "Ingresa kilómetros" en la ventana principal
l4.grid(row=2, column=2)                                            # Ubica la etiqueta en la


e1_value = StringVar()                                              # Crea una variable de cadena para almacenar el valor del campo de entrada
e1 = Entry(window, textvariable=e1_value)                           # Crea un campo de entrada de texto en la ventana principal
e1.grid(row=0, column=1)                                            # Ubica el campo de entrada en la posición (0,0) de una cuadrícula dentro de la ventana
t1 = Text(window, height=1, width=20)                               # Crea un área de texto con una altura de 5 líneas y un ancho de 30 caracteres
t1.grid(row=1, column=0)                                            # Ubica el área de texto en la posición (2,0) de una cuadrícula dentro de la ventana
t2 = Text(window, height=1, width=20)                               # Crea un área de texto con una altura de 5 líneas y un ancho de 30 caracteres
t2.grid(row=1, column=1)                                            # Ubica el área de texto en la posición (2,1) de una cuadrícula dentro de la ventana
t3 = Text(window, height=1, width=20)                               # Crea un área de texto con una altura de 5 líneas y un ancho de 30 caracteres
t3.grid(row=1, column=2)                                            # Ubica el área de texto en la posición (2,2) de una cuadrícula dentro de la ventana
window.mainloop()                                                   # Inicia el bucle principal de la aplicación para mostrar la ventana y esperar interacciones del usuario