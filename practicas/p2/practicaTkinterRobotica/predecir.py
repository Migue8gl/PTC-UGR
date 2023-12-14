#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:07:13 2023

@author: migue8gl
"""

import time
import vrep
from agrupar import create_clusters
from caracteristicas import depth, width, perimeter


def read_laser_data(clientID):
    # Acceder a los datos del laser
    _, datosLaserComp = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_streaming)

    # Tiempo para leer los datos
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
        puntos_x.append(float(datos_laser[indice+1]))
        puntos_y.append(float(datos_laser[indice+2]))
        puntos_z.append(float(datos_laser[indice]))

    # Retornamos los valores leídos
    return {"PuntosX": puntos_x, "PuntosY": puntos_y}


def predict(clientID, parameters):
    data = read_laser_data(clientID)
    clusters = create_clusters(data, parameters.get_min_points(
    ), parameters.get_max_points(), parameters.get_distance_threshold())

    print(clusters)
