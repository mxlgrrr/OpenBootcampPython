"""
    Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
"""
import math

def areaTriangulo(altura,base):
    area = altura*(base**2)
    return print("El area del triangulo de altura: %s y base: %s es = %s" % (altura,base,area))

def areaCirculo(radio):
    area = math.pi*(radio**2)
    return print("El area de la circunferencia de radio: %s es = %s" % (radio,area))

areaTriangulo(2,3)
areaCirculo(5)