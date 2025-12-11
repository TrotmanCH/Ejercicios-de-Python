"""
Número mayor: Pide al usuario números hasta que ingrese -1, y muestra el mayor número ingresado.
"""
print("Ingrese un numero, si quiere parar el ciclo ingrese -1")
num = int(input())
mayor = num

while num != -1: 
    if num > mayor:
        mayor = num 
    num = int(input("Ingrese otro numero (-1 para salir)"))
if mayor != -1:
    print(mayor)
print("Programa Finalizado")