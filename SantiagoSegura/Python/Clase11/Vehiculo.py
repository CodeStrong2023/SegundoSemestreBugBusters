class Vehiculo:
    """
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo, La clase
    padre debe tener los siguientes atributos y métodos:

    Vehiulo (clase padre)
    -Atributos(color, ruedas)
    Metodos(__init__(color, ruedas) y __str__())

    Auto (clase hija de Vehiculo)
    -Atributos(velocidad (km/hr))
    -Métodos(__init__(color, ruedas, velocidad) y __str__())

    Bicibleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Métodos(__init__(color, ruedas, tipo) y __str__()

    Crear un objeto de cada clase
    """

    class Vehiculo:
        def __init__(self, color, ruedas):
            self.color = color
            self.ruedas = ruedas

        def __str__(self):
            return f"Color: {self.color}, Ruedas: {self.ruedas}"

    class Auto(Vehiculo):
        def __init__(self, color, ruedas, velocidad):
            super().__init__(color, ruedas)
            self.velocidad = velocidad

        def __str__(self):
            return f"{super().__str__()}, Velocidad: {self.velocidad} km/hr"

    class Bicicleta(Vehiculo):
        def __init__(self, color, ruedas, tipo):
            super().__init__(color, ruedas)
            self.tipo = tipo

        def __str__(self):
            return f"{super().__str__()}, Tipo: {self.tipo}"

    # Objetos
    vehiculo = Vehiculo("Negro", 4)
    auto = Auto("Blanco", 4, 120)
    bicicleta = Bicicleta("Verde", 2, "Montaña")


    print("Info del Vehículo:")
    print(vehiculo)

    print("\nInfo del Auto:")
    print(auto)

    print("\nInfo de la Bicicleta:")
    print(bicicleta)
