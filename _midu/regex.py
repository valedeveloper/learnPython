import re

pattern="Hola"

text="Hola mundo hola"
result=re.search(pattern,text)

if(result):
    print(result)
    print("Lo ha encontrado")
else:
    print("NO")

  


#Devuelve la palabra que coincide
print(result.group())
#Sitcs / Intro

#Devuelve la posición inicial de la coincidencia
print(result.start())

#Devuelve la posición final de la coincidencia:
print(result.end())

#Enumera la cantidad de veces que aparece ese patrón
#El matches devuelve una lista
matches=re.findall(pattern,text,re.IGNORECASE)
print(matches)

#re.IGNORCASE Ignora la mayúsciñas y minùsulas

#Reemplazar por parámetro entra la palabra del texto que quieres reemplzar, la palabra la cual se quiere reemplzar, y el texto en donde se va a reemplazar
new_text=re.sub("Hola","Adiós",text,count=2,flags=re.IGNORECASE)
print(new_text)

found=r"."
word="H.ola"

matchi=re.findall(found,word)
print(matchi)