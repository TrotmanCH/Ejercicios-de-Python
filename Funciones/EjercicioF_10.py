"""
Función filtrar positivos. Crea una función que reciba una lista de números 
y devuelva una nueva lista con solo los números positivos. El método append() se usa para agregar un único elemento 
al final de una lista, sin importar su tipo de dato.
"""
def positivos(numeros):
    lista = []
    for i in numeros:
        if i >= 0: 
            lista.append(i)
    return lista

result = positivos([-1,1,2,4,-1,0,-3,1,2])
print(result)
        
    