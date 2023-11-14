#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:07:46 2023

@author: migue8gl
"""

'''
Función de Lectura de Decimales:
    Esta función solicita al usuario un número (en el formato 99.99), no puede
    tener más de dos decimales
    y valida la entrada para asegurarse de que cumple con los requisitos de
    formato correcto.

Parámetros:
    - mensaje (str): El mensaje para la petición de los datos

Retorno:
    - valorValidado (float): (en el formato 99.9) introducida por el usuario.
    - numeroIntentosIncorrectos (int): número de intentos incorrectos
'''


def leerFloatMax2Decimales(mensaje):
    correct = False
    numeroIntentosIncorrectos = 0
    valorValidado = ''

    while not correct:
        try:
            valorValidado = input(mensaje)
            decimales = valorValidado.split('.')
            assert valorValidado, f'La entrada no puede estar vacía. Se introdujo: {valorValidado}'
            assert valorValidado.replace(
                ".", "").replace('-', '').isdigit(), f'La entrada debe ser un número. Se introdujo: {valorValidado}'
            if (len(decimales) > 1):
                assert len(decimales[1]) <= 2 and decimales[1].isdigit(
                ), f'El número puede tener máximo 2 decimales. Se introdujo: {valorValidado}'
            assert float(
                valorValidado) > 0, f'La entrada debe ser un número positivo. Se introdujo: {valorValidado}'
            correct = True
            print('El número {} es válido'.format(valorValidado))
        except AssertionError as error:
            print(error)
            numeroIntentosIncorrectos += 1
    return float(valorValidado), int(numeroIntentosIncorrectos)


'''
Función de Validación Entera Positiva:
    Esta función verifica si una cadena (string) contiene solo caracteres numéricos,
    enteros y positivos. Se utiliza para validar si una entrada es entero positivo.

Parámetros:
    - mensaje (str): El mensaje para la petición de los datos

Retorno:
    - valorValidado (int): La cadena que se va a validar pasada a entero positivo
'''


def leerEnteroPositivo(mensaje):
    correct = False
    numeroIntentosIncorrectos = 0
    valorValidado = -1

    while not correct:
        try:
            valorValidado = input(mensaje)
            assert valorValidado, f'La entrada no puede estar vacía. Se introdujo: {valorValidado}'
            assert valorValidado.isdigit(), f'El número debe ser entero. Se introdujo: {valorValidado}'
            assert float(
                valorValidado) >= 0, f'La entrada debe ser un número positivo. Se introdujo: {valorValidado}'
            correct = True
            print('El número {} es válido'.format(valorValidado))
        except AssertionError as error:
            print(error)
            numeroIntentosIncorrectos += 1
    return int(valorValidado), int(numeroIntentosIncorrectos)


if __name__ == "__main__":
    nCorrectos = 0
    nIncorrectas = 0
    capital, nInc = leerFloatMax2Decimales(
        "Dime capital inicial con 2 decimales máximo: ")
    nCorrectos += 1
    nIncorrectas = nIncorrectas+nInc
    interés, nInc = leerFloatMax2Decimales(
        "Dime interés anual con 2 decimales máximo: ")
    nCorrectos += 1
    nIncorrectas = nIncorrectas+nInc
    anios, nInc = leerEnteroPositivo("Dime el número de años: ")
    nCorrectos += 1
    nIncorrectas = nIncorrectas+nInc
    print("Fin del programa de validación de euros")
    print("Nombre estudiante: Miguel García López")
    print("Entradas correctas: ", nCorrectos, " incorrectas: ", nIncorrectas)
