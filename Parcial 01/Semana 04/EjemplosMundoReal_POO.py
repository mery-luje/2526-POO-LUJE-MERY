class Vestido:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def probarse (self):
        print("Modelo del vestido es perfecto")

class Persona:
    def __init__(self, nombre, talla, color):
        self.nombre = nombre
        self.talla = talla
        self.color = color

    def comprar(self):
        print(f"Hola mi nombre es {self.nombre} y compre el vestido {self.talla} de color {self.color}.")

    def pagar(self):
        print(f"mi vestido es {self.color} y es talla {self.talla}.")

mi_vestido = Vestido("Calvin Klein", "gala", "red")
persona1 = Persona("Mery", "M", "red")
persona1.comprar()
persona1.pagar()


