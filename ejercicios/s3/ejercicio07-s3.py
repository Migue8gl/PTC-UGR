#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:17:48 2023

@author: migue8gl
"""

"""
Escribe una función mayusculas(palabra) que devuelva la palabra pasada a 
mayúsculas.
"""


def mayusculas(palabra):
    # Inicializa una cadena vacía para almacenar la palabra en mayúsculas
    palabra_mayus = ''
    for letra in palabra:
        # Comprueba si la letra está en minúsculas y la convierte a mayúsculas
        if 'a' <= letra <= 'z':
            palabra_mayus += chr(ord(letra) - 32)
        else:
            palabra_mayus += letra
    return palabra_mayus


def mayusculas_v2(palabra):
    # Utiliza el método upper() para convertir la palabra completa a mayúsculas
    return palabra.upper()


palabra = input('Introduce una cadena: ')

print('\nUsando func restrictiva -> {}'.format(mayusculas(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(mayusculas_v2(palabra)))
