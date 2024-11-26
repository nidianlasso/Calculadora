import tkinter as tk
from tkinter import PhotoImage
from tkinter import Frame, Grid

#CREACION DE LA VENTANA PRINCIPAL
window = tk.Tk()

#CAMBIAR NOMBRE DE LA VENTANA
window.title("CALCULADORA")

#CONFIGURAR TAMANO DE LA VENTANA
window.geometry("300x500")
#TAMANO MINIMO Y MAXIMO
window.minsize(200, 400)
window.maxsize(400, 600)

# #AGREGAR MENSAJE DE BIENVENIDA
# welcome_message = tk.Label(window, text="Bienvenido a mi aplicación")
# welcome_message.grid()

#CAMBIAR COLOR DE LA VENTANA
window.configure(bg='lightblue')

#CAMBIAR EL ICONO DE LA VENTANA POR UNA IMAGEN
icono = PhotoImage(file='C:/Users/nidia/Documents/Cursos/Python/Calculator/calculadora.png')
window.iconphoto(True, icono)

#MOSTRAR PANTALLA DE LA CALCULADORA
screen_main = Frame()
screen_main =tk.Entry(window, justify='center')
screen_main.grid(row=0, column=0, columnspan=4)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (texto, fila, columna) in botones:
    if texto == '=':
        btn = tk.Button(window, text=texto)
    elif texto == 'C':
        btn = tk.Button(window, text=texto)
    else:
        btn = tk.Button(window, text=texto)
    btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew") 





#EJECUTA LA CALCULADORA
window.mainloop()
