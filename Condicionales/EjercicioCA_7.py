"""
Escribe un programa que pida al usuario su edad y género (puede ser "M" para masculino o "F" para femenino). Luego, realiza la siguiente clasificación:

Si la edad es menor de 18:
Si el género es "M", imprime: "Eres un chico menor de edad."
Si el género es "F", imprime: "Eres una chica menor de edad."
Si la edad está entre 18 y 60:
Si el género es "M", imprime: "Eres un hombre adulto."
Si el género es "F", imprime: "Eres una mujer adulta."
Si la edad es mayor de 60:
Si el género es "M", imprime: "Eres un hombre mayor."
Si el género es "F", imprime: "Eres una mujer mayor."
"""

edad = int(input("Ingrese su edad "))
genero = input("Ingrese su genero M -> Masculino, F -> Femenino ")

if edad < 18:
    if genero == "M":
        print("Eres un chico menor de edad.")
    else: 
        print("Eres una chica menor de edad.")
elif 18 <= edad <= 60:
    if genero == "M":
        print("Eres un hombre adulto.")
    else: 
        print("Eres una mujer adulta.")
else:
    if genero == "M":
        print("Eres un hombre mayor")
    else: 
        print("Eres una mujer mayor")