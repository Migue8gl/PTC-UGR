#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:42:53 2023

@author: migue8gl
"""

"""
Crea una lista con los valores enteros de 1 a N e implementa una función que 
reciba dicha lista y nos devuelva una lista con los valores impares y el 
número de dichos valores. Solicitar N por teclado y mostrar el resultado por 
pantalla.
"""


# Inicializo lista con enteros hasta N incluida y la devuelvo
def inicializar_lista(n):
    lista = []
    for i in range(0, n+1):
        lista.append(i)
    return lista


# Itero buscando impares (resto entre 2 debe ser 0), incremento contador de
# impares y los guardo en lista
def impares(lista):
    contador = 0
    lista_impares = []
    for item in lista:
        if item % 2 == 0:
            contador += 1
            lista_impares.append(item)
    return lista_impares, contador


# Uso comprensión de listas
def impares_v2(lista):
    lista_impares = [item for item in lista if item % 2 == 0]
    return lista_impares, len(lista_impares)


n = int(input('Introduce un número N para crear lista: '))
lista = inicializar_lista(n)

print('Función restricción -> {}'.format(impares(lista)))
print('Función NO restricción -> {}'.format(impares_v2(lista)))
