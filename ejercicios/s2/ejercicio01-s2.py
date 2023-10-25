#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:14:39 2023

@author: migue8gl
"""

'''
Calculador precio vehículo:
    1 - Precio bruto
    2 - Porcentaje ganancia
    3 - IVA
'''

print('----- Calculador de precios de vehículos -----')
gross_price = float(input('Precio bruto: '))
benefit_percentage = float(input('Porcentaje de ganancia (sobre 100%): '))
IVA = float(input('IVA (sobre 100%): '))

base_price = gross_price + (gross_price * (benefit_percentage / 100))
final_price = base_price + (base_price * (IVA / 100))

print("El precio final del vehículo es: {}".format(final_price))
print('----- Calculador de precios de vehículos -----')
