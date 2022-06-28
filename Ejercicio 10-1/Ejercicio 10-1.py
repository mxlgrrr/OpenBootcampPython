"""
    En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

    Al principio no tiene que haber una opción seleccionada.
"""

import tkinter as tk

window = tk.Tk()
window.geometry('1080x720')

radioValue = tk.IntVar() 
radioOne = tk.Radiobutton(window, text='Opcion 1',
                             variable=radioValue, value=1) 
radioTwo = tk.Radiobutton(window, text='Opcion 2',
                             variable=radioValue, value=2) 

radioOne.grid(column=0, row=0)
radioTwo.grid(column=0, row=1)

def clearFunc():
    radioValue.set(None)

Reset=tk.Button(text="Reset",command=clearFunc)
Reset.grid(column=0, row=2)

window.mainloop()