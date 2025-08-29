import random

# Generar dos números aleatorios entre 1 y 100
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Sumar los números
suma = num1 + num2

print(f"Los números generados son: {num1} y {num2}")
print(f"La suma es: {suma}")


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"


def potencia(a, b):
    return a**b


print(f"La resta es: {resta(num1, num2)}")
print(f"La multiplicación es: {multiplicacion(num1, num2)}")
print(f"La división es: {division(num1, num2)}")
print(f"La potencia es: {potencia(num1, num2)}")
