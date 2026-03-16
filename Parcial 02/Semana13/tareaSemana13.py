import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Lista de Datos")
ventana.geometry("400x300")

# -------- FUNCIONES --------

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada_texto.get()

    if dato != "":
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# -------- COMPONENTES --------

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista donde se mostrarán los datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()