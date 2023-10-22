#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:04:21 2023

@author: migue8gl
"""

"""
Script R1: Calcular la variación de la población por provincias desde el año 
2011 a 2017 en términos absolutos y relativos.
"""




import csv
def ejecutar():

    # Leemos el fichero inicial, lo limpiamos y añadimos cabezera
    fichero_inicial = open(
        './entradas/poblacionProvinciasHM2010-17.csv', 'r', encoding='utf8')
    cadena_inicial = fichero_inicial.read()
    fichero_inicial.close()

    primero = cadena_inicial.find('Total Nacional')
    ultimo = cadena_inicial.find('Notas')
    cadena_final = cadena_inicial[primero:ultimo]

    # Limpiamos el último caracter ';' que es innecesario
    lines = cadena_final.split('\n')
    cleaned_lines = [line.rstrip(';') for line in lines]  # Cogemos último ';'
    cadena_final = '\n'.join(cleaned_lines)

    # Creamos cabecera y se la añadimos al fichero csv final
    cabecera = 'Provincia;2017;2016;2015;2014;2013;2012;2011;2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010'

    fichero_final = open(
        './resultados/poblacionProvinciasHM2010-17-final.csv', 'w',
        encoding='utf8')
    fichero_final.write(cabecera + '\n' + cadena_final)
    fichero_final.close()

# --------------------------------------------------------------------------- #

    # Leemos el fichero csv limpio como un diccionario
    with open('./resultados/poblacionProvinciasHM2010-17-final.csv',
              encoding="utf8") as csvarchivo:
        poblacionDict = csv.DictReader(csvarchivo, delimiter=';')

        # Creamos la tabla html
        file_table = open(
            "./resultados/variacionProvincias2011-17.html", "w",
            encoding="utf8")

        # Añadimos la cabecera y el inicio del html
        cadena_html = """<!DOCTYPE HTML5><html>
        <head><title>Variación Provincias</title>
        <link rel="stylesheet" href="../entradas/aux/estilo.css">
        <meta charset="utf8"></head>  
        <body><table><caption>Tabla variaciones relativas/absolutas</caption>
        <tbody>"""

        # Añadimos las columnas correspondientes
        cadena_html += """<tr><th scope="col"></th><th scope="col">Variación 
        Absoluta</th><th scope="col">Variación Relativa</th></tr><tr>"""

        # Añadimos los campos de nuestra tabla
        cabecera = '2017;2016;2015;2014;2013;2012;2011;'.split(';')
        cadena_html += '<tr><th scope="col">Provincia</th>'
        for _ in range(2):
            for campo in cabecera:
                cadena_html += '<th>' + campo + '</th>'

        """ Vamos rellenando la tabla con los valores calculados directamente 
        de nuestro diccionario """
        for dict in poblacionDict:
            cadena_html += '<tr><th scope="row">' + dict['Provincia'] + '</th>'

            # Debemos evitar 2010, por ello comenzamos desde ahí
            for año in range(2017, 2011, -1):
                varAbs = (float(dict[str(año)]) /
                          float(dict[str(año-1)])) * 100
                cadena_html += '<td>' + str(varAbs) + '</td>'

            for año in range(2017, 2011, -1):
                varRel = float(dict[str(año)]) - float(dict[str(año-1)])
                cadena_html += '<td>' + str(varRel) + '</td>'

        cadena_html += '</tr></tbody></body></html>'
        file_table.write(cadena_html)
        file_table.close()


ejecutar()
