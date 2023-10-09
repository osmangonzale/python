n = int(input("Ingrese el número de niveles de la pirámide: "))

max_width = len(str(n * (n + 1) // 2))

numero_actual = 1

for i in range(1, n + 1):
    espacios = " " * (max_width - len(str(numero_actual)))
    print(espacios, end=" ")

    for j in range(i):
        print(numero_actual, end= " ")
        numero_actual += 1

    print()


