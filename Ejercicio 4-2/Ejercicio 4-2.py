"""
    Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

    Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
"""
print("Este programa mostrara todos los numeros impares desde un inicio a un final")

numero_inicial = input("Ingrese un numero inicial: ")
numero_final = input("Ingrese un numero final: ")

if numero_final>numero_inicial:
    if (int(numero_inicial) % 2)==0:
        for i in range(int(numero_inicial)+1,int(numero_final)+1,2):
            print(i)

    else:
        for i in range(int(numero_inicial),int(numero_final)+1,2):
            print(i)
else:
    if (int(numero_inicial) % 2)==0:
        for i in range(int(numero_final)+1,int(numero_inicial)+1,2):
            print(i)
    else:
        for i in range(int(numero_final),int(numero_inicial)+1,2):
            print(i)