"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular
el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
payasos = int(input("Ingrese el numero de payasos vendidos "))
muñecas = int(input("Ingrese el numero de muñecas vendidos "))

pesomu = muñecas * 75 
pesopa = payasos * 112 
totalp = pesomu + pesopa

print(f"El peso por {payasos} payasos vendidos es de {pesopa}g y el peso por {muñecas} muñecas vendidos es de {pesomu}g, el total del paquete es de {totalp}g") 