altura = int(input("Ingrese la altura de la letra Z: "))

for i in range(altura):
    for j in range(altura):
        if i == 0 or i == altura - 1:
            print('*', end=' ')
        elif j == altura - i - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
