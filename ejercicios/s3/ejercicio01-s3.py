#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:53:03 2023

@author: migue8gl
"""

"""
Escribe una función contar_letras(palabra, letra) que devuelva el número de 
veces que aparece una letra en una palabra.
"""


def contar_letras(palabra, letra):
    contador = 0
    for l in palabra:
        if l == letra:
            contador += 1
    return contador


def contar_letras_v2(palabra, letra):
    return palabra.count(letra)


palabra = input('Introduce una cadena: ')
letra = input('Introduce una letra a buscar: ')

print('\nUsando func restrictiva, la cadena \'{}\' contiene {} veces la letra \'{}\''.format(
    palabra, contar_letras(palabra, letra), letra))
print('Usando func NO restrictiva, la cadena \'{}\' contiene {} veces la letra \'{}\''.format(
    palabra, contar_letras_v2(palabra, letra), letra))
