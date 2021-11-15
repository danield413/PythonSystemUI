from tkinter import*
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
        ventana.title("MENÚ")
        ventana.anchor("center")
        ventana.config(bg="#323232") 
        Button(ventana, text="Ingresar empleado", cursor="hand2", relief="flat", width="25", bg="#258187", fg="white", command = lambda: cambiarOpcion('INGRESAR_EMPLEADO'), font=('Arial', 13, 'bold')).grid(pady=5, padx=10,column=0, row=0)
        Button(ventana, text="Ingresar salario", cursor="hand2", relief="flat", width="25", bg="#254087", fg="white", command = lambda: cambiarOpcion('INGRESAR_INFORMACION_LABORAL'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=0)
        Button(ventana, text="Estadísticas", cursor="hand2",relief="flat", width="25", bg="#5D00FF", fg="white", command = lambda: cambiarOpcion('VER_ESTADISTICAS'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=0, row=1)
        Button(ventana, text="Imprimir salario", cursor="hand2",relief="flat", width="25", bg="#692587", fg="white", command = lambda: cambiarOpcion('IMPRIMIR_SALARIO'), font=('Arial', 13, 'bold')).grid(pady=5,padx=10, column=1, row=1)
        Button(ventana, text="Salir del programa", cursor="hand2",relief="flat", width="25", bg="#688725", fg="white", command=cerrarPrograma, font=('Arial', 13, 'bold')).grid(pady=20, row=2, column=0, columnspan=2)

    configuracionInicialVentana()
    ventana.mainloop()


if __name__ == "__main__":
    main()

