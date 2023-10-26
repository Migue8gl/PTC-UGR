#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:24:33 2023

@author: migue8gl
"""

"""
Escribe una función inicio_fin_vocal(palabra) que determine si una palabra 
empieza y acaba con una vocal.
"""


def inicio_fin_vocal(palabra):
    # Definimos vocales en una cadena
    vocales = 'aeiouAEIOU'
    # Si la palabra empieza y termina con alguna vocal
    return palabra[0] in vocales and palabra[-1] in vocales


def inicio_fin_vocal_v2(palabra):
    # Convierte la palabra a minúsculas para que no importe si las vocales
    # están en mayúsculas o minúsculas
    palabra = palabra.lower()
    # Verifica si la palabra comienza y termina con alguna vocal
    vocales = ('a', 'e', 'i', 'o', 'u')
    return palabra.startswith(vocales) and palabra.endswith(vocales)


palabra = input('Introduce una cadena: ')

print('\nUsando func restrictiva -> {}'.format(inicio_fin_vocal(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(inicio_fin_vocal_v2(palabra)))