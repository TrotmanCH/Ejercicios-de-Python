"""
Tabla de multiplicar: Pide un número y muestra su tabla de multiplicar usando while.
"""
print("Ingrese un numero para conocer su tabla de multiplicar")
num = int(input())
limite = 1

while limite <= 12:
    print(f"{num} x {limite} = {num * limite}")
    limite += 1