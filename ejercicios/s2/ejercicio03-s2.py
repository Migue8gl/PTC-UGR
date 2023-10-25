#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:11:27 2023

@author: migue8gl
"""

'''
Transformador tiempo.
    Debemos introducir un número arbitrário de horas, minutos y segundos, 
    después transformarlos dentro de un rango [0,59]
'''

print('----- Transformador tiempo -----')

h = int(input('Introduzca cantidad de horas: '))
m = int(input('Introduzca cantidad de minutos: '))
s = int(input('Introduzca cantidad de segundos: '))

if h >= 0 and m >= 0 and s >= 0:
    # Segundos que se puedan agrupar en minutos
    m += s//60
    # Segundos restantes
    s %= 60

    # Minutos que se puedan agrupar en horas
    h += m//60
    # Minutos restantes
    m %= 60

    print('{} horas, {} minutos y {} segundos'.format(h, m, s))
else:
    print('Debe introducir números positivos')

print('----- Transformador tiempo -----')
