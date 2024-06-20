#Nombrar variables. Todo es en minúscula. 
#Camelcase
myVariable="My String Variable"
print(myVariable)
#Convenciones de python. Todo en minúscula o snakecase
myvariable="Mi variable de forma correcta"
my_variable="Otra forma correcta. Esta es snake case"
#NUNCA
#  
#De un dato a otro

int_variable=3
bool_variable=True


#Entero a String

int_to_string=str(int_variable)
bool_to_string=str(bool_variable)



print("Variable entera:",int_variable)
print("Variable string",int_to_string )

print("Variable booleano",bool_variable)
print("Variable string",bool_to_string)

#Concatenación en el print
print(int_variable,bool_to_string)

#Cantidad de caracteres
print(len(my_variable), "Esta es la cantidad de caracteres")


#Variables en una sola línea
name,last_name,years="Valeria","Jiménez",21

print("El nombre",name)
print("El apellido",last_name)
print("La edad:",years)


#Inputs
first_name=input("¿Cuál es tu nombre")
years=input("¿Cuántos años tines")

print("Te llamas : ", first_name," y tienes", years," años de edad")