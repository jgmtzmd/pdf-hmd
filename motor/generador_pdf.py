import pydf
import chameleon
template = '/run/media/injektilo/datos/propio/hmd/p_reporte/probando/'
template += 'recursos/template.tp'

def genera_pdf(rutarchivo,resultados):
    """
    genera pdf apoyandose en template chameleon.
    usa lista de dicts q le pasa 'lee_csv'
    """
    pagina_0 = chameleon.PageTemplateFile(template)
    pagina = pagina_0.render(resultados=resultados)
    print(pagina)        
    pdf = pydf.generate_pdf(pagina, orientation='Landscape', page_size='A3')
    with open(rutarchivo,'wb') as f:
        f.write(pdf)
