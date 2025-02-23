import math
from datetime import datetime

dia_actual = datetime.today().strftime("%A")


def main():
    lado_1=int(input("Escriba el lado 1"))
    lado_2=int(input("Escriba el lado 2"))

    longitud_cable=Calcular_Longitud(lado_1,lado_2)
    valor_cable=Calcular_Valor_Cable(longitud_cable)
    valor_final=Descuento_Dia(dia_actual,valor_cable)   

    print(f"El precio es: {valor_final}")


def Calcular_Longitud(lado_1,lado_2):
    longitud= math.sqrt((lado_1)**2+(lado_2)**2)
    return longitud

def Calcular_Valor_Cable(longitud):
    valor_cable=0
    if longitud>100:
        valor_cable=longitud*1.5
    elif 50<=valor_cable<=100:
        valor_cable=longitud*1.8
    else:
        valor_cable=longitud*2
    return valor_cable
    
def Descuento_Dia(dia,costo_cable):
    if(dia=="Wednesday"):
        costo_cable*=0.95
    return costo_cable

        
main()