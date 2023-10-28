#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:42:15 2023

@author: migue8gl
"""

"""
Usando el módulo “random” genera dos listas de N y M números enteros aleatorios 
entre 1 y 10 e implementa una función que devuelva una tercera lista que 
represente la intersección de las dos primeras. Los valores deben estar 
ordenados en orden ascendente. Solicitar N y M por teclado y mostrar el 
resultado por pantalla.
"""




import random as rd
def inicializa_lista_aleatoria(N):
    lista = []
    for i in range(N):
        # Generamos un número entero aleatorio entre 1 y 10 y lo añadimos a la lista
        lista.append(rd.randint(1, 10))
    return lista


def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                # Intercambiamos los elementos si están en el orden incorrecto
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def interseccion(lista1, lista2):
    lista3 = []
    for item in lista1:
        if item in lista2 and item not in lista3:
            # Añadimos el elemento a lista3 si está en lista1 y lista2 y no
            # está ya en lista3 para no repetir valores
            lista3.append(item)
    return ordenar(lista3)


def interseccion_v2(lista1, lista2):
    # Usamos una comprensión de lista para encontrar la intersección
    return [x for x in set(lista1) if x in lista2]


n = int(input('Introduce un número N para crear lista: '))
m = int(input('Introduce un número M para crear otra lista: '))
lista1 = inicializa_lista_aleatoria(n)
lista2 = inicializa_lista_aleatoria(m)

print('Lista 1: ', lista1)
print('Lista 2: ', lista2)
print('Función restricción -> ', interseccion(lista1, lista2))
print('Función NO restricción -> ', interseccion_v2(lista1, lista2))
