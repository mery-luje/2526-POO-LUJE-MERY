import json

# CLASE PRODUCTO ========================

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    #Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    #Setters
    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    # Convierte a diccionario (guarda archivo)
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

# CLASE INVENTARIO  ===========================

class Inventario:
        def __init__(self):
            # Diccionario clave = ID,valor = objeto Producto
            self.productos = {}

        # Añadir producto
        def añadir_producto(self, producto):
            if producto.get_id() in self.productos:
                print("El producto ya existe.")
            else:
                self.productos[producto.get_id()] = producto
                print("Producto añadido correctamente.")

        # Eliminar producto
        def eliminar_producto(self, id_producto):
            if id_producto in self.productos:
                del self.productos[id_producto]
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        # Actualizar producto
        def actualizar_producto(self, id_producto, cantidad=None, precio=None):
            if id_producto in self.productos:
                if cantidad is not None:
                    self.productos[id_producto].set_cantidad(cantidad)
                if precio is not None:
                    self.productos[id_producto].set_precio(precio)
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        # Buscar pro nombre (usa lista)
        def buscar_por_nombre(self, nombre):
            resultados = []
            for producto in self.productos.values():
                if producto.get_nombre().lower() == nombre.lower():
                    resultados.append(producto)
            return resultados

        # Muestra todos los productos
        def mostrar_productos(self):
            if not self.productos:
                print("Inventario vacío.")
            else:
                for producto in self.productos.values():
                    print(f"ID: {producto.get_id()}, "
                          f"Nombre: {producto.get_nombre()}, "
                          f"Cantidad: {producto.get_cantidad()}, "
                          f"Precio: ${producto.get_precio()}")

        # Guarda en archivo
        def guardar_archivo(self, archivo):
            with open(archivo, "w") as f:
                datos = {id: prod.to_dict() for id, prod in self.productos.items()}
                json.dump(datos, f, indent=4)
            print("Inventario guardado correctamente.")

        # Carga desde el archivo
        def cargar_archivo(self, archivo):
            try:
                with open(archivo, "r") as f:
                    datos = json.load(f)
                    for id, info in datos.items():
                        producto = Producto(
                            info["id"],
                            info["nombre"],
                            info["cantidad"],
                            info["precio"]
                        )
                        self.productos[id] = producto
                print("Inventario cargado correctamente.")
            except FileNotFoundError:
                print("Archivo no encontrado. Se iniciará inventario vacío.")

# MENÚ INTERACTIVO =======================================

def menu():
    inventario = Inventario()
    inventario.cargar_archivo("inventario.json")

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")

            inventario.actualizar_producto(
                id_producto,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(f"ID: {p.get_id()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio()}")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_archivo("inventario.json")

        elif opcion == "7":
            inventario.guardar_archivo("inventario.json")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()





