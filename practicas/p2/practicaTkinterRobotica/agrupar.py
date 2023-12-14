#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:16:08 2023

@author: migue8gl
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt


def get_data(file):
    """
    Lee un archivo JSON y devuelve los datos como una lista de puntos.

    Parámetros:
    - file: Nombre del archivo JSON.

    Retorna:
    - Lista de puntos [PuntosX, PuntosY].
    """
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return [[point['PuntosX'], point['PuntosY']] for point in data[1:]]


def read_files(files):
    """
    Lee varios archivos JSON y combina los datos en una lista.

    Parámetros:
    - files: Lista de nombres de archivos JSON.

    Retorna:
    - Lista combinada de puntos [PuntosX, PuntosY].
    """
    data = []
    for file in files:
        data += get_data(file)
    return data


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


def create_clusters(data_points, min_points, max_points, distance_threshold):
    """file_name
    Agrupa los puntos en clusters basándose en la distancia y el número de puntos.

    Parámetros:
    - data_points: Lista de puntos [PuntosX, PuntosY].
    - min_points: Número mínimo de puntos por cluster.
    - max_points: Número máximo de puntos por cluster.
    - distance_threshold: Umbral de distancia para agrupar puntos en un cluster.

    Retorna:
    - Lista de clusters, donde cada cluster es una lista de puntos [PuntosX, PuntosY].
    """
    clusters = []
    cluster = []
    for points in data_points:
        for i in range(0, len(points[0])):
            point = [points[0][i], points[1][i]]
            if not cluster:
                # Si no hay puntos en el nuevo cluster añadimos el primero
                cluster.append(point)
            # Si el número de puntos por cluster es inferior al máximo y la distancia
            # es menor al umbral permitido
            elif len(cluster) < max_points and euclidean_distance(cluster[-1], point) < distance_threshold:
                cluster.append(point)
            elif len(cluster) < min_points:
                cluster.append(point)
            else:
                clusters.append(cluster)
                cluster = []
    return clusters

def visualize_clusters(clusters, plot_name='clusters'):
    plt.figure()
    for cluster in clusters:
       cluster_x, cluster_y = zip(*cluster)
       plt.scatter(cluster_x, cluster_y)
       
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Cluster Visualization')
    plt.savefig(plot_name)


def clusters_to_json(clusters, file_name):
    """
    Guarda los clusters en un archivo JSON.

    Parámetros:
    - clusters: Lista de clusters.
    - file_name: Nombre del archivo JSON de salida.

    Retorna:
    - No retorna nada, pero guarda los clusters en un archivo JSON.
    """
    # Abro el archivo
    with open(file_name, 'w') as f:
        # Cada cluster es una línea del json
        for i, cluster in enumerate(clusters):
            # Número de puntos del cluster
            points_number = len(cluster)

            points = np.array(cluster)
            points_x = list(points[:, 0])
            points_y = list(points[:, 1])

            # Formato del cluster
            clusters_json = {'numero_cluster': i, 'numero_puntos': points_number,
                             'puntosX': points_x, 'puntosY': points_y}
            f.write(json.dumps(clusters_json)+'\n')


def group(files, json_names, min_points, max_points, distance_threshold):
    """
    Agrupa los puntos de archivos positivos y negativos en clusters y guarda los resultados en archivos JSON separados.

    Parámetros:
    - files: Lista de nombres de archivos.
    - json_names: Lista de nombres para los json finales.
    - min_points: Número mínimo de puntos por cluster.
    - max_points: Número máximo de puntos por cluster.
    - distance_threshold: Umbral de distancia para agrupar puntos en un cluster.

    Retorna:
    - No retorna nada, pero guarda los clusters en archivos JSON.
    """
    positive_files = [item for item in files if 'positivo' in item]
    negative_files = [item for item in files if 'negativo' in item]

    # Leemos los datos de todos los archivos positivos
    positive_data = read_files(positive_files)

    # Creamos los clusters positivos
    positive_clusters = create_clusters(
        positive_data, min_points, max_points, distance_threshold)
    
    # Guardamos un plot de visualización
    visualize_clusters(positive_clusters, 'Clusters positivos')

    # Pasamos los clusters a json
    clusters_to_json(positive_clusters, json_names[0])

    # Leemos los datos de todos los archivos negativos
    negative_data = read_files(negative_files)

    # Creamos los clusters positivos
    negative_clusters = create_clusters(
        negative_data, min_points, max_points, distance_threshold)
    
    # Guardamos un plot de visualización
    visualize_clusters(negative_clusters, 'Clusters negativos')

    # Pasamos los clusters a json
    clusters_to_json(negative_clusters, json_names[1])
