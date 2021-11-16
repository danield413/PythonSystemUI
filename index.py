from datetime import datetime
from tkinter import *
from tkinter import messagebox

from menuOptions.imprimirSalario import imprimirSalario
from menuOptions.ingresarEmpleado import ingresarEmplado
from menuOptions.ingresarInformacionLaboral import ingresarInformacionLaboral
from menuOptions.verEstadisticas import verEstadisticas

def main():
    ventana = Tk()

    def limpiarVentana():
        list = ventana.grid_slaves()
        for l in list:
            l.destroy()   

    def cerrarPrograma():
        ventana.destroy()

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

    def volverAtras():
        limpiarVentana()
        configuracionInicialVentana()

    
    def configuracionInicialVentana():
        ventana.title("MENÚ")
        ventana.geometry("650x350")
        ventana.anchor("center")
        ventana.config(bg="#323232") 
        ventana.resizable = False
        Label(text="Menú principal", bg="#323232", fg="white", font=('Arial', 13, 'bold')).grid(pady=10, row=0, column=0)
        Label(text=f"Fecha: {datetime.today().strftime('%Y-%m-%d')}", bg="#323232", fg="white", font=('Arial', 13, 'bold')).grid(pady=10, row=0, column=1)
        Button(ventana, text="Ingresar empleado", cursor="hand2", relief="flat", width="25", bg="#258187", fg="white", command = lambda: cambiarOpcion('INGRESAR_EMPLEADO'), font=('Arial', 13, 'bold')).grid(pady=5, padx=10,column=0, row=1)
        Button(ventana, text="Ingresar salario", cursor="hand2", relief="flat", width="25", bg="#254087", fg="white", command = lambda: cambiarOpcion('INGRESAR_INFORMACION_LABORAL'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=1)
        Button(ventana, text="Estadísticas", cursor="hand2",relief="flat", width="25", bg="#5D00FF", fg="white", command = lambda: cambiarOpcion('VER_ESTADISTICAS'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=0, row=2)
        Button(ventana, text="Imprimir salario", cursor="hand2",relief="flat", width="25", bg="#692587", fg="white", command = lambda: cambiarOpcion('IMPRIMIR_SALARIO'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=2)
        Button(ventana, text="Salir del programa", cursor="hand2",relief="flat", width="25", bg="#688725", fg="white", command=cerrarPrograma, font=('Arial', 13, 'bold')).grid(pady=20, row=3, column=0, columnspan=2)

    def ventanaLogin():

        usuario = StringVar()
        password = StringVar()

        passwordUsuarioRoot = 'root'

        def verificar():
            if(usuario.get() == '' or password.get() == ''):
                messagebox.showwarning(title="Advertencia", message="No dejes los campos vacíos")
            elif(usuario.get() == 'root' and password.get() == passwordUsuarioRoot): 
                msg = f"¡Bienvenid@ usuario {usuario.get()}"
                messagebox.showinfo(title="Mensaje", message=msg)
                limpiarVentana()
                configuracionInicialVentana()

        

        def olvidoPassword():

            usuario = StringVar()
            codigo = StringVar()

            def generar():
                if(usuario.get() == 'root' and codigo.get() == 'RESETPASS'):
                    messagebox.showinfo(title="Recuperación", message=f"Tu contraseña es {passwordUsuarioRoot}")
                    usuario.set('')
                    codigo.set('')
                elif(usuario.get() == '' or codigo.get() == ''):
                    messagebox.showwarning('Alerta', 'Debes llenar los campos')

            def volver():
                limpiarVentana()
                ventanaLogin()
            
            limpiarVentana()
            ventana.title('Recuperar contraseña')
            ventana.resizable = False
            Label(text="Recuperación", bg="#55476D", fg="white", font=('Arial', 15, 'bold')).grid(pady=10, row=0)
            Label(ventana, text="Ingresar usuario", bg="#55476D", fg="white", font=('Arial', 11, 'bold')).grid(padx=5, pady=5, row=1, column=0)
            Entry(ventana, textvariable=usuario).grid(padx=5, pady=5, row=1, column=1)
            Label(ventana, text="Código de restauración", bg="#55476D", fg="white", font=('Arial', 11, 'bold')).grid(padx=5, pady=5, row=2, column=0)
            Entry(ventana, textvariable=codigo).grid(padx=5, pady=5, row=2, column=1)

            Button(text="Atrás", command = volver, width="15", relief="flat", cursor="hand2").grid(pady=5, row=3, column=0)
            Button(text="Recordar contraseña", command = generar, bg="#00FFD8", cursor="hand2", font=('Arial', 10, 'bold')).grid(pady=5, row=3, column=1)

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
        Button(text="¿Olvidaste la contraseña?", relief="flat", bg="#55476D", fg="white", command=olvidoPassword, font=('Arial', 10, 'bold'), cursor="hand2").grid(row=4, column=0, columnspan=2)

    ventanaLogin()

    ventana.mainloop()


if __name__ == "__main__":
    main()

