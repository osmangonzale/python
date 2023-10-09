cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

descuento = 0  

if cantidad_articulos > 5 and cantidad_articulos < 10:
    descuento = 0.05  
elif cantidad_articulos >= 10:
    descuento = 0.08  

precio_unitario_con_descuento = precio_unitario_original * (1 - descuento)

valor_total_a_pagar = cantidad_articulos * precio_unitario_con_descuento

print("El valor total a pagar es: $", valor_total_a_pagar)
