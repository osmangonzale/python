n = int(input("Ingrese el número de filas del triángulo: "))

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)
