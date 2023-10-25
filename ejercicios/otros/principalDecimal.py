#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:08:59 2023

@author: migue8gl
"""

from decimal import Decimal, ROUND_HALF_UP


def leerFloat2decimales():
    while True:
        entrada = input("Ingrese una cantidad en euros: ")
        if not entrada:
            print("La entrada no puede estar vacía.")
            continue

        parts = entrada.split('.')
        if len(parts) != 2 or not (parts[0].isdigit() and parts[1].isdigit()):
            print("Entrada no válida. Debe ser en formato euros.centavos.")
            continue

        euros, cents = int(parts[0]), int(parts[1])
        cantidad_decimal = Decimal(f"{euros}.{cents:02d}")
        return cantidad_decimal


def leerInt():
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        if not entrada:
            print("La entrada no puede estar vacía.")
            continue

        if entrada.isdigit():
            entrada_decimal = Decimal(entrada)
            if entrada_decimal % 1 == 0 and entrada_decimal >= 0:
                return int(entrada_decimal)
            else:
                print("Entrada no válida. Debe ser un número entero positivo.")
        else:
            print("Entrada no válida. Debe ser un número entero positivo.")



def redondear(numero, decimales):
    return numero.quantize(Decimal('0.' + '0' * decimales), rounding=ROUND_HALF_UP)


def calcularCapitalAnual(capitalInicial, interes):
    capitalAnual = capitalInicial + capitalInicial * interes / Decimal('100')
    return redondear(capitalAnual, 2)


capitalInicial = leerFloat2decimales()
interes = Decimal(input('Introduzca interes en tanto por ciento: '))
años = int(input('Introduzca número de años: '))
capitalAcumulado = capitalInicial

for i in range(0, años):
    capitalAnual = calcularCapitalAnual(capitalInicial, interes)
    capitalAcumulado += capitalAnual - capitalInicial
    capitalInicial = capitalAnual  
    print(f'Año {i + 1}: {capitalAcumulado:.2f}')
