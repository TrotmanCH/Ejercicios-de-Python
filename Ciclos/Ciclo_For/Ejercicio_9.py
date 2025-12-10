"""
Crea una lista de los cuadrados de los números del 1 al 10 usando un ciclo for.
"""
cuadrado = []

for i in range (1,11):
    cuadrado.append(i ** 2)
    print(f"El cuadrado de {i} es {i ** 2}")

print(f"Lista de cuadrados, {cuadrado}")