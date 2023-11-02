# -*- coding: utf-8 -*-
"""

@author: Eugenio
Ejemplo de operaciones con ficheros .csv y diccionarios
En este ejemplo el separador es el ;

Leemos el fichero poblacionPrueba.csv como un fichero de texto
para quitar la información que no interesa y generar un nuevo
poblacionPruebaFinal.csv con los datos de provincias y población en columnas

Aviso: hay que tener cuidado con el valor de codificación si trabajamos con ficheros
procedentes de windows que suele usar windows-1250 o ISO-8859-1
en este caso hemos salvado el fichero poblacionPrueba.csv en utf8 usando el
bloc de notas de windows

Primero limpiar el archivo para quitar los datos no útiles
dejar cabecera y datos

"""
import csv

ficheroInicial=open("poblacionPrueba.csv","r", encoding="utf8")


cadenaPob=ficheroInicial.read()

ficheroInicial.close()

print("\nFichero leido inicial es\n",cadenaPob)

primero=cadenaPob.find("Provincia")
ultimo=cadenaPob.rfind("2010")

cadenaFinal=cadenaPob[primero:ultimo]
#print(cadenaPob)


        
      

  
 
