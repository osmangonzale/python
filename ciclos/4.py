suma = 0
contador = 0

for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero
    contador += 1

promedio = suma / contador

print(f"La suma de los 10 números es: {suma}")
print(f"El promedio de los 10 números es: {promedio}")
