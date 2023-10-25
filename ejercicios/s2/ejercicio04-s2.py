#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:24:46 2023

@author: migue8gl
"""

'''
Calculador de cambio
'''

print('----- Calculador de cambio -----')

charging = float(input('Introduzca precio: '))
payment = float(input('Introduzca cantidad aportada: '))

# Calculamos cambio euros
change = payment - charging

one_euros, fifty_cents, ten_cents, one_cents = 0, 0, 0, 0

if change >= 1:
    one_euros = int(change)
    change -= one_euros

# Calculamos cambio 50 cents
if change >= .5:
    fifty_cents = int(change / .5)
    change -= fifty_cents * .5

# Calculamos cambio 10 cents
if change >= .1:
    ten_cents = int(change / .1)
    change -= ten_cents * .1

# Calculamos cambio 1 cents
if change >= .01:
    one_cents = int(change / .01)
    change -= one_cents * .01

print('Devolvemos {} monedas de 1 euros, {} monedas de 50 cent, {} monedas de 10 cents y {} monedas de 1 cent'.format(
    one_euros, fifty_cents, ten_cents, one_cents))

print('----- Calculador de cambio -----')
