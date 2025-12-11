"""
Pide al usuario un número n e imprime su factorial usando un ciclo for.
"""

N = int(input("Introduzca un numero "))
fact = 1

for i in range (1,N+1):
    fact *= i

print(f"El factorial de {N}! es: {fact}")