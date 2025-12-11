"""
Adivina el número: Define un número secreto y pide al usuario que lo adivine usando while hasta que 
"""
num_secret = 7
numero = int(input("Adivina el numero!, ingresa un numero "))

while numero != num_secret:
    print("Numero incorrecto")
    numero = int(input("Ingrese otro numero "))

print(f"Felicidades Adivinaste el numero {num_secret}")