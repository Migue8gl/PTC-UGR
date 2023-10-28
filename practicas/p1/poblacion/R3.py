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
def get_media_poblacional():
    # Creamos un diccionario en el que meteremos las comunidades autónomas como
    # clave y un diccionario con media poblacional dividia por sexos como
    # valor -> 'Comunidad Autónoma': {'PobHombres': None, 'PobMujeres': None}
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
        comunidades_dict[ca[0]] = {'PobHom': 0, 'PobMuj': 0}
        for i in range(8, 16):
            comunidades_dict[ca[0]]['PobHom'] += int(celdas[i])
            
        # Ahora lo mismo pero para las mujeres
        for i in range(16, 24):
            comunidades_dict[ca[0]]['PobMuj'] += int(celdas[i])
        
        # Dividimos los valores totales entre 8 años para obtener la media
        comunidades_dict[ca[0]]['PobMuj'] /= 8
        comunidades_dict[ca[0]]['PobMuj'] /= 8
        index += 1
    print(comunidades_dict)


get_media_poblacional()
