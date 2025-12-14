"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.  
"""
ht = int(input("Ingrese el numero de horas trabajadas "))
ch = float(input("Ingrese el coste por hora "))

salario = ht * ch 
print(f"Su salario por {ht} horas trabajadas es de {salario}")