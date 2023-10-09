numero_llantas = int(input("Ingrese el número de llantas compradas: "))

precio_unidad_menos_6 = 240000
precio_unidad_6_7 = 221000
precio_unidad_mas_7 = 180000

if numero_llantas < 6:
    valor_total = numero_llantas * precio_unidad_menos_6
elif 6 <= numero_llantas <= 7:
    valor_total = numero_llantas * precio_unidad_6_7
else:
    valor_total = numero_llantas * precio_unidad_mas_7

print("El valor total a pagar es: $", valor_total)
