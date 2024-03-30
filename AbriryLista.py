import tkinter as tk
from tkinter import filedialog
import graphviz

class Nodo:
    def __init__(self, tablero):
        self.tablero = tablero
        self.siguiente = None

class Tablero:
    def __init__(self, nombre, filas, columnas, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.estructura = estructura

def abrir_archivos():
    archivos = filedialog.askopenfilenames(initialdir='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768', title='Explorador')
    if archivos:
        global tableros
        tableros = None
        for archivo in archivos:
            try:
                with open(archivo, 'r', encoding='utf-8') as file:
                    datos = file.readlines()  # Leer el contenido del archivo línea por línea
                    nuevos_tableros = leer_tableros(datos)  # Procesar los datos y crear los tableros
                    if nuevos_tableros:
                        # Concatenar las listas de tableros
                        if tableros is None:
                            tableros = nuevos_tableros
                        else:
                            actual = tableros
                            while actual.siguiente:
                                actual = actual.siguiente
                            actual.siguiente = nuevos_tableros
            except Exception as e:
                print("Error al cargar archivo:", e)
        
        if tableros:
            generar_graphiz(tableros)

def leer_tableros(datos):
    tableros = None
    nombre = filas = columnas = estructura = None

    for linea in datos:
        linea = linea.strip()
        if linea.startswith("<maqueta>"):
            nombre = filas = columnas = estructura = None  # Reiniciar variables para la nueva maqueta
        elif linea.startswith("<nombre>") and nombre is None:
            nombre = linea.replace("<nombre>", "").replace("</nombre>", "").strip()
        elif linea.startswith("<filas>"):
            filas = int(linea.replace("<filas>", "").replace("</filas>", "").strip())
        elif linea.startswith("<columnas>"):
            columnas = int(linea.replace("<columnas>", "").replace("</columnas>", "").strip())
        elif linea.startswith("<estructura>"):
            estructura = linea.replace("<estructura>", "").replace("</estructura>", "").strip()
        elif linea.startswith("</maqueta>"):
            if nombre is not None and filas is not None and columnas is not None and estructura is not None:
                tablero = Tablero(nombre, filas, columnas, estructura)
                nuevo_nodo = Nodo(tablero)
                if tableros is None:
                    tableros = nuevo_nodo
                else:
                    actual = tableros
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = nuevo_nodo
                # Reiniciar variables para la próxima maqueta
                nombre = filas = columnas = estructura = None

    return tableros

def mostrar_tableros():
    root = tk.Tk()
    root.title("Seleccionar tablero")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Seleccione el tablero a graficar:").pack()

    var_tablero = tk.StringVar()  # Mover la creación de var_tablero aquí

    for nodo in tableros_generator(tableros):
        tk.Radiobutton(frame, text=nodo.tablero.nombre, variable=var_tablero, value=nodo.tablero.nombre).pack(anchor="w")

    btn_graficar = tk.Button(frame, text="Graficar", command=lambda: generar_graphiz(tableros))
    btn_graficar.pack()

    root.mainloop()

def tableros_generator(tableros):
    actual = tableros
    while actual:
        yield actual
        actual = actual.siguiente

def generar_graphiz(tableros):
    dot_code = "digraph Tableros {\n"
    actual = tableros
    while actual:
        dot_code += f'    subgraph cluster_{actual.tablero.nombre} ' + '{\n'
        dot_code += '        label="' + actual.tablero.nombre + '"\n'
        dot_code += '        node [shape=plaintext style=filled]\n'
        dot_code += '        struct [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n'
        for fila in range(actual.tablero.filas):
            dot_code += '            <TR>'
            for columna in range(actual.tablero.columnas):
                posicion = fila * actual.tablero.columnas + columna
                if actual.tablero.estructura[posicion] == '*':
                    dot_code += f'<TD bgcolor="black" fontcolor="white">{actual.tablero.estructura[posicion]}</TD>'
                else:
                    dot_code += '<TD></TD>'
            dot_code += '</TR>\n'
        dot_code += '        </TABLE>>]\n'
        dot_code += '    }\n'
        actual = actual.siguiente
    dot_code += "}\n"

    dot_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tableros.dot"
    png_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tablero_seleccionado.png"

    with open(dot_file_path, "w") as f:
        f.write(dot_code)

    try:
        graphviz.render('dot', 'png', dot_file_path)
        print(f"Se ha generado el archivo '{png_file_path}' del tablero seleccionado.")
    except Exception as e:
        print("Error al generar el archivo PNG:", e)

def imprimir_tableros(tableros):
    actual = tableros
    while actual:
        print("Nombre:", actual.tablero.nombre)
        print("Filas:", actual.tablero.filas)
        print("Columnas:", actual.tablero.columnas)
        print("Estructura:", actual.tablero.estructura)
        print("---------------")
        actual = actual.siguiente

#abrir_archivos()



