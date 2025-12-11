"""
Contraseña: Pide al usuario que ingrese una contraseña hasta que sea correcta 
(define una fija en el programa).
"""
password = input("Ingrese su contraseña ")    
passd = "admin1234"

while password != passd:
    password = input("Contraseña invalida, ingrese de nuevo ")
    
print("Contraseña Correcta")

"""
Mismo ejercicios pero con validacion de intentos

passd = "admin1234"
intentos = 1

while intentos <= 5 :
    password = input('Ingrese su contraseña ')
    if password == passd:
        print("Contraseña correcta")
        break
    else:
        print(f"Te quedan {5 - intentos} intentos")
        intentos += 1
   
if intentos > 5:
    print('Sistema Bloqueado')    
"""

