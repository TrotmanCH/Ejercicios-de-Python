"""
Contador regresivo: Pide un número y haz un conteo regresivo hasta llegar a 0. 
"""
"""
Manera #1
numero = int(input("Ingrese un numero "))

while numero >= 0:
    print(numero)
    numero -= 1
"""

"""Manera #2"""
num = int(input("ingrese un numero "))
contador = num
while contador >= 0:
    print(contador)
    contador -= 1

print("Programa terminado")
