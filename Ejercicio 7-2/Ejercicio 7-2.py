"""
    En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
    En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""
from datetime import datetime, time
from email import message
from tkinter import dialog

hora_actual = datetime.now() 
hora_actual_string = hora_actual.strftime('%H:%M:%S')
hora = hora_actual.strftime('%S')
dia = hora_actual.strftime('%d')
mes = hora_actual.strftime('%m')
año = hora_actual.strftime('%Y')
limite_horario = datetime(int(año), int(mes), int(dia), 19, 0, 00, 00000)
horario_completo_actual = hora_actual.time()

if (int(hora)<10 and int(hora)>19):
    termino_jornada = limite_horario - hora_actual
    print("Falta %s para terminar la jornada" % termino_jornada)
else:
    hora_nueva_jornada = datetime(int(año), int(mes), int(dia)+1, 10, 0, 00, 00000)
    diferencia_nueva_jornada = hora_nueva_jornada - hora_actual
    print("Su jornada laboral termino a las 19 horas")
    print("Su proxima jornada laboral comienza a las 10 hs, le queda %s" % diferencia_nueva_jornada)