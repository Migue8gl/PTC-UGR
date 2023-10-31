#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Sáb Oct 21 13:04:21 2023
Por: migue8gl
"""

"""
Script R4: Generar una tabla en una página web con las variaciones absolutas y
relativas de población desde 2017 a 2011 para cada comunidad autónoma, debe de
estar desgregado por hombres y mujeres.
"""




import csv
import funciones
def calcular_variaciones_ca(poblacion_dict):
    ca_provincias = funciones.obtener_ca_provincias()
    poblaciones_ccaa = funciones.obtener_poblaciones_ccaa(
        ca_provincias, poblacion_dict)
    
    poblaciones_sorted = sorted(
        poblaciones_ccaa,
        key=lambda x: sum(
            int(poblaciones_ccaa[x][str(y)]) for y in range(2017, 2009, -1)
        ),
        reverse=True
    )

    variaciones = {}

    # Obtenemos claves de años para hombres y mujeres
    ca = poblaciones_sorted[0]
    años_h = [key for key in poblaciones_ccaa[ca].keys() if key.startswith('H')]
    años_m = [key for key in poblaciones_ccaa[ca].keys() if key.startswith('M')]
    
    # Var absoluta
    for ca in poblaciones_sorted:
        if ca not in variaciones:
            variaciones[ca] = {'VarAbs': {'H': {}, 'M': {}},
                               'VarRel': {'H': {}, 'M': {}}}

        # Var absoluta hombre
        for año in años_h:
            if año != 'H2010':
                año_minus_one = 'H' + str(int(año.replace('H', '')) - 1)
                var_abs = float(poblaciones_ccaa[ca][año]) - \
                    float(poblaciones_ccaa[ca][año_minus_one])
                var_abs = funciones.redondear_numero(var_abs, 2)
                variaciones[ca]['VarAbs']['H'][año.replace('H', '')] = var_abs

        # Var absoluta mujeres
        for año in años_m:
            if año != 'M2010':
                año_minus_one = 'M' + str(int(año.replace('M', '')) - 1)
                var_abs = float(poblaciones_ccaa[ca][año]) - \
                    float(poblaciones_ccaa[ca][año_minus_one])
                var_abs = funciones.redondear_numero(var_abs, 2)
                variaciones[ca]['VarAbs']['M'][año.replace('M', '')] = var_abs
            
        # Var relativa hombres
        for año in años_h:
            if año != 'H2010':
                año_minus_one = 'H' + str(int(año.replace('H', '')) - 1)
                var_abs = float(poblaciones_ccaa[ca][año]) - \
                    float(poblaciones_ccaa[ca][año_minus_one])
                var_rel = (var_abs / float(poblaciones_ccaa[ca][año_minus_one]) * 100)
                var_rel = funciones.redondear_numero(var_rel, 2)
                variaciones[ca]['VarRel']['H'][año.replace('H', '')] = var_rel

        # Var relativa mujeres
        for año in años_m:
            if año != 'M2010':
                año_minus_one = 'M' + str(int(año.replace('M', '')) - 1)
                var_abs = float(poblaciones_ccaa[ca][año]) - \
                    float(poblaciones_ccaa[ca][año_minus_one])
                var_rel = (var_abs / float(poblaciones_ccaa[ca][año_minus_one]) * 100)
                var_rel = funciones.redondear_numero(var_rel, 2)
                variaciones[ca]['VarRel']['M'][año.replace('M', '')] = var_rel
                
    print(variaciones)
    return variaciones	


def ejecutar():
    # Limpiamos el CSV de provincias y le damos un nuevo nombre
    funciones.limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')

    # Leemos el archivo CSV limpio como un diccionario
    with open('./resultados/poblacionProvinciasHM2010-17-final.csv', encoding="utf8") as csvarchivo:
        poblacion_dict = csv.DictReader(csvarchivo, delimiter=';')

        # Creamos la tabla HTML
        file_table = open(
            "./resultados/variacionComAutonomas.html", "w", encoding="utf8")

        # Agregamos la cabecera y el inicio del HTML
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
        <body><table><caption>Tabla variaciones relativas/absolutas CA</caption>
        <tbody>"""

        # Agregamos las columnas correspondientes de variaciones
        cadena_html += """<tr><th scope="col"></th><th scope="col" colspan=14>
        Variación Absoluta</th><th scope="col" colspan=14>Variación Relativa
        </th></tr><tr>"""

        # Agregamos las columnas de hombres y mujeres
        cadena_html += """<tr><th scope="col"></th><th scope="col" colspan=14>
        Hombres</th><th scope="col" colspan=14>Mujeres</th>
        <th scope="col" colspan=14>Hombres</th>
        <th scope="col" colspan=14>Mujeres</th></tr><tr>"""

        # Agregamos los campos de nuestra tabla
        cabecera = '2017;2016;2015;2014;2013;2012;2011'.split(';')
        cadena_html += '<tr><th scope="col">Provincia</th>'
        for _ in range(4):
            for campo in cabecera:
                cadena_html += '<th>' + campo + '</th>'

        calcular_variaciones_ca(poblacion_dict)
        # Calculamos las variaciones por comunidad autonoma

        for registro in poblacion_dict:
            cadena_html += '<tr><th scope="row">' + \
                registro['Provincia'] + '</th>'

            for año in range(2017, 2010, -1):
                varAbs = float(registro[str(año)]) - \
                    float(registro[str(año-1)])
                varAbs = funciones.redondear_numero(varAbs, 2)
                cadena_html += '<td>' + \
                    funciones.separador_miles(varAbs) + '</td>'

            for año in range(2017, 2010, -1):
                varAbs = float(registro[str(año)]) - \
                    float(registro[str(año-1)])
                varRel = (varAbs / float(registro[str(año-1)]) * 100)
                varRel = funciones.redondear_numero(varRel, 2)
                cadena_html += '<td>' + \
                    funciones.separador_miles(varRel) + '</td>'
            cadena_html += '</tr>'

        cadena_html += '</tbody></table></body></html>'
        file_table.write(cadena_html)
        file_table.close()


if __name__ == "__main__":
    ejecutar()
