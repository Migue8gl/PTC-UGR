#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:05:56 2023

@author: migue8gl
"""

'''
Función de Validación Numérica:
    Esta función verifica si una cadena (string) contiene solo caracteres numéricos. 
    Se utiliza para validar si una entrada de usuario es numérica.

Parámetros:
    - x (str): La cadena que se va a validar.

Retorno:
    - bool: Devuelve True si todos los caracteres en la cadena son numéricos,
             de lo contrario, devuelve False.
'''


def is_numeric_var(x):
    valid_chars = '0123456789.'
    for char in x:
        if char not in valid_chars:
            return False
    return True


'''
Función de División de Cadenas:
    Esta función divide una cadena en dos partes en función de un separador dado.
    Se utiliza para dividir una cantidad en euros en parte entera y parte decimal.

Parámetros:
    - x (str): La cadena que se va a dividir.
    - sep (str, opcional): El carácter que se utiliza como separador. El valor por defecto es '.'.

Retorno:
    - left (str): La parte izquierda de la cadena antes del separador.
    - right (str): La parte derecha de la cadena después del separador.
'''


def split_var(x, sep='.'):
    left, right = '', ''
    leftPart = True

    for char in x:
        if char == sep:
            leftPart = False
        if leftPart:
            left += char
        else:
            if char != sep:
                right += char
    return left, right


'''
Función de Lectura de Cantidad en Euros:
    Esta función solicita al usuario una cantidad en euros (en el formato euros.centimos)
    y valida la entrada para asegurarse de que cumple con los requisitos de formato correcto.

Retorno:
    - x (str): La cantidad en euros (en el formato euros.centimos) introducida por el usuario.
'''


def leer_euros():
    correct = False

    while not correct:
        x = input(
            'Introduzca una cantidad en euros de forma correcta (euros.centimos): ')
        if not x:
            print('La entrada no puede estar vacía.')
        else:
            euros, cents = split_var(x)
            if is_numeric_var(euros) and is_numeric_var(cents) and len(cents) <= 2:
                print('El input es correcto para representar los euros.')
                correct = True


leer_euros()
