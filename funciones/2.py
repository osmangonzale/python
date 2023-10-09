import math

def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

print("Selecciona una figura geométrica:")
print("1. Cuadrado")
print("2. Triángulo")
print("3. Círculo")

opcion = int(input("Ingresa el número de la figura: "))

if opcion == 1:
    lado = float(input("Ingresa la longitud del lado del cuadrado: "))
    resultado = area_cuadrado(lado)
    print(f"El área del cuadrado es: {resultado}")
elif opcion == 2:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    resultado = area_triangulo(base, altura)
    print(f"El área del triángulo es: {resultado}")
elif opcion == 3:
    radio = float(input("Ingresa el radio del círculo: "))
    resultado = area_circulo(radio)
    print(f"El área del círculo es: {resultado}")
else:
    print("Opción no válida")
