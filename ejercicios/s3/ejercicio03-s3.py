#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:16:51 2023

@author: migue8gl
"""

"""
Escribe una función mayusculas_minusculas(palabra) que devuelva una cadena en 
la que las mayúsculas y las minúsculas estén al contrario.
"""


def mayusculas_minusculas(palabra):
    resultado = ''
    for letra in palabra:
        if 'A' <= letra <= 'Z':
            # Convertimos mayúsculas a minúsculas
            resultado += chr(ord(letra) + 32)
        else:
            # Convertimos minúsculas a mayúsculas
            resultado += chr(ord(letra) - 32)
    return resultado


def mayusculas_minusculas_v2(palabra):
    return palabra.swapcase()


palabra = input('Introduce una cadena con mayúsculas y minúsculas: ')

print('\nUsando func restrictiva -> {}'.format(mayusculas_minusculas(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(mayusculas_minusculas(palabra)))
