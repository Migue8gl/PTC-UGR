#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:33:31 2023

@author: migue8gl
"""

import locale
from decimal import Decimal, ROUND_HALF_UP


def separador_miles(numero):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string('%.2f', numero, grouping=True)


def redondear_numero(numero, decimales=2):
    return Decimal(numero).quantize(Decimal('1e-{0}'.format(decimales)),
                                    rounding=ROUND_HALF_UP)
