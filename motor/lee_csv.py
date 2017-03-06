import csv

class Datos():
    def __init__(self,reader):
        self.tabla = list(reader)
    def limpia_temperaturas(self):
        for e in self.tabla:
            e['T1(amb)'] = e['T1(amb)'].replace('�',u'\xb0')
            e['T2'] = e['T2'].replace('�',u'\xb0')
            e['T3'] = e['T3'].replace('�',u'\xb0')
            e['T4'] = e['T4'].replace('�',u'\xb0')

def lee_archivo(ruta,archivo):
    """
    lee archivo teniendo ruta completa. resultado luego se lee algo asi:
    x = lee_archivo(ruta, archivo)
    print(x[2]['URMS PROM'])
    """
    # with open(ruta+archivo, encoding='cp1254') as chv:
    with open(ruta+archivo, encoding='utf-8') as chv:
        dts = Datos(csv.DictReader(chv))
        dts.limpia_temperaturas()
        return dts.tabla
