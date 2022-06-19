"""
    En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
    Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno(): 
    nombre = ""
    nota = ""

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def evaluar_nota(self):
        if self.nota<5:
            print("El alumno desaprobo")
        else:
            print("El alumno aprobo")

nuevoAlumno = Alumno("Juan", 4)
print("El alumno %s tiene una nota de %d" % (nuevoAlumno.nombre, nuevoAlumno.nota))
nuevoAlumno.evaluar_nota()