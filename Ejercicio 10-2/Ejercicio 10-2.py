"""
   En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
   también debe de tener un label con el texto que queráis.
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('1080x720')

tk.Label(window, text="Nombre").grid(column=0, row=1)
nombre = tk.Entry()
nombre.grid(column=1, row=1)

tk.Label(window, text="Preferencia Horaria").grid(column=1, row=2)
horario = ttk.Combobox(window, values=["Mañana", "Tarde","Noche"])
horario.grid(column=2, row=2)

tk.Label(window, text="Disponibilidad").grid(column=0, row=3)
radioValue = tk.IntVar() 
radioOne = tk.Radiobutton(window, text='Inmediata', variable=radioValue, value=1) 
radioTwo = tk.Radiobutton(window, text='1 Semana', variable=radioValue, value=2)
radioThree = tk.Radiobutton(window, text='15 dias', variable=radioValue, value=3)  
radioOne.grid(column=0, row=4)
radioTwo.grid(column=1, row=4)
radioThree.grid(column=3, row=4)

def clearFunc():
    radioValue.set(None)

Reset=tk.Button(text="Reset",command=clearFunc)
Reset.grid(column=0, row=5)

window.mainloop()