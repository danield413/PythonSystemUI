from tkinter import *
#import matplotlib.pyplot as plt

def verEstadisticas(ventana, volverAtras):
    ventana.title('Estadísticas')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    def verGráfico():
        # Gráfico
        print("grafico")
    
    Label(ventana, text="Estadísticas laborales", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)
    Button(ventana, text="Volver atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=4, column=0, columnspan=1)
    Button(ventana, text="Ver Gráfico", command=verGráfico, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=6, column=0, columnspan=1)


    