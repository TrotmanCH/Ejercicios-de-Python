"""
Función número repetido. Crea una función que reciba una lista de números y devuelva el número que más veces se repite.
"""
def num(numeros):
    contador = {}
    num_repetido = None
    max_repeticion = 0
    for i in numeros: 
        if i in contador:
           contador[i] += 1
        else: 
           contador[i] = 1
           
    for num, rep in contador.items():
        if rep > max_repeticion:
            max_repeticion = rep
            num_repetido = num
            
    return num_repetido

result = num([1,2,2,6,3,4,5,5,5,6,6,6])
print(result)
   