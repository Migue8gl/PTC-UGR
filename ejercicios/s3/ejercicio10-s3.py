#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:43:25 2023

@author: migue8gl
"""

"""
Escribe una función es_inversa(palabra1, palabra2) que determine si una 
palabra es la misma que la otra pero con los caracteres en orden inverso. 
Por ejemplo 'absd' y 'dsba'.
"""


def es_inversa(palabra1, palabra2):
    # Verifica si las dos palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    # Recorremos las palabras en orden normal la primera y en inverso la segunda
    for i, j in zip(range(len(palabra1)), range(len(palabra2) - 1, -1, -1)):
        if palabra1[i] != palabra2[j]:
            return False
    return True


def es_inversa_v2(palabra1, palabra2):
    # Verifica si las dos palabras son inversas
    return palabra1 == palabra2[::-1]


palabra1 = input('Introduce una cadena: ')
palabra2 = input('Introduce una cadena (inversa): ')

print('\nUsando func restrictiva -> {}'.format(es_inversa(palabra1, palabra2)))
print('\nUsando func NO restrictiva -> {}'.format(es_inversa_v2(palabra1, palabra2)))
