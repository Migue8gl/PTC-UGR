#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:44:05 2023

@author: migue8gl
"""

"""
Escribe una función buscar(palabra, sub) que devuelva la posición en la que se 
puede encontrar sub dentro de palabra o -1 en caso de que no esté.
"""


def buscar(palabra, sub):
    contador = 0
    pos = -1

    # Buscamos en toda la palabra
    for indice in range(0, len(palabra)):

        # Vamos incrementando contador si las letras coinciden con la subcadena
        if palabra[indice] == sub[contador]:
            contador += 1

            # Donde empieza la posible subcadena
            if contador == 1:
                pos = indice

            # El contador no se ha reiniciado, es la subcadena
            if contador == len(sub):
                return pos
        else:
            # No es la subcadena, reiniciamos búsqueda
            pos = -1
            contador = 0
    return pos


def buscar_v2(palabra, sub):
    return palabra.find(sub)


palabra = input('Introduce una cadena: ')
sub = input('Introduce una subcadena a buscar: ')

print('\nUsando func restrictiva -> {}'.format(buscar(palabra, sub)))
print('\nUsando func NO restrictiva -> {}'.format(buscar_v2(palabra, sub)))
