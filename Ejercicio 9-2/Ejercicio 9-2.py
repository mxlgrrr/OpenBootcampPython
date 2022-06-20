"""
    En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y 
    realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
import functools

def sumatoria(lista):
    listaFiltrada = filter(lambda x : x % 2 != 0, lista)
    sumatoria = functools.reduce(lambda a, b: a+b, listaFiltrada)
    return sumatoria


print(sumatoria([1,3,5,7,9,12,16]))