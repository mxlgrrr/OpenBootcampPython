"""
    Escribe una función que pueda decirte si un número (número entero) es primo o no.
"""

def esPrimo(numero):
    if numero < 1:
        return print("El numero %s no es primo" % numero)
    elif numero == 2:
        return print("El numero %s no es primo" % numero)
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return print("El numero %s no es primo" % numero)
        return print("El numero %s es primo" % numero)

esPrimo(17)
