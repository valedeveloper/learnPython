"""
Operadores aritméticos (+,-,*,/,%,**) // Si el resultado de la división es decimal, la convierte a entero (10 // 3)=Da 3,3333. La convierte 3
Operadores relacionales (>,<,==,>=,<=,!=)
Operadores Bit a Bit (&, |, ^, ~,>>,<<)
Operadores de asignación (=,+=,-=)
Operadores lógicos (and, or,not)
Operadores de pertenencia (in => si esta. not in=>ture si no edstá)
Operadores de identidad

"""
a=5
b=5

#Operadores ariméticos: 
print(
"Operadores númericos",
suma=a+b,
subt=a-b,
product=a*b,
div=a/b,
mod=a%b,
elev=a**b,
)
print(
"Operadores relacionales",
min=a>b,
max=a<b,
equal=a==b,
min_or_equal=a<=b,
max_or_equal=a>=b,
diferent=a!=b,
)
print(
"Operadores  Bit a Bits",
min=a&b,
max=a|b,
var_false=~True,
min_or_equal=a>>b,
maxx=a<<b,
)
print(
"Operadores lógicos",
and_logic=a>b and b==4,
or_logic=a==b | a==b
)
print(
"Operadores pertenencia",
a in b,
a not in  b
)


