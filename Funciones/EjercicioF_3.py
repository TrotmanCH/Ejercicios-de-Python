"""
Función número mayor. Crea una función que reciba una lista de números y devuelva el número mayor.
Recomendacion inicializar la variable contador con el primer numero de la lista.
"""
def num_mayor(*numeros):
    contador = numeros[0]
    for i in numeros:
        if i >= contador: 
            contador = i
    return contador

mayor = num_mayor(39,2,40,34,1)
print(mayor)