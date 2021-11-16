import numpy as np
from db import Db

class Nomina:
    
    def __init__ (self):
        self.db = Db()

    def verificarSiYaExiste(self, cedula):
        cedulas = np.array(self.db.obtenerCedulas()).tolist()
        for i in cedulas:
            if str(i) == str(cedula):
                return True
        return False
        
    def introducirInfoSalario(self,array):
        self.db.agregarInfoSalario(array)

    def añadirEmpleado(self, nuevoEmpleado):
        self.db.agregarTrabajador(nuevoEmpleado)
        print("se añade")
             

    def buscarEmpleadoPorCedula(self, cedula):
        #se busca por cedula
        print("se busca")

    def getEmpleados(self):
        #obtener empleados
        print("xd")