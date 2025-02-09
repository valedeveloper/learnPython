###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


# user_number_first=int(input('Escriba el primer número'))
# user_number_second=int(input('Escriba el segundo número'))
# if(user_number_first>user_number_second):
#     print(f"{user_number_first} es mayor a {user_number_second}")
# elif user_number_first<user_number_second :
#     print(f"{user_number_second} es mayor a {user_number_first}")
# else:
#     print(f"Los valores son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)


# user_number_first=int(input('Escriba el primer número'))
# user_number_second=int(input('Escriba el segundo número'))
# operator_user=input('Escriba la operación')


# if(operator_user=="+"):
#     result_operator=user_number_first+user_number_second
#     print(result_operator)
# elif operator_user=="-":
#     result_operator=user_number_first-user_number_second
#     print(result_operator)
# elif operator_user=="*":
#     result_operator=user_number_first*user_number_second
#     print(result_operator)
# elif operator_user=="/" and user_number_second!=0:
#     result_operator=user_number_first/user_number_second
#     print(result_operator)
# else:
#     print("Hay algo que estás haciendo mal :(")

# if 'result_operator' in locals(): #Comprueba si la variable resultado existe.
#     print(f"El resultado es: {result_operator}")




# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# year_user=int(input('Introduzca el año que quiere evaluar'))
# is_leap_year=print("Es año bisiesto") if (year_user%4==0 and year_user%100!=0) or year_user%400==0 else print("No es año bisiesto")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


# user_age=int(input("¿Cuál es tu edad?"))
# if(user_age>=65):
#     print("Eres adulto mayor")
# elif (user_age>=18 and user_age<=64):
#     print("Eres adulto")
# elif(13<=user_age<=17):
#     print("Eres adolescente")
# elif(user_age>=3 and user_age<=12):
#     print("Eres un niño")
# elif(0<=user_age<=2):
#     print("Es un bebé")
# else:
#     print("No es válida la edad")


 # EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# numbers=[1,2,3,4,5]
# numbers.append(6)
# print(numbers)

# numbers.insert(2,10)
# print(numbers)

# numbers[0]=0
# print(numbers)






# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]

# lista_a.extend(lista_b)
# print(lista_a)
# lista_a.remove(1)
# print(lista_a)
# number_poped=lista_a.pop(3)
# print(number_poped)

# lista_b.clear()
# print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.


# numbers_list=[1,2,3,4,5,6,7,8,9,10]
# numbers_slicing=numbers_list[2:4]
# del numbers_list[2:5]

# print(numbers_slicing,numbers_list)






# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# numbers_list= [5, 2, 8, 1, 9, 4, 2]
# numbers_list.sort
# print(numbers_list)

# count_two=numbers_list.count(2)
# print(f"Aparece el número dos: {count_two}")

# print(
#     7 in numbers_list
# )


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.


numbers= [1, 2, 3]

copia_1= numbers[:]
copia_2=numbers.copy()
referencia=numbers
print(numbers,copia_1,copia_2)





# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

fruits= ["Manzana", "pera", "BANANA", "naranja"]
fruits.sort(str.lower)