"""
Pide al usuario un número n e imprime su tabla de multiplicar del 1 al 10.
"""
print("Tabla de multiplicar")
N = int(input("Introduzca el numero para elaborar la tabla "))

for i in range (1,11):
    print(f"{N} x {i} = {N * i}")