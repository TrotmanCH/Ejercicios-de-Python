"""
Función eliminar duplicados. Crea una función que reciba una lista y devuelva 
una nueva lista sin elementos repetidos. La estructura set() permite guardar elementos unicos.
"""
def repetitivos(*lista):
    return list(set(lista))

resultado = repetitivos(1,2,1,2,4,5,6,3,3,6)
print(resultado)