#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:30:46 2023

@author: migue8gl
"""

"""
Escribe una función elimina_vocales(palabra) que elimine todas las vocales que 
aparecen en la palabra.
"""


def elimina_vocales(palabra):
    # Definimos una cadena con las vocales y cadena vacía
    vocales = 'aeiouAEIOU'
    palabra_sin_vocales = ''

    # Recorremos la palabra
    for letra in palabra:
        if letra not in vocales:
            # Añadimos solo las consonantes
            palabra_sin_vocales += letra
    return palabra_sin_vocales


def elimina_vocales_v2(palabra):
    # Define una tabla de traducción que mapea las vocales a ''
    tabla_de_traduccion = str.maketrans(
        {'a': '', 'e': '', 'i': '', 'o': '', 'u': ''})
    # Utiliza el método translate() para eliminar las vocales
    palabra_sin_vocales = palabra.lower().translate(tabla_de_traduccion)
    return palabra_sin_vocales


palabra = input('Introduce una cadena: ')

print('\nUsando func restrictiva -> {}'.format(elimina_vocales(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(elimina_vocales_v2(palabra)))
