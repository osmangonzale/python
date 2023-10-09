valor_unitario = float(input("Ingrese el valor unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

subtotal = valor_unitario * cantidad

iva = subtotal * 0.19

total = subtotal + iva

print("Valor total antes del IVA:", subtotal)
print("Valor del IVA (16%):", iva)
print("Valor total a pagar (incluyendo el IVA):", total)
