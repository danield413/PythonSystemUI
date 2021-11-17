from tkinter import * #Libreria para desarrollar interfaz grafica
from functions.comprobarLongitud import comprobarLongitud #importa la funcion para 
from tkinter import messagebox #Libreria para mostrar mensajes en la interfaz grafica
from nomina import Nomina #Libreria para desarrollar los arrays 

#Funcion que se encarga de toda la vista para ingresar mas empleados
def ingresarEmplado(ventana, volverAtras):
    ventana.title('Ingresar empleado')
    ventana.geometry("650x500")
    ventana.anchor("center")
    ventana.config(bg="#323232") 

    nombre = StringVar()
    telefono = StringVar()
    cedula = StringVar()
    codigo = StringVar()
    nit = StringVar()
    eps = StringVar()
    afp = StringVar()

    #Limpia los campos donde son ingresados los datos
    def limpiar():
        nombre.set('')
        telefono.set('')
        cedula.set('')
        codigo.set('')
        nit.set('')
        eps.set('')
        afp.set('')

    #Verifica que los datos son validos y añade en la BD
    def verificar():
        nombreV = comprobarLongitud('nombre', nombre.get())
        telefonoV = comprobarLongitud('telefono', telefono.get())
        cedulaV = comprobarLongitud('cedula',cedula.get())
        codigoV = comprobarLongitud('codigo',codigo.get())
        nitV = comprobarLongitud('nit',nit.get())
        epsV = comprobarLongitud('eps',eps.get())
        afpV = comprobarLongitud('afp',afp.get())

        if(nombreV and telefonoV and cedulaV and codigoV and nitV and epsV and afpV):
            N = Nomina()
            array = [nombre.get(),telefono.get(),cedula.get(),codigo.get(),nit.get(),eps.get(),afp.get()]
            N.añadirEmpleado(array)
            limpiar()
            messagebox.showinfo(title="Todo correcto", message="Nuevo empleado añadido!")
        else: 
            messagebox.showwarning(title="Campos incorrectos", message="Revisa los campos")
            

    Label(ventana, text="Ingresar Empleado", bg="#323232", fg="white", font=("Verdana", 13)).grid(pady=10, row=0, column=0)

    Label(ventana, text="Nombre", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=1, column=0)
    Entry(ventana, textvariable=nombre).grid(pady=5, row=1, column=1)
    
    Label(ventana, text="Telefono", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=2, column=0)
    Entry(ventana, textvariable=telefono).grid(pady=5, row=2, column=1)

    Label(ventana, text="Cedula", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=3, column=0)
    Entry(ventana, textvariable=cedula).grid(pady=5, row=3, column=1)

    Label(ventana, text="Código", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=4, column=0)
    Entry(ventana, textvariable=codigo).grid(pady=5, row=4, column=1)

    Label(ventana, text="NIT", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=5, column=0)
    Entry(ventana, textvariable=nit).grid(pady=5, row=5, column=1)

    Label(ventana, text="EPS", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=6, column=0)
    Entry(ventana, textvariable=eps).grid(pady=5, row=6, column=1)

    Label(ventana, text="AFP", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=7, column=0)
    Entry(ventana, textvariable=afp).grid(pady=5, row=7, column=1)
    Button(ventana, text="Atrás", width="20", bg="gray", fg="white", relief="flat", font=('Verdana', 10, 'bold'), cursor="hand2", command=volverAtras).grid(row=8, column=0)
    Button(ventana, text="Guardar empleado", command=verificar, width="20", bg="#5D00FF", relief="flat", fg="white", font=('Verdana', 10, 'bold'), cursor="hand2").grid(pady=20, row=8, column=1)

    