def encontrar_maximo(num1, num2, num3):
    maximo = num1
    if num2 > maximo:
        maximo = num2
    if num3 > maximo:
        maximo = num3
    return maximo

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

maximo = encontrar_maximo(numero1, numero2, numero3)

print("El número máximo es:", maximo)
