
# Online Python - IDE, Editor, Compiler, Interpreter
# 2246548 - Valeria Jiménez Bedoya

cantidad_productos=int(input('¿Cuántos productos va a comprar?'))
productos=[]

for i in range(cantidad_productos):
    nombre_producto=input(f"¿Cuàl es el nombre del producto {i+1}? ")
    precio_producto=float(input(f"¿Cuàl es el precio del producto {i+1}"))
    cantidad_producto=int(input(f"¿Cuàl es la cantidad del producto {i+1}"))
    productos.append({"nombre": nombre_producto, "precio": precio_producto, "cantidad": cantidad_producto})

print(productos)

total=float(sum(producto["cantidad"] * producto["precio"] for producto in productos))


if 2<= cantidad_productos<=4:
    total*=0.9
else:
    total*=0.8
    
print(f"El valor total a pagar es: {total} ")
print("El valor total a pagar es:", total )



"""
if 2<= cantidad_productos<=4:
    total*=0.8
else:
    total*=0.9 
""" 
