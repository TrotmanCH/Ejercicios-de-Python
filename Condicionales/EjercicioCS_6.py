"""
Crea un programa que:

Pida al usuario que ingrese un número entero.

Determine si el número es positivo, negativo o cero.

Imprima un mensaje indicando si el número es positivo, negativo o cero.
"""
numero = int(input("Ingrese un numero entero "))

if numero > 0: 
    print("El numero es positivo")
elif numero < 0: 
    print("El numero es negativo")
else:
    print("El numero es cero")
    