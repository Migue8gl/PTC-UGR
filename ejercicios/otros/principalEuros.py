#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:36:31 2023

@author: migue8gl
"""

from financiacion import calcularCapitalAnual, leerFLoat2Decimales, redondear

capitalInicial = leerFLoat2Decimales()
interes = float(input('Introduzca interes en tanto por ciento: '))
años = int(input('Introduzca número de años: '))
capitalAcumulado = capitalInicial

for i in range(0, años):
    capitalAnual = calcularCapitalAnual(capitalInicial, interes)
    capitalAcumulado += capitalAnual - capitalInicial
    capitalInicial = capitalAnual  # Update the initial capital for the next year
    print(f'Año {i + 1}: {capitalAcumulado:.2f}')