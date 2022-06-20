"""
    En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
    Para ello, tendréis que acceder dos veces al archivo creado.
"""
f = open('mi_archivo.txt', 'w')
f.write('Hola mundo\n')
f.close()

fi = open('mi_archivo.txt', 'a')
fi.write('Estoy aqui\n')
fi.close()