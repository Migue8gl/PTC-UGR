#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:30:32 2023

@author: migue8gl
"""

import vrep
import json
import cv2
import numpy as np


def capture(clientID, file, iterations):
    
    print(clientID)
    # Guardar la referencia de la camara
    _, camhandle = vrep.simxGetObjectHandle(
        clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)

    # Creamos el archivo JSON
    max_iter = iterations
    iteration = 1

    cabecera = {"MaxIteraciones": max_iter}
    data_laser = open(file, "w")
    data_laser.write(json.dumps(cabecera)+'\n')

    # Leemos datos
    while iteration <= max_iter:
        # Listas para recibir las coordenadas (x y z) de los puntos detectados por el laser
        puntos_x = []
        puntos_y = []
        puntos_z = []

        _, signal_value = vrep.simxGetStringSignal(
            clientID, 'LaserData', vrep.simx_opmode_buffer)

        datos_laser = vrep.simxUnpackFloats(signal_value)
        for indice in range(0, len(datos_laser), 3):
            puntos_x.append(datos_laser[indice+1])
            puntos_y.append(datos_laser[indice+2])
            puntos_z.append(datos_laser[indice])

        # Guardamos los puntosx, puntosy en el fichero JSON
        lectura = {"Iteracion": iteration,
                   "PuntosX": puntos_x, "PuntosY": puntos_y}
        data_laser.write(json.dumps(lectura)+'\n')

        if iteration == 0 or iteration == max_iter-1:
            # Guardar frame de la camara, rotarlo y convertirlo a BGR
            _, resolution, image = vrep.simxGetVisionSensorImage(
                clientID, camhandle, 0, vrep.simx_opmode_buffer)

            img = np.array(image, dtype=np.uint8)
            img.resize([resolution[0], resolution[1], 3])
            img = np.rot90(img, 2)
            img = np.fliplr(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            # Salvo a disco la imagen
            cv2.imwrite(file+str(iteration)+'.jpg', img)
        iteration += 1
