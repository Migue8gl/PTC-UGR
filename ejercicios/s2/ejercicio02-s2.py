#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:01:33 2023

@author: migue8gl
"""

'''
Calculador desviación típica
'''

from math import sqrt
print('----- Calculador desviación típica -----')

x1 = float(input('Introduzca número x1: '))
x2 = float(input('Introduzca número x2: '))
x3 = float(input('Introduzca número x3: '))

mean = (x1 + x2 + x3) / 3
standard_deviation = sqrt(
    ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3)

print('La desviación típica es: {:.2f}'.format(standard_deviation))

print('----- Calculador desviación típica -----')
