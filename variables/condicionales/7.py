def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def fahrenheit_a_rankine(fahrenheit):
    return fahrenheit + 459.67

def fahrenheit_a_reaumur(fahrenheit):
    return (fahrenheit - 32) * 4/9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def celsius_a_rankine(celsius):
    return (celsius + 273.15) * 9/5

def celsius_a_reaumur(celsius):
    return celsius * 4/5

def kelvin_a_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_rankine(kelvin):
    return kelvin * 1.8

def kelvin_a_reaumur(kelvin):
    return (kelvin - 273.15) * 4/5

def rankine_a_fahrenheit(rankine):
    return rankine - 459.67

def rankine_a_celsius(rankine):
    return (rankine - 491.67) * 5/9

def rankine_a_kelvin(rankine):
    return rankine * 5/9

def rankine_a_reaumur(rankine):
    return (rankine - 491.67) * 4/9

def reaumur_a_fahrenheit(reaumur):
    return (reaumur * 9/4) + 32

def reaumur_a_celsius(reaumur):
    return reaumur * 5/4

def reaumur_a_kelvin(reaumur):
    return (reaumur * 5/4) + 273.15

def reaumur_a_rankine(reaumur):
    return (reaumur * 9/4) + 491.67

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Convertir de Fahrenheit")
    print("2. Convertir de Celsius")
    print("3. Convertir de Kelvin")
    print("4. Convertir de Rankine")
    print("5. Convertir de Réaumur")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 6:
        print("¡Hasta luego!")
        break

    if opcion < 1 or opcion > 5:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue

    valor = float(input("Ingrese el valor de temperatura: "))

    if opcion == 1:
        print("Fahrenheit a Celsius:", fahrenheit_a_celsius(valor))
        print("Fahrenheit a Kelvin:", fahrenheit_a_kelvin(valor))
        print("Fahrenheit a Rankine:", fahrenheit_a_rankine(valor))
        print("Fahrenheit a Réaumur:", fahrenheit_a_reaumur(valor))
    elif opcion == 2:
        print("Celsius a Fahrenheit:", celsius_a_fahrenheit(valor))
        print("Celsius a Kelvin:", celsius_a_kelvin(valor))
        print("Celsius a Rankine:", celsius_a_rankine(valor))
        print("Celsius a Réaumur:", celsius_a_reaumur(valor))
    elif opcion == 3:
        print("Kelvin a Fahrenheit:", kelvin_a_fahrenheit(valor))
        print("Kelvin a Celsius:", kelvin_a_celsius(valor))
        print("Kelvin a Rankine:", kelvin_a_rankine(valor))
        print("Kelvin a Réaumur:", kelvin_a_reaumur(valor))
    elif opcion == 4:
        print("Rankine a Fahrenheit:", rankine_a_fahrenheit(valor))
        print("Rankine a Celsius:", rankine_a_celsius(valor))
        print("Rankine a Kelvin:", rankine_a_kelvin(valor))
        print("Rankine a Réaumur:", rankine_a_reaumur(valor))
    elif opcion == 5:
        print("Réaumur a Fahrenheit:", reaumur_a_fahrenheit(valor))
        print("Réaumur a Celsius:", reaumur_a_celsius(valor))
        print("Réaumur a Kelvin:", reaumur_a_kelvin(valor))
        print("Réaumur a Rankine:", reaumur_a_rankine(valor))
