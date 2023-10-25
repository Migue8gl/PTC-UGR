# -*- coding: utf-8 -*-4
"""
Created on Thu Oct  3 21:10:55 2019

@author: Eugenio

Sobre los numeros reales en python y el redondeo

"""
from math import floor

print("Problemas de representación con 0.1 + 0.1 + 0.1")

numero1=0.1 + 0.1 + 0.1
numero2=0.3

if(numero1==numero2): print("Son iguales")
else: print("No son iguales")

if(numero1==0.3): print("Son iguales")
else: print("No son iguales")

print(numero1)
print(numero2)

print("Problemas con la funcion round")


print(round(0.315, 2))

print(round(0.325, 2))

print(round(0.335, 2))

print(round(0.345, 2))

print(round(0.355, 2))

print(round(0.365, 2))


print("Alternativa para redondear a las centésimas")

numero=0.34878
print(numero)
numero=numero*100
print(numero)
numero=numero + 0.5
print(numero)
numero=(int)(numero) # también se puede usar floor(numero)
print(numero)
numero=numero/100
print(numero)


#soluciones a la imprecisión de los floats. Tipo Decimal y Fraction
print("Uso del tipo Decimal")

import decimal
from decimal import Decimal, getcontext

x=Decimal('0.1')
suma=x+x+x

print(suma)

if(suma==Decimal('0.3')):print("Son iguales")
else: print("No son iguales")

y=Decimal('523.348')
#y=Decimal('5.348')
print(y)

x2=y*4 #se puede operar con enteros pero no con float

print(x2)

z=Decimal('3456.298')

#z=Decimal('36.298')
print("y = {} + z={} es= {}".format(y,z, y+z))

print(getcontext())


#para cambiar la precision getcontext().prec=20
#prec no sirve para especificar que se va a redondear a esa posición

#para cambiar la forma de redondear

# Here are all your options for rounding:
# This one offers the most out of the box control
# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP



getcontext().rounding = decimal.ROUND_HALF_UP

print("Suma: ",(y+z).quantize(Decimal("1.00")), "Resta: ", \
(y-z).quantize(Decimal("1.00")))


capitalInicial=Decimal("10000.45")
capitalFinal=capitalInicial*Decimal("1.10")


print("capitalFinal ", capitalFinal)

capitalFinal=capitalFinal.quantize(Decimal("1.00"))

print("capitalFinal ", capitalFinal)

print("Funcionamiento con numeros negativos")

negativo=Decimal("-3.568222")
negativoRedondeado=negativo.quantize(Decimal("1.00"))
print("{} se redondea a {}".format(negativo, negativoRedondeado))



#más información en https://realpython.com/python-rounding/










