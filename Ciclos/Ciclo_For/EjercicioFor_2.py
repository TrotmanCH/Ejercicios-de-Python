"""
Pide al usuario un número N e imprime la suma de todos los números del 1 al N.
"""
numero = int(input("Introduzca su numero "))
suma = 0

for i in range (1, numero + 1):
    suma += i

print(f"La suma de la secuencia es de {suma}")


