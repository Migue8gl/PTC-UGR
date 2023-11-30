#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:33:14 2023

@author: migue8gl
"""

"""
Crea una lista con los valores enteros de 1 a N e implementa una función que 
reciba dicha lista y nos devuelva la suma de dichos valores. Solicitar N por 
teclado y mostrar el resultado por pantalla.
"""


# Inicializo lista con enteros hasta N incluida y la devuelvo
def inicializar_lista(n):
    lista = []
    for i in range(0, n+1):
        lista.append(i)
    return lista


# Itero y sumo cada elemento a un contador
def suma(lista):
    suma = 0
    for item in lista:
        suma += item
    return suma


# Utilizo función sum()
def suma_v2(lista):
    return sum(lista)


n = int(input('Introduce un número N para crear lista: '))
lista = inicializar_lista(n)

print('Función restricción -> {}'.format(suma(lista)))
print('Función NO restricción -> {}'.format(suma_v2(lista)))
