import csv


def lee_archivo(ruta,archivo):
    """
    lee archivo teniendo ruta completa. resultado luego se lee algo asi:
    x = lee_archivo(ruta, archivo)
    print(x[2]['URMS PROM'])
    """
    with open(ruta+archivo, encoding='cp1254') as chv:
        dts = csv.DictReader(chv)
        return [e for e in dts]

