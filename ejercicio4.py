# Escribir un programa que lea un entero positivo, N, introducido por el usuario
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta N.
# La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma:
# suma= n(n+1) / 2

print("Introduzca un número entero (positivo)")
N = int(input())
suma = N * (N + 1) / 2
print("La suma de todos los enteros desde 1 hasta el", N, "son:")
print(suma)
