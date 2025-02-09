#Librerìa que ingresa al sistema
import os

os.system("clear")

my_age=int(input("Escribe tu edad"))

if(my_age>=35):
    print('Ya pasas los 35')
elif my_age>=18 and my_age<=35 :
    print('Estás entre los 18 y 35')
else:
    print("Eres menor de edad")


"""
== iGUALES
!= DIFERENTE

Comparación lexicográficamente. No compara la longuitud, compara es por la posiciónde las letras
Compara por letras 
"""
print("manzana < pera", "manzana"<"pera") 
print("manzana < pera", "Hola"=="hola") 

#El 0 se evalua como False
#La cadena de texto vacia se evalua com false

print("\n La condición ternaria")

# Javascript-  my_age>=18?"Es mayor de edad":"No es mayor "
# ternaria en Python.
mensaje="Es mayor de edad" if my_age>=18 else "Es menor de edad"