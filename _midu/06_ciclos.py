"""
Ejecutar un bloque de código 
repetitivamente hasta que se cumpla una condición 

"""

contador=0

#Muestra el primer múltiplo de 5 y termina
while contador<=100:
    if(contador%5==0):
        print("Es múltiplo de 5")
        break;
    print(contador)
    contador+=1

#Se salta todos múltiplos de 5 
while contador<=100:
    if(contador%5==0):
        continue;
    print(contador)
    contador+=1



while contador<5:
    print(contador)
    contador+=1
else:
    print("El bucle ha terminado")



numero=-1

while numero<0:
    try:
        numero=int(input("Escribe un número positivo"))
    except:
        print("Solo coloca números")
    if numero<0:
        print("El número debe ser positivos")
    
print("El número es positivo")

frutas=["manzana", "pera"]

for i,fruta in enumerate(frutas):
    print(f"Estás en el índice {i} y la fruta es:{fruta}")


letras=["A","B","C"]
numeros=[1,2,3]

for letra in letras:
    for num in numeros:
        print(f"Numéro {num} y su letra:{letra}")

"""
https://pythontutor.com/
"""

animales_mayuscula=[fruta.upper() for fruta in frutas]

# numero_par=[for num in numeros if num%2==0]

# Range crea los números sobre la marcha, no guarda en memoria
range(2,20,2)


###
# EJERCICIOS (for)
###

# # Ejercicio 1: Imprimir números pares
# # Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
# print("\nEjercicio 1:")

# numeros_lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for num in numeros_lista:
#     if(num%2==0):
#         print(num)

# for numero in range(2, 21, 2):  # range(inicio, fin, paso)
#   print(numero)


# # Ejercicio 2: Calcular la media de una lista
# # Dada la siguiente lista de números:
# # numeros = [10, 20, 30, 40, 50]
# # Calcula la media de los números usando un bucle for.
# print("\nEjercicio 2:")

# numeros = [10, 20, 30, 40, 50]
# suma_numeros=0
# for num in numeros:
#     suma_numeros +=num
# media_numeros=suma_numeros/len(numeros)



# # Ejercicio 3: Buscar el máximo de una lista
# # Dada la siguiente lista de números:
# # numeros = [15, 5, 25, 10, 20]
# # Encuentra el número máximo en la lista usando un bucle for.
# print("\nEjercicio 3:")


# numeros = [15, 5, 25, 10, 20]
# numero_maximo=numeros[0]

# for num in numeros:
#     if(num>numero_maximo):
#         numero_maximo=num
    


# # Ejercicio 4: Filtrar cadenas por longitud
# # Dada la siguiente lista de palabras:
# # palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# # Crea una nueva lista que contenga solo las palabras con más de 5 letras
# # usando un bucle for y list comprehension.
# print("\nEjercicio 4:")

# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# cinco_caracteres=[]
# for palabra in palabras:
#     if(len(palabra)>5):
#         cinco_caracteres.append(palabra)

# cinco_caracteres=[palabra for palabra in palabras if(len(palabra)>5)]


# # Ejercicio 5: Contar palabras que empiezan con una letra
# # Dada la siguiente lista de palabras:
# # palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# # Pide al usuario que introduzca una letra.
# # Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
# print("\nEjercicio 5:")

# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
# contador=0
# for palabra in palabras:
#     if palabra.lower().startswith(letra):
#         contador +=1


###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for num in range(1,11):
    print(num)




# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for num in range(1,21,2):
    print(num)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for num in range(5,51):
    if(num%5==0):
        print(num)
        
for i in range(5, 51, 5):  # El paso 5 genera los múltiplos de 5
  print(i)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

for num in range(10,0,-1):
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

suma=0

for num in range(1,101):
    suma+=num
print(suma)


# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

numero_usuario=int(input("Escribe un número"))

for num in range(1,11,1):
    print(f"{numero_usuario} * {num} = {numero_usuario*num}")
