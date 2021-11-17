from datetime import datetime #Libreria para obtener la fecha de hoy
from tkinter import * #Libreria para desarrollar interfaz grafica
from tkinter import messagebox #Libreria para mostrar mensajes en la interfaz grafica
from db import Db #importacion de la clase DB que controla los archivos

#importacion de una nueva vista en el menu
from menuOptions.imprimirSalario import imprimirSalario 
from menuOptions.ingresarEmpleado import ingresarEmplado
from menuOptions.ingresarInformacionLaboral import ingresarInformacionLaboral
from menuOptions.verEstadisticas import verEstadisticas

#METODO PRINCIPAL DEL PROGRAMA
def main():
    #Se crean dos objetos de Tkinter y otro de Db ( una clase que maneja los datos .CSV )
    ventana = Tk()
    db = Db()

    #La función limpiarVentana destruye todos los elementos grid, para poder agregar
    #nuevos elementos
    def limpiarVentana():
        list = ventana.grid_slaves()
        for l in list:
            l.destroy()   

    #La función cerrarPrograma destruye la ventana y consigo el programa
    def cerrarPrograma():
        ventana.destroy()

    #CambiarOpción recibe un tipo, dependiendo del tipo limpia la ventana y carga la configuración
    #de la ventana deseada
    def cambiarOpcion(opcion):
        if(opcion == 'INGRESAR_EMPLEADO'):
            limpiarVentana()
            ingresarEmplado(ventana, volverAtras)
        if(opcion == 'INGRESAR_INFORMACION_LABORAL'):
            limpiarVentana()
            ingresarInformacionLaboral(ventana, volverAtras)
        if(opcion == 'VER_ESTADISTICAS'):
            limpiarVentana()
            verEstadisticas(ventana, volverAtras)
        if(opcion == 'IMPRIMIR_SALARIO'):
            limpiarVentana()
            imprimirSalario(ventana, volverAtras)

    #volverAtras, como su nombre dice devuelve al usuario al principio del menú ejecutando la función
    #configuracionInicialVentana()
    def volverAtras():
        limpiarVentana()
        configuracionInicialVentana()

    #Esta función muestra el menú principal, cuando esta se llama los elementos de la ventana cambian 
    #dando paso al menú
    #lambda es para pasar una funcion con sus parametros
    def configuracionInicialVentana():
        ventana.title("MENÚ")
        ventana.geometry("650x350")
        ventana.anchor("center")
        ventana.config(bg="#323232") 
        ventana.resizable = False
        Label(text="Menú principal", bg="#323232", fg="white", font=('Arial', 13, 'bold')).grid(pady=10, row=0, column=0)
        Label(text=f"Fecha: {datetime.today().strftime('%Y-%m-%d')}", bg="#323232", fg="white", font=('Arial', 13, 'bold')).grid(pady=10, row=0, column=1)
        Button(ventana, text="Ingresar empleado", cursor="hand2", relief="flat", width="25", bg="#258187", fg="white", command = lambda: cambiarOpcion('INGRESAR_EMPLEADO'), font=('Arial', 13, 'bold')).grid(pady=5, padx=10,column=0, row=1)
        Button(ventana, text="Ingresar información laboral", cursor="hand2", relief="flat", width="25", bg="#254087", fg="white", command = lambda: cambiarOpcion('INGRESAR_INFORMACION_LABORAL'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=1)
        Button(ventana, text="Estadísticas", cursor="hand2",relief="flat", width="25", bg="#5D00FF", fg="white", command = lambda: cambiarOpcion('VER_ESTADISTICAS'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=0, row=2)
        Button(ventana, text="Imprimir salario", cursor="hand2",relief="flat", width="25", bg="#692587", fg="white", command = lambda: cambiarOpcion('IMPRIMIR_SALARIO'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=2)
        Button(ventana, text="Salir del programa", cursor="hand2",relief="flat", width="25", bg="#688725", fg="white", command=cerrarPrograma, font=('Arial', 13, 'bold')).grid(pady=20, row=3, column=0, columnspan=2)

    #Esta función es la que primero se ejecuta al iniciar el programa, se encarga de manejar el login
    #usando tkinter, la clase db que maneja los .csv.
    def ventanaLogin():

        usuario = StringVar()
        password = StringVar()

        def verificar():
            #Se verifica que no estén vacíos los campos
            if(usuario.get() == '' or password.get() == ''):
                messagebox.showwarning(title="Advertencia", message="No dejes los campos vacíos")
                #sino se verifica que sean mayores a 0 en caracteres
            elif(len(usuario.get()) > 0 and len(password.get()) > 0): 
                    #si lo anterior pasa, se inicia sesión usando la clase db y pasandole los datos
                    #esté metodo de esa clase retorna True (si es correcto ) o False (Si no lo es) 
                if(db.iniciarSesion(usuario.get(), password.get())):
                    msg = f"¡Bienvenid@ usuario {usuario.get()}"
                    messagebox.showinfo(title="Mensaje", message=msg)
                    #Se limpia la ventana y se cargan en la ventana los widgets del menú
                    limpiarVentana()
                    configuracionInicialVentana()
                else:
                    #si no puede iniciar sesión, se reestablecen los datos y se muestra un mensaje
                    usuario.set('')
                    password.set('')
                    messagebox.showerror(title="Inicio de sesión", message="Inicio de sesión incorrecto, intenta de nuevo")

        ventana.title("Inicio de sesión")
        ventana.geometry("400x300")
        ventana.anchor("center")
        ventana.config(bg="#55476D") 
        Label(text="Hola de nuevo!", bg="#55476D", fg="white", font=('Arial', 15, 'bold')).grid(pady=10, row=0)
        Label(ventana, text="Ingresar usuario", bg="#55476D", fg="white", font=('Arial', 11, 'bold')).grid(padx=5, pady=5, row=1, column=0)
        Entry(ventana, textvariable=usuario).grid(padx=5, pady=5, row=1, column=1)
        Label(ventana, text="Ingresar contraseña", bg="#55476D", fg="white", font=('Arial', 11, 'bold')).grid(padx=5, pady=5, row=2, column=0)
        Entry(ventana, textvariable=password, show="*").grid(padx=5, pady=5, row=2, column=1)

        Button(text="Salir", command=lambda: ventana.destroy(), width="15", relief="flat", cursor="hand2").grid(pady=5, row=3, column=0)
        Button(text="Ingresar", command=verificar, width="15", relief="flat", bg="#00FFD8", fg="black", cursor="hand2", font=('Arial', 10, 'bold')).grid(pady=5, row=3, column=1)

    #Se ejecuta la ventana login, puesto que es la primera que debe aparecer
    ventanaLogin()

    #la ventana mantiene activa y asi evita cierres
    ventana.mainloop()


if __name__ == "__main__": # Por defecto __name__ = a __main__
    #SE EJECUTA EL MÉTODO PRINCIPAL
    main()
