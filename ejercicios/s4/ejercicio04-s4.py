#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:10:52 2023

@author: migue8gl
"""

"""
Usando el módulo “random” genera dos listas de N y M números enteros aleatorios 
entre 1 y 10 e implementa una función que devuelva una tercera lista que 
contenga los números de las dos primeras listas en orden ascendente sin 
contener valores repetidos. Solicitar N y M por teclado y mostrar el resultado 
por pantalla.
"""




import random as rd
def inicializa_lista_aleatoria(N):
    lista = []
    for i in range(N):
        # Generar un número entero aleatorio entre 1 y 10
        lista.append(rd.randint(1, 10))
    return lista


# Función para ordenar dos listas y eliminar duplicados
def listas_ordenadas(lista1, lista2):
    lista_final = lista1 + lista2
    lista_ordenada_sin_duplicados = []

    # Eliminar duplicados y construir lista ordenada sin duplicados
    for elemento in lista_final:
        if elemento not in lista_ordenada_sin_duplicados:
            lista_ordenada_sin_duplicados.append(elemento)

    n = len(lista_ordenada_sin_duplicados)

    # Implementar un algoritmo de ordenamiento simple
    for i in range(n):
        for j in range(i + 1, n):
            if lista_ordenada_sin_duplicados[i] > lista_ordenada_sin_duplicados[j]:
                # Intercambiar elementos para ordenar
                lista_ordenada_sin_duplicados[i], lista_ordenada_sin_duplicados[
                    j] = lista_ordenada_sin_duplicados[j], lista_ordenada_sin_duplicados[i]

    return lista_ordenada_sin_duplicados


# Función usando sort() y set()
def listas_ordenadas_v2(lista1, lista2):
    lista_final = lista1 + lista2

    # Eliminar duplicados y construir lista ordenada sin duplicados
    lista_ordenada_sin_duplicados = list(set(lista_final))

    # Ordenar la lista sin duplicados en orden ascendente
    lista_ordenada_sin_duplicados.sort()

    return lista_ordenada_sin_duplicados


n = int(input('Introduce un número N para crear lista: '))
m = int(input('Introduce un número M para crear otra lista: '))
lista1 = inicializa_lista_aleatoria(n)
lista2 = inicializa_lista_aleatoria(m)

print('Lista 1: ', lista1)
print('Lista 2: ', lista2)
print('Función restricción -> ', listas_ordenadas(lista1, lista2))
print('Función CON restricción -> {}'.format(listas_ordenadas_v2(lista1, lista2)))
