#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:31:32 2023

@author: migue8gl
"""

import tkinter as tk
import vrep
from parameters import Parameters
import capturar
import agrupar
import caracteristicas
import clasificarSVM
import os

# -------------- GLOBAL VALUES ------------- #

title = 'Práctica PTC Tkinter Robótica'
clientID = -1
parameters = Parameters()
items = (
    "positivo1/enPieCerca.json",
    "positivo2/enPieMedia.json",
    "positivo3/enPieLejos.json",
    "positivo4/sentadoCerca.json",
    "positivo5/sentadoMedia.json",
    "positivo6/sentadoLejos.json",
    "negativo1/cilindroMenorCerca.json",
    "negativo2/cilindroMenorMedia.json",
    "negativo3/cilindroMenorLejos.json",
    "negativo4/cilindroMayorCerca.json",
    "negativo5/cilindroMayorMedia.json",
    "negativo6/cilindroMayorLejos.json",
)
selected_files_boolean = [False for _ in range(0, len(items))]

# -------------- FUNCTIONALITY ------------- #


def start_vrep():
    global clientID

    if clientID != -1:
        tk.messagebox.showinfo(
            title=title, message='Ya está conectado a VREP.')
    else:
        vrep.simxFinish(-1)
        clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

        if clientID == -1:
            tk.messagebox.showerror(
                title, message='Debe iniciar el simulador.')
        else:
            tk.messagebox.showinfo(
                title=title, message='Conexión con VREP establecida.')
            status_text.set('Estado: Conectado a VREP.')
            exit_vrep_button.config(state=tk.NORMAL)
            capture_button.config(state=tk.NORMAL)


def exit_vrep():
    global clientID
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
    vrep.simxFinish(clientID)
    clientID = -1
    status_text.set('Estado: No conectado a VREP')
    exit_vrep_button.config(state=tk.DISABLED)
    capture_button.config(state=tk.DISABLED)
    group_button.config(state=tk.DISABLED)
    extract_features_button.config(state=tk.DISABLED)
    train_classifier_button.config(state=tk.DISABLED)
    predict_button.config(state=tk.DISABLED)


def capture():
    global selected_files_boolean
    selected_files = file_list.curselection()

    # Si un archivo ha sido seleccionado
    if selected_files:
        selected_file = file_list.get(selected_files[0])

        # Comprobamos si existe el archivo
        file_exists = os.path.isfile(selected_file)

        # Si existe el archivo
        if file_exists:
            user_response = tk.messagebox.askyesno(
                message="El fichero: '{}' ya existe. Se creará de nuevo. ¿Está seguro?".format(
                    selected_file),
                title=title
            )

        # Si el archivo no existe
        else:
            user_response = tk.messagebox.askyesno(
                message="Se va a crear el fichero: '{}' ¿Está seguro?".format(
                    selected_file),
                title=title
            )

        if user_response:
            with open(selected_file, "w"):
                pass  # Creo un archivo vacío

            # Obtenemos los límites por los que debe moverse el personaje/objeto
            capture_parameters = {
                'clientID': clientID,
                'iterations': parameters.get_iterations(),
                'file': selected_file,
                'lower_bound': parameters.get_near(),
                'upper_bound': parameters.get_medium(),
                'entity': 'Bill#0'}

            if 'Cerca' in selected_file:
                capture_parameters['lower_bound'] = parameters.get_near()
                capture_parameters['upper_bound'] = parameters.get_medium()
            elif 'Media' in selected_file:
                capture_parameters['lower_bound'] = parameters.get_medium()
                capture_parameters['upper_bound'] = parameters.get_far()
            else:
                capture_parameters['lower_bound'] = parameters.get_far()
                capture_parameters['upper_bound'] = parameters.get_far()+1

            if 'enPie' in selected_file:
                capture_parameters['entity'] = 'Bill#0'
            elif 'sentado' in selected_file:
                capture_parameters['entity'] = 'Bill'
            elif 'cilindroMenor' in selected_file:
                capture_parameters['entity'] = 'Cylinder2'
            else:
                capture_parameters['entity'] = 'Cylinder0'

            capturar.capture(**capture_parameters)
            tk.messagebox.showinfo(
                title, message='Captura de datos para: {} completada.'.format(selected_file))

            # Actualizamos el estado de ficheros seleccionados
            selected_files_boolean[items.index(selected_file)] = True

            # Si todos los ficheros han sido seleccionados, ya se puede habilitar el botṕn de agrupar
            if all(selected_files_boolean):
                group_button.config(state=tk.NORMAL)
    else:
        # Si no se ha seleccionado ningún archivo
        tk.messagebox.showwarning(
            title=title, message="Debe elegir algún fichero de la lista.")


def group():
    # Parámetros de función de agrupación
    group_parameters = {
        'files': items,
        'json_names': ('clustersPiernas.json', 'clustersNoPiernas.json'),
        'min_points': parameters.get_min_points(),
        'max_points': parameters.get_max_points(),
        'distance_threshold': parameters.get_distance_threshold()}

    # Llamamos a la funcionalidad principal
    agrupar.group(**group_parameters)
    msg = 'Agrupamiento en clusters completado. Se han creado los archivos: {}, {}'.format(group_parameters['json_names'][0],
                                                                                           group_parameters['json_names'][1])
    tk.messagebox.showinfo(title, message=msg)
    extract_features_button.config(state=tk.NORMAL)


def extract_features():
    # Parámetros de función de agrupación
    extract_features_parameters = {
        'files': ('clustersPiernas.json', 'clustersNoPiernas.json'),
        'data_names': ('caracteristicasPiernas.dat', 'caracteristicasNoPiernas.dat',
                       'piernasDataset.csv')}

    caracteristicas.extract_features(**extract_features_parameters)
    msg = 'Extracción de características completado. Se han creado los archivos: {}, {}, {}'.format(extract_features_parameters['data_names'][0],
                                                                                                    extract_features_parameters[
                                                                                                        'data_names'][1],

                                                                                                    extract_features_parameters['data_names'][2])
    tk.messagebox.showinfo(title, message=msg)
    train_classifier_button.config(state=tk.NORMAL)


def train_classifier():
    train_classifier_parameters = {'dataset': 'piernasDataset.csv'}
    clasificarSVM.train(**train_classifier_parameters)

    msg = 'Entrenamiento del clasificador completado.'
    tk.messagebox.showinfo(title, message=msg)
    predict_button.config(state=tk.NORMAL)


def predict():
    pass


def debug():
    current_state = capture_button.cget("state")

    new_state = tk.NORMAL if current_state == tk.DISABLED else tk.DISABLED

    exit_vrep_button.config(state=new_state)
    capture_button.config(state=new_state)
    group_button.config(state=new_state)
    extract_features_button.config(state=new_state)
    train_classifier_button.config(state=new_state)
    predict_button.config(state=new_state)


def exit_window():
    if clientID != -1:
        tk.messagebox.showerror(title, message='Antes de salir desconectar')
    else:
        answer = tk.messagebox.askyesno(
            title, message='¿Estás seguro de que desea salir?')
        if answer:
            root.destroy()


def change_parameters():
    global parameters

    # Convertir los parámetros de cadena a flotante
    iterations = float(iterations_parameter_str.get())
    near = float(near_parameter_str.get())
    medium = float(medium_parameter_str.get())
    far = float(far_parameter_str.get())
    min_points = float(min_points_parameter_str.get())
    max_points = float(max_points_parameter_str.get())
    distance_threshold = float(distance_threshold_parameter_str.get())

    # Crear un objeto Parameters con valores enteros
    parameters = Parameters(iterations, near, medium,
                            far, min_points, max_points, distance_threshold)
    message = f"Parámetros cambiados:\n{parameters}"
    tk.messagebox.showinfo("Cambios de Parámetros", message)


def validate_numeric_input(value, name):
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        tk.messagebox.showwarning(
            title, message='Se debe introducir un número.')
        return False


# ------------- WINDOW SIZE ------------- #

root = tk.Tk()
root.title(title)
root.geometry('700x300')

# ------------- FIRST COLUMN ------------ #

label = tk.Label(root, text='Es necesario ejecutar el simulador VREP.')
label.grid(row=0, column=0)

start_vrep_button = tk.Button(
    root, text='Conectar con VREP', command=start_vrep)
start_vrep_button.grid(row=1, column=0)

exit_vrep_button = tk.Button(
    root, text='Detener y desconectar VREP', state=tk.DISABLED, command=exit_vrep)
exit_vrep_button.grid(row=2, column=0)

status_text = tk.StringVar()
status_text.set('Estado: No conectado a VREP')
status_label = tk.Label(root, textvariable=status_text)
status_label.grid(row=3, column=0)

capture_button = tk.Button(
    root, text='Capturar', state=tk.DISABLED, command=capture)
capture_button.grid(row=4, column=0)

group_button = tk.Button(
    root, text='Agrupar', state=tk.DISABLED, command=group)
group_button.grid(row=5, column=0)

group_button = tk.Button(
    root, text='Agrupar', state=tk.DISABLED, command=group)
group_button.grid(row=5, column=0)

extract_features_button = tk.Button(
    root, text='Extraer características', state=tk.DISABLED, command=extract_features)
extract_features_button.grid(row=6, column=0)

train_classifier_button = tk.Button(
    root, text='Entrenar clasificador', state=tk.DISABLED, command=train_classifier)
train_classifier_button.grid(row=7, column=0)

predict_button = tk.Button(
    root, text='Predecir', state=tk.DISABLED, command=predict)
predict_button.grid(row=8, column=0)

exit_window_button = tk.Button(
    root, text='Salir', command=exit_window)
exit_window_button.grid(row=9, column=0)

debug_button = tk.Button(
    root, text='Debug', command=debug)
debug_button.grid(row=10, column=0)

# ------------ SECOND COLUMN ------------ #

parameter_label = tk.Label(root, text='Parámetros')
parameter_label.grid(row=1, column=1, sticky='e')

iterations_label = tk.Label(root, text="Iteraciones:")
iterations_label.grid(row=2, column=1, sticky='e')

near_label = tk.Label(root, text="Cerca:")
near_label.grid(row=3, column=1, sticky='e')

medium_label = tk.Label(root, text="Media:")
medium_label.grid(row=4, column=1, sticky='e')

far_label = tk.Label(root, text="Lejos:")
far_label.grid(row=5, column=1, sticky='e')

min_points_label = tk.Label(root, text="MinPuntos:")
min_points_label.grid(row=6, column=1, sticky='e')

max_points_label = tk.Label(root, text="MaxPuntos:")
max_points_label.grid(row=7, column=1, sticky='e')

distance_threshold_label = tk.Label(root, text="UmbralDistancia:")
distance_threshold_label.grid(row=8, column=1, sticky='e')

change_button = tk.Button(root, text='Cambiar', command=change_parameters)
change_button.grid(row=9, column=1)

# ------------- THIRD COLUMN ------------ #

# Validación de entrada
validate_numeric = (root.register(validate_numeric_input), '%P', '%W')

# Variables de texto
iterations_parameter_str = tk.StringVar()
iterations_parameter_str.set(str(parameters.get_iterations()))

near_parameter_str = tk.StringVar()
near_parameter_str.set(str(parameters.get_near()))

medium_parameter_str = tk.StringVar()
medium_parameter_str.set(str(parameters.get_medium()))

far_parameter_str = tk.StringVar()
far_parameter_str.set(str(parameters.get_far()))

min_points_parameter_str = tk.StringVar()
min_points_parameter_str.set(str(parameters.get_min_points()))

max_points_parameter_str = tk.StringVar()
max_points_parameter_str.set(str(parameters.get_max_points()))

distance_threshold_parameter_str = tk.StringVar()
distance_threshold_parameter_str.set(str(parameters.get_distance_threshold()))

# Elementos de entrada de texto
iterations_box = tk.Entry(root, width=5, textvariable=iterations_parameter_str,
                          validate='key', validatecommand=validate_numeric)
near_box = tk.Entry(root, width=5, textvariable=near_parameter_str,
                    validate='key', validatecommand=validate_numeric)
medium_box = tk.Entry(root, width=5, textvariable=medium_parameter_str,
                      validate='key', validatecommand=validate_numeric)
far_box = tk.Entry(root, width=5, textvariable=far_parameter_str,
                   validate='key', validatecommand=validate_numeric)
min_points_box = tk.Entry(root, width=5, textvariable=min_points_parameter_str,
                          validate='key', validatecommand=validate_numeric)
max_points_box = tk.Entry(root, width=5, textvariable=max_points_parameter_str,
                          validate='key', validatecommand=validate_numeric)
distance_threshold_box = tk.Entry(
    root, width=5, textvariable=distance_threshold_parameter_str,
    validate='key', validatecommand=validate_numeric)

# Posición de los elementos
iterations_box.grid(row=2, column=2)
near_box.grid(row=3, column=2)
medium_box.grid(row=4, column=2)
far_box.grid(row=5, column=2)
min_points_box.grid(row=6, column=2)
max_points_box.grid(row=7, column=2)
distance_threshold_box.grid(row=8, column=2)

# ------------- FOURTH COLUMN ------------ #

files = tk.Label(root, text="Fichero para la captura")
files.grid(row=1, column=3)

file_list = tk.Listbox(root, width=35, height=12)
file_list.insert(0, *items)
file_list.grid(row=3, column=3, rowspan=6)

root.mainloop()
