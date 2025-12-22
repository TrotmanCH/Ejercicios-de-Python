"""
Crea un programa que:

Pida al usuario que ingrese un número entero.

Determine si el número es par o impar.

Imprima un mensaje indicando si el número es par o impar.
"""
numero = int(input("Introduzca un numero entero "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else: 
    print(f"El numero {numero} es impar")