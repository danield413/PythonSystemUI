from tkinter import *

class Option:

    def __init__(self, padre, tipo):
        self.tipo = tipo
        self.ventana = Tk()
        self.padre = padre

    def mostrarVentanaSegunTipo(self):
        self.ventana.title(f"{self.tipo} - Menú")
        self.ventana.geometry("700x500")
        self.ventana.config(bg="#323232") 
        self.ventana.anchor('center')
        self.padre.withdraw()

        if(self.tipo == 'INGRESAR_EMPLEADO'):
            self.ventanaIngresarEmpleado()
        if(self.tipo == 'INGRESAR_SALARIO_EMPLEADO'):
            self.ventanaIngresarSalario()
        if(self.tipo == 'VER_ESTADISTICAS'):
            self.ventanaVerEstadisticas()
        if(self.tipo == 'VER_SALARIO_COMPLETO'):
            self.ventanaVerSalarioCompleto()
    
    def volver(self):
        self.ventana.destroy()
        self.padre.deiconify()

    def ventanaIngresarEmpleado(self):
        nombre = StringVar()
        telefono = StringVar()
        cedula = StringVar()
        codigo = StringVar()
        nit = StringVar()
        eps = StringVar()
        afp = StringVar()

        def validar():
            #Validar datos
            print("Validar")

        def guardarEmpleado():
            #guardar empleado (verificar antes que no esté registrado previamente)
            print("Guardar")
        

        Label(self.ventana, text="Datos del Empleado", bg="#323232", fg="white", font=("Arial", 20)).grid(pady=10, row=0)
        Label(self.ventana, text="Nombre del empleado", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=1, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=1, column=1)
        Label(self.ventana, text="Telefono", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=2, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=2, column=1)
        Label(self.ventana, text="Cedula", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=3, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=3, column=1)
        Label(self.ventana, text="Código", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=4, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=4, column=1)
        Label(self.ventana, text="NIT", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=5, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=5, column=1)
        Label(self.ventana, text="EPS", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=6, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=6, column=1)
        Label(self.ventana, text="AFP", bg="#323232", fg="#fff", font=("Arial", 16)).grid(pady=5, row=7, column=0)
        Entry(self.ventana, width="20").grid(pady=5, row=7, column=1)
        Button(self.ventana, text="Atrás", width="30", cursor="hand2", command=self.volver).grid(pady=5, row=8, column=0)
        Button(self.ventana, text="Guardar", width="30", bg="#5D00FF", fg="white", relief="flat", cursor="hand2", command=validar).grid(pady=5, row=8, column=1)

        self.ventana.mainloop()
    
    def ventanaIngresarSalario(self):
        Label(self.ventana, text="Ingresar salario", fg="white")
        Button(self.ventana, text="Atrás", command=self.volver)

        self.ventana.mainloop()
    
    def ventanaVerEstadisticas(self):
        Label(self.ventana, text="Ver estadísticas", fg="white")
        Button(self.ventana, text="Atrás", command=self.volver)

        self.ventana.mainloop()
    
    def ventanaVerSalarioCompleto(self):
        Label(self.ventana, text="Ver salario completo", fg="white")
        Button(self.ventana, text="Atrás", command=self.volver)
    
        self.ventana.mainloop()