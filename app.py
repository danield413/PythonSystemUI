from tkinter import *
class Aplication:

    def __init__(self, padre, usuario):
        self.ventana = Tk()
        self.padre = padre
        self.usuario = usuario
        self.ventanaMenu()

        self.usuario = ''

    #aplicación
    def ventanaMenu(self):

        def cerrarSesion():
            self.ventana.destroy()
            self.padre.deiconify()

        self.ventana.title("SISTEMA NOMINAL")
        self.ventana.geometry("550x150")
        self.ventana.anchor("center")
        self.ventana.config(bg="#323232")           
        Label(self.ventana, text=f'Bienvenido {self.usuario}', bg="#323232", fg="#fff").grid(row=0, column=0)
        Button(self.ventana, text="cerrar", cursor="hand2", relief="flat", bg="#323232", fg="white",command=cerrarSesion).grid(column=1, columnspan=3, row=0)

        Button(self.ventana, text="ingresar empleado", cursor="hand2", relief="flat", width="20",bg="#5D00FF", fg="white", command=self.ventanaIngreso).grid(column=0, row=1,pady=6)
        Button(self.ventana, text="ingresar datos del salario", cursor="hand2", relief="flat", width="20",bg="#5D00FF", fg="white",).grid(column=1, row=1,padx=3,pady=6)
        Button(self.ventana, text="ver estadisticas", cursor="hand2",relief="flat", width="20", bg="#5D00FF", fg="white",).grid(column=0, row=2,pady=6)
        Button(self.ventana, text="ver salario empleado", cursor="hand2",relief="flat", width="20", bg="#5D00FF", fg="white",).grid(column=1, row=2,padx=3,pady=6)
        self.ventana.mainloop()

    def limpiarVentana(self):
        list = self.ventana.grid_slaves()
        for l in list:
            l.destroy()

    def ventanaIngreso(self):
        usuario = StringVar()

        def cambiarValores():
            self.usuario = usuario.get()
            print(self.usuario)

        self.limpiarVentana()
        self.ventana.geometry("600x400")
        self.ventana.title("VENTANA INGRESO")
        self.ventana.anchor("center")
        self.ventana.config(bg="#323232")          
        Label(self.ventana, text="Digite su usuario", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=0, column=0)
        Entry(self.ventana, width=40, textvariable=usuario).grid(padx=5, row=0, column=2)
    
        Button(self.ventana, text="Ingresar", cursor="hand2",relief="flat", width="25", bg="#5D00FF", command = cambiarValores, fg="white").grid(column=2, row=2)
       


















        