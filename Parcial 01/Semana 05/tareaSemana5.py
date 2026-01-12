"""
El programa calcula el area del rectángulo, primero solicita
el nombre del usuario, le pide el largo del rectángulo y el ancho.
Saluda al usuario, le da el área del rectángulo y le indica si el
área es grande o pequena basado en el condicional.
"""

# Función para calcular el área del rectángulo
def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo a partir de su largo y ancho.
    """
    area = largo * ancho
    return area

# Entrada de datos (string y float)
nombre_usuario = input("Ingrese su nombre: ")
largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))

# Para carcular el área (float)
area_total = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)

# Uso de booleano para evaluación del condicional

es_area_grande = area_total > 50

# Salida de resultados
print(f"\nHola {nombre_usuario}")
print(f"El área del rectángulo es: {area_total}")

# Decisión basada en un valor booleano
if es_area_grande:
    print("El área del rectángulo es grande.")
else:
    print("El área del rectángulo es pequeña.")

