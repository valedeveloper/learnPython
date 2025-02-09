"""
La convensión para nombrar es 
todo minúscula y se separa con guiòn bajo

snake_case
MiNombreDeVariable . PascalCase
minombredevariable. Todo Junto
MI_CONSTANTES= Valor que no cambia y no va a ser redifinido


Funciones: bloques de còdigo que podemos llamar para ejecutarse
Se puede ejecutar de consola python3 (nombre_archivo)

Lo màs importante de un lenguaje es almacenar los datos. Es por ello que es importante
saber los tipos de datos que se usan en un lenguaje de programación. 

Lo que ingrese el usuario simpre es una cadena de texto. Se debe de parsear para operarse

"""


#Para mostrar mensaje en consola
print('¡Hola, mundo!')


#El sep sirve para separar con lo que se le indique
print("Python", "es", "brutal", sep="-", )


"""
Tipo de datos
int, floar, complex, str,bool,NoneType,list,tuple, dict,range,set

"""
print("--------Tipos de datos----------")
print(type(10))
print(type("10"))
print(type(False))
print(type(-5))
print(type(3.141641485212))
print(type(1+2j))


"cast de variables"

"""
Python no realiza tranformaciones de tipos incompatibles automàticas
Tiene tipado fuerte.
"""

number_string="100"
number_cast=int(number_string)

print(type(number_string))
print(type(number_cast))

"""
El ùnico entero que tranformando es falso
es el cero. 

El 1,2,3,4,-1,-2 son true
El 0 es false
El "" es False
"""
print(bool(3))
print(bool(0))
print(bool(""))
print(bool(" "))


"""
Redonde al par más cercano

5.5=6
3.5

"""


print(round(3.4))


"""
Tipado dinàmico: el tipo de dato se determina en tiempo de ejecuciòn, se pùede cambiar
Tipado estàtico: el tipo de dato siempre serà el que se determine desde un comienzo

"""
print(f"Hola, tengo {18} años")

name,age,city="Valeria",22,"Palmira"

