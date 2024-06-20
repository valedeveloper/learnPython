my_name,my_age="Valeria",21
"""
Formas de formatear strings  
"""
print("Hola, mi nombre es {} y tengo {} de edad".format(my_name,my_age))
print("Mi nombre es %s y mi edad %d" %(my_name,my_age))
print(f"Mi nombre es {my_name} y tengo {22+1}")

#Desempaqueado de caracteres
name="Valeria"
a,b,c,d,e,f,g=name
print(a)

#División
#[indice del número donde quiere iniciar, indice + 1 donde quiere finalizar]
name_slice=name[0:4]
name2_slice=name[1:]
name3_slice=name[-2]

print(name_slice,name2_slice,name3_slice)

reverse_name=name[::-1]
print(reverse_name)

languaje4_slice=name[0:8:3]
#El dos es el salpto de cada `palabrs`
print(languaje4_slice)
 

 #Funciones
print(name.capitalize(),
name.replace("V","L"),
name.upper(),
name.index("l"),
name.count("a")      
)