def imprimir_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

entrada = input("Ingrese una lista de números separados por comas: ")

lista_ingresada = [int(numero) for numero in entrada.split(',')]

print("Números pares en la lista:")
imprimir_pares(lista_ingresada)
