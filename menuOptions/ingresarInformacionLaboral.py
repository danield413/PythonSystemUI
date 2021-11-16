from tkinter import *
from tkinter import messagebox
from nomina import Nomina

def ingresarInformacionLaboral(ventana, volverAtras):
    ventana.title('Ingresar información laboral del empleado')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    cedulaEmpleado = StringVar()
    horasTrabajadas = IntVar()
    horasExtrasTrabajadas = IntVar()
    horasNoTrabajadas = IntVar()
    numeroVentas = IntVar()

    def limpiar():
        cedulaEmpleado.set('')
        horasTrabajadas.set('')
        horasExtrasTrabajadas.set('')
        horasNoTrabajadas.set('')
        numeroVentas.set('')

    def verificar():
        nomina = Nomina()
        if(len(cedulaEmpleado.get()) > 7):
            if nomina.verificarSiYaExiste(cedulaEmpleado.get()):
               nomina.introducirInfoSalario([horasTrabajadas.get(),horasExtrasTrabajadas.get(),horasNoTrabajadas.get(),numeroVentas.get(),cedulaEmpleado.get()])
               limpiar()
               messagebox.showinfo(title="Todo correcto", message="Informacion guardada!")
            else:
                messagebox.showwarning(title="Cedula incorrecta", message="No existe!")
        
            

    Label(ventana, text="Información laboral", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)

    Label(ventana, text="Cédula del empleado", fg="white", bg="#258787", font=('Verdana', 10, 'bold')).grid(pady=10, row=1, column=0, padx=10)
    Entry(ventana, textvariable=cedulaEmpleado).grid(pady=5, row=1, column=1)

    Label(ventana, text="Horas trabajadas", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=2, column=0)
    Entry(ventana, textvariable=horasTrabajadas).grid(pady=5, row=2, column=1)
    
    Label(ventana, text="Horas extras trabajadas", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=3, column=0)
    Entry(ventana, textvariable=horasExtrasTrabajadas).grid(pady=5, row=3, column=1)

    Label(ventana, text="Horas No trabajadas", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=4, column=0)
    Entry(ventana, textvariable=horasNoTrabajadas).grid(pady=5, row=4, column=1)

    Label(ventana, text="Horas No trabajadas", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=4, column=0)
    Entry(ventana, textvariable=horasNoTrabajadas).grid(pady=5, row=4, column=1)

    Label(ventana, text="Número de ventas", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=5, column=0)
    Entry(ventana, textvariable=numeroVentas).grid(pady=5, row=5, column=1)

    Button(ventana, text="Atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=6, column=0)
    Button(ventana, text="Guardar información", command=verificar, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=6, column=1)

    