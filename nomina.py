import numpy as np
import pandas

from empleado import Empleado

class Nomina:
    
    def __init__ (self):
        #NOTA: los datos se pueden leer de un excel usando PANDAS, no creo que sea necesario usar la clase Empleado(), creo que no hace falta 
        self.empleados = np.array([
            Empleado('Pedro Ruiz', 8879832, '1004653578', '20211202-13', '70009827172', 'Nueva eps', 'Colpensiones'),
            Empleado('Karina Gonzales', 315043123, '1002652786', '2021114-87', '7000942348', 'Sanitas', 'Colpensiones'),
            Empleado('Harrison Castañeda', 3103659032, '1002652173', '20190245-87', '8000876453', 'Salud total', 'Colpensiones'),
        ])

    def verificarSiYaExiste(self, cedula):
        #se verifica si el empleado ya existe
        print("se verifica si el usuario con la cedula 'x' ya está en la lista")
        
    
    def añadirEmpleado(self, nuevoEmpleado):
        #se añade un nuevo empleado
        print("se añade")
             

    def buscarEmpleadoPorCedula(self, cedula):
        #se busca por cedula
        print("se busca")

    def getEmpleados(self):
        #obtener empleados
        print("xd")

