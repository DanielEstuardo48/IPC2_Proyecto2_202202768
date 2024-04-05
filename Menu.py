import tkinter as tk
from tkinter import ttk
from AbriryLista import *

win = tk.Tk()
win.title('Menu Principal')
#win.geometry("550x450+530+180")
window_width = 650  # Ancho de la ventana
window_height = 550
screen_width = win.winfo_screenwidth()  # Ancho de la pantalla
screen_height = win.winfo_screenheight()  # Altura de la pantalla
x_coordinate = (screen_width - window_width) // 2  # Coordenada x para centrar la ventana
y_coordinate = (screen_height - window_height) // 2  # Coordenada y para centrar la ventana
win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # Establecer la geometría de la ventana

# Estilo de botones
style = ttk.Style()
style.configure("Modern.TButton", foreground="black", background="blue", font=("Helvetica", 12, "bold"))

# !Boton para cargar archivos
# *Esta es la imagen
icono_abrir = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/agregar-documento.png')

ButtonArchivo = ttk.Button(win, text='Cargar archivo', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_abrir, command = abrir_archivos)
ButtonArchivo.pack(pady=30)

# !Boton para ver maquetas
# *Esta es la imagen
icono_verlab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/ver_laberinto.png')

ButtonVerLab = ttk.Button(win, text='Ver Maquetas', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_verlab, command = mostrar_tableros)
ButtonVerLab.pack(pady=30)

# !Boton para ver  solucion de maquetas
# *Esta es la imagen
icono_sollab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/sol_laberinto.png')

ButtonSolLab = ttk.Button(win, text='Solucionar Maqueta', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icono_sollab, command= mostrar_tableros_solucion)
ButtonSolLab.pack(pady=30)

# !Boton para ayuda
icon_ayuda = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/ayuda.png')

Buttonayuda = ttk.Button(win, text='Ayuda', cursor='hand2', compound=tk.LEFT,style='Modern.TButton', image=icon_ayuda, command= ayuda)
Buttonayuda.pack(pady=30)

win.mainloop()


