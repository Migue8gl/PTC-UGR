#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Sáb Oct 28 19:23:05 2023
Por: migue8gl
"""

import funciones
import matplotlib.pyplot as plt
import numpy as np


def generar_grafico_poblacion(poblaciones_comunidades):
    # Ordenamos las comunidades autónomas de mayor a menor población total
    poblaciones_comunidades_sorted = funciones.obtener_lista_ccaa_ordenada(
        poblaciones_comunidades)[:10]  # Select the top 10

    hombres = np.array([poblaciones_comunidades[comunidad_autonoma]['H2017'] for comunidad_autonoma in poblaciones_comunidades_sorted])
    mujeres = np.array([poblaciones_comunidades[comunidad_autonoma]['M2017'] for comunidad_autonoma in poblaciones_comunidades_sorted])

    ind = np.arange(len(poblaciones_comunidades_sorted))  # Índices para las barras

    plt.figure("barras", figsize=(15, 14))
    plt.title('Población por sexo en el año 2017 (CCAA)')

    plt.bar(ind - 0.1, hombres, color="b", width=0.25, label='Hombres')
    plt.bar(ind - 0.1 + 0.25, mujeres, color="r", width=0.25, label='Mujeres')

    etiquetas = [''.join(letra for letra in comunidad_autonoma if not letra.isdigit()) for comunidad_autonoma in poblaciones_comunidades_sorted]

    plt.xticks(ind, etiquetas, rotation=60)
    plt.legend()
    plt.savefig('./imagenes/R3.jpg')


def ejecutar():
    poblaciones_comunidades = funciones.cargar_y_procesar_datos()
    generar_grafico_poblacion(poblaciones_comunidades)
    ruta_html = './resultados/poblacionComAutonomas.html'
    ruta_imagen = '../imagenes/R3.jpg'
    funciones.insertar_imagen_en_html(ruta_html, ruta_imagen)


if __name__ == "__main__":
    ejecutar()
