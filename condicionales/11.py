precio_tamano = {
    1: 15000,
    2: 24000,
    3: 36000
}

precio_ingrediente_adicional = 4000

tamaño_pizza = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

if tamaño_pizza not in precio_tamano:
    print("Tamaño de pizza no válido.")
else:
    precio_base = precio_tamano[tamaño_pizza]

    costo_ingredientes = precio_ingrediente_adicional * ingredientes_adicionales

    precio_total = precio_base + costo_ingredientes

    print("El precio total a pagar es: $", precio_total)
