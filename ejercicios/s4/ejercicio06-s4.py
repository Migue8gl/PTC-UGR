#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:47:04 2023

@author: migue8gl
"""

"""
Solicitar un número entero N por teclado e implentar una función que devuelva
una lista con la descomposición en factores primos de N. Mostrar el resultado
por pantalla.
"""


def descomposicion_primos(n):
    # Inicializamos una lista vacía para almacenar los factores primos
    resultado = []
    primo_divisor = 2  # Empezamos con el primer número primo, que es 2
    while n != 1:
        if n % primo_divisor == 0:
            # Si n es divisible por el primo_divisor, lo añadimos a la lista
            # de factores
            resultado.append(primo_divisor)
            # Actualizamos n dividiéndolo por el primo_divisor
            n = n // primo_divisor
            # Restauramos el primo_divisor a 2 para buscar el siguiente factor
            primo_divisor = 2
        else:
            # Si no es divisible, pasamos al siguiente número primo
            primo_divisor += 1
    return resultado  # Devolvemos la lista de factores primos de n


n = int(input('Introduce un número N: '))

print('Función restricción -> {}'.format(descomposicion_primos(n)))
#print('Función CON restricción -> {}'.format(descomposicion_primos_v2(n)))
