distancia_metros = float(input("Ingrese una distancia en metros: "))

unidad = input("Ingrese la unidad a la que desea convertir (km, cm o mm): ")

if unidad == "km":
    distancia_km = distancia_metros / 1000
    print("La distancia en kilómetros es:", distancia_km, "km")
elif unidad == "cm":
    distancia_cm = distancia_metros * 100
    print("La distancia en centímetros es:", distancia_cm, "cm")
elif unidad == "mm":
    distancia_mm = distancia_metros * 1000
    print("La distancia en milímetros es:", distancia_mm, "mm")
else:
    print("Unidad no válida. Por favor, ingrese 'km', 'cm' o 'mm'.")
