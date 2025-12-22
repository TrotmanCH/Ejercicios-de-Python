"""
Crea un programa que:

Pida al usuario que ingrese dos números.

Determine cuál de los dos números es mayor.

Imprima un mensaje indicando cuál número es mayor o si ambos son iguales.
"""

numero1 = int(input("Introduzca un numero entero "))
numero2 = int(input("Introduzca otro numero "))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}")
else:
    print(f"{numero1} ambos son iguales {numero2}")