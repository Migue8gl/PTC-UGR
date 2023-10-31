#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Sáb Oct 28 19:23:05 2023
Por: migue8gl 
"""

import funciones
import csv
import matplotlib.pyplot as plt


def cargar_y_procesar_datos():
    # Obtenemos las comunidades autónomas y provincias
    comunidades = funciones.obtener_ca_provincias()

    #  Limpiar el CSV de provincias y darle un nuevo nombre
    funciones.limpiar_csv_poblaciones('poblacionProvinciasHM2010-17-final.csv')
    # Abrimos y procesamos el archivo CSV
    datos_csv = open(
        './resultados/poblacionProvinciasHM2010-17-final.csv', 'r', encoding="utf8")
    poblacion_dict = csv.DictReader(datos_csv, delimiter=';')
    poblaciones_comunidades = funciones.obtener_poblaciones_ccaa(
        comunidades, poblacion_dict)
    return poblaciones_comunidades


def generar_grafico_poblacion(poblaciones_comunidades):
    # Ordenamos las comunidades autónomas de mayor a menor población total
    poblaciones_comunidades_sorted = sorted(
        poblaciones_comunidades,
        key=lambda x: sum(
            int(poblaciones_comunidades[x][str(y)]) for y in range(2017, 2009, -1)
        ),
        reverse=True
    )

    plt.figure("barras", figsize=(15, 14))
    plt.title('Población por sexo en el año 2017 (CCAA)')
    etiquetas = []
    for indice in range(10):
        comunidad_autonoma = poblaciones_comunidades_sorted[indice]
        hombres = poblaciones_comunidades[comunidad_autonoma]['H2017']
        mujeres = poblaciones_comunidades[comunidad_autonoma]['M2017']
        plt.bar(indice - 0.1, hombres, color="b", width=0.25)
        plt.bar(indice - 0.1 + 0.25, mujeres, color="r", width=0.25)
        etiquetas.append(''.join(
            letra for letra in poblaciones_comunidades_sorted[indice] if not letra.isdigit()))

    plt.xticks(range(len(etiquetas)), etiquetas, rotation=60)
    plt.savefig('./imagenes/R3.jpg')


def manipular_archivo_html():
    # Insertamos la imagen en el archivo HTML
    cadena_html = ''
    with open('./resultados/poblacionComAutonomas.html', 'r') as archivo:
        contenido_html = archivo.read()

        # Eliminamos la imagen anterior si existe
        cadena_html = contenido_html.replace('</body></html>', '')
        if '<img src="../imagenes/R3.jpg" style="display: block; margin: 0 auto;">' not in contenido_html:
            # Insertamos la nueva imagen
            cadena_html += '<img src="../imagenes/R3.jpg" style="display: block; margin: 0 auto;">'
        cadena_html += '</body></html>'

    with open('./resultados/poblacionComAutonomas.html', 'w') as archivo:
        archivo.write(cadena_html)


def ejecutar():
    poblaciones_comunidades = cargar_y_procesar_datos()
    generar_grafico_poblacion(poblaciones_comunidades)
    manipular_archivo_html()


if __name__ == "__main__":
    ejecutar()
