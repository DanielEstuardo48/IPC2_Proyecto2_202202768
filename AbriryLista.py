import tkinter as tk
from tkinter import filedialog,messagebox
import graphviz
from tkinter import ttk

class Nodo:
    def __init__(self, nombre, filas, columnas, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.estructura = estructura
        self.entrada = None
        self.objetos = ObjetoLinkedList()
        self.siguiente = None

    def Entrada(self, fila, columna):
        self.entrada = (fila, columna)
class ObjetoLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, nombre, fila, columna):
        nuevo_objeto = ObjetoNodo(nombre, fila, columna)
        if not self.head:
            self.head = nuevo_objeto
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = nuevo_objeto
    

    def append(self, objeto):
        if not self.head:
            self.head = ObjetoNodo(objeto)
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = ObjetoNodo(objeto)

    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.siguiente
class ObjetoNodo:
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = nodo

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.siguiente

class NodoCamino:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.siguiente = None
class CaminoLinkedList:
    def __init__(self):
        self.head = None

    def append(self, fila, columna):
        if not self.head:
            self.head = NodoCamino(fila, columna)
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = NodoCamino(fila, columna)

    def pop(self):
        if not self.head:
            return None
        elif not self.head.siguiente:
            popped = self.head
            self.head = None
            return popped
        else:
            current = self.head
            while current.siguiente.siguiente:
                current = current.siguiente
            popped = current.siguiente
            current.siguiente = None
            return popped

    def __iter__(self):
        current = self.head
        while current:
            yield (current.fila, current.columna)
            current = current.siguiente

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.siguiente
        return count
    
    def copy(self):
        new_camino = CaminoLinkedList()
        current = self.head
        while current:
            new_camino.append(current.fila, current.columna)
            current = current.siguiente
        return new_camino

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedoList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)
    
    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            popped = self.head.value
            self.head = None
            return popped
        else:
            current = self.head
            while current.next.next:
                current = current.next
            popped = current.next.value
            current.next = None
            return popped

    def __iter__(self):
        current = self.head
        while current:
            yield current.movimiento
            current = current.siguiente
class MovimientoNode:
    def __init__(self, movimiento, siguiente=None):
        self.movimiento = movimiento
        self.siguiente = siguiente
class MovimientoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, movimiento):
        nuevo_nodo = MovimientoNode(movimiento)
        if not self.head:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        elif self.length == 1:
            nodo_eliminado = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return nodo_eliminado
        else:
            nodo_actual = self.head
            while nodo_actual.siguiente != self.tail:
                nodo_actual = nodo_actual.siguiente
            nodo_eliminado = nodo_actual.siguiente
            nodo_actual.siguiente = None
            self.tail = nodo_actual
            self.length -= 1
            return nodo_eliminado

    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.movimiento  # Devolver la tupla de coordenadas
            current = current.siguiente


def abrir_archivos():
    archivos = filedialog.askopenfilenames(initialdir='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768', title='Explorador')
    if archivos:
        global tableros
        tableros = LinkedList()
        for archivo in archivos:
            try:
                with open(archivo, 'r', encoding='utf-8') as file:
                    datos = file.readlines()  # Leer el contenido del archivo línea por línea
                    leer_tableros(datos)  # Procesar los datos y crear los tableros
            except Exception as e:
                print("Error al cargar archivo:", e)

def leer_tableros(datos):
    global tableros
    nombre = filas = columnas = estructura = None
    entrada_fila = entrada_columna = None
    entrada_flag = False
    objetivo_flag = False

    for linea in datos:
        linea = linea.strip()
        if linea.startswith("<maqueta>"):
            nombre = filas = columnas = estructura = None  # Reiniciar variables para la nueva maqueta
            entrada_fila = entrada_columna = None  # Reiniciar variables para la nueva maqueta
            objetivo_flag = False  # Reiniciar la variable objetivo_flag
            objetoFC = ObjetoLinkedList()  # Inicializar la lista enlazada de objetos para este tablero
        elif linea.startswith("<nombre>") and nombre is None:
            nombre = linea.replace("<nombre>", "").replace("</nombre>", "").strip()
        elif linea.startswith("<filas>"):
            filas = int(linea.replace("<filas>", "").replace("</filas>", "").strip())
        elif linea.startswith("<columnas>"):
            columnas = int(linea.replace("<columnas>", "").replace("</columnas>", "").strip())
        elif linea.startswith("<estructura>"):
            estructura = linea.replace("<estructura>", "").replace("</estructura>", "").strip().replace(" ", "").replace("\n", "")
        elif linea.startswith("<entrada>"):
            entrada_flag = True
        elif entrada_flag:
            if linea.startswith("<fila>"):
                entrada_fila = int(linea.replace("<fila>", "").replace("</fila>", "").strip())
            elif linea.startswith("<columna>"):
                entrada_columna = int(linea.replace("<columna>", "").replace("</columna>", "").strip())
            elif linea.startswith("</entrada>"):
                entrada_flag = False
                if entrada_fila is not None and entrada_columna is not None:
                    print("Posición de entrada:", entrada_fila, entrada_columna)
        elif linea.startswith("<objetivo>"):
            objetivo_flag = True
        elif linea.startswith("</objetivo>"):
            objetivo_flag = False
        elif objetivo_flag:
            if linea.startswith("<nombre>"):
                objetivo_nombre = linea.replace("<nombre>", "").replace("</nombre>", "").strip()
            elif linea.startswith("<fila>"):
                objetivo_fila = int(linea.replace("<fila>", "").replace("</fila>", "").strip())
            elif linea.startswith("<columna>"):
                objetivo_columna = int(linea.replace("<columna>", "").replace("</columna>", "").strip())
                objetoFC.agregar(objetivo_nombre, objetivo_fila, objetivo_columna)  # Agregar objeto a la lista enlazada
        elif linea.startswith("</maqueta>"):
            if nombre is not None and filas is not None and columnas is not None and estructura is not None:
                nuevo_nodo = Nodo(nombre, filas, columnas, estructura)
                if entrada_fila is not None and entrada_columna is not None:
                    nuevo_nodo.Entrada(entrada_fila, entrada_columna)
                nuevo_nodo.objetos = objetoFC  # Asignar la lista de objetos al tablero
                tableros.agregar(nuevo_nodo)
                # Reiniciar variables para la próxima maqueta
                nombre = filas = columnas = estructura = None
                entrada_fila = entrada_columna = None

def mostrar_tableros():
    mostrar_tableros_ordenados(tableros)

def mostrar_tableros_ordenados(tableros):
    if not tableros:
        tk.messagebox.showerror("Error", "No se ha cargado ningún tablero previamente.")
        return

    def generar_tablero_seleccionado():
        seleccionado = entrada_nombre.get().strip()  # Obtener el nombre ingresado y eliminar espacios en blanco al inicio y al final
        if seleccionado:
            for nodo in tableros:
                if nodo.nombre == seleccionado:
                    generar_graphiz(nodo)  # Pasamos el tablero seleccionado como argumento
                    root.destroy()  # Destruir la ventana principal después de generar el archivo
                    break  # Terminar el bucle una vez que se haya encontrado el tablero seleccionado
            else:
                tk.messagebox.showerror("Error", f"No se encontró ningún tablero con el nombre '{seleccionado}'")

    root = tk.Tk()
    root.title("Seleccionar tablero")

    # Centrar la ventana principal
    window_width = 450  # Ancho de la ventana
    window_height = 350  # Altura de la ventana
    screen_width = root.winfo_screenwidth()  # Ancho de la pantalla
    screen_height = root.winfo_screenheight()  # Altura de la pantalla
    x_coordinate = (screen_width - window_width) // 2  # Coordenada x para centrar la ventana
    y_coordinate = (screen_height - window_height) // 2  # Coordenada y para centrar la ventana
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # Establecer la geometría de la ventana

    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)  # Expandir el Frame para llenar la ventana

    tk.Label(frame, text="Maquetas disponibles:").pack()

    # Obtener los nombres de las maquetas y ordenarlos alfabéticamente
    nombres_maquetas = [nodo.nombre for nodo in tableros]
    nombres_maquetas.sort()

    text_maquetas = tk.Text(frame, height=10, width=30)
    text_maquetas.pack()
    for nombre in nombres_maquetas:
        text_maquetas.insert(tk.END, nombre + "\n")

    tk.Label(frame, text="Ingrese el nombre del tablero a graficar:").pack()

    entrada_nombre = tk.Entry(frame)
    entrada_nombre.pack()

    style = ttk.Style()
    style.configure("Modern.TButton", foreground="black", background="blue", font=("Helvetica", 12, "bold"))
    #icono_grablab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/mostrar_lab.png')
    btn_graficar = ttk.Button(frame, text="Mostrar", cursor='hand2', compound=tk.LEFT, style="Modern.TButton", command=generar_tablero_seleccionado)
    btn_graficar.pack(pady=20)

    root.mainloop()

def generar_graphiz(tablero):
    dot_code = f'digraph {tablero.nombre} ' + '{\n'
    dot_code += '    subgraph cluster_' + tablero.nombre + ' {\n'
    dot_code += '        label="' + tablero.nombre + '"\n'
    dot_code += '        node [shape=plaintext style=filled]\n'
    dot_code += '        struct [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">\n'  # Cambio CELLBORDER a 0

    # Recorrer la estructura del tablero y agregar los objetos
    for fila in range(tablero.filas):
        dot_code += '            <TR>'
        for columna in range(tablero.columnas):
            posicion = fila * tablero.columnas + columna
            if (fila, columna) == tablero.entrada:
                dot_code += f'<TD bgcolor="green" fontcolor="white"></TD>'
            else:
                objeto_encontrado = False
                current_objeto = tablero.objetos.head
                while current_objeto:
                    if (fila, columna) == (current_objeto.fila, current_objeto.columna):
                        dot_code += f'<TD bgcolor="orange" fontcolor="black">{current_objeto.nombre}</TD>'
                        objeto_encontrado = True
                        break
                    current_objeto = current_objeto.siguiente

                if not objeto_encontrado:
                    if tablero.estructura[posicion] == '*':
                        dot_code += f'<TD bgcolor="black" fontcolor="white">{tablero.estructura[posicion]}</TD>'
                    else:
                        dot_code += '<TD></TD>'
        dot_code += '</TR>\n'

    dot_code += '        </TABLE>>]\n'
    dot_code += '    }\n'
    dot_code += "}\n"

    dot_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tablero.dot"
    png_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tablero.png"

    with open(dot_file_path, "w") as f:
        f.write(dot_code)

    try:
        graphviz.render('dot', 'png', dot_file_path)
        print(f"Se ha generado el archivo '{png_file_path}' del tablero seleccionado.")
    except Exception as e:
        print("Error al generar el archivo PNG:", e)

def mostrar_tableros_solucion():
    mostrar_tableros_ordenados_solucion(tableros)

def mostrar_tableros_ordenados_solucion(tableros):
    if not tableros:
        tk.messagebox.showerror("Error", "No se ha cargado ningún tablero previamente.")
        return

    def generar_tablero_seleccionado_solucion(): 
        seleccionado = entrada_nombre.get().strip()  # Obtener el nombre ingresado y eliminar espacios en blanco al inicio y al final
        if seleccionado:
            for nodo in tableros:
                if nodo.nombre == seleccionado:
                    camino = generar_camino(nodo)
                    generar_graphiz_solucion(nodo, camino)  # Corregir aquí, pasar también el camino encontrado
                    root.destroy()
                    break
            else:
                tk.messagebox.showerror("Error", f"No se encontró ningún tablero con el nombre '{seleccionado}'")

    root = tk.Tk()
    root.title("Seleccionar tablero")

    # Centrar la ventana principal
    window_width = 450  # Ancho de la ventana
    window_height = 350  # Altura de la ventana
    screen_width = root.winfo_screenwidth()  # Ancho de la pantalla
    screen_height = root.winfo_screenheight()  # Altura de la pantalla
    x_coordinate = (screen_width - window_width) // 2  # Coordenada x para centrar la ventana
    y_coordinate = (screen_height - window_height) // 2  # Coordenada y para centrar la ventana
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # Establecer la geometría de la ventana

    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)  # Expandir el Frame para llenar la ventana

    tk.Label(frame, text="Maquetas disponibles:").pack()

    # Obtener los nombres de las maquetas y ordenarlos alfabéticamente
    nombres_maquetas = [nodo.nombre for nodo in tableros]
    nombres_maquetas.sort()

    text_maquetas = tk.Text(frame, height=10, width=30)
    text_maquetas.pack()
    for nombre in nombres_maquetas:
        text_maquetas.insert(tk.END, nombre + "\n")

    tk.Label(frame, text="Ingrese el nombre del tablero a graficar:").pack()

    entrada_nombre = tk.Entry(frame)
    entrada_nombre.pack()

    style = ttk.Style()
    style.configure("Modern.TButton", foreground="black", background="blue", font=("Helvetica", 12, "bold"))
    icono_grablab = tk.PhotoImage(file='C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/Imagenes/mostrar_lab.png')
    btn_graficar = ttk.Button(frame, text="Solucion", cursor='hand2', compound=tk.LEFT, style="Modern.TButton", command=generar_tablero_seleccionado_solucion)
    btn_graficar.pack(pady=20)

    root.mainloop()

def generar_camino(tablero):
    mejor_camino = CaminoLinkedList()

    def dfs(fila, columna, actual, visitados, objetos_restantes):
        nonlocal mejor_camino

        if not objetos_restantes:
            if len(actual) < len(mejor_camino) or not mejor_camino:
                mejor_camino = actual.copy()  # Hacer una copia del camino actual
            return

        movimientos = MovimientoLinkedList()
        movimientos.append((fila - 1, columna))
        movimientos.append((fila + 1, columna))
        movimientos.append((fila, columna - 1))
        movimientos.append((fila, columna + 1))

        for movimiento in movimientos:
            nueva_fila, nueva_columna = movimiento
            if 0 <= nueva_fila < tablero.filas and 0 <= nueva_columna < tablero.columnas \
                    and tablero.estructura[nueva_fila * tablero.columnas + nueva_columna] == '-':
                visitado = False
                current = visitados.head
                while current:
                    if current.value == (nueva_fila, nueva_columna):
                        visitado = True
                        break
                    current = current.next

                if not visitado:
                    nuevos_objetos_restantes = objetos_restantes.copy()
                    objeto_actual = buscar_objeto(tablero.objetos, nueva_fila, nueva_columna)
                    if objeto_actual and objeto_actual in nuevos_objetos_restantes:
                        nuevos_objetos_restantes.remove(objeto_actual)
                    actual.append(nueva_fila, nueva_columna)
                    visitados.append((nueva_fila, nueva_columna))
                    dfs(nueva_fila, nueva_columna, actual, visitados, nuevos_objetos_restantes)
                    actual.pop()
                    visitados.pop()

    entrada_fila, entrada_columna = tablero.entrada
    dfs(entrada_fila, entrada_columna, CaminoLinkedList(), LinkedoList(), set(tablero.objetos))

    return mejor_camino

def buscar_objeto(lista, fila, columna):
    for current in lista:
        if current.fila == fila and current.columna == columna:
            return current
    return None

def generar_graphiz_solucion(tablero, camino):
    dot_code = f'digraph {tablero.nombre} ' + '{\n'
    dot_code += '    subgraph cluster_' + tablero.nombre + ' {\n'
    dot_code += '        label="' + tablero.nombre + '"\n'
    dot_code += '        node [shape=plaintext style=filled]\n'
    dot_code += '        struct [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">\n'  # Cambio CELLBORDER a 0

    # Recorrer la estructura del tablero y agregar los objetos
    for fila in range(tablero.filas):
        dot_code += '            <TR>'
        for columna in range(tablero.columnas):
            posicion = fila * tablero.columnas + columna
            if (fila, columna) == tablero.entrada:
                dot_code += f'<TD bgcolor="green"></TD>'
            elif (fila, columna) in camino:
                dot_code += f'<TD bgcolor="blue"></TD>'
            else:
                objeto_encontrado = False
                current_objeto = tablero.objetos.head
                while current_objeto:
                    if (fila, columna) == (current_objeto.fila, current_objeto.columna):
                        dot_code += f'<TD bgcolor="orange">{current_objeto.nombre}</TD>'
                        objeto_encontrado = True
                        break
                    current_objeto = current_objeto.siguiente

                if not objeto_encontrado:
                    if tablero.estructura[posicion] == '*':
                        dot_code += f'<TD bgcolor="black">{tablero.estructura[posicion]}</TD>'
                    else:
                        dot_code += '<TD></TD>'
        dot_code += '</TR>\n'

    dot_code += '        </TABLE>>]\n'
    dot_code += '    }\n'
    dot_code += "}\n"

    dot_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tablero_solucion.dot"
    png_file_path = "C:/Users/danis/OneDrive/Documents/Quinto Semestre/IPC2/[IPC2]Proyecto2_202202768/tablero_solucion.png"

    with open(dot_file_path, "w") as f:
        f.write(dot_code)

    try:
        graphviz.render('dot', 'png', dot_file_path)
        print(f"Se ha generado el archivo '{png_file_path}' del tablero seleccionado.")
    except Exception as e:
        print("Error al generar el archivo PNG:", e)

def ayuda():
    wina = tk.Tk()
    wina.title('Menu Principal')
    # Crea los textos dentro del nuevo frame
    label_nombre = tk.Label(wina, text="Nombre: Daniel Estuardo Salvatierra Macajola")
    label_nombre.pack()
    label_carnet = tk.Label(wina, text="carnet: 202202768")
    label_carnet.pack()
    label_link = tk.Label(wina, text="link: https://github.com/DanielEstuardo48/IPC2_Proyecto2_202202768/tree/main")
    label_link.pack()

# Inicialización de variables globales
tableros = None
tablero_seleccionado = None

