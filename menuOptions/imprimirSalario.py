from tkinter import *
from tkinter import messagebox

from nomina import Nomina
#import matplotlib.pyplot as plt

def imprimirSalario(ventana, volverAtras):
    ventana.title('Estadísticas')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    cedulaEmpleado = StringVar()
    n = Nomina()
    
    SUELDO_BASICO = 908526
    HORA_EXTRA = 4731
    #>100 ventas = 5%, >150 ventas 10% -> sueldo básico
    BONIFICACIONES = 0
    DESCUENTO_SALUD = 72750
    AUXILIO_TRANSPORTE = 106454
    INFORMACION_BANCARIA = ''
    #Si trabaja < 180 horas, por cada hora no trabajada se descuenta 3785
    #la pensión será del 3.8% del salario, el aumento es para la empresa, al empleado
    #se le descuenta
    #se aumenta 4% de ICBG

    def calcularSalario(empleado, infoLaboral):
        horasTrabajadas = infoLaboral[0]
        horasExtrasTrabajadas = infoLaboral[1]
        horasNoTrabajadas = infoLaboral[2]
        numeroVentas = infoLaboral[3]

        SUELDO_BASICO + (horasExtrasTrabajadas * HORA_EXTRA)
        if(numeroVentas > 150): 
            #Mayores a 150
            SUELDO_BASICO + (SUELDO_BASICO * .1)
        elif(numeroVentas > 100 and numeroVentas < 150):
            #mayores de 100 y menores de 150
            SUELDO_BASICO + (SUELDO_BASICO * .05)
        
        #Se descuenta la salud y se da auxilio de transporte
        SUELDO_BASICO - DESCUENTO_SALUD
        SUELDO_BASICO + AUXILIO_TRANSPORTE
         
        if(horasTrabajadas < 180): 
            aDescontar = horasExtrasTrabajadas * 3785
            SUELDO_BASICO - aDescontar
        
        #Se descuenta pensión
        SUELDO_BASICO - (SUELDO_BASICO * 0.38)

        #Se aumenta el 4% del ICBF
        SUELDO_BASICO + (SUELDO_BASICO * 0.04)

        print('SUELDO:', SUELDO_BASICO)

    
    def buscar():
        #calcular salario
        if(len(cedulaEmpleado.get()) > 0 ):
            if( n.verificarSiYaExiste(cedulaEmpleado.get()) ):
                #Si el usuario buscado existe y tiene información laboral se hace lo siguiente
                infoLaboral = n.obtenerInfoEmpleado(cedulaEmpleado.get())
                if( len(infoLaboral) > 0 ):
                    empleadoBuscado = n.obtenerEmpleado(cedulaEmpleado.get())
                    msg = f"Emplead@ {empleadoBuscado[0]} - CC: {cedulaEmpleado.get()} encontrad@"
                    messagebox.showinfo(title="Empleado encontrado", message=msg)

                    calcularSalario( empleadoBuscado, infoLaboral )
                    

                elif( not infoLaboral ):
                    msg = f"El empleado con cédula: {cedulaEmpleado.get()} no tiene información laboral todavía"
                    messagebox.showerror(title="Error", message=msg)

    def imprimir():
        #imprimir
        print("imprimir")

    Label(ventana, text="Gastos Empresariales", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)

    Label(ventana, text="Cédula del empleado", fg="white", bg="#258787", font=('Verdana', 10, 'bold')).grid(pady=10, row=1, column=0, padx=10)
    Entry(ventana, textvariable=cedulaEmpleado).grid(pady=5, row=1, column=1)
    Button(ventana, text="Calcular", command=buscar, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=2, column=0, columnspan=2)
    
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
   