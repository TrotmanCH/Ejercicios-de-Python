"""
Crea un programa que:

Pida al usuario que ingrese una calificación (un número entre 0 y 100).

Determine si la calificación es aprobatoria (mayor o igual a 60).

Imprima un mensaje indicando si la calificación es aprobatoria o no.
"""
nota = float(input("Ingrese su nota (0 - 100) "))

if nota >= 60:
    print("Aprobado")
else:
    print("Reprobado") 
