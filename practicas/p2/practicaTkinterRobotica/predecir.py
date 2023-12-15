#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:07:13 2023

@author: migue8gl
"""

import time
import vrep
import pickle
import pandas as pd
from agrupar import create_clusters
from caracteristicas import depth, width, perimeter
from clasificarSVM import scale_data
import matplotlib.pyplot as plt


def read_laser_data(clientID):
    # Acceder a los datos del laser
    _, datosLaserComp = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_streaming)

    # Tiempo para leer los datos (se llena el buffer)
    time.sleep(1)
    seconds = 0.5

    # Listas para recibir las coordenadas (x y z) de los puntos detectados por el laser
    puntos_x = []
    puntos_y = []
    puntos_z = []

    _, signal_value = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_buffer)
    time.sleep(seconds)

    datos_laser = vrep.simxUnpackFloats(signal_value)
    for indice in range(0, len(datos_laser), 3):
        puntos_x.append(datos_laser[indice+1])
        puntos_y.append(datos_laser[indice+2])
        puntos_z.append(datos_laser[indice])

    # Retornamos los valores leídos
    return [[puntos_x, puntos_y]]


def generate_features(clusters):
    features = []
    for cluster in clusters:
        features_cluster = [perimeter(cluster), depth(cluster), width(cluster)]
        features.append(features_cluster)
    return features


def predict_data(data):
    # Pasamos a DataFrame
    feature_names = ['perimeter', 'depth', 'width']
    df = pd.DataFrame(data, columns=feature_names)

    data = scale_data(df)

    # Cargamos el clasificador
    with open('clasificador.pkl', 'rb') as file:
        classifier = pickle.load(file)
        predictions = classifier.predict(data)
    return predictions


def visualize_clusters(clusters, predictions, plot_name='Predictions'):
    plt.figure()
    for i, cluster in enumerate(clusters):
        color = 'red' if predictions[i] == 1 else 'blue'
        cluster_x, cluster_y = zip(*cluster)
        plt.scatter(cluster_x, cluster_y, c=color, s=1.2)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.ylim(-2.4, 2.4)
    plt.xlim(1.0, 4.0)
    plt.title('Cluster Visualization')
    plt.savefig(plot_name)


def predict(clientID, parameters):
    # Leemos los datos del láser
    data = read_laser_data(clientID)

    # Creamos los clusters
    clusters = create_clusters(data, parameters.get_min_points(
    ), parameters.get_max_points(), parameters.get_distance_threshold())

    # Obtenemos características por cada cluster
    data = generate_features(clusters)

    # Hacemos las predicciones
    predictions = predict_data(data)

    # Ploteamos las predicciones
    visualize_clusters(clusters, predictions)
