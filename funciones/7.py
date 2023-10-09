def esta_en_rango(numero, rango_inicio, rango_fin):
    return numero >= rango_inicio and numero <= rango_fin

numero = int(input("Ingrese un número: "))
rango_inicio = int(input("Ingrese el inicio del rango: "))
rango_fin = int(input("Ingrese el fin del rango: "))

if esta_en_rango(numero, rango_inicio, rango_fin):
    print(f"{numero} está en el rango [{rango_inicio}, {rango_fin}]")
else:
    print(f"{numero} no está en el rango [{rango_inicio}, {rango_fin}]")
