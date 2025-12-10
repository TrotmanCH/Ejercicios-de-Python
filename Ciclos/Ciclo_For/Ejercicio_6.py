"""
Pide un número N e imprime todos los números pares desde 2 hasta N.
"""
numero = int(input("Introduzca un numero "))

for i in range (1,numero + 1):
    if i % 2 == 0:
     print(f"{i}")

