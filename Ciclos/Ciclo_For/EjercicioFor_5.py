"""
Pide al usuario una palabra y cuenta cuántas veces aparece la letra 'a'.
"""
palabra = input("Introduzca una palabra ")
suma = 0
for i in palabra:
    if i.lower() == "a":
        suma += 1



print(f"La letra A se repite {suma} veces")