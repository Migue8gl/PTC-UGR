#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:58:24 2023

@author: migue8gl
"""

"""
Escribe una función vocales(palabra) que devuelva las vocales que aparecen 
en la palabra.
"""


def vocales(palabra):
    # Define un string que contiene todas las vocales en minúsculas y mayúsculas
    vocales = 'aeiouAEIOU'
    # Inicializa una lista vacía para almacenar las vocales únicas
    vocales_captadas = []
    for letra in palabra:
        # Comprueba si la letra es una vocal y no se ha capturado previamente
        if letra in vocales and letra not in vocales_captadas:
            vocales_captadas.append(letra)
    # Devuelve la lista de vocales únicas
    return vocales_captadas


def vocales_v2(palabra):
    # Convierte la palabra en un conjunto para eliminar duplicados, encuentra 
    # la intersección con el conjunto de todas las vocales y luego convierte 
    # el resultado en una lista antes de devolverlo
    return list(set('aeiouAEIOU').intersection(set(palabra)))


palabra = input('Introduce una cadena: ')

print('\nUsando func restrictiva -> {}'.format(vocales(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(vocales_v2(palabra)))
