#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Dom Oct 22 13:33:31 2023
Por: migue8gl
"""

import locale
from lxml import html
from decimal import Decimal, ROUND_HALF_UP


def separador_miles(numero, precision='%.2f'):
    # Configuramos la localización para separador de miles
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string(precision, numero, grouping=True)


def redondear_numero(numero, decimales=2):
    return Decimal(numero).quantize(Decimal('1e-{0}'.format(decimales)), rounding=ROUND_HALF_UP)


def limpiar_csv_poblaciones(csv_nombre):
    # Leemos el archivo CSV inicial, lo limpiamos y agregamos encabezado
    fichero_inicial = open(
        './entradas/poblacionProvinciasHM2010-17.csv', 'r', encoding='utf8')
    cadena_inicial = fichero_inicial.read()
    fichero_inicial.close()

    primero = cadena_inicial.find('Total Nacional')
    ultimo = cadena_inicial.find('Notas')
    cadena_final = cadena_inicial[primero:ultimo]

    # Eliminamos el último carácter ';' que es innecesario
    lines = cadena_final.split('\n')
    cleaned_lines = [line.rstrip(';') for line in lines]
    cadena_final = '\n'.join(cleaned_lines)

    # Creamos el encabezado y lo agregamos al archivo CSV final
    cabecera = 'Provincia;2017;2016;2015;2014;2013;2012;2011;2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010'

    fichero_final = open('./resultados/' + csv_nombre, 'w', encoding='utf8')
    fichero_final.write(cabecera + '\n' + cadena_final)
    fichero_final.close()


def obtener_ca_provincias():
    # Creamos un diccionario en el que almacenaremos las comunidades autónomas como clave y una lista de provincias asociadas
    comunidades_dict = {}

    # Leemos el archivo HTML de comunidades autónomas y provincias
    comunidades_fich = open(
        './entradas/comunidadAutonoma-Provincia.htm', 'r', encoding="utf8")
    com_string = comunidades_fich.read()

    # Creamos un árbol HTML para analizar el documento HTML como cadenas
    tree = html.fromstring(com_string)

    celdas = tree.xpath('//td/text()')

    for index in range(1, len(celdas), 4):
        comunidad_autonoma = celdas[index - 1] + ' ' + celdas[index]
        provincia = celdas[index + 1] + ' ' + celdas[index + 2]
        comunidades_dict[provincia] = comunidad_autonoma

    return comunidades_dict


def obtener_poblaciones_ccaa(comunidades, datos_csv):
    poblacion_total_ccaa = {}
    claves = datos_csv.fieldnames.copy()
    claves.remove('Provincia')

    for registro in datos_csv:
        provincia = registro['Provincia']
        # La primera fila no es una provincia, la omitimos
        if provincia != 'Total Nacional':
            ca = comunidades[provincia]

            # Sumar las poblaciones de la provincia a las poblaciones totales de la comunidad autónoma
            for clave in registro:
                if clave != 'Provincia':
                    if ca not in poblacion_total_ccaa:
                        # Creamos un diccionario con claves para cada año
                        poblacion_total_ccaa[ca] = {
                            clave: 0 for clave in claves}
                    # Sumamos para obtener finalmente un total de población
                    poblacion_total_ccaa[ca][clave] += float(registro[clave])

    return poblacion_total_ccaa
