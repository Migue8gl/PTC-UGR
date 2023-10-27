#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:57:22 2023

@author: migue8gl
"""

"""
Partiendo de una lista que contiene a su vez N listas de M enteros, si la
consideramos como una matriz de dimensión NxM, implementar una función que nos
devuelva la matriz traspuesta MxN (intercambiando filas y columnas) que
contedrá M listas de N enteros. Solicitar N y M por teclado y mostrar el
resultado por pantalla.
"""


# Inicializo lista con enteros hasta N incluida y la devuelvo
def inicializar_lista(n):
    lista = []
    for i in range(0, n):
        lista.append(i)
    return lista


# Función auxiliar para visualizar una matriz
def imprimir_matriz(matriz):
    if not matriz:
        print("La matriz está vacía.")
        return

    # Obtener el número de filas y columnas de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    # Encontrar la longitud máxima de cada elemento en la matriz
    max_longitud = max(len(str(matriz[i][j]))
                       for i in range(filas) for j in range(columnas))

    # Imprimir la matriz
    for i in range(filas):
        for j in range(columnas):
            elemento = str(matriz[i][j])
            espacios_relleno = max_longitud - len(elemento)
            # Espacios para igualar las longitudes
            espacios = " " * espacios_relleno
            print(f"{elemento}{espacios}", end=" ")
        print()  # Nueva línea después de cada fila


# Manualmente iterando
def traspuesta(lista_matriz):
    lista_matriz_traspuesta = []
    for i in range(0, len(lista_matriz[0])):
        aux = []
        for j in range(0, len(lista_matriz)):
            aux.append(lista_matriz[j][i])
        lista_matriz_traspuesta.append(aux)
    return lista_matriz_traspuesta


# Usamos comprensión de litas y zip(*a) = zip(a[0], a[1], ...)
def traspuesta_v2(lista_matriz):
    return [list(column) for column in zip(*lista_matriz)]


n = int(input('Introduce un número N de listas: '))
m = int(input('Introduce un número M de números en cada lista: '))

lista = [inicializar_lista(m) for i in range(0, n)]

print('\nMatriz original')
imprimir_matriz(lista)
print('\nFunción restricción')
imprimir_matriz(traspuesta(lista))
print('\nFunción CON restricción ')
imprimir_matriz(traspuesta_v2(lista))
