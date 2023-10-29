#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:27:27 2023

@author: migue8gl
"""

"""
Script R2: Mostrar en página web los valores poblacionales de cada comunidad
autónoma en cada año de 2010 a 2017, en total y desagregado por sexos
"""




import csv
import funciones
from lxml import html
def ejecutar():
    # Creamos un diccionario en el que meteremos las comunidades autónomas como
    # clave y una lista de provincias asociadas
    comunidades_dict = {}

    # Leemos del fichero html
    comunidades_fich = open(
        './entradas/comunidadAutonoma-Provincia.htm', 'r', encoding="utf8")
    com_string = comunidades_fich.read()

    # Creamos el objeto tree para analizar el documento HTML como cadenas
    tree = html.fromstring(com_string)

    celdas = tree.xpath('//td/text()')

    for index in range(1, len(celdas), 4):
        comunidad_autonoma = celdas[index - 1] + ' ' + celdas[index]
        provincia = celdas[index + 1] + ' ' + celdas[index + 2]
        comunidades_dict[provincia] = comunidad_autonoma

    #-------------------------------------------------------------------------#

    # Limpiamos el csv de provincias y le damos un nuevo nombre
    funciones.limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')

    # Leemos el fichero csv limpio como un diccionario
    with open('./resultados/poblacionProvinciasHM2010-17-final.csv',
              encoding="utf8") as csvarchivo:
        poblacion_dict = csv.DictReader(csvarchivo, delimiter=';')

        # Creamos la tabla html
        file_table = open(
            "./resultados/poblacionComAutonomas.html", "w",
            encoding="utf8")

        # Añadimos la cabecera y el inicio del html
        cadena_html = """<!DOCTYPE HTML5><html>
        <head><title>Población comunidades Autónomas</title>
        <link rel="stylesheet" href="../entradas/aux/estilo.css">
        <meta charset="utf8">
        <style>
            th, td {
                text-align: center;
            }
        </style>
        </head>  
        <body><table><caption>Tabla poblaciones</caption>
        <tbody>"""

        # Añadimos las columnas correspondientes
        cadena_html += """<tr><th scope="col" rowspan=2>CCAA</th>
        <th scope="col" colspan=8>Total</th>
        <th scope="col" colspan=8>Hombres</th>
        <th scope="col" colspan=8>Mujeres</th></tr><tr>"""

        # Añadimos los campos de nuestra tabla
        cabecera = '2017;2016;2015;2014;2013;2012;2011;2010'.split(';')
        for _ in range(3):
            for campo in cabecera:
                cadena_html += '<th>' + campo + '</th>'

        # Creamos una lista de claves para almacenar el recuento de cada CA
        claves = '2017;2016;2015;2014;2013;2012;2011;2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010'.split(
            ';')

        # Vamos rellenando la tabla con las comunidades autónomas y sumando
        # los valores de cada provincia dentro de esta en total
        poblacion_total_ccaa = {}
        for dict in poblacion_dict:
            prov = dict['Provincia']
            # La primera fila nos la saltamos, no es una provincia
            if prov != 'Total Nacional':
                ca = comunidades_dict[prov]

                # Sumar las poblaciones de la provincia a las poblaciones
                # totales de la comunidad autónoma
                for clave in dict:
                    if clave != 'Provincia':
                        if ca not in poblacion_total_ccaa:
                            # Creamos diccionario con claves para cada año
                            poblacion_total_ccaa[ca] = {
                                clave: 0 for clave in claves}
                        # Sumamos para obtener finalmente un total de población
                        poblacion_total_ccaa[ca][clave] += float(dict[clave])

        # Ordenamos por índice de Comunidad Autónoma
        poblacion_total_ccaa = {k: v for k, v in sorted(
            poblacion_total_ccaa.items(), key=lambda item: int(item[0].split()[0]))}

        # Vamos rellenando la tabla con los valores finales
        for ca in poblacion_total_ccaa:
            cadena_html += '<tr><th scope="row">' + ca + '</th>'

            for año in claves:
                cadena_html += '<td>' + \
                    funciones.separador_miles(
                        poblacion_total_ccaa[ca][año], '%0.f') + '</td>'
            cadena_html += '</tr>'

        cadena_html += '</tbody></table></body></html>'

        file_table.write(cadena_html)
        file_table.close()


ejecutar()
