class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Vehiculo: [Color: {self.color}, Ruedas: {self.ruedas}]"


class Auto(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()} Auto: [Velocidad(km/hr): {self.velocidad}]"


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Bicicleta: [Tipo(urbana/montaña,etc): {self.tipo}]"


vehiculo1 = Vehiculo("Rojo", 4)
print(vehiculo1)

auto1 = Auto("Negro", 4, 120)
print(auto1)

bici1 = Bicicleta("Blanca", 2, "Ruta")
print(bici1)