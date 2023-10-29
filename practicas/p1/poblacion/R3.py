#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:23:05 2023

@author: migue8gl
"""

"""
Script R3: Mostrar en página web gráfico de la media poblacional de cada
comunidad autónoma.
"""




from lxml import html
import funciones
import csv
import matplotlib.pyplot as plt
def get_media_poblacional():
    # Creamos un diccionario en el que meteremos las comunidades autónomas como
    # clave y un diccionario con media poblacional dividia por sexos como
    # valor -> 'Comunidad Autónoma': {'PobHombres': {'2017:, ...},
    # 'PobMujeres': {'2017:, ...}}}
    comunidades_dict = {}

    # Leemos del fichero html
    comunidades_fich = open(
        './resultados/poblacionComAutonomas.html', 'r', encoding="utf8")
    com_string = comunidades_fich.read()

    # Creamos el objeto tree para analizar el documento HTML como cadenas
    tree = html.fromstring(com_string)

    ca = ['Comunidad vacía']
    index = 3

    while ca:
        celdas = tree.xpath('//tr[' + str(index) + ']/td/text()')
        ca = tree.xpath('//tr[' + str(index) + ']/th/text()')

        # Iteramos desde el índice que corresponde a los años para hombres. Los
        # primeros 8 años (2010-2017) son totales, los siguientes hombres.
        años = '2017,2016,2015,2014,2013,2012,2011,2010'.split(',')
        if ca:
            comunidades_dict[ca[0]] = {'PobHom': {}, 'PobMuj': {}}
            for i, año in enumerate(años):
                # Inicializamos los valores del diccionario si no existen
                if año not in comunidades_dict[ca[0]]['PobHom']:
                    comunidades_dict[ca[0]]['PobHom'][año] = 0
                if año not in comunidades_dict[ca[0]]['PobMuj']:
                    comunidades_dict[ca[0]]['PobMuj'][año] = 0

                # Ahora podemos incrementar los valores de forma segura.
                # Incrementamos +8 en i, ya que los primeros años son totales
                comunidades_dict[ca[0]
                                 ]['PobHom'][año] += int(celdas[i+8].replace(',', ''))

            # El mismo proceso para la métrica en mujeres.
            # Incrementamos +16 en i, ya que los primeros años son totales y de
            # hombres.
            for i, año in enumerate(años):
                comunidades_dict[ca[0]
                                 ]['PobMuj'][año] += int(celdas[i+16].replace(',', ''))

        index += 1
    return comunidades_dict


def get_grafico(poblaciones_comunidades):
    # Ordenamos las comunidades autónomas de más población total a menos
    poblaciones_comunidades_sorted = sorted(
        poblaciones_comunidades,
        key=lambda x: sum(
            int(poblaciones_comunidades[x][str(y)]) for y in range(2017, 2009, -1)
        ),
        reverse=True
    )

    plt.figure("barras", figsize=(15, 14))
    plt.title('Población por sexo en el año 2017 (CCAA)')
    labels = []
    for index in range(10):
        ca = poblaciones_comunidades_sorted[index]
        x_h = poblaciones_comunidades[ca]['H2017']
        x_m = poblaciones_comunidades[ca]['M2017']
        plt.bar(index - 0.1, x_h, color="b", width=0.25)
        plt.bar(index - 0.1 + 0.25, x_m, color="r", width=0.25)
        labels.append(''.join(
            char for char in poblaciones_comunidades_sorted[index] if not char.isdigit()))

    plt.xticks(range(len(labels)), labels, rotation=60)
    plt.savefig('./resultados/grafico.jpg')


def ejecutar():
    comunidades = funciones.get_ca_provincias()

    datos_csv = open('./resultados/poblacionProvinciasHM2010-17-final.csv', 'r',
                     encoding="utf8")
    poblacion_dict = csv.DictReader(datos_csv, delimiter=';')
    # Cogemos la información de las comunidades y el csv procesado
    poblaciones_comunidades = funciones.get_poblaciones_ccaa(
        comunidades, poblacion_dict)
    # Obtenemos el gráfico y lo guardamos
    get_grafico(poblaciones_comunidades)

    # Insertamos la imagen en la web
    cadena_html = ''
    with open('./resultados/poblacionComAutonomas.html', 'r') as file:
        file_table = file.read()

        # Quitamos las etiquetas de cierre html
        cadena_html = file_table.replace('</body></html>', '')
        # Si se ejecuta varias veces, debemos borrar los anteriores graficos
        cadena_html = file_table.replace(
            '<img src="../resultados/grafico.jpg" style="display: block; margin: 0 auto;">', '')
        cadena_html += '<img src="../resultados/grafico.jpg" style="display: block; margin: 0 auto;">'
        cadena_html += '</body></html>'
    with open('./resultados/poblacionComAutonomas.html', 'w') as file:
        file.write(cadena_html)


ejecutar()
