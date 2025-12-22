"""
Crea un programa que pida el monto total de una compra y la categoría de cliente ("A", "B", "C"). Luego:

Si la categoría es "A", aplica un 10% de descuento.
Si la categoría es "B", aplica un 5% de descuento.
Si la categoría es "C", no aplica descuento.
Al final, imprime el monto final de la compra.
""" 
compra = float(input("Ingrese el monto total de su compra "))
categoria = input("Ingrese su categoria (A, B, C) -> ")
descuento = 0 

if categoria == "A":
    descuento = compra * 0.10
    compra -= descuento
    print(f"Su descuento es del 10%, el total de su compra es de {compra}")
elif categoria == "B":
    descuento = compra * 0.05
    compra -= descuento
    print(f"Su descuento es del 5%, el total de su compra es de {compra}")
else:
    print(f"No aplica para descuento, el toal de su compra es de {compra}")