#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:04:28 2023

@author: migue8gl
"""

"""
Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de
palabra que no contiene el carácter letra ninguna vez.
"""


def eliminar_letras(palabra, letra):
    index = 0
    while index != len(palabra):
        # Si es la letra a eliminar, nos saltamos ese índice
        if letra == palabra[index]:
            palabra = palabra[0:index] + palabra[index+1:]
        else:
            index += 1
    return palabra


def eliminar_letras_v2(palabra, letra):
    return palabra.replace(letra, '')


palabra = input('Introduce una cadena: ')
letra = input('Introduce una letra a eliminar: ')

print('\nUsando func restrictiva -> {}'.format(eliminar_letras(palabra, letra)))
print('\nUsando func NO restrictiva -> {}'.format(eliminar_letras_v2(palabra, letra)))
