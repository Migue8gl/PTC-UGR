#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:04:21 2023

@author: migue8gl
"""

"""
Script R1: Calcular la variación de la población por provincias desde el año 2011 a
2017 en términos absolutos y relativos.
"""

import csv
def ejecutar():

    # Leemos el fichero inicial, lo limpiamos y añadimos cabezera
    fichero_inicial = open(
        './entradas/poblacionProvinciasHM2010-17.csv', 'r', encoding='utf8')
    cadena_inicial = fichero_inicial.read()
    fichero_inicial.close()

    primero = cadena_inicial.find('Total Nacional')
    ultimo = cadena_inicial.find('Notas')
    cadena_final = cadena_inicial[primero:ultimo]
    
    # Limpiamos el último caracter ';' que es innecesario
    lines = cadena_final.split('\n')
    cleaned_lines = [line.rstrip(';') for line in lines] # Cogemos último ';'
    cadena_final = '\n'.join(cleaned_lines)

    # Creamos cabecera y se la añadimos al fichero csv final
    cabecera = "Provincia;2017;2016;2015;2014;2013;2012;2011;2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010"
    fichero_final = open(
        './resultados/poblacionProvinciasHM2010-17-final.csv', 'w', encoding='utf8')
    fichero_final.write(cabecera + '\n' + cadena_final)
    fichero_final.close()

    print("\n------------------------------------------------------------\n")

    # Leemos el fichero csv limpio como un diccionario
    with open('./resultados/poblacionProvinciasHM2010-17-final.csv', encoding="utf8") as csvarchivo:
        poblacionDict = csv.DictReader(csvarchivo, delimiter=';')
        for regD in poblacionDict:
            print(regD)

ejecutar()
