import numpy as np #Libreria para desarrollar los arrays 
import pandas as pd #Libreria para crear archivos y leerlos (CSV)

#Clase DB que sirve para manejar todos los archivos como si fuera una base de datos
class Db:
    def __init__(self):
        #Se inicializan los encabezados de la clase Db
        #Cada tabla tiene su encabezado
        self.encabezadoTrabajador = ['Nombre','Telefono','Cedula','Codigo','Nit','EPS','AFP']
        self.encabezadoInfoSalario = ['Trabajadas','Extras','No Trabajadas','Ventas','Cedula']


    #Agrega un trabajador, leyendo el csv con los que ya hay almacenados, creando un dataframe
    #para que pandas pueda guardar ese dataframe (encabezado:valor) en el archivo csv 
    def agregarTrabajador(self, array):
        df = pd.read_csv('./DataBase/trabajador.csv')
        dataTrabajador = {}
        for i in range(len(self.encabezadoTrabajador)):
            dataTrabajador[self.encabezadoTrabajador[i]] = array[i]
        df = df.append(dataTrabajador,ignore_index=True)
        df.to_csv('./DataBase/trabajador.csv',index=False)
    
    #Agrega la informacion del salario de la misma manera que la funcion de arriba
    #Pero a un archivo csv diferente
    def agregarInfoSalario(self, array):
        df = pd.read_csv('./DataBase/informacionLaboral.csv')
        dataInfoSalario = {}
        for i in range(len(self.encabezadoInfoSalario)):
            dataInfoSalario[self.encabezadoInfoSalario[i]] = array[i]
        df = df.append(dataInfoSalario,ignore_index=True)
        df.to_csv('./DataBase/informacionLaboral.csv',index=False)
        
    #Lee el archivo de trabajadores.csv y devuelve un array con todas las cedulas encontradas
    def obtenerCedulas(self):
        df = pd.read_csv('./DataBase/trabajador.csv')
        return df['Cedula'].to_numpy()
    
    #Lee el archivo de trabajadores.csv y devuelve en un array de numpy todos los datos de un trabajador
    #Con su cedula
    def obtenerTrabajador(self, cedula):
        df = pd.read_csv('./DataBase/trabajador.csv')
        trabajadores = df.to_numpy()
        for i in range(len(trabajadores)):
            if(trabajadores[i][2] == int(cedula)):
                return trabajadores[i]

    #Lee el archivo de informacionLaboral.csv y devuelve un array de numpy con los datos segun su cedula
    def obtenerInfoLaboralTrabajador(self, cedula):
        df = pd.read_csv('./DataBase/informacionLaboral.csv')
        infoTrabajadores = df.to_numpy()
        infoTrabajador = False
        for i in range(len(infoTrabajadores)):
            if(infoTrabajadores[i][4] == int(cedula)):
                infoTrabajador = infoTrabajadores[i]
        
        return infoTrabajador


    #Lee el archivo de informacionLaboral.csv y suma todos los datos para asi dar su estadistica sobre el total de empleados ingresadas sus hora, etc
    def obtenerInformacionEstadisticas(self):
        df = pd.read_csv('./DataBase/informacionLaboral.csv')
        info = df.to_numpy()

        countTrabajadas = 0
        countExtras = 0
        countNoTrabajadas = 0
        
        for i in range(len(info)):
            countTrabajadas += info[i][0]
            countExtras += info[i][1]
            countNoTrabajadas += info[i][2]
        
        infoFormateada = np.array([countTrabajadas, countExtras, countNoTrabajadas])
        return infoFormateada
    
    #Lee usuarios.csv para determinar si el login es correcto
    def iniciarSesion(self, usuario, password):
        df = pd.read_csv('./DataBase/usuarios.csv')
        info = df.to_numpy()
        for i in range(len(info)):
            if(info[i][0] == usuario):
                if(info[i][1] == password):
                    return True
                else :
                    return False
