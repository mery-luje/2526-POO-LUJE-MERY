class TemperaturasCiudades:
    def __init__(self):
        self.ciudades = ["Latacunga", 'Quito']
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves",
                     "Viernes", "Sabado", "Domingo"]
        self.semanas = ["Semana 1", "Semana 2"]

        # Matriz tridimensional: [ciudad][semana][día]
        self.temperaturas = [
            [  # Latacunga
                [19.2, 21.7, 19.8, 24.3, 22.1, 18.6, 23.5],
                [18.9, 24.6, 23.9, 18.4, 21.2, 19.7, 25.8]
            ],
            {  # Quito
                [23.2, 19.7, 25.8, 19.3, 23.1, 21.6, 20.5],
                [19.9, 22.6, 22.9, 21.4, 20.2, 24.7, 21.8]
            }
        ]

    def calcular_promedios(self):
        for ciudad in range(len(self.ciudades)):
            print("Ciudad:", self.ciudades[ciudad])

            for semana in range(len(self.temperaturas[ciudad])):
                suma = sum(self.temperaturas[ciudad][semana])
                promedio = suma / len(self.temperaturas[ciudad][semana])

                print(f"{self.semanas[semana]}: "
                      f"Promedio = {promedio:.2f} grados centígrados")

            print()


# Programa principal
if __name__ == "__main__":
    temperaturas = TemperaturasCiudades()
    temperaturas.calcular_promedios()


