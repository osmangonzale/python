class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def tiene_restriccion_pico_y_placa(self, dia):
        restriccion_por_dia = {
            1: [0, 1],
            2: [2, 3],
            3: [4, 5],
            4: [6, 7],
            5: [8, 9]
        }

        ultimo_digito_placa = int(self.placa[-1])

        if dia in restriccion_por_dia and ultimo_digito_placa in restriccion_por_dia[dia]:
            return True
        else:
            return False

placa_vehiculo = input("Ingrese la placa del vehículo (sin guiones ni espacios): ")
dia_actual = int(input("Ingrese el día actual (1-5): "))

vehiculo = Vehiculo(placa_vehiculo)
tiene_restriccion = vehiculo.tiene_restriccion_pico_y_placa(dia_actual)

if tiene_restriccion:
    print("El vehículo tiene restricción por pico y placa hoy en Bogotá.")
else:
    print("El vehículo no tiene restricción por pico y placa hoy en Bogotá.")
