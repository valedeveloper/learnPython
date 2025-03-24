#2246548 - Valeria Jiménez Bedoya

def main():
    peso_paquete=float(input(f"Coloca el peso del paquete"))
    distancia_paquete=float(input(f"Coloca el peso la distancia"))
    dia_envio=int(input("Coloca el día de envío"))

    
    costo_peso=Calcular_Costo_Peso(peso_paquete)
    costo_distancia=Calcular_Costo_Distancia(distancia_paquete,costo_peso)
    costo_envio=Calcular_Costo_Envio(dia_envio,costo_distancia)
    #costo_final=Calcular_Cargo_Urgencia(False,costo_envio)

   

    
    print(f"El costo del envío es de: {costo_envio}")


def Calcular_Costo_Peso(peso):
    """Calcula el costo según el peso"""
    costo_peso=5
    if(peso>5):
        costo_peso+=10
    elif(2<=peso<=5):
        costo_peso+=5
    return costo_peso

def Calcular_Costo_Distancia(distancia,costo_peso):
    costo_distancia=costo_peso
    if(50<=distancia<=200):
        costo_distancia+=0.05*(distancia-50)
    elif (distancia>200):
        costo_distancia+= 0.05*(distancia-200)**(1/2)

    return costo_distancia

def Calcular_Costo_Envio(dia,costo_distancia_peso):
    print("0 - Lunes. 1 - Martes. 2 - Miércoles")
    if(dia==2):
        costo_distancia_peso*=0.92
    return costo_distancia_peso

def Calcular_Cargo_Urgencia(es_envio_urgente,costo_distancia_peso):
    if(es_envio_urgente):
        costo_distancia_peso+=costo_distancia_peso*0.8
    return costo_distancia_peso
    

main()
        
