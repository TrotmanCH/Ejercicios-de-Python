"""
Escribe un programa que calcule el porcentaje de impuestos según los ingresos anuales y el estado civil:

Si los ingresos son menores a $30,000:
Si el estado civil es "soltero", aplica un impuesto del 10%.
Si el estado civil es "casado", aplica un impuesto del 5%.
Si los ingresos son mayores o iguales a $30,000:
Si el estado civil es "soltero", aplica un impuesto del 20%.
Si el estado civil es "casado", aplica un impuesto del 15%.
Imprime el monto del impuesto a pagar.
"""

ingreso = float(input("Ingrese sus ingresos anuales "))
estado = input("Ingrese su estado civil (soltero) o (casado) ")

if ingreso <= 30000:
    if estado == 'soltero':
        descuento = ingreso * 0.10
        ingreso -= descuento
        print(f"Su estado civil es {estado} aplica a un descuento del 10%, su descuento es de {descuento}")
        print(f"monto del impuesto a pagar {ingreso:.2f}")
    else:
        descuento = ingreso * 0.05
        ingreso -=  descuento
        print(f"Su estado civil es {estado} aplica a un descuento del 5%, su descuento es de {descuento}")
        print(f"monto del impuesto a pagar {ingreso:.2f}")
else:
    if estado == 'soltero':
        descuento = ingreso * 0.20
        ingreso -= descuento
        print(f"Su estado civil es {estado} aplica a un descuento del 20%, su descuento es de {descuento}")
        print(f"monto del impuesto a pagar {ingreso:.2f}")
    else:
        descuento = ingreso * 0.15
        ingreso -= descuento
        print(f"Su estado civil es {estado} aplica a un descuento del 15%, su descuento es de {descuento}")
        print(f"monto del impuesto a pagar {ingreso:.2f}")