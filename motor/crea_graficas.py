from os import remove
import matplotlib.pyplot as plt
import datetime


def prepara_dts(dts_bruto,limpia):
    lineas = list()
    for n,k in enumerate(dts_bruto):
        for e in range(len(dts_bruto[k])):
            if len(lineas) == e:
                lineas.append([])
            lineas[e].append(dts_bruto[k][e])
    x =[datetime.datetime.strptime(k,'%d-%b-%y %H:%M:%S') for k in dts_bruto]
    ys = list()
    for e in lineas:
        previo_0 = map(lambda jg:jg.replace(limpia,''),e)
        previo_1 = map(float,previo_0)
        ys.append(list(previo_1))
    return x,ys

def genera_grafica(self,dts_uso):
        x,ys = prepara_dts(dts_uso,self.limpia)
        plt.clf()
        estilos = ['g-','ro-.','ko-.','bo-.']
        for n,e in enumerate(ys):
            plt.plot(e,estilos[n])
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.title(self.nombre)
        plt.ylabel(self.eje_y)
        plt.xticks(range(len(x)), x,rotation=67)        
        plt.savefig(self.ruta+self.nombre+'.png')
        

class Graficas():
    """
    conjunto de graficas para este reporte.
    """
    def __init__(self,resultados):
        self.tabla = resultados
        self.ruta = '/run/media/injektilo/datos/propio/hmd/p_reporte/probando/'
        self.ruta += 'recursos/tmp/'
        self.archivos = list()
    def UMN(self):
        self.nombre = 'UMN'
        self.eje_y = 'Volts'
        self.limpia = 'V'
        dts_uso = {e['TIMESTAMP']:(e['SETPOINT'],e['UMN1'],e['UMN2'],e['UMN3'])\
                   for e in self.tabla}        
        genera_grafica(self,dts_uso)
        self.archivos.append(self.ruta+self.nombre+'.png')
    def URMS(self):
        self.nombre = 'URMS'
        self.eje_y = 'Volts'
        self.limpia = 'V'
        dts_uso = {e['TIMESTAMP']:(e['SETPOINT'],e['URMS1'],e['URMS2'],e['URMS3'])\
                   for e in self.tabla}        
        genera_grafica(self,dts_uso)
        self.archivos.append(self.ruta+self.nombre+'.png')
    def borra(self):
        for e in self.archivos:
            remove(e)
