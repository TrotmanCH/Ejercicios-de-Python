'''var1 = int(input())
var2 = int(input())

number = []

for i in range(var1, var2 + 1):
    if i % 2 == 0 and i > 5:
        number.append(i)
        break
for i in range(var1, var2 + 1):
    if i % 7 == 0:
        number.append(i)
        break

print(f"First even number greater than 5: {number[0]}")
print(f"First number divisible by 7: {number[1]}")

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)

# Tarea 1: Números divisibles por 4 entre 30-80
print("Numbers divisible by 4 between 30-80:")
# Tu código aquí
for i in range(30, 81):
    if i % 4 == 0:
        print(i, end=", ",)  # nueva línea

# Tarea 2: Primeros 8 números impares desde 15
print("\n\nFirst 8 odd numbers from 15:")
# Tu código aquí
contador = 0
for i in range(15, 100):
    if i % 2 == 0:
        contador += 1
        continue
    elif contador == 8:
        break
    print(i, end=", ")  # nueva línea
# Tarea 3: Contando hacia atrás, divisibles por 5
print("\n\nCounting backwards, divisible by 5:")
# Tu código aquí
for i in range(50,9,-1):
    if i % 5 == 0:
        print(i, end=", ")  # nueva línea

print("\n\nProduct of numbers divisible by 3 (1-30):")
producto = 1
for i in range(1,31):

    if i % 3 == 0:
        producto *= i


print(producto)
n = int(input('numero'))
# Escribe tu código a continuación
for i in range(1,n+1):
    for j in range(1, n+1):
         if i * j == n:
            print(f"{i} {j}")



def sum_numbers():
    contador = 0
    for j in range(1, 10001):
        contador += j
    print(contador)

n = int(input())
for i in range(n):
    sum_numbers()
def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

for i in range(15, 34):
    is_even(i)
for i in range(153, 219):
    is_even(i)

def suma_number(num1, num2):
    print(num1 * num2)

num1 = int(input())
num2 = int(input())

suma_number(num1, num2)'''

def square(n):
    return n ** 2

resultado = square(2)
print(resultado)