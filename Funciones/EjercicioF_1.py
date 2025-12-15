"""
Función suma de números pares. Crea una función que reciba una lista de números 
y devuelva la suma de todos los números pares.
"""

def sum(*numeros):
    contador = 0
    for i in numeros:
        if i % 2 == 0:
             contador += i
    return contador
suma = sum(1,2,3,4,6)
print(suma)