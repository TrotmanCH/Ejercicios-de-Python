"""
Promedio de notas: Pide notas al usuario hasta que ingrese -1, y luego muestra el promedio. 
"""

promedio = 0 
contador = 0

while True:
    notas = float(input("Ingrese su nota, (-1 para cerrar el ciclo) "))
    if notas == -1:
        break
    elif 0 <= notas <= 100:
        promedio += notas
        contador += 1
    else:
       print("Nota invalida, Ingrese una nota entre 0 y 100")

if promedio > 0:
    print(f"el promedio de sus notas es de {round(promedio / contador, 2)}")
else:
    print("No se ingresaron notas validas")
    