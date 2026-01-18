# SUPER CLASE O CLASE PADRE
class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre # atributo privado Encapsulación

    def get_nombre(self): # getter para obtener información
        return self.__nombre

    def presentacion(self): # Polimorfismo sobreescritura
        return "Soy un estudiante"


# SUBCLASE O CLASE HIJA
class EstudianteUniversitario(Estudiante):
    def __init__(self, nombre, carrera):
        super().__init__(nombre) # Herencia
        self.carrera = carrera

    def presentacion(self): # Polimorfismo sobreescritura
        return f"Soy {self.get_nombre()} y estudio {self.carrera}"


est1 = Estudiante("Mery")
est2 = EstudianteUniversitario("Jairo", "Ingeniería Mecánica")

print(est1.presentacion())
print(est2.presentacion())

