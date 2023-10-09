def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un número entero no negativo: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
