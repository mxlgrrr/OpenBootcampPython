"""
    En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""


class Vehiculo(): 
    color = ""
    ruedas = ""
    puertas = ""

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def getColor(self):
        return self.color
    
    def getRuedas(self):
        return self.ruedas
    
    def getPuertas(self): 
        return self.puertas
    
nuevoVehiculo = Vehiculo("Rojo", 4, 5)

f = open('mi_nuevo_archivo.txt', 'w')
f.write('Objeto Vehiculo\n')
f.write(f'Color: {nuevoVehiculo.getColor()} \n')
f.write(f'Ruedas: {nuevoVehiculo.getRuedas()}\n')
f.write(f'Puertas: {nuevoVehiculo.getPuertas()}\n')
f.close()

fi = open('mi_nuevo_archivo.txt', 'r')
print(fi.read())
fi.close()