from tkinter import * #Libreria para desarrollar interfaz grafica
from tkinter import messagebox #Libreria para mostrar mensajes en la interfaz grafica
import numpy #Libreria para desarrollar los arrays 
import functions.generarPDF as f # Se importa la funcion para generar el pdf
from nomina import Nomina #Se llama a la Clase nomina para manejar datos de los empleados

#Esta funcion es la encargada de toda la ventana de imprimir salario
def imprimirSalario(ventana, volverAtras):
    ventana.title('Imprimir salario')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    cedulaEmpleado = StringVar()
    n = Nomina()
    INFORMACION_BANCARIA = '**** - **** - ****'

    #esta funcion guarda los datos en un array y llama a la funcion para guardar en pdf
    def imprimirEnArchivo(pension, icbf, sueldo, auxTransporte, bonificaciones, nombre, telefono, cedula, codigoTrabajador, horasTrabajadas, horasExtrasTrabajadas, horasNoTrabajadas, numeroVentas, total ):
        dato = [nombre,telefono,codigoTrabajador,horasTrabajadas,horasExtrasTrabajadas,horasNoTrabajadas,numeroVentas,bonificaciones,icbf,pension,sueldo,auxTransporte,total]
        f.imprimir(dato,cedula)

    #Se calcula el salario de el empleado
    def calcularSalario(empleado, infoLaboral):
        horasTrabajadas = infoLaboral[0]
        horasExtrasTrabajadas = infoLaboral[1]
        horasNoTrabajadas = infoLaboral[2]
        numeroVentas = infoLaboral[3]

        SUELDO_BASICO = 908526
        sueldoInicial = 908526
        HORA_EXTRA = 4731
        bonificaciones = 0
        DESCUENTO_SALUD = 72750
        AUXILIO_TRANSPORTE = 106454

        #se suman las horas extras, cada una por $4.731
        sueldoInicial += (horasExtrasTrabajadas * HORA_EXTRA)
        
        #si el numero de ventas fue mayor a 150, se bonifica el 10%
        if(numeroVentas > 150): 
            #Mayores a 150
            bonificaciones + (sueldoInicial * .1)
        #si el numero de ventas fue mayor a 100 y menos a 150, se bonifica el 5%
        elif(numeroVentas > 100 and numeroVentas < 150):
            #mayores de 100 y menores de 150
            bonificaciones + (sueldoInicial * .05)

        #Se suman las bonitifaciones
        sueldoInicial += bonificaciones
        
        #Se descuenta la salud y se da auxilio de transporte
        sueldoInicial -= DESCUENTO_SALUD
        sueldoInicial += AUXILIO_TRANSPORTE
         
        #Si las horas trabajadas son menores a 180 entonces se descuenta $3.875 por cada hora NO trabajada
        if(horasTrabajadas < 180): 
            aDescontar = horasNoTrabajadas * 3785
            sueldoInicial -= aDescontar
        
        #Se descuenta pensión
        pension = sueldoInicial * 0.38
        sueldoInicial -= (sueldoInicial * 0.38)

        #Se aumenta el 4% del ICBF
        icbf = sueldoInicial * 0.04
        sueldoInicial += (sueldoInicial * 0.04)

        #se llama a las dos funciones una para mostrar y la otra para crear el desprendible
        imprimirEnPantalla(pension, icbf, SUELDO_BASICO, AUXILIO_TRANSPORTE, bonificaciones, sueldoInicial)
        imprimirEnArchivo(pension, icbf, SUELDO_BASICO , AUXILIO_TRANSPORTE, bonificaciones, empleado[0], empleado[1], empleado[2], empleado[3], horasTrabajadas, horasExtrasTrabajadas, horasNoTrabajadas, numeroVentas, sueldoInicial)
    
    #Se busca si el empleado existe para empezar a calcular
    def buscar():
        #calcular salario
        if(len(cedulaEmpleado.get()) > 0 ):
            if( n.verificarSiYaExiste(cedulaEmpleado.get()) ):
                #Si el usuario buscado existe y tiene información laboral se hace lo siguiente
                infoLaboral = n.obtenerInfoEmpleado(cedulaEmpleado.get())
                if( type(infoLaboral) == numpy.ndarray):

                    empleadoBuscado = n.obtenerEmpleado(cedulaEmpleado.get())
                    msg = f"Emplead@ {empleadoBuscado[0]} - CC: {cedulaEmpleado.get()} encontrad@"
                    messagebox.showinfo(title="Empleado encontrado", message=msg)
                    calcularSalario( empleadoBuscado, infoLaboral )
                    
                elif( type(infoLaboral) == bool ):
                    msg = f"El empleado con cédula: {cedulaEmpleado.get()} no tiene información laboral todavía"
                    messagebox.showerror(title="Error", message=msg)
        cedulaEmpleado.set('')

    #Se muestra en pantalla la informacion optenida del salario
    def imprimirEnPantalla( pension, icbf, sueldoBasico, auxTrans, bonificaciones, total ):
        Label(ventana, text="Pensión", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=3, column=0)
        Label(ventana, text=f"$ {pension:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=3, column=1)
        
        Label(ventana, text="ICBF", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=4, column=0)
        Label(ventana, text=f"$ {icbf:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=4, column=1)

        Label(ventana, text="Sueldo", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=5, column=0)
        Label(ventana, text=f"$ {sueldoBasico:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=5, column=1)

        Label(ventana, text="Auxilio transporte", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=6, column=0)
        Label(ventana, text=f"$ {auxTrans:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=6, column=1)

        Label(ventana, text="Bonificaciones", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=7, column=0)
        Label(ventana, text=f"$ {bonificaciones:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=7, column=1)

        Label(ventana, text="Neto a pagar", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=7, column=0)
        Label(ventana, text=f"$ {total:,.2f}", bg="#323232", fg="#fff", font=('Verdana', 10, 'bold')).grid(pady=5, row=7, column=1)

    Label(ventana, text="Gastos Empresariales", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)

    Label(ventana, text="Cédula del empleado", fg="white", bg="#258787", font=('Verdana', 10, 'bold')).grid(pady=10, row=1, column=0, padx=10)
    Entry(ventana, textvariable=cedulaEmpleado).grid(pady=5, row=1, column=1)
    Button(ventana, text="Atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=2, column=0)
    Button(ventana, text="Calcular", command=buscar, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=2, column=1)
    
   