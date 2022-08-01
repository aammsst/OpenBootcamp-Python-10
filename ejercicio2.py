import tkinter
from tkinter import ttk

# Configuración inicial de pantalla
window = tkinter.Tk()
window.columnconfigure(0, weight = 1)
window.columnconfigure(0, weight = 2)

# Creación de lista con elementos
lista = ['La Renga', 'Slothrust', 'Iron Maiden', 'Annihilator', 'Blind Guardian']
lista_items = tkinter.StringVar(value = lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)

# Etiqueta (Título)
label = tkinter.Label(text='Algunas bandas de Metal y Rock!')

# Posicionamiento de elementos en pantalla
label.grid(column=0,row=0, sticky=tkinter.N)
listbox.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()
