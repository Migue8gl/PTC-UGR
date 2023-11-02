#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:29:17 2023

@author: migue8gl
"""

"""
Usando Matplotlib, para las 10 comunidades elegidas en el punto R3 generar un
gráfico de líneas que refleje la evolución de la población total de cada 
comunidad autónoma desde el año 2010 a 2017, salvar el gráfico a fichero e 
incorporarlo a la página web 3 del punto R4.
"""




import matplotlib.pyplot as plt
import funciones
def generar_grafico_poblacion(poblaciones_comunidades):
    # Ordenamos las comunidades autónomas de mayor a menor población total
    poblaciones_comunidades_sorted = funciones.obtener_lista_ccaa_ordenada(
        poblaciones_comunidades)

    plt.figure("lineal", figsize=(14, 15))
    plt.title('Población total en 2010-2017 (CCAA)', fontsize=20)
    comunidad_autonoma = poblaciones_comunidades_sorted[0:10]
    total_poblacion_ca = {}

    for ca in comunidad_autonoma:
        total_poblacion_ca[ca] = [poblaciones_comunidades[ca]
                                  [str(año)] for año in range(2010, 2018)]
        plt.plot(total_poblacion_ca[ca], marker='o',
                 label=ca,  linewidth=4, markersize=10)

    años = range(2010, 2018)
    plt.xticks(range(len(años)), años)
    plt.legend(comunidad_autonoma, loc='right',
               bbox_to_anchor=(1.39, 0.5), prop={'size': 17})

    plt.savefig('./imagenes/R5.jpg',  bbox_inches='tight')


def ejecutar():
    poblaciones_comunidades = funciones.cargar_y_procesar_datos()
    generar_grafico_poblacion(poblaciones_comunidades)
    ruta_html = './resultados/variacionComAutonomas.html'
    ruta_imagen = '../imagenes/R5.jpg'
    funciones.insertar_imagen_en_html(ruta_html, ruta_imagen)


if __name__ == "__main__":
    ejecutar()
