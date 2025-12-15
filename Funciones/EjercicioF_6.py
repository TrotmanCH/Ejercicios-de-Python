"""
Función contar vocales. Crea una función que reciba una cadena y devuelva la cantidad de vocales que tiene.
"""

def contar(palabra):
    contador = 0 
    for i in palabra.lower():
        if i in "aeiou":
            contador += 1
    return contador

suma = contar("Hola Mundo")
print(f"La palabra tiene {suma} vocales ")