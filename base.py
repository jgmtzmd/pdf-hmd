from motor.lee_csv import lee_archivo
from motor.crea_graficas import Graficas
from motor.generador_pdf import genera_pdf


ruta = '/run/media/injektilo/datos/propio/hmd/p_reporte/probando/otjetibo/'
csv_a_leer = '01241230.csv'
pdf_a_crear = ruta+csv_a_leer.replace('.csv','.pdf')

resultados = lee_archivo(ruta,csv_a_leer)
graficas = Graficas(resultados)
x = graficas.UMNs()
genera_pdf(pdf_a_crear,resultados)
graficas.borra()
# print(x)


"""PND
. grafs flex
. grafs interpolar
. grafs brr
. log()
. timeado
. usar tmpfile?
. pdf: unidades temperatura.
. grafs: usar subplots? figure()?
"""