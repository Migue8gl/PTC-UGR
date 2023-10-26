#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:53:13 2023

@author: migue8gl
"""

"""
Escribe una función num_vocales(palabra) que devuelva el número de vocales que 
aparece en la palabra.
"""


def num_vocales(palabra):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


def num_vocales_v2(palabra):
    vocales = 'aeiouAEIOU'
    return sum(map(palabra.count, vocales))


palabra = input('Introduce una cadena: ')

print('\nUsando func restrictiva -> {}'.format(num_vocales(palabra)))
print('\nUsando func NO restrictiva -> {}'.format(num_vocales_v2(palabra)))
