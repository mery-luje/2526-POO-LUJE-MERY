class RegistroClimatico:
    def __init__(self, ciudades, temperaturas):
        # Encapsulamiento (atributos protegidos)
        self._ciudades = ciudades
        self._temperaturas = temperaturas

    def calcular_promedio(self, datos):
        return sum(datos) / len(datos)

    # Polimorfismo: método a sobrescribir
    def mostrar_resultados(self):
        pass


class TemperaturasCiudades(RegistroClimatico):
    def __init__(self):
        ciudades = ["Latacunga", "Quito"]
        temperaturas = [
            [  # Latacunga
                [19.2, 21.7, 19.8, 24.3, 22.1, 18.6, 23.5],
                [18.9, 24.6, 23.9, 18.4, 21.2, 19.7, 25.8]
            ],
            [  # Quito
                [23.2, 19.7, 25.8, 19.3, 23.1, 21.6, 20.5],
                [19.9, 22.6, 22.9, 21.4, 20.2, 24.7, 21.8]
            ]
        ]
        super().__init__(ciudades, temperaturas)
        self._semanas = ["Semana 1", "Semana 2"]

    # Polimorfismo aplicado
    def mostrar_resultados(self):
        for i, ciudad in enumerate(self._ciudades):
            print(f"Ciudad: {ciudad}")
            for j, semana in enumerate(self._temperaturas[i]):
                promedio = self.calcular_promedio(semana)
                print(f"{self._semanas[j]}: Promedio = {promedio:.2f} °C")
            print()


# Programa principal (equivalente al main en Java)
if __name__ == "__main__":
    reporte = TemperaturasCiudades()
    reporte.mostrar_resultados()
