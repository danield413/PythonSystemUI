from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

from nomina import Nomina

def verEstadisticas(ventana, volverAtras):
    ventana.title('Estadísticas')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 
    n = Nomina()

    def verGráfico():
        n.obtenerHorasTrabajadas()
        
        np.random.seed(19680801)


        plt.rcdefaults()
        fig, ax = plt.subplots()

        horas = ('Trabajadas', 'Extras trabajadas', 'No trabajadas')
        y_pos = np.arange(len(horas))
        performance = n.obtenerHorasTrabajadas()
        error = np.random.rand(len(horas))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(horas)
        ax.invert_yaxis()  
        ax.set_xlabel('Horas')
        ax.set_title('Gráfico - horas trabajadas, no trabajadas y extras')

        plt.show()
    
    Label(ventana, text="Estadísticas laborales", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)
    Button(ventana, text="Volver atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=4, column=0, columnspan=1)
    Button(ventana, text="Ver Gráfico", command=verGráfico, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=6, column=0, columnspan=1)


    