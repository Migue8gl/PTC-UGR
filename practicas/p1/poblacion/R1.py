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
import funciones
def ejecutar():

    # Limpiamos el csv de provincias y le damos un nuevo nombre
    funciones.limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')

    # Leemos el fichero csv limpio como un diccionario
    with open('./resultados/poblacionProvinciasHM2010-17-final.csv',
              encoding="utf8") as csvarchivo:
        poblacion_dict = csv.DictReader(csvarchivo, delimiter=';')

        # Creamos la tabla html
        file_table = open(
            "./resultados/variacionProvincias2011-17.html", "w",
            encoding="utf8")

        # Añadimos la cabecera y el inicio del html
        cadena_html = """<!DOCTYPE HTML5><html>
        <head><title>Variación Provincias</title>
        <link rel="stylesheet" href="../entradas/aux/estilo.css">
        <meta charset="utf8">
        <style>
            th, td {
                text-align: center;
            }
        </style>
        </head>
        <body><table><caption>Tabla variaciones relativas/absolutas</caption>
        <tbody>"""

        # Añadimos las columnas correspondientes
        cadena_html += """<tr><th scope="col"></th><th scope="col" colspan=7>
        Variación Absoluta</th><th scope="col" colspan=7>Variación Relativa
        </th></tr><tr>"""

        # Añadimos los campos de nuestra tabla
        cabecera = '2017;2016;2015;2014;2013;2012;2011'.split(';')
        cadena_html += '<tr><th scope="col">Provincia</th>'
        for _ in range(2):
            for campo in cabecera:
                cadena_html += '<th>' + campo + '</th>'

        """ Vamos rellenando la tabla con los valores calculados directamente 
        de nuestro diccionario """
        for dict in poblacion_dict:
            cadena_html += '<tr><th scope="row">' + dict['Provincia'] + '</th>'

            for año in range(2017, 2010, -1):
                varAbs = float(dict[str(año)]) - float(dict[str(año-1)])
                varAbs = funciones.redondear_numero(varAbs, 2)
                cadena_html += '<td>' + \
                    funciones.separador_miles(varAbs) + '</td>'

            for año in range(2017, 2010, -1):
                varAbs = float(dict[str(año)]) - float(dict[str(año-1)])
                varRel = (varAbs / float(dict[str(año-1)]))*100
                varRel = funciones.redondear_numero(varRel, 2)
                cadena_html += '<td>' + \
                    funciones.separador_miles(varRel) + '</td>'
            cadena_html += '</tr>'

        cadena_html += '</tbody></table></body></html>'
        file_table.write(cadena_html)
        file_table.close()


ejecutar()
