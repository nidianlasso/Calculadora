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
route_icon = "C:/Users/nidia/Documents/Cursos/Python/Calculadora/Calculadora/calculadora.ico"
window.iconbitmap(route_icon)


#FUNCIONALIDADES DE LAS TECLAS
#VARIABLE QUE MUESTRA LO SI TIENE ALGO EL VISOR
expression = ""

#VARIABLE PARA ALMACENAR EL ESTADO DEL VISOR
state_calculator = False

#ACTUALIZAR LA PANTALLA SEGUN LO QUE ESCRIBA EL USUARIO
def pulsar_tecla(tecla):
    global expression

    expression+= str(tecla)
    visor_texto.set(expression)


def limpiar():
    global expression, state_calculator

    expression = ""
    visor_texto.set(expression)
    state_calculator= False


def calcular():
    global expression, state_calculator
    resultado = eval(expression)
    visor_texto.set(resultado)
    state_calculator= True
    print(f'El resultado es {resultado}')

for i in range (5):
    window.grid_rowconfigure(i, weight=1)
for i in range (4):
    window.grid_columnconfigure(i, weight=1)


#INTANCIAR LA CLASE STRINGVAR
visor_texto = tk.StringVar() #Permite enlazar el visor con los botones para que se actualice
visor =tk.Entry(window, textvariable=visor_texto,
                      font=('Helvetica', 24),
                       bd=10,
                        insertwidth=4, #Cantidad de digitos que se pueden ingresar
                         width=14,
                         borderwidth=4,
                         justify='right')

visor.grid(row=0, column=0, columnspan=4)

botones = [
    ('7', 1, 0,), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), (',', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

#FUNCION PARA ACTUALIZAR LA EXPRESION

for (texto, fila, columna) in botones:

    if texto == 'C':
        comando = limpiar
    else:
        comando = lambda x=texto: pulsar_tecla(x)

    tk.Button(window, text=texto, padx=20, pady=20, font=('Helvetica', 18),
    command=comando).grid(row=fila, column=columna, sticky='nsew')
            # if texto == ',' or texto == 'C':
            #     btn = tk.Button(window, text=texto, bg='#075396', fg='#F9F8FE', font=('Helvetica', 18), borderwidth=4)
            # elif texto == '/' or texto == '*' or texto =='-' or texto == '+':
            #     btn = tk.Button(window, text=texto, bg='#907BC7', fg='#F9F8FE', font=('Helvetica', 18), borderwidth=4)
            # else:
            #     btn = tk.Button(window, text=texto, bg="#A4C4FA", fg='#0A010C', font=('Helvetica', 18), borderwidth=4)
            # btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew") 
        
btn_equal = tk.Button(window, text='=',
                       width=40,
                       height=2,
                       bd=10,
                       borderwidth=4,
                       justify='center',
                       command=calcular).grid(row=5, column=0, columnspan=4)




#EJECUTA LA CALCULADORA
window.mainloop()
