"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión.  
"""
cantidad = float(input("Ingrese la cantidad que desea invertir "))
interes = float(input("Ingrese el interes anual en % "))
años = int(input("Ingrese el numero de años "))

capital = round(cantidad * (1+ (interes / 100)) ** años, 2)

print(f"Su capital obtenido por {años} años es de {capital}")