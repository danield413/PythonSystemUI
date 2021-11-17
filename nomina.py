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

    def obtenerEmpleado(self, cedula):
        empleado = self.db.obtenerTrabajador(cedula)
        return empleado
    
    def obtenerInfoEmpleado(self, cedula):
        info = self.db.obtenerInfoLaboralTrabajador(cedula)
        return info

    def obtenerHorasTrabajadas(self):
        info = self.db.obtenerInformacionEstadisticas()
        return info