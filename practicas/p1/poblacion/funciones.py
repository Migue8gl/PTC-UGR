#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Dom Oct 22 13:33:31 2023
Por: migue8gl
"""

import locale
from lxml import html
import csv
from decimal import Decimal, ROUND_HALF_UP

"""
Esta función toma una cadena de texto y elimina todos los dígitos numéricos,
dejando solo los caracteres no numéricos.

Args:
    cadena (str): La cadena de texto que se va a limpiar de dígitos.

Returns:
    str: La cadena de texto resultante sin dígitos numéricos.
"""


def limpiar_digitos(cadena):
    # Inicializamos una cadena vacía para almacenar el resultado
    resultado = ""

    # Iteramos a través de cada carácter en la cadena
    for caracter in cadena:
        # Verificamos si el carácter no es un dígito
        if not caracter.isdigit():
            # Si no es un dígito, lo agregamos al resultado
            resultado += caracter

    return resultado


"""
Esta función toma un número y opcionalmente una cadena de formato de precisión
y devuelve el número formateado con separadores de miles.

Args:
    numero (float): El número que se formateará.
    precision (str, opcional): La cadena de formato de precisión. 
    Por defecto, '%.2f'.

Returns:
    str: El número formateado con separadores de miles.
"""


def separador_miles(numero, precision='%.2f'):
    # Configuramos la localización para separador de miles
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string(precision, numero, grouping=True)


"""
Esta función toma un número y un número de decimales y redondea el número al 
número de decimales especificado.

Args:
    numero (float): El número que se redondeará.
    decimales (int, opcional): El número de decimales al que se redondeará el 
    número. Por defecto, 2.

Returns:
    Decimal: El número redondeado.
"""


def redondear_numero(numero, decimales=2):
    return Decimal(numero).quantize(Decimal('1e-{0}'.format(decimales)), rounding=ROUND_HALF_UP)


"""
Esta función limpia un archivo CSV de poblaciones y agrega un encabezado.

Args:
    csv_nombre (str): El nombre del archivo CSV a limpiar y al que se le 
    agregará un encabezado.
"""


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


"""
Esta función obtiene un diccionario que asocia comunidades autónomas con sus 
provincias correspondientes.

Returns:
    dict: Un diccionario que asocia comunidades autónomas con provincias.
"""


def obtener_ca_provincias():
    # Creamos un diccionario en el que almacenaremos las comunidades autónomas
    # como clave y una lista de provincias asociadas
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


"""
Esta función calcula la población total de cada comunidad autónoma a partir de 
un archivo CSV de poblaciones y un diccionario de asociación de comunidades autónomas con provincias.

Args:
    comunidades (dict): Un diccionario que asocia comunidades autónomas con 
    provincias.
    datos_csv (csv.DictReader): El archivo CSV de poblaciones.

Returns:
    dict: Un diccionario que asocia comunidades autónomas con la población 
    total de cada año.
"""


def obtener_poblaciones_ccaa(comunidades, datos_csv):
    poblacion_total_ccaa = {}
    claves = datos_csv.fieldnames.copy()
    claves.remove('Provincia')

    for registro in datos_csv:
        provincia = registro['Provincia']
        # La primera fila no es una provincia, la omitimos
        if provincia != 'Total Nacional':
            ca = comunidades[provincia]

            # Sumar las poblaciones de la provincia a las poblaciones totales
            # de la comunidad autónoma
            for clave in registro:
                if clave != 'Provincia':
                    if ca not in poblacion_total_ccaa:
                        # Creamos un diccionario con claves para cada año
                        poblacion_total_ccaa[ca] = {
                            clave: 0 for clave in claves}
                    # Sumamos para obtener finalmente un total de población
                    poblacion_total_ccaa[ca][clave] += float(registro[clave])

    return poblacion_total_ccaa


def obtener_lista_ccaa_ordenada(poblaciones_ccaa):
    """
    Esta función devuelve una lista de comunidades autónomas ordenadas por su 
    población total.

    Args:
        poblaciones_ccaa (dict): Un diccionario que asocia comunidades 
        autónomas con la población total de cada año.

    Returns:
        list: Una lista de comunidades autónomas ordenadas por su población 
        total.
    """
    poblaciones_sorted = sorted(
        poblaciones_ccaa,
        key=lambda x: sum(
            int(poblaciones_ccaa[x][str(y)]) for y in range(2017, 2009, -1)
        ),
        reverse=True
    )
    return poblaciones_sorted


def cargar_y_procesar_datos():
    """
    Esta función carga y procesa los datos de población y devuelve un 
    diccionario que asocia comunidades autónomas con la población total.

    Returns:
        dict: Un diccionario que asocia comunidades autónomas con la población 
        total.
    """
    # Obtenemos las comunidades autónomas y provincias
    comunidades = obtener_ca_provincias()

    #  Limpiar el CSV de provincias y darle un nuevo nombre
    limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')
    # Abrimos y procesamos el archivo CSV
    datos_csv = open(
        './resultados/poblacionProvinciasHM2010-17-final.csv', 'r', encoding="utf8")
    poblacion_dict = csv.DictReader(datos_csv, delimiter=';')
    poblaciones_comunidades = obtener_poblaciones_ccaa(
        comunidades, poblacion_dict)
    return poblaciones_comunidades


def insertar_imagen_en_html(ruta_html, ruta_imagen):
    """
    Esta función inserta una imagen en un archivo HTML.

    Args:
        ruta_html (str): La ruta al archivo HTML en el que se insertará la 
        imagen.
        ruta_imagen (str): La ruta a la imagen que se insertará en el archivo 
        HTML.
    """
    # Insertar la imagen en el archivo HTML
    contenido_html = ''

    with open(ruta_html, 'r') as archivo_html:
        contenido_html = archivo_html.read()

        # Eliminar la imagen anterior si existe
        contenido_html = contenido_html.replace('</body></html>', '')
        if f'<img src="{ruta_imagen}" style="display: block; margin: 50px auto;">' not in contenido_html:
            # Insertar la nueva imagen
            contenido_html += f'<img src="{ruta_imagen}" style="display: block; margin: 50px auto;">'
        contenido_html += '</body></html>'

    with open(ruta_html, 'w') as archivo_html:
        archivo_html.write(contenido_html)
