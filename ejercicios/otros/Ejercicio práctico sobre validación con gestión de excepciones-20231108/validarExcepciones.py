# -*- coding: utf-8 -*-
"""

@author: Eugenio
Validación de entradas usando gestión de excepciones
Contamos las entradas correctas e incorrectas para informar al finalizar
el programa.
Solo se aceptan enteros positivos y además que sean múltiplos de 3 y 7 al mismo tiempo
"""


# vemos si el entero positivo es múltiplo de 3 y 7
def validarMultiplo3y7(enteroPos):
    
    if enteroPos%3==0 and enteroPos%7==0:
        validacion=True
    else:
        validacion=False
    
    return validacion

    
    
##Main    



entradasCorrec_a_leer=4 # pedir 4 valores correctos
entradasCorrectas=0
entradasIncorrectas=0
nombreEstudiante="Manolo García"

while entradasCorrectas< entradasCorrec_a_leer:    
    try:
        entrada=input("Dime un entero positivo múltiplo de 3 y 7: ")
        valor=int(entrada)
        assert valor>0, f"La entrada debe ser mayor a cero y ha indicado {valor}"
        assert validarMultiplo3y7(valor), f"Debe ser múltiplo de 3 y 7 y {valor} no lo es"
        print(f"La entrada es {valor} y es correcta")
        entradasCorrectas+=1
    except ValueError:
        print (f"Debe introducir un número entero positivo y su entrada fue: {entrada}")
        entradasIncorrectas+=1
    except AssertionError as error:
        print(error)
        entradasIncorrectas+=1
 
       
   
print("Fin del programa de ejemplo de validación con excepciones")
print("Nombre estudiante: ",nombreEstudiante)
print("Entradas correctas: ",entradasCorrectas," incorrectas: ",entradasIncorrectas)



  


