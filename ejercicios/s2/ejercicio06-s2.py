#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:25:19 2023

@author: migue8gl
"""

'''
Calculador mínimo y máximo de tres números
'''

print('----- Calculador mínimo y máximo de tres números -----')

x1 = float(input('Introduzca número x1: '))
x2 = float(input('Introduzca número x2: '))
x3 = float(input('Introduzca número x3: '))

max, min = x1, x1

# Comparar con x2
if x2 > max:
    max = x2
elif x2 < min:
    min = x2

# Comparar con x3
if x3 > max:
    max = x3
elif x3 < min:
    min = x3

print('Maximo {} y mínimo {}'.format(max, min))

print('----- Calculador mínimo y máximo de tres números -----')
