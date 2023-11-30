#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:31:32 2023

@author: migue8gl
"""

import tkinter as tk
import vrep

# -------------- GLOBAL VALUES ------------- #
title = 'Práctica PTC Tkinter Robótica'
clientID = -1


def start_vrep():
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    print(clientID)

    if clientID == -1:
        tk.messagebox.showerror(title, message='Debe iniciar el simulador')
    else:
        tk.messagebox.showinfo(
            title=title, message='Conexión con VREP establecida')
        status_text.set('Estado: Conectado a VREP')
        exit_vrep_button.config(state=tk.NORMAL)


def exit_vrep():
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
    vrep.simxFinish(clientID)
    status_text.set('Estado: No conectado a VREP')
    exit_vrep_button.config(state=tk.DISABLED)


# ------------- WINDOW SIZE ------------- #
root = tk.Tk()
root.title(title)
root.geometry('700x300')

# ------------- FIRST COLUMN ------------ #

label = tk.Label(root, text='Es necesario ejecutar el simulador VREP')
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

# ------------ SECOND COLUMN ------------ #
# ------------- THIRD COLUMN ------------ #

root.mainloop()
