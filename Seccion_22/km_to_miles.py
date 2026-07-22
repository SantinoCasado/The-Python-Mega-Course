from tkinter import *                           # Tkinter es una biblioteca de interfaz gráfica de usuario para aplicaciones de escritorio

def km_to_miles():                                # Define la función para convertir kilómetros a millas
    miles = float(e1_value.get()) * 1.6           # Obtiene el valor ingresado en el campo de entrada
    t1.insert(END, miles)                         # Inserta el resultado de la conversión en el área de texto               



window = Tk()                                                       # Crea la ventana principal de la aplicación
window.geometry("400x300")                                          # Define el tamaño de la ventana (ancho x alto)

window.title("Mi Aplicación de Escritorio")                         # Establece el título de la ventana


b1 = Button(window, text="Convertir", command=km_to_miles)          # Crea un botón con el texto "¡Confirma!" en la ventana principal
b1.grid(row=0, column=0)                                            # Ubica el botón en la posición (0,1) de una cuadrícula dentro de la ventana


e1_value = StringVar()                                               # Crea una variable de cadena para almacenar el valor del campo de entrada
e1 = Entry(window, textvariable=e1_value)                            # Crea un campo de entrada de texto en la ventana principal
e1.grid(row=0, column=1)                                             # Ubica el campo de entrada en la posición (0,0) de una cuadrícula dentro de la ventana

t1 = Text(window, height=1, width=20)                                # Crea un área de texto con una altura de 5 líneas y un ancho de 30 caracteres
t1.grid(row=0, column=2)                                             # Ubica el área de texto en la posición (2,0) de una cuadrícula dentro de la ventana

window.mainloop()                                                    # Inicia el bucle principal de la aplicación para mostrar la ventana y esperar interacciones del usuario