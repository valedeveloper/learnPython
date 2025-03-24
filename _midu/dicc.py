# persona={
#     "nombre":"Valeria Jiménez B",
#     "es_estudiante":True,
#     "social_media":{
#         "instagram":"valeriajbe"
#     }

# }

# print(persona["social_media"])

# persona["nombre"]="Val"
# del persona["es_estudiante"]

# a={"name":"V","age":22}
# b={"name":"J","age":28}

# b.update(a)
# print(a)
# print("nombre" in persona)

# for key,value in persona.items():
#     print(f"{key}:{value}")


# def find_first_sum(nums,goal):
#     "Esta función realiza suma"
#     seen={}

#     for index,value in enumerate(nums):
#         missing=goal-value
#         if(missing in seen): return [seen[missing],index]
        
#         seen[value]=index


# nums=[1,2,3,4,5]
# goal=8
# result=find_first_sum(nums)
# print(result)


lista_a=[1,2,3]
lista_b=[2,4,1]

def battle(lista_a, lista_b):
    puntos_a = sum(lista_a)
    puntos_b = sum(lista_b)
    return f"{puntos_a - puntos_b}a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}b" if puntos_b > puntos_a else "x"


lista_a = [4, 4, 4]
lista_b = [2, 8, 2]
winner = battle(lista_a, lista_b)
print(winner)