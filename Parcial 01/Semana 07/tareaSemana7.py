class ReservaViaje:
    def __init__(self, nombre_pasajero, destino): # Constructor, se ejecuta de forma automática.

        self.nombre_pasajero = nombre_pasajero
        self.destino = destino
        print(f"Reserva creada para {self.nombre_pasajero} con destino a {self.destino}.")

    def mostrar_reserva(self): # Personalizado para mostrar información de la resreva.

        print(f"Pasajero: {self.nombre_pasajero} | Destino: {self.destino}")

    def __del__(self): # Destructor, se cuando el objeto es eliminado o cuando el programa finaliza.

        print(f"La reserva de {self.nombre_pasajero} hacia {self.destino} ha sido cancelada.")

# Creación del objeto (aquí se activa el constructor __init__)
reserva1 = ReservaViaje("Joel Cardenas", "Brasil")
reserva2 = ReservaViaje ("Jairo Parreño", "Londres")
reserva3 = ReservaViaje ("Mery Luje", "Argentina")

# Uso del objeto
reserva1.mostrar_reserva()
reserva2.mostrar_reserva()
reserva3.mostrar_reserva()

# Eliminación del objeto (aquí se activa el destructor __del__)
del reserva1
del reserva2
del reserva3
