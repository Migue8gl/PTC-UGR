# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:39:21 2019

@author: Eugenio

Validación de euros.
Vemos si es un digito numérico y formato 99.99
"""

def leerEuros():
    seguirPidiendo=True

    while seguirPidiendo:    
        precio=input("Dime precio con 2 decimales: ")
        #pruebaExcepcionValueError=float(precio)
        if len(precio)==0:
            print("Introduce un valor")
            esCorrecto=False
        else:         
            esCorrecto=True
        for digito in precio:
            if esCorrecto and (digito!=".") and (digito <'0' or digito >'9'):
                esCorrecto=False
                print("Hay digitos no validos", digito)
        if esCorrecto:
            precioLista=precio.split(".")
            if (len(precioLista) >1): print("Hay decimales:", len(precioLista[1]))
            if len(precioLista)==1 or (len(precioLista) >1 and len(precioLista[1])<3):
                #Todo está bien y podemos salir del while de validación
                seguirPidiendo=False
            else: 
                print("Introduce solo con dos decimales")
                
                
    return(float(precio))#no se va a producir excepción de valueError



print("El precio es",leerEuros())
  


