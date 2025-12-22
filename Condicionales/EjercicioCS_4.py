"""
Crea un programa que:

Pida al usuario que ingrese su edad.

Determine si el usuario es mayor de edad (18 años o más) y si puede votar.

Imprima un mensaje indicando si el usuario puede votar o no.
"""
edad = int(input("Ingrese su edad "))

if edad >= 18:
    print("Tiene derecho a votar")
else:
    print("No tiene derecho a votar")
    