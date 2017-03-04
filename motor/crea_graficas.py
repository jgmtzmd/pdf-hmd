import os
import matplotlib.pyplot as plt
import datetime


def prepara_dts(dts_bruto):
    lineas = list()
    for n,k in enumerate(dts_bruto):
        for e in range(len(dts_bruto[k])):
            if len(lineas) == e:
                lineas.append([])
            lineas[e].append(dts_bruto[k][e])
    x =[datetime.datetime.strptime(k,'%d-%b-%y %H:%M:%S') for k in dts_bruto]
    unidades = 'V'
    ys = list()
    for e in lineas:
        previo_0 = map(lambda jg:jg.replace(unidades,''),e)
        previo_1 = map(float,previo_0)
        ys.append(list(previo_1))
    return x,ys

class Graficas():
    def __init__(self,resultados):
        self.tabla = resultados
        self.ruta = '/run/media/injektilo/datos/propio/hmd/p_reporte/probando/'
        self.ruta += 'recursos/tmp/'
        self.archivos = list()
    def UMNs(self):
        self.nombre = 'UMNs'
        self.archivo = self.ruta+self.nombre+'.png'
        dts_uso = {e['TIMESTAMP']:(e['SETPOINT'],e['UMN1'],e['UMN2'],e['UMN3'])\
                   for e in self.tabla}
        x,ys = prepara_dts(dts_uso)
        plt.clf()
        estilos = ['g-','ro-.','ko-.','bo-.']
        for n,e in enumerate(ys):
            plt.plot(e,estilos[n])
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.title('UMNs')
        plt.ylabel('Voltios')
        plt.xticks(range(len(x)), x,rotation=67)        
        plt.savefig(self.archivo)
        self.archivos.append(self.archivo)
        return self.archivo
    def borra(self):
        print(self.archivos)
        for e in self.archivos:
            print('borro: ',e)
            os.remove(e)
        

