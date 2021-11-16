from db import Db

class Nomina:
    
    def __init__ (self):
        self.db = Db()

    def verificarSiYaExiste(self, cedula):
        #se verifica si el empleado ya existe
        print("se verifica si el usuario con la cedula 'x' ya está en la lista")
        
    
    def añadirEmpleado(self, nuevoEmpleado):
        self.db.agregarTrabajador(nuevoEmpleado)
        print("se añade")
             

    def buscarEmpleadoPorCedula(self, cedula):
        #se busca por cedula
        print("se busca")

    def getEmpleados(self):
        #obtener empleados
        print("xd")
