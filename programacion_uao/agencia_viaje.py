from datetime import date
"""
costo_paquete=float(input('¿Cuál es el costo del paquete?'))
dia_reserva=date.today().strftime("%A")
costo_final=0

if(tipo_paquete==2 or tipo_paquete==3):
    costo_final=costo_paquete* 0.9
    if(dia_reserva=="Monday")
        costo_final=costo_paquete* 0.05

if(costo_final>500):
    costo_final+=20

print(f"El costo final es: {costo_final}")

"""
def main():
    costo_paquete=calcular_precio_paquete()
    costo_descuento=calcular_descuento_dia_reserva(costo_paquete,dia_reserva=date.today().strftime("%A"))
    valor_servicio=calcular_servicio_final(costo_descuento)


def calcular_precio_paquete():
    tipo_paquete=int(input('¿Cuál es el tipo del paquete'))
    costo_paquete=float(input('¿Cuál es el costo del paquete?'))
    if(tipo_paquete==2 or tipo_paquete==3):
        costo_paquete*= 0.9

    return costo_paquete

def calcular_descuento_dia_reserva(costo_final,dia_reserva):
        if(dia_reserva=="Monday"):
            costo_final*= 0.95

        return costo_final

def calcular_servicio_final(costo_final):
    if(costo_final>500):
        costo_final+=20
    print(f"El costo final es: {costo_final}")

main()


        

    
    
    
