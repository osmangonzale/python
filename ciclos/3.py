def fibonacci(n):
    fibonacci_sequence = [0, 1]  

    for i in range(2, n):
        siguiente = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(siguiente)

    return fibonacci_sequence

n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea mostrar: "))

secuencia = fibonacci(n)

print("Secuencia de Fibonacci:")
for termino in secuencia:
    print(termino, end=" ")

suma = sum(secuencia)

print(f"\nLa suma de los primeros {n} términos de la secuencia de Fibonacci es: {suma}")
