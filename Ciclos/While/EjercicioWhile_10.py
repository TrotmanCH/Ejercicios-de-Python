"""
Menú interactivo: Muestra un menú con opciones (1 = Saludar, 2 = Despedirse, 3 = Salir)
 y usa while para repetir hasta que elija la opción 3. 
"""
opcion = 0

while opcion != 3:
    opcion = int(input("Ingrese una opcion (1 = Saludar, 2 = Despedirse, 3 = Salir) "))
    if opcion == 1:
        print("Hola, Bienvenido a los ejercicios de python")
    elif opcion == 2:
        print("Un gusto conocerte, Hasta luego!")
    elif opcion == 3:
        print("Fin del programa")
    else:
        print("Opcion invalida")
    
