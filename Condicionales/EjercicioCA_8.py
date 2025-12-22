'''
Ejercicio 4: Clasificación de triángulos
Pide al usuario que introduzca las longitudes de los tres lados de un triángulo. Luego clasifica el triángulo:

Si los tres lados son iguales, imprime: "Es un triángulo equilátero".
Si dos lados son iguales y uno diferente, imprime: "Es un triángulo isósceles".
Si todos los lados son diferentes, imprime: "Es un triángulo escaleno".
Si las longitudes no forman un triángulo válido (la suma de dos lados debe ser mayor que el tercero), imprime: "No es un triángulo válido".
'''

ladoA = int(input("Introduzca el valor del Lado A "))
ladoB = int(input("Introduzca el valor del Lado B "))
ladoC = int(input("Introduzca el valor del Lado C "))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA == ladoB == ladoC:
        print("Es un triangulo Equilatero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Es un triangulo Isosceles")
    else:
        print("Es un triangulo escaleno")
else:
    print("La suma de dos lados debe ser mayor que el tercero")