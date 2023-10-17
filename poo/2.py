class Rectangle:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

rectangulo = Rectangle(longitud, ancho)
area = rectangulo.calcular_area()
print(f"El área del rectángulo es: {area}")
