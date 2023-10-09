salario_diario = float(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))

salario_bruto = salario_diario * dias_trabajados

descuento_pension = salario_bruto * 0.10

descuento_salud = salario_bruto * 0.15

salario_neto = salario_bruto - descuento_pension - descuento_salud

print("Salario bruto antes de descuentos:", salario_bruto)
print("Descuento por pensión (10%):", descuento_pension)
print("Descuento por salud (15%):", descuento_salud)
print("Salario neto a pagar:", salario_neto)
