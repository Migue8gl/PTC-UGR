#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:59:17 2023

@author: migue8gl
"""

"""
Crea una lista con los valores enteros de 1 a N e implementa una función que 
reciba dicha lista y nos devuelva el máximo y el mínimo de dichos valores, así 
como sus respectivas posiciones. Solicitar N por teclado y mostrar el resultado
por pantalla.
"""


# Inicializo lista con enteros hasta N incluida y la devuelvo
def inicializar_lista(n):
    lista = []
    for i in range(0, n+1):
        lista.append(i)
    return lista


# Iteramos por la lista
def max_min(lista):
    # Máximos, mínimos e índices por defecto
    maximo = -9999
    i_maximo = -1
    minimo = 9999
    i_minimo = -1

    # Iteramos y buscamos máximos, mínimos y correspondientes posiciones
    for i in range(0, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            i_maximo = i
        if lista[i] < minimo:
            minimo = lista[i]
            i_minimo = i
    return maximo, i_maximo, minimo, i_minimo


# Usamo funciones max(), min() e index()
def max_min_v2(lista):
    valor_maximo = max(lista)
    indice_maximo = lista.index(valor_maximo)
    valor_minimo = min(lista)
    indice_minimo = lista.index(valor_minimo)
    return valor_maximo, indice_maximo, valor_minimo, indice_minimo


n = int(input('Introduce un número N para crear lista: '))
lista = inicializar_lista(n)

print('Lista: {}'.format(lista))
print('Función restricción -> {}'.format(max_min(lista)))
print('Función NO restricción -> {}'.format(max_min_v2(lista)))
