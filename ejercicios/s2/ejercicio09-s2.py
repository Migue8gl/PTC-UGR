#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:08:21 2023

@author: migue8gl
"""

'''
Calculador mínimo de paneles solares
'''

from math import ceil

print('----- Calculador mínimo de paneles solares -----')

rend = .17  # % expresado entre [0,1]
tam = 1.6  # m²
obj = 1000  # Kwh
one_month = 30  # dias

mean_sol_rad = float(input('Introduce la radicación solar media: '))

energy_panel_month = one_month * mean_sol_rad * rend * tam
min_solar_panels = ceil(obj/energy_panel_month)

print('Se necesitan como mínimo {} paneles solares'.format(min_solar_panels))

print('----- Calculador mínimo de paneles solares -----')
