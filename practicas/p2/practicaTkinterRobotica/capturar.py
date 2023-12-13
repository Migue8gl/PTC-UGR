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
import time
import math
import random


def capture(clientID, file, iterations, lower_bound, upper_bound, entity):
    """
   Captura datos del sensor láser y la posición de un objeto/persona en un entorno V-REP.

   Parámetros:
   - clientID: Identificación del cliente V-REP.
   - file: Nombre del archivo donde se guardarán los datos capturados.
   - iterations: Número de iteraciones para capturar datos.
   - lower_bound: Límite inferior de distancia para cambiar la dirección de movimiento.
   - upper_bound: Límite superior de distancia para cambiar la dirección de movimiento.
   - entity: Nombre de la entidad (objeto/persona) en el entorno V-REP.

   Retorna:
   - No retorna nada, pero guarda los datos capturados en un archivo JSON y las imágenes en formato JPG.
   """
    # Guardar la referencia al robot
    _, robothandle = vrep.simxGetObjectHandle(
        clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)

    # Guardar la referencia de la camara
    _, camhandle = vrep.simxGetObjectHandle(
        clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)

    # Obtenermos la referencia a la entidad
    _, entityhandle = vrep.simxGetObjectHandle(
        clientID, entity, vrep.simx_opmode_oneshot_wait)

    # Acceder a los datos del laser
    _, datosLaserComp = vrep.simxGetStringSignal(
        clientID, 'LaserData', vrep.simx_opmode_streaming)

    # Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(
        clientID, camhandle, 0, vrep.simx_opmode_streaming)

    # Esperamos a que el buffer se llene
    time.sleep(1)

    # Creamos el archivo JSON
    max_iter = iterations
    seconds = 0.5
    iteration = 1
    change_direction = True

    cabecera = {'TiempoSleep': seconds, "MaxIteraciones": max_iter}
    data_laser = open(file, "w")
    data_laser.write(json.dumps(cabecera)+'\n')

    # Leemos datos
    while iteration <= max_iter:
        # Listas para recibir las coordenadas (x y z) de los puntos detectados por el laser
        puntos_x = []
        puntos_y = []
        puntos_z = []

        # Obtenemos la posición de la persona
        _, entity_position = vrep.simxGetObjectPosition(
            clientID, entityhandle, -1, vrep.simx_opmode_oneshot_wait)
        _, entity_orientation = vrep.simxGetObjectOrientation(
            clientID, entityhandle, -1, vrep.simx_opmode_oneshot_wait)

        # Obtenemos la posición del robot
        _, robot_position = vrep.simxGetObjectPosition(
            clientID, robothandle, -1, vrep.simx_opmode_oneshot_wait)

        # Variables de movimiento
        movement_step = 0.05
        random_step_x = random.uniform(0, 0.05)
        random_step_y = random.uniform(-0.2, 0.2)
        rotation_step = 0.5

        # Controlamos el movimiento
        if change_direction:
            new_x = entity_position[0] + movement_step + random_step_x
            new_y = entity_position[1] - movement_step - random_step_y
            new_distance_to_person = math.sqrt(new_x**2 + new_y**2)

            if lower_bound >= new_distance_to_person or new_distance_to_person >= upper_bound:
                change_direction = False
                new_x = lower_bound + random_step_x

        else:
            new_x = entity_position[0] + movement_step + random_step_x
            new_y = entity_position[1] + movement_step + random_step_y
            new_distance_to_person = math.sqrt(new_x**2 + new_y**2)

            if lower_bound >= new_distance_to_person or new_distance_to_person >= upper_bound:
                change_direction = True
                new_x = lower_bound + random_step_x

        # Cambiamos posición y rotamos al objeto/persona
        vrep.simxSetObjectPosition(
            clientID, entityhandle, -1, [new_x, new_y, entity_position[2]], vrep.simx_opmode_oneshot_wait)
        new_orientation = [entity_orientation[0],
                           entity_orientation[1], entity_orientation[2] + rotation_step]
        vrep.simxSetObjectOrientation(
            clientID, entityhandle, -1, new_orientation, vrep.simx_opmode_oneshot_wait)

        _, signal_value = vrep.simxGetStringSignal(
            clientID, 'LaserData', vrep.simx_opmode_buffer)
        time.sleep(seconds)

        datos_laser = vrep.simxUnpackFloats(signal_value)
        for indice in range(0, len(datos_laser), 3):
            puntos_x.append(datos_laser[indice+1])
            puntos_y.append(datos_laser[indice+2])
            puntos_z.append(datos_laser[indice])

        # Guardamos los puntosx, puntosy en el fichero JSON
        lectura = {"Iteracion": iteration,
                   "PuntosX": puntos_x, "PuntosY": puntos_y}
        data_laser.write(json.dumps(lectura)+'\n')

        if iteration == 1 or iteration == max_iter:
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
