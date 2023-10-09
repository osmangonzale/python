numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

numeros = [numero1, numero2, numero3]

print("Números en orden ascendente:", sorted(numeros))

print("Números en orden descendente:", sorted(numeros, reverse=True))
