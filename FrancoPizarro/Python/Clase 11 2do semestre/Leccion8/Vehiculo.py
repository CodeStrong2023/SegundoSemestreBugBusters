'''
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas Auto y bicicleta, las cuales
    heredan de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y métodos:
    
    Vehiculo (clase padre)
    -Atributos(Color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())
    
    Auto(Clase hija de Vehiculo)
    -Atributos(velocidad (km/h))
    -Métodos(__init__(color, ruedas, velocidad) y __str__())
    
    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Métodos(__init__(color, ruedas, tipo) y __str__()
    
    Crear un objeto de cada clase
'''
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: '+self.color+', Ruedas: '+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(km/h): '+str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo

# Primer objeto de la clase vehiculo padre
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto, de la clase auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# Tercer objeto, el ultimo de la clase Bicicleta
bici = Bicicleta('Azul', 2, 'urbana')
print(bici)
