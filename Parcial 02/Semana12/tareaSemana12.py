# CLASE LIBRO -----------------------------------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para almacenar título y autor (no cambian)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Indica si el libro está disponible

    def mostrar_info(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# CLASE USUARIO -----------------------------------------------------
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def mostrar_libros(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return [libro.info[0] for libro in self.libros_prestados]

# ClASE BIBLIOTECA -------------------------------------------------
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros por ISBN
        self.libros = {}

        # Diccionario para usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    # Añadir libro ------------------------------------------------
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente.")

    # Quitar libro ------------------------------------------------
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario -------------------------------------------
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print("Usuario registrado.")
        else:
            print("El ID ya existe.")

    # Dar de baja usuario -----------------------------------------
    def eliminar_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro ------------------------------------------------
    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]

            if libro.disponible:
                usuario.prestar_libro(libro)
                libro.disponible = False
                print("Libro prestado correctamente.")
            else:
                print("El libro no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver libro ----------------------------------------------
    def devolver_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]

            usuario.devolver_libro(libro)
            libro.disponible = True
            print("Libro devuelto.")

    # Buscar libros -----------------------------------------------
    def buscar_libros(self, criterio):
        resultados = []

        for libro in self.libros.values():
            if (criterio.lower() in libro.info[0].lower() or
                criterio.lower() in libro.info[1].lower() or
                criterio.lower() in libro.categoria.lower()):
                resultados.append(libro.mostrar_info())

        return resultados


# -----------------------------
# PRUEBAS DEL SISTEMA
# -----------------------------

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Algebra de Baldor", "Dr.Aurelio Baldor", "Ciencias", "593005001")
libro2 = Libro("Hoy es el tiempo...los hijos no esperan...", "Giovanny Izquierdo", "Novela", "593005002")
libro3 = Libro("Administración de la Calidad", "Donna Summers", "Finanzas", "593005003")
libro4 = Libro("Interchange 3B", "Jack Richards", "Idiomas", "593005043")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
biblioteca.añadir_libro(libro4)

# Crear usuarios
usuario1 = Usuario("Joel", 1)
usuario2 = Usuario("Jairo", 2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("593005001", 1)
biblioteca.prestar_libro("533005002", 2)

# Mostrar libros prestados
print("Libros de Joel:", usuario1.mostrar_libros())
print("Libros de Jairo:", usuario2.mostrar_libros())

# Devolver libro
biblioteca.devolver_libro("593005001", 1)

# Buscar libro
print("Búsqueda:", biblioteca.buscar_libros("Python"))