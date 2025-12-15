"""
Función contar palabras. Crea una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Lo recomendable en este tipo de ejercicios es separar la palabras con la funcion split y luego contarlas con la funcion len.
"""
def conp(cadena):
    palabras = cadena.split()
    return len(palabras) 

suma = conp("Hola mundo")
print(suma) 
        