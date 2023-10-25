#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:53:59 2023

@author: migue8gl
"""

'''
Calculador centímetros cúbicos

C1​V1​=C2​V2​

Donde:

    C1​ es la concentración inicial (80% en este caso).
    V1​ es el volumen inicial (la cantidad desconocida de la disolución al 
                                 80% que necesitas encontrar).
    C2​ es la concentración final deseada (y% en este caso, pero expresada 
                                             como un decimal, 
                                             es decir, y/100y/100).
    V2​ es el volumen final deseado (x centímetros cúbicos).

Puedes resolver esta ecuación para encontrar V1​:

V1=(C2⋅V2)/C1​
'''

print('----- Calculador centímetros cúbicos -----')

x = float(input('Introduce centímetros cúbicos: '))
y = float(input('Introduce porcentaje de concentración (sobre 100%): '))


# Verificar si y es menor que 80
if y > 80:
    print("La concentración deseada debe ser menor que 80%.")
else:
    # Concentración inicial y volumen inicial
    c1 = 0.80  # 80% de concentración inicial
    v1 = (y / 100) * x / c1

    # Volumen de agua necesario
    v_agua = x - v1

    # Resultados
    print(f"Para obtener {x} cm³ al {y}% de concentración, necesitas:")
    print(f"{v1} cm³ de la disolución al 80%")
    print(f"{v_agua} cm³ de agua")


print('----- Calculador centímetros cúbicos -----')
