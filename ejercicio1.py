import tkinter
from tkinter import ttk

window = tkinter.Tk()

# Configuración de pantalla
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=5)

# Variable de registro de opción marcada
selected = tkinter.StringVar()

# función que desmarca la opción marcada
def reiniciar(evento):
    selected.set(None)

# Elementos
# RadioButton
r1 = ttk.Radiobutton(window, text='Sí', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=selected)
r4 = ttk.Radiobutton(window, text='Preguntar más tarde', value='4', variable=selected)
r5 = ttk.Radiobutton(window, text='Prefiere no responder', value='5', variable=selected)
# Boton de Reinicio
b1 = ttk.Button(window, text='Reiniciar')
b1.bind('<Button-1>', reiniciar)

# Ubiciación de elementos en pantalla
r1.grid(column = 0, row=0, pady=5, padx=5)
r2.grid(column = 0, row=1, pady=5, padx=5)
r3.grid(column = 0, row=2, pady=5, padx=5)
r4.grid(column = 0, row=3, pady=5, padx=5)
r5.grid(column = 0, row=4, pady=5, padx=5)
b1.grid(column = 1, row=5, pady=7, padx=7)

window.mainloop()
