import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas diarias - Bajar de peso")
        self.root.geometry("500x500")

        # Campo de entrada para nuevas tareas ------------------------------------------------------------
        self.task_entry = tk.Entry(root, font=("Monotype cursiva", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        self.task_entry.focus_set()

        # Botones de acción ------------------------------------------------------------------------------
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.pack(pady=5)

        # Componente de Lista (Listbox) ------------------------------------------------------------------
        self.tasks_listbox = tk.Listbox(root, font=("Monotype cursiva", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Botones inferiores ----------------------------------------------------------------------------
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed, bg="#2196f3",
                                         fg="pink")
        self.complete_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#f44336", fg="pink")
        self.delete_button.pack(side=tk.RIGHT, padx=20, pady=10)

        # Manejo de Eventos -----------------------------------------------------------------------------

        # Evento de Teclado: Presionar Enter en el Entry para añadir ------------------------------------
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Evento de Mouse Opcional: Doble clic para completar tarea ---------------------------------------
        self.tasks_listbox.bind("<Double-Button-1>", lambda event: self.mark_completed())

    # Manejadores -----------------------------------------------------------------------------------------

    def add_task(self):
        """Añade la tarea del Entry al Listbox."""
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpia el campo después de añadir ---------------------------
        else:
            messagebox.showwarning("Atención", "Escribe algo antes de añadir.")

    def mark_completed(self):
        """Cambia el color de fondo de la tarea seleccionada."""
        try:
            index = self.tasks_listbox.curselection()[0]
            # Cambiamos el color visualmente (Estado: Completado) ----------------------------------------------
            self.tasks_listbox.itemconfig(index, fg="gray", bg="#e0e0e0")

            current_text = self.tasks_listbox.get(index)
            if "✔ " not in current_text:
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {current_text}")
                self.tasks_listbox.itemconfig(index, fg="green")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

