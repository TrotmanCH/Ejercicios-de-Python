"""
Suma acumulativa: Pide números al usuario y súmalos hasta que ingrese el número 0.
"""
suma = 0
numero = int(input("Ingrese números para sumarlos, si quiere parar el ciclo ingrese 0: "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para salir): "))
    

print(f"La suma acumulativa es de: {suma}")