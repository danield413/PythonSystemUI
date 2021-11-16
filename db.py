import io
import numpy as np
from numpy.lib.shape_base import apply_along_axis
import pandas as pd


class Db:
    def __init__(self):
        self.encabezadoTrabajador = ['Nombre','Telefono','Cedula','Codigo','Nit','EPS','AFP']
        self.encabezadoInfoSalario = ['Trabajadas','Extras','No Trabajadas','Ventas','Cedula']

    def agregarTrabajador(self, array):
        df = pd.read_csv('./DataBase/trabajador.csv')
        dataTrabajador = {}
        for i in range(len(self.encabezadoTrabajador)):
            dataTrabajador[self.encabezadoTrabajador[i]] = array[i]
        df = df.append(dataTrabajador,ignore_index=True)
        df.to_csv('./DataBase/trabajador.csv',index=False)
    
    def agregarInfoSalario(self, array):
        df = pd.read_csv('./DataBase/informacionLaboral.csv')
        dataInfoSalario = {}
        for i in range(len(self.encabezadoInfoSalario)):
            dataInfoSalario[self.encabezadoInfoSalario[i]] = array[i]
        df = df.append(dataInfoSalario,ignore_index=True)
        df.to_csv('./DataBase/informacionLaboral.csv',index=False)
        
    def obtenerCedulas(self):
        df = pd.read_csv('./DataBase/trabajador.csv')
        return df['Cedula'].to_numpy()