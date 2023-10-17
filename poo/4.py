class PowerCalculator:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2

        return result

x = float(input("Ingrese la base (x): "))
n = int(input("Ingrese la potencia (n): "))

calculator = PowerCalculator()
resultado = calculator.myPow(x, n)
print(f"{x}^{n} = {resultado}")
