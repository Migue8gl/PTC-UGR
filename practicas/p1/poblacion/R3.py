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




import funciones
import csv
import matplotlib.pyplot as plt
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
    plt.savefig('./imagenes/R3.jpg')


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
        
        print(file_table)

        # Quitamos las etiquetas de cierre html
        cadena_html = file_table.replace('</body></html>', '')
        # Si se ejecuta varias veces, debemos borrar los anteriores graficos
        cadena_html = cadena_html.replace(
            '<img src="../imagenes/R3.jpg" style="display: block; margin: 0 auto;">', '')
        cadena_html += '<img src="../imagenes/R3.jpg" style="display: block; margin: 0 auto;">'
        cadena_html += '</body></html>'
    with open('./resultados/poblacionComAutonomas.html', 'w') as file:
        file.write(cadena_html)


ejecutar()
