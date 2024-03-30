import tkinter as tk
from tkinter import ttk
from AbriryLista import *

win = tk.Tk()
win.title('Menu Principal')
win.geometry("550x450+530+180")

# Estilo de botones
style = ttk.Style()
style.configure("Modern.TButton", foreground="black", background="blue", font=("Helvetica", 12, "bold"))

# !Boton para cargar archivos
# *Esta es la imagen
icono_abrir = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/agregar-documento.png')

ButtonArchivo = ttk.Button(win, text='Cargar archivo', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_abrir, command= abrir_archivos)
ButtonArchivo.pack(pady=30)

# !Boton para ver maquetas
# *Esta es la imagen
icono_verlab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/ver_laberinto.png')

ButtonVerLab = ttk.Button(win, text='Ver Maquetas', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_verlab, command=mostrar_tableros)
ButtonVerLab.pack(pady=30)

# !Boton para ver  solucion de maquetas
# *Esta es la imagen
icono_sollab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/sol_laberinto.png')

ButtonSolLab = ttk.Button(win, text='Solucionar Maqueta', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_sollab)
ButtonSolLab.pack(pady=30)

win.mainloop()
