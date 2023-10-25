#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:46:14 2023

@author: migue8gl
"""

'''
Prueba con strings. 
    Debemos imprimir el nombre y apellidos en una sola línea, luego al revés
    y luego cada uno por separado
'''


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


print('----- Prueba con strings -----')

n = input('Introduzca su nombre: ')
a1 = input('Introduzca su primer apellido: ')
a2 = input('Introduzca su segundo apellido: ')

print('Nombre completo: {} {} {}'.format(n, a1, a2))
print('Nombre inverso: {} {} {}'.format(
    reverse_string(n), reverse_string(a1), reverse_string(a2)))
print('Nombre: {}'.format(n))
print('Apellido 1: {}'.format(a1))
print('Apellido 2: {}'.format(a2))

print('----- Prueba con strings -----')
