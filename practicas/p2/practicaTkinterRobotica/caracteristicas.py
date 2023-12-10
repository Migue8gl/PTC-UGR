#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:57:45 2023

@author: migue8gl
"""

import math
import json


def euclidean_distance(point1, point2):
    """
    Calcula la distancia euclidiana entre dos puntos.

    Parámetros:
    - point1: Primer punto en formato [x, y].
    - point2: Segundo punto en formato [x, y].

    Retorna:
    - Distancia euclidiana entre los dos puntos.
    """
    # Los puntos deben tener misma dimensionalidad
    if len(point1) != len(point2):
        raise ValueError("Los puntos deben ser de igual dimensionalidad")

    # Calculate the Euclidean distance
    distance = math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
    return distance


def perimeter(points):
    """
    Calcula el perímetro como la suma de las distancias entre puntos consecutivos.

    Parámetros:
    - points: Lista de puntos que representan el polígono.

    Retorna:
    - Perímetro del polígono.
    """
    perimeter = 0
    n = len(points)

    for i in range(n - 1):
        perimeter += euclidean_distance(points[i], points[i + 1])

    return perimeter


def depth(points):
    """
    Calcula la profundidad como la distancia máxima desde un punto a la línea que une los extremos del polígono.

    Parámetros:
    - points: Lista de puntos que representan el polígono.

    Retorna:
    - Profundidad del polígono.
    """
    max_distance = 0
    n = len(points)

    for i in range(1, n - 1):
        distance = point_to_line_distance(points[i], points[0], points[n - 1])
        max_distance = max(max_distance, distance)

    return max_distance


def width(points):
    """
    Calcula la anchura como la distancia entre el primer y último punto.

    Parámetros:
    - points: Lista de puntos que representan el polígono.

    Retorna:
    - Anchura del polígono.
    """
    return euclidean_distance(points[0], points[-1])


def point_to_line_distance(point, line_start, line_end):
    """
    Calcula la distancia entre un punto y una línea definida por dos puntos.

    Parámetros:
    - point: Punto en formato (x, y).
    - line_start: Primer punto de la línea en formato (x, y).
    - line_end: Segundo punto de la línea en formato (x, y).

    Retorna:
    - Distancia entre el punto y la línea.
    """
    x, y = point
    x1, y1 = line_start
    x2, y2 = line_end

    numerator = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    return numerator / denominator


def extract_features(files, data_names):
    """
    Extrae características de archivos de entrada y guarda los resultados en archivos de salida.

    Parámetros:
    - files: Lista de nombres de archivos de entrada.
    - data_names: Lista de nombres de archivos de salida correspondientes.

    La función recorre los archivos de entrada, calcula características para cada cluster y guarda los resultados
    en archivos de salida. Cada línea en los archivos de salida contiene un diccionario JSON con las siguientes propiedades:

    - 'numero_cluster': Número de cluster.
    - 'perimetro': Perímetro del polígono representado por el cluster.
    - 'profundidad': Profundidad del polígono representado por el cluster.
    - 'anchura': Anchura del polígono representado por el cluster.
    - 'esPierna': Valor binario (1 o 0) que indica si el cluster es una pierna (1) o no (0).

    Nota: La función utiliza las funciones auxiliares euclidean_distance, perimeter, depth, width y point_to_line_distance.
    """
    # Recorro los archivos para extraer las características de cada cluster
    for i, file in enumerate(files):
        # Abro el archivo de salida
        output_file = data_names[i]
        with open(output_file, 'w') as output:
            # Abro el archivo de lectura
            with open(file, 'r') as f:
                for line in f:
                    line_dict = json.loads(line)
                    # Asociar cada coordenada x, y para crear lista de puntos
                    points = list(
                        zip(line_dict['puntosX'], line_dict['puntosY']))
                    features_json = {'numero_cluster': line_dict['numero_cluster'],
                                     'perimetro': perimeter(points),
                                     'profundidad': depth(points),
                                     'anchura': width(points),
                                     'esPierna': 1 if i == 0 else 0}
                    output.write(json.dumps(features_json)+'\n')
