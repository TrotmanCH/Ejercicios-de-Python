"""
Pide al usuario una cadena y usa un ciclo for para imprimir la cadena al revés.
"""
cadena = input("Introduzca una palabra ")
inverti = ""
for i in range(len(cadena)-1,-1,-1):
    inverti += cadena[i]

print(inverti)