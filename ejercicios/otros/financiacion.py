#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:13:54 2023

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

import math

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
    - x (float): La cantidad en euros (en el formato euros.centimos) introducida por el usuario.
'''


def leerFLoat2Decimales():
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
    return float(x)


'''
Función de Validación Entera Positiva:
    Esta función verifica si una cadena (string) contiene solo caracteres numéricos,
    enteros y positivos. Se utiliza para validar si una entrada es entero positivo.

Parámetros:
    - x (str): La cadena que se va a validar.

Retorno:
    - x (int): La cadena que se va a validar pasada a entero positivo
'''


def leerInt():
    correct = False

    while not correct:
        x = input(
            'Introduzca un número entero positivo: ')
        if not x:
            print('La entrada no puede estar vacía.')
        else:
            valid_chars = '0123456789'
            correct = True
            for char in x:
                if char not in valid_chars:
                    correct = False
    return int(x)


'''
Función de Redondeo:
    Esta función redondea con cálculos manuales un número a partir de otro número 
    de decimales. 

Parámetros:
    - numero (float): Número a redondear
    - decimales (int): Decimales a redondear

Retorno:
    - numero (float): Número redondeado
'''
def redondear(numero, decimales):
    numero = numero * math.pow(10, decimales)
    numero = numero + 0.5
    numero = int(numero)
    numero = numero / math.pow(10, decimales)
    return numero


'''
Función de calculo de Capital Anual:
    Esta función calcula dado un capital inicial y un interés anual, cuando dinero
    total al año queda

Parámetros:
    - capitalInicial (float): Dinero inicial
    - interes (float): Interés anual sobre el capital

Retorno:
    - capitalAnul (float): Dinero anual
'''
def calcularCapitalAnual(capitalInicial, interes):
    capitalAnual = capitalInicial + capitalInicial * interes /  100
    return redondear(capitalAnual, 2)
    