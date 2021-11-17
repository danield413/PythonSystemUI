import numpy as np #Libreria para desarrollar los arrays
from db import Db #Libreria para crear archivos y leerlos (CSV)

#Clase encargada de todos los empleados
class Nomina:
    #Constructor o funcion principal la cual se acciona al crear una instancia de la clase
    def __init__ (self):
        self.db = Db()

    #funcion que se comunica con DB para determinar si una cedula existe o no
    def verificarSiYaExiste(self, cedula):
        cedulas = np.array(self.db.obtenerCedulas()).tolist()
        for i in cedulas:
            if str(i) == str(cedula):
                return True
        return False

    #funcion que se comunica con DB para ingresar los datos de las horas trabajadas del empleado
    def introducirInfoSalario(self,array):
        self.db.agregarInfoSalario(array)

    #funcion que se comunica con DB para ingresar los datos del empleado
    def añadirEmpleado(self, nuevoEmpleado):
        self.db.agregarTrabajador(nuevoEmpleado)

    #funcion que se comunica con DB para obtener los datos de un empleado con su cedula
    def obtenerEmpleado(self, cedula):
        empleado = self.db.obtenerTrabajador(cedula)
        return empleado
    
    #funcion que se comunica con DB para obtener los datos de las horas trabajadas de un empleado con su cedula
    def obtenerInfoEmpleado(self, cedula):
        info = self.db.obtenerInfoLaboralTrabajador(cedula)
        return info

    #funcion que se comunica con DB para obtener el total de horas trabajadas, extra, etc de toda la empresa
    def obtenerHorasTrabajadas(self):
        info = self.db.obtenerInformacionEstadisticas()
        return info