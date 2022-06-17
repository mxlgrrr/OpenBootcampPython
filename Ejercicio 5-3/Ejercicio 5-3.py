"""
    Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""

def esBisiesto(año):
    if año % 4 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0:
        print("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        print("Es bisiesto")

esBisiesto(2020)
