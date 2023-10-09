monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    tipo_pago = "Efectivo"
elif 150000 <= monto_cuenta <= 300000:
    tipo_pago = "Celular (dinero electrónico)"
elif 300000 < monto_cuenta <= 600000:
    tipo_pago = "Tarjeta de débito"
else:
    tipo_pago = "Tarjeta de crédito"

print(f"Recomendamos pagar con: {tipo_pago}")
