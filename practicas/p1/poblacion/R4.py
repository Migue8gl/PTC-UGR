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




import funciones
import numpy as np
def calcular_variaciones_ccaa():
    poblaciones_ccaa = funciones.cargar_y_procesar_datos()
    poblaciones_sorted = funciones.obtener_lista_ccaa_ordenada(
        poblaciones_ccaa)
    variaciones = {}

    # Obtenemos claves de años para hombres y mujeres
    ca = poblaciones_sorted[0]
    años_h = np.array(
        [key for key in poblaciones_ccaa[ca].keys() if key.startswith('H')])
    años_m = np.array(
        [key for key in poblaciones_ccaa[ca].keys() if key.startswith('M')])

    for ca in poblaciones_sorted:
        if ca not in variaciones:
            variaciones[ca] = {'VarAbs': {'H': {}, 'M': {}},
                               'VarRel': {'H': {}, 'M': {}}}

        # Var absoluta
        for año in años_h:
            if año != 'H2010':
                año_minus_one = 'H' + str(int(año.replace('H', '')) - 1)
                var_abs = np.float64(
                    poblaciones_ccaa[ca][año]) - np.float64(poblaciones_ccaa[ca][año_minus_one])
                var_abs = funciones.redondear_numero(var_abs, 2)
                variaciones[ca]['VarAbs']['H'][año.replace('H', '')] = var_abs

        for año in años_m:
            if año != 'M2010':
                año_minus_one = 'M' + str(int(año.replace('M', '')) - 1)
                var_abs = np.float64(
                    poblaciones_ccaa[ca][año]) - np.float64(poblaciones_ccaa[ca][año_minus_one])
                var_abs = funciones.redondear_numero(var_abs, 2)
                variaciones[ca]['VarAbs']['M'][año.replace('M', '')] = var_abs

        # Var relativa
        for año in años_h:
            if año != 'H2010':
                año_minus_one = 'H' + str(int(año.replace('H', '')) - 1)
                var_abs = np.float64(
                    poblaciones_ccaa[ca][año]) - np.float64(poblaciones_ccaa[ca][año_minus_one])
                var_rel = (
                    var_abs / np.float64(poblaciones_ccaa[ca][año_minus_one])) * 100
                var_rel = funciones.redondear_numero(var_rel, 2)
                variaciones[ca]['VarRel']['H'][año.replace('H', '')] = var_rel

        for año in años_m:
            if año != 'M2010':
                año_minus_one = 'M' + str(int(año.replace('M', '')) - 1)
                var_abs = np.float64(
                    poblaciones_ccaa[ca][año]) - np.float64(poblaciones_ccaa[ca][año_minus_one])
                var_rel = (
                    var_abs / np.float64(poblaciones_ccaa[ca][año_minus_one])) * 100
                var_rel = funciones.redondear_numero(var_rel, 2)
                variaciones[ca]['VarRel']['M'][año.replace('M', '')] = var_rel

    return variaciones


def ejecutar():
    # Limpiamos el CSV de provincias y le damos un nuevo nombre
    funciones.limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')

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
    cadena_html += """<tr><th scope="col"></th><th scope="col" colspan=7>
        Hombres</th><th scope="col" colspan=7>Mujeres</th>
        <th scope="col" colspan=7>Hombres</th>
        <th scope="col" colspan=7>Mujeres</th></tr><tr>"""

    # Agregamos los campos de nuestra tabla
    cabecera = '2017;2016;2015;2014;2013;2012;2011'.split(';')
    cadena_html += '<tr><th scope="col">Provincia</th>'
    for _ in range(4):
        for campo in cabecera:
            cadena_html += '<th>' + campo + '</th>'

    # Calculamos las variaciones por comunidad autonoma
    variaciones = calcular_variaciones_ccaa()

    for ca in variaciones:
        cadena_html += '<tr><th scope="row">' + \
            funciones.limpiar_digitos(ca) + '</th>'
        for campo in cabecera:
            cadena_html += '<td>' + \
                funciones.separador_miles(
                    variaciones[ca]['VarAbs']['H'][campo]) + '</td>'
        for campo in cabecera:
            cadena_html += '<td>' + \
                funciones.separador_miles(
                    variaciones[ca]['VarAbs']['M'][campo]) + '</td>'
        for campo in cabecera:
            cadena_html += '<td>' + \
                funciones.separador_miles(
                    variaciones[ca]['VarRel']['H'][campo]) + '</td>'
        for campo in cabecera:
            cadena_html += '<td>' + \
                funciones.separador_miles(
                    variaciones[ca]['VarRel']['M'][campo]) + '</td>'
        cadena_html += '</tr>'

    cadena_html += '</tbody></table></body></html>'
    file_table.write(cadena_html)
    file_table.close()


if __name__ == "__main__":
    ejecutar()
