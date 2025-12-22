"""
Crea un programa que:

Pida al usuario que ingrese dos cadenas de texto.

Compare las longitudes de las cadenas.

Imprima un mensaje indicando cuál cadena es más larga o si ambas tienen la misma longitud.
"""
cadena1 = input("Ingrese una cadena de texto ")
cadena2 = input("Ingrese otra cadena ")

if len(cadena1) > len(cadena2):
    print(f"{cadena1} es mas largo que {cadena2}")
elif len(cadena1) < len(cadena2):
     print(f"{cadena2} es mas largo que {cadena1}")
else: 
    print(f"{cadena1} Ambas tienen la misma longitud {cadena2}")     