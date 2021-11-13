from tkinter import *
class Aplication:

    def __init__(self, padre, usuario):
        self.ventana = Tk()
        self.padre = padre
        self.usuario = usuario
        self.ventanaMenu()

    #aplicación
    def ventanaMenu(self):

        def cerrarSeccion():
            self.ventana.destroy()
            self.padre.deiconify()

        def ingresarEmpleado():
            #aqui se abre la ventana para ingresar el empleado
            print("ventana1")
        
        def ingresarSalarioEmpleado():
            #aqui se abre la ventana para calcular el el salario de un empleado
            print("ventana2")
        
        def verEstadisticas():
            #aqui se abre la ventana para ver las estadisticas de gastos de la empresa
            print("ventana3")

        def verSalario():
            #aqui se abre la ventana para ver los salario de un empleado
            print("ventana4")

        self.ventana.title("Login")
        self.ventana.geometry("550x150")
        self.ventana.anchor("center")
        self.ventana.config(bg="#323232")          # color de fondo, background   # relieve del root 
        Label(self.ventana, text=f'Bienvenido {self.usuario}', bg="#323232", fg="#fff").grid(row=0, column=0)
        Button(self.ventana, text="cerrar", cursor="hand2", relief="flat", bg="#323232", fg="white",command=cerrarSeccion).grid(column=1, columnspan=3, row=0)

        Button(self.ventana, text="ingresar empleado", cursor="hand2", relief="flat", width="20",bg="#5D00FF").grid(column=0, row=1,pady=6)
        Button(self.ventana, text="ingresar datos del salario", cursor="hand2", relief="flat", width="20",bg="#5D00FF").grid(column=1, row=1,padx=3,pady=6)
        Button(self.ventana, text="ver estadisticas", cursor="hand2",relief="flat", width="20", bg="#5D00FF", fg="white").grid(column=0, row=2,pady=6)
        Button(self.ventana, text="ver salario empleado", cursor="hand2",relief="flat", width="20", bg="#5D00FF", fg="white").grid(column=1, row=2,padx=3,pady=6)
        self.ventana.mainloop()




















        