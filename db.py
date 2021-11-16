import io
import numpy as np
import pandas as pd


class Db:
    def __init__(self):
        self.encabezadoTrabajador = ['Nombre','Telefono','Cedula','Codigo','Nit','EPS','AFP']
        

    def agregarTrabajador(self, array):
        self.trabajador = np.array(array)
        self.__guardarTrabajador()
        
    def __guardarTrabajador(self): # Metodo Privado
        df = pd.read_csv('./DataBase/trabajador.csv')
        data = {}
        for i in range(len(self.encabezadoTrabajador)):
            data[self.encabezadoTrabajador[i]] = self.trabajador[i]
        df = df.append(data,ignore_index=True)
        df.to_csv('./DataBase/trabajador.csv',index=False)
