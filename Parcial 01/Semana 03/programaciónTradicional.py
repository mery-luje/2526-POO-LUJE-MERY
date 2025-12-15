# Arreglos
ciudades = ["Latacunga", "Quito"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
semanas = ["Semana 1", "Semana 2"]

# Matriz tridimensional: [ciudad][semana][día]
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

# Recorrido de la matriz
for ciudad in range(len(ciudades)):
    print("Ciudad", ciudades[ciudad])

    for semana in range(len(temperaturas[ciudad])):
        suma = 0

        for dia in range(len(temperaturas[ciudad][semana])):
            suma += temperaturas[ciudad][semana][dia]

        promedio = suma / len(temperaturas[ciudad][semana])
        print(f"Semana {semana + 1}: Promedio = {promedio:.2f} grados centígrados")

    print()
