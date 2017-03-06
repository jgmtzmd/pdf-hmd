from motor.lee_csv import lee_archivo
from motor.crea_graficas import Graficas
from motor.generador_pdf import genera_pdf
import os
import time
import logging

periodo = 3
ruta = '/run/media/injektilo/datos/propio/hmd/p_reporte/probando/otjetibo/'
formato_log ="%(levelname)s:%(asctime)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formato_log)

def revisa(ruta):
    contenido = os.listdir(ruta)
    csvs = [e for e in contenido if e.lower().endswith('.csv')]
    pdfs = [e for e in contenido if e.lower().endswith('.pdf')]
    logging.debug(f'revisando carpeta {ruta}')
    pnds = list()
    for e in csvs:
        x = e.replace('.csv','.pdf').replace('.CSV','.pdf')
        if x not in pdfs:
            pnds.append(e.replace('.CSV','.csv'))
    return pnds

while True:
    time.sleep(periodo)
    pnds = revisa(ruta)
    if len(pnds):
        for csv_a_leer in pnds:
            tiempo = list()
            tiempo.append(time.time())
            pdf_a_crear = ruta+csv_a_leer.replace('.csv','.pdf')
            resultados = lee_archivo(ruta,csv_a_leer)
            tiempo.append(time.time())
            graficas = Graficas(resultados)
            graficas.UMN()
            graficas.URMS()
            tiempo.append(time.time())
            genera_pdf(pdf_a_crear,resultados)
            tiempo.append(time.time())
            graficas.borra()
            tiempo.append(time.time())
            logging.info(f'haciendo reporte de {csv_a_leer}')
            tiempo.append(time.time())
            logging.debug(f'tiempo lect csv: {tiempo[1]-tiempo[0]:.3}')
            logging.debug(f'tiempo gen grfs: {tiempo[2]-tiempo[1]:.3}')
            logging.debug(f'tiempo gen pdf: {tiempo[3]-tiempo[2]:.3}')
            logging.debug(f'tiempo brr pdf: {tiempo[4]-tiempo[3]:.3}')
            logging.debug(f'tiempo msj log: {tiempo[5]-tiempo[4]:.3}')
            logging.info(f'tiempos de ejecucion {tiempo[5]-tiempo[0]:.3}')

"""
CREMAS
. grafs: usar subplots? figure()?
. grafs interpolar
"""