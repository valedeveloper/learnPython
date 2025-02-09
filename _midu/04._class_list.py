import os

os.system("clear")


my_first_list=[1,2,3,4,5,6,7,8,9]
fruits=["Manzana", "Pera","Banano","Mandarina"]
list_int:list[int]=[1,2,3,4,5]
list_clear=[]

matrix=[[1,2],[2,3],[4,5]]
print(matrix[0][1])

#Para acceder al ùltimo elemento  fruits[-1]

#Slicing Rebanada de listas
#lista[desde,hasta,paso]. El hasta no lo involucra. El paso es el patrón que se quier
#Si no se dice el desde, lo coge del inicio. Si no involucra el hasta lo lleva hasta el final- Si no se pone el paso lo coge uno a uno 

fruits=["Manzana", "Pera","Banano","Mandarina"]
print(fruits[2:3])

#Devuelve indice par
print(fruits[1::2]) 
#Invierte la lista
print(fruits[::-1])
print(fruits+my_first_list)

fruits +=["Uva"]
print(fruits)

#Métodos de las listas

#Calcular tamaño de la lista
len(fruits)


#Añadir al final
fruits.append("Sandia")

#Añadir en el ìndice que se le indique

fruits.insert(1,"Lulo")

#Añadir en el ìndice que se le indique
fruits.extend(["Borojó"])
print(fruits)

#Eliminar la primera aparición de la cadena de texto

fruits.remove("Sandia")
print(fruits)

#Eliminar el último element de la lista y retonrna ese elemento. 
#También por parámetro se le pasa el índice a eliminar.

last_fruit=fruits.pop()
print(last_fruit)

#Eliminar toda la lista 
fruits.clear()

#Eliminar por rango
del list[1,3] 

#Ordenar lista mutable. Modifica la original 
my_first_list.sort(key=str.lower)
#Ordenar lista, creando una nueva lista. No modifica la original.
sorted_numbers=sorted(my_first_list)

#Primero coloca mayúsulas luego minúsculas. 
sorted_fruits=sorted(fruits)

#Utilidades listas
print(fruits.count("Sandia"))
print("Sandia" in fruits)


