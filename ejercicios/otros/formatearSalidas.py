# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:52:04 2021

@author: Eugenio
Diferentes maneras de formatear una salida de números reales
"""
import math

radio = float(input("Introduce el radio de la circunferencia: "))

longitud = 2 * math.pi * radio
area = math.pi * radio ** 2

print("La longitud de la circunferencia es: ", longitud)
print("El área de la circunferencia es: ", area)

print("La longitud es ", longitud, "y el área es", area)


print("La longitud y área de la circunferencia son: %6.2f y %6.2f" % (longitud, area))



print("La longitud y área con radio {} son {} y {}".format(radio, longitud, area))
print("La longitud y área con radio {0} son {1:6.2f} y {2} {2:6.3f} ".format(radio, longitud, area))

'''
Desde python 3.6 se pueden usar las cadenas f
Una cadena "f" se suele presentar como un literal
entrecomillado al que le precede el carácter "f" o "F":
'''

print(f"La longitud y área con {radio} son {longitud:6.2f} y {area:6.3f} ")

#solo a partir de python 3.8
print(f"El {radio=}")
