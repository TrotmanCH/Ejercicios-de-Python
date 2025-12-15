"""
Función palabras largas. Crea una función que reciba una lista de palabras
y devuelva solo las que tengan más de 5 letras.
"""

def palabra(palabras):
    newlist = []
    for i in palabras:
        if len(i) > 5:
            newlist.append(i)
    return newlist

result = palabra(["Hola", "Software", "Holass"])
print(result)
        
        