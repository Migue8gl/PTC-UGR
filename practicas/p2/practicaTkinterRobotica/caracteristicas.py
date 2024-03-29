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

    # Calculamos distancia euclidia
    sum = 0
    for a1, a2 in zip(point1, point2):
        sum += (a1 - a2) ** 2
    distance = math.sqrt(sum)
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

    for i in range(0, n - 1):
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

    for i in range(1, n - 2):
        distance = point_to_line_distance(points[i], points[0], points[-1])
        if distance < 0:
            print(distance)
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
    x, y = point
    x0, y0 = line_start
    xn, yn = line_end

    a = yn - y0
    b = x0 - xn
    c = y0 * xn - yn * x0

    return abs(a * x + b * y + c) / math.sqrt(a ** 2 + b ** 2)


def generate_dataset(output_file, files):
    with open(output_file, 'w') as output:
        for file in reversed(files):
            with open(file, 'r') as f:
                for line in f:
                    line_dict = json.loads(line)
                    output.write('{},{},{},{}\n'.format(
                        line_dict['perimetro'], line_dict['profundidad'],
                        line_dict['anchura'], line_dict['esPierna']))


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
    generate_dataset(data_names[-1], data_names)
