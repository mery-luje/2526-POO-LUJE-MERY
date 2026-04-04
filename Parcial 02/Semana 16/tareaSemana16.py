import tkinter as tk

class AppTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas --------------------------------------------------------------------------------
        self.tareas = []

        # Campo de entrada -------------------------------------------------------------------------------
        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=15)

        # Botones ----------------------------------------------------------------------------------------
        self.btn_agregar = tk.Button(root, text="Agregar tarea", command=self.agregar_tarea)
        self.btn_agregar.pack()

        self.btn_completar = tk.Button(root, text="Marcar como completada", command=self.marcar_completada)
        self.btn_completar.pack()

        self.btn_eliminar = tk.Button(root, text="Eliminar tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

        # Atajos de teclado -----------------------------------------------------------------------------
        self.root.bind("<Return>", lambda event: self.agregar_tarea())
        self.root.bind("c", lambda event: self.marcar_completada())
        self.root.bind("C", lambda event: self.marcar_completada())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("d", lambda event: self.eliminar_tarea())
        self.root.bind("D", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    # FUNCIONES PRINCIPALES ------------------------------------------------------------------------------

    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto:
            self.tareas.append({"texto": texto, "completada": False})
            self.entry.delete(0, tk.END)
            self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.tareas:
            texto = tarea["texto"]

            if tarea["completada"]:
                self.lista.insert(tk.END, "✔ " + texto)
                self.lista.itemconfig(tk.END, fg="green")
            else:
                self.lista.insert(tk.END, "✗ " + texto)
                self.lista.itemconfig(tk.END, fg="blue")


# EJECUCIÓN -----------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()