#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:13:47 2023

@author: migue8gl
"""

'''
Calculador diferencia de tiempo
'''


from math import sqrt
print('----- Calculador diferencia de tiempo -----')

print('-- Instante 1 --')
h1 = int(input('Introduzca cantidad de horas: '))
m1 = int(input('Introduzca cantidad de minutos: '))
s1 = int(input('Introduzca cantidad de segundos: '))

print('-- Instante 2 --')
h2 = int(input('Introduzca cantidad de horas: '))
m2 = int(input('Introduzca cantidad de minutos: '))
s2 = int(input('Introduzca cantidad de segundos: '))


diff_hours = int(sqrt((h1 - h2)**2))
diff_min = int(sqrt((m1 - m2)**2))
diff_sec = int(sqrt((s1 - s2)**2))

print('\nDiferencia de tiempo entre instante1 e instante2: {}:{}:{}'.format(
    diff_hours, diff_min, diff_sec))

print('----- Calculador diferencia de tiempo-----')
