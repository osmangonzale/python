class Ave:
    def __init__(self, nombre, habitat, alimentacion):
        self.nombre = nombre
        self.habitat = habitat
        self.alimentacion = alimentacion

    def volar(self):
        print(f"{self.nombre} está volando.")

    def cantar(self):
        print(f"{self.nombre} está cantando.")

class PajaroCantor(Ave):
    def __init__(self, nombre, habitat, alimentacion, canto):
        super().__init__(nombre, habitat, alimentacion)
        self.canto = canto

    def cantar(self):
        print(f"{self.nombre} está cantando {self.canto}.")

class Aguilas(Ave):
    def __init__(self, nombre, habitat, alimentacion, velocidad_vuelo):
        super().__init__(nombre, habitat, alimentacion)
        self.velocidad_vuelo = velocidad_vuelo

    def volar(self):
        print(f"{self.nombre} está volando a una velocidad de {self.velocidad_vuelo} km/h.")

pajaro = PajaroCantor("Canario", "Bosque", "Semillas", "una melodía alegre")
aguila = Aguilas("Águila Calva", "Montañas", "Peces", 120)

pajaro.volar()
pajaro.cantar()

aguila.volar()
