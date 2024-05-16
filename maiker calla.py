import math

while True:
    operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division, seno, coseno, tangente): ")

    if operacion in ['suma', 'resta', 'multiplicacion', 'division']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            resultado = num1 / num2

    elif operacion in ['seno', 'coseno', 'tangente']:
        angulo = float(input("Ingrese el ángulo en grados: "))
        angulo_radianes = math.radians(angulo)

        if operacion == 'seno':
            resultado = math.sin(angulo_radianes)
        elif operacion == 'coseno':
            resultado = math.cos(angulo_radianes)
        elif operacion == 'tangente':
            resultado = math.tan(angulo_radianes)

    else:
        print("Operación no válida.")
        continue

    print(f"El resultado de la operación {operacion} es: {resultado}")






    