"""
Las listas son una estructura de datos
Python es un lenguaje orientado a objetos
Caja que ingreso datos que tienen posición

Lista!== array
Las listas son estructuras de datos 
incorporadas en Python que pueden 
almacenar diferentes tipos de datos. 
Son muy flexibles y pueden crecer y reducirse dinámicamente.
Arrays son 
Lista proporcionan elementos de difernetes tipos, 
soportan una amplia gama de métodos y operaciones
Son menos efiicentes en términos de memoria y rendimiento

Los arrays: 
Deben contener elementos del mismo tipo.
Ofrecen operaciones matemáticas y de álgebra lineal rápidas y eficientes.
Consumen menos memoria y son más rápidos para grandes conjuntos de datos numéricos en comparación con las listas.
"""
my_list=list()
#               0  1  2    3
my_other_list=[20,18,32,"Valeria"]
#               -4  -3  -2    -1
my_list=[3,2,1]
print(type(my_other_list))
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list+my_list)


#Contante
PI_CONSTANT=3,14


#Funciones listas
#Insertar
my_other_list.append(360)
print(my_other_list)


#Insertar según el índice donse se especifique
my_other_list.insert(2,"Hola")
print(my_other_list)

my_other_list[2]="Hola2"
print(my_other_list)


#Elimina el dato que se pase por parámetro
my_other_list.remove(20)
print(my_other_list)

del my_other_list[2]
print("Con el del",my_other_list)

#Elimina el último dato de la lista y devuelve el dato eliminado
my_other_list.pop()
print(my_other_list)



my_pop_element=my_other_list.pop(2)
print(my_pop_element)

my_new_list=my_other_list.copy()
print(my_new_list)
print(my_other_list.clear())
print(my_new_list[1:3])