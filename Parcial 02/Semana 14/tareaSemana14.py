# AGENDA PERSONAL -------------------

# Importación de librerías
import tkinter as tk  # Librería principal para una interfaz gráfica
from tkinter import ttk, messagebox  # ttk para diseño moderno, messagebox para alertas
from datetime import datetime  # Para validar fechas y horas

# Intentar importar DatePicker (calendario)
try:
    from tkcalendar import DateEntry
    datepicker_disponible = True  # Si se instala de forma correcta
except:
    datepicker_disponible = False  # Si no está instalada

# VENTANA PRINCIPAL ---------------------------------------

root = tk.Tk()  # Crear ventana
root.title("AGENDA PERSONAL")  # Título
root.geometry("800x600")  # Tamaño de la ventana
root.configure(bg="#f5ff7a")  # Color de fondo

# ESTILO VISUAL -------------------------------------------
style = ttk.Style()
style.theme_use("clam")  # Tema moderno
style.configure("TLabel", background="#f5f7fa", font=("Segoe UI", 10)) # estilo de etiquetas
style.configure("TFrame", background="#f5f7fa") # estilo de frames
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6) # estilo de botones
style.configure("Treeview", font=("Segoe UI", 10), rowheight=28) # estilo de tabla
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

# TÍTULO PRINCIPAL -----------------------------------------------
titulo = tk.Label(root, text="AGENDA PERSONAL",
                  font=("Segoe UI", 16, "bold"),
                  bg="#f5f7fa", fg="#2c3e50")
titulo.pack(pady=10)

# FRAME DE ENTRADA DE DATOS --------------------------------------
frame_inputs = ttk.LabelFrame(root, text=" Ingresar nuevo evento ")
frame_inputs.pack(fill="x", padx=15, pady=10)

label_fecha = ttk.Label(frame_inputs, text="Fecha:") # etiqueta para ingresar fecha
label_hora = ttk.Label(frame_inputs, text="Hora:") # etiqueta para ingresar hora:minutos
label_desc = ttk.Label(frame_inputs, text="Descripción:")  # etiqueta para ingresar la descripción

label_fecha.grid(row=0, column=0, padx=10, pady=5)
label_hora.grid(row=0, column=1, padx=10, pady=5)
label_desc.grid(row=0, column=2, padx=10, pady=5)

if datepicker_disponible:
    entry_fecha = DateEntry(frame_inputs, date_pattern="dd/mm/yyyy")  # entrada de datos por calendario
else:
    entry_fecha = ttk.Entry(frame_inputs)  # entrada de datos manual

entry_hora = ttk.Entry(frame_inputs)
entry_desc = ttk.Entry(frame_inputs, width=30)

entry_fecha.grid(row=1, column=0, padx=10, pady=5)
entry_hora.grid(row=1, column=1, padx=10, pady=5)
entry_desc.grid(row=1, column=2, padx=10, pady=5)

# FRAME DE VISUALIZACIÓN DE TABLA ---------------------------------------

frame_list = ttk.LabelFrame(root, text=" Lista de eventos ")
frame_list.pack(fill="both", expand=True, padx=15, pady=5)

columns = ("Fecha", "Hora", "Descripción") # Crear tabka con columnas
tree = ttk.Treeview(frame_list, columns=columns, show="headings")

for col in columns: # configuración del encabezado
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.tag_configure("par", background="#ecf0f4") # colores para mejor visulaización
tree.tag_configure("impar", background="#ffffff")

scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=tree.yview) # barra lateral
tree.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# FRAME DE BOTONES ----------------------------------------------------------------
frame_buttons = ttk.Frame(root)
frame_buttons.pack(fill="x", pady=15)

# FUNCIONES ----------------------------------------------------------------------
contador_filas = 0  # Para alternar colores

def agregar_evento(): # función para agragar evento
    global contador_filas

    fecha = entry_fecha.get() #obtener datos
    hora = entry_hora.get()
    desc = entry_desc.get()

    # Validar fecha y hora
    try:
        datetime.strptime(fecha, "%d/%m/%Y") # valida formato fecha
        datetime.strptime(hora, "%H:%M") # valida formato hora
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha u hora incorrecto") # error si no ingresa formato correcto
        return

    if desc.strip() == "":
        messagebox.showwarning("Advertencia", "Debe ingresar una descripción") # valida descripción
        return

    tag = "par" if contador_filas % 2 == 0 else "impar"
    tree.insert("", "end", values=(fecha, hora, desc), tags=(tag,))
    contador_filas += 1

    if not datepicker_disponible: # limpiar campos
        entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def eliminar_evento(): # función para limpiar eventos
    seleccion = tree.selection()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un evento")
        return

    confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")

    if confirmacion:
        tree.delete(seleccion)

def salir(): # función para salir
    root.quit()

# BOTONES ---------------------------------------------------------------------------------------
btn_agregar = ttk.Button(frame_buttons, text="➕ Agregar", command=agregar_evento) # click agrega el evento
btn_eliminar = ttk.Button(frame_buttons, text="🗑 Eliminar", command=eliminar_evento) # click elimina evento
btn_salir = ttk.Button(frame_buttons, text="❌ Salir", command=salir) # click salir del evento

btn_agregar.grid(row=0, column=0, padx=15)
btn_eliminar.grid(row=0, column=1, padx=15)
btn_salir.grid(row=0, column=2, padx=15)

# EJECUCIÓN DEL PROGRAMA ------------------------------------------------------------------------

root.mainloop()  # Mantiene la ventana abierta