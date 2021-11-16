from tkinter import *
#import matplotlib.pyplot as plt

def imprimirSalario(ventana, volverAtras):
    ventana.title('Estadísticas')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    cedulaEmpleado = StringVar()
    
    def calcular():
        #calcular salario
        print("calcular")

    def imprimir():
        #imprimir
        print("imprimir")

    Label(ventana, text="Gastos Empresariales", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)

    Label(ventana, text="Cédula del empleado", fg="white", bg="#258787", font=('Verdana', 10, 'bold')).grid(pady=10, row=1, column=0, padx=10)
    Entry(ventana, textvariable=cedulaEmpleado).grid(pady=5, row=1, column=1)
    Button(ventana, text="Calcular", command=calcular, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=2, column=0, columnspan=2)
    
    Label(ventana, text="Pensión", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=3, column=0)
    Label(ventana, text="pension").grid(pady=5, row=3, column=1)
    
    Label(ventana, text="ICBF", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=4, column=0)
    Label(ventana, text="ICBF").grid(pady=5, row=4, column=1)

    Label(ventana, text="Sueldo", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=5, column=0)
    Label(ventana, text="SUELDO").grid(pady=5, row=5, column=1)

    Label(ventana, text="Auxilio transporte", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=6, column=0)
    Label(ventana, text="AUX TRANSP").grid(pady=5, row=6, column=1)

    Label(ventana, text="Bonificaciones", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=7, column=0)
    Label(ventana, text="BONIFICACIONES").grid(pady=5, row=7, column=1)

    Button(ventana, text="Atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=8, column=0)
    Button(ventana, text="Imprimir", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=imprimir).grid(row=8, column=1)
   