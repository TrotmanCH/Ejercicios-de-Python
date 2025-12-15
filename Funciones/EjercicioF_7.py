"""
Función promedio
Crea una función que reciba una lista de números y devuelva el promedio de todos ellos.
"""
"""
Recomendacion #1
def promedio(*lista): 
    return round(sum(lista) / len(lista), 2)

resultado = promedio(5.0,5.0,4.0)
print(resultado)
"""
def promedio(*lista):
    suma = 0 
    contador = 0 
    for i in lista:
        suma += i
        contador += 1
    prom = suma / contador
    return round(prom,2)

resultado = promedio(5,5,4)
print(f"El promedio es: {resultado}")