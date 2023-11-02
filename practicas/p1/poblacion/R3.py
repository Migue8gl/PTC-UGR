#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado el Sáb Oct 28 19:23:05 2023
Por: migue8gl
"""

import funciones
import matplotlib.pyplot as plt


def generar_grafico_poblacion(poblaciones_comunidades):
    # Ordenamos las comunidades autónomas de mayor a menor población total
    poblaciones_comunidades_sorted = funciones.obtener_lista_ccaa_ordenada(
        poblaciones_comunidades)

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


def ejecutar():
    poblaciones_comunidades = funciones.cargar_y_procesar_datos()
    generar_grafico_poblacion(poblaciones_comunidades)
    ruta_html = './resultados/poblacionComAutonomas.html'
    ruta_imagen = '../imagenes/R3.jpg'
    funciones.insertar_imagen_en_html(ruta_html, ruta_imagen)


if __name__ == "__main__":
    ejecutar()
