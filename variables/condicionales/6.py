import math

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", area)

def calcular_area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print("El área del rectángulo es:", area)

def calcular_area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * altura
    print("El área del triángulo es:", area)

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)

def calcular_area_rombo():
    diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print("El área del rombo es:", area)

def calcular_area_trapecio():
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = ((base_mayor + base_menor) * altura) / 2
    print("El área del trapecio es:", area)

while True:
    print("Menú de opciones:")
    print("1. Calcular área de cuadrado")
    print("2. Calcular área de rectángulo")
    print("3. Calcular área de triángulo")
    print("4. Calcular área de círculo")
    print("5. Calcular área de rombo")
    print("6. Calcular área de trapecio")
    print("7. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        calcular_area_cuadrado()
    elif opcion == 2:
        calcular_area_rectangulo()
    elif opcion == 3:
        calcular_area_triangulo()
    elif opcion == 4:
        calcular_area_circulo()
    elif opcion == 5:
        calcular_area_rombo()
    elif opcion == 6:
        calcular_area_trapecio()
    elif opcion == 7:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
