#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:55:05 2023

@author: migue8gl
"""

'''
Calculador tercios según alcohol.
    Debemos calcular el número máximo de tercios que podemos beber, dada
    la restricción de que no queremos ingerir más de 50cc de alcohol
'''

print('----- Calculador tercios según alcohol -----')

x = float(input('Introduzca porcentaje de alcohol de la cerveza (sobre 100%): '))
tercio = 333  # 333cc
max_alcohol = 50  # 50cc

alcohol_tercio = (333 * x) / 100  # alcohol por cada tercio

if alcohol_tercio >= max_alcohol:
    print('No puedes beber ningún tercio')
else:
    num_tercios = int(max_alcohol/alcohol_tercio)
    print('Puedes beber {} tercios'.format(num_tercios))

print('----- Calculador tercios según alcohol -----')
