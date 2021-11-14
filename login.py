
from tkinter import *
from tkinter import messagebox

from app import Aplication
class Login:

    def __init__(self):
        self.ventana = Tk()
        self.usuario = ''
        self.password = ''
        self.codigo = 'resetPass'
        self.passwordRoot = '1234'
        self.usuarioVerificado = False

    def ventanaPassword(self):
        usuario = StringVar()
        codigo = StringVar()

        def cancelar():
            usuario.set('')
            codigo.set('')

        def salir():
            self.ventana.destroy()
        
        def verificar():
            if(usuario.get() == 'root' and codigo.get() == self.codigo):
                self.passwordRoot = 'abcde'
                messagebox.showinfo(title="Código correcto", message=f"Nueva contraseña: {self.passwordRoot}")
                cancelar()
                self.ventanaLogin()

        self.ventana.title('Recuperación de contraseña')
        self.ventana.geometry("700x300")
        self.ventana.anchor('center')
        Label(self.ventana, text="Digite su usuario", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=0, column=0)
        Label(self.ventana, text="Digite el código de recuperación", bg="#323232", fg="#fff", font=("Verdana", 10)).grid( pady=5, row=1, column=0)
        Entry(self.ventana, width=40, textvariable=usuario).grid(padx=5, row=0, column=2)
        Entry(self.ventana, width=40, textvariable=codigo).grid(padx=5, row=1, column=2)
    
        Button(self.ventana, text="Salir", cursor="hand2", relief="flat", width="15", command=salir).grid(column=0, row=3)
        Button(self.ventana, text="Cancelar", cursor="hand2", relief="flat", width="15", command=cancelar).grid(column=1, row=3)
        Button(self.ventana, text="Generar nueva contraseña", cursor="hand2",relief="flat", width="25", bg="#5D00FF", command = verificar, fg="white").grid(column=2, row=3)
        self.ventana.mainloop()

    def ventanaLogin(self):
        usuario = StringVar()
        password = StringVar()

        def salir():
            self.ventana.destroy()

        def cancelar():
            usuario.set('')
            password.set('')

        def cambiarValores():
            self.usuario = usuario.get()
            self.password = password.get()
            verificado = self.verificarDatos()
            if(verificado == True):
                #verificado
                self.login()
                cancelar()
            else: 
                messagebox.showwarning(message="Escribe bien los datos", title="Ten en cuenta")  
    
        self.ventana.title("Login")
        self.ventana.geometry("650x150")
        self.ventana.anchor("center")
        self.ventana.config(bg="#323232")          # color de fondo, background   # relieve del root 
        Label(self.ventana, text="Digite su usuario", bg="#323232", fg="#fff", font=("Verdana", 10)).grid(pady=5, row=0, column=0)
        Label(self.ventana, text="Digite su contraseña", bg="#323232", fg="#fff", font=("Verdana", 10)).grid( pady=5, row=1, column=0)
        Entry(self.ventana, width=40, textvariable=usuario).grid(padx=5, row=0, column=2)
        Entry(self.ventana, width=40, show="*", textvariable=password).grid(padx=5, row=1, column=2)
    
        Button(self.ventana, text="Salir", cursor="hand2", relief="flat", width="10", command=salir).grid(column=0, row=3)
        Button(self.ventana, text="Cancelar", cursor="hand2", relief="flat", width="10", command=cancelar).grid(column=1, row=3)
        Button(self.ventana, text="Ingresar", cursor="hand2",relief="flat", width="25", bg="#5D00FF", command = cambiarValores, fg="white").grid(column=2, row=3)
        Button(self.ventana, text="¿Olvidó su contraseña?", cursor="hand2", relief="flat", bg="#323232", fg="white", command=self.ventanaPassword).grid(pady=5, column=0, columnspan=3, row=4)

        self.ventana.mainloop()

    def verificarDatos(self):
        if self.usuario == '' or self.password == '':
            return False
        else: return True

    def login(self):
        if(self.usuario == 'root' and self.password == self.passwordRoot):
            messagebox.showinfo(message='¡Login correcto!',title="Bienvenid@")
            self.usuarioVerificado = True

            self.ventana.withdraw()
            aplicacion = Aplication(self.ventana, self.usuario)

        else: 
            messagebox.showerror(message='Login inválido',title="Incorrecto")