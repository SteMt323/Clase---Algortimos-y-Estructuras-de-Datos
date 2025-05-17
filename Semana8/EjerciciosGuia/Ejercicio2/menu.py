from agente import Agente
from cola import ColaLlamadas
import os
def menu():
    cola: ColaLlamadas = ColaLlamadas()
    agentes =[Agente("Agente 1"), Agente("Agente 2"), Agente("Agente 3")]
    while True:
        print("=== Call Centewr ===")
        print("1. Registrar llamada")
        print("2. Atender Llamada")
        print("3. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1":
                cliente = input("Registre el nombre del cliente: ")
                motivo = input("Registre motivo de la llamada: ")
                cola.agregar_llamada_cola(cliente, motivo)
                os.system("pause")
            case "2":
                for i, agente in enumerate(agentes):
                    if agente.disponibilidad == True:
                        cola.atender_llamada()
                        agente.disponibilidad = False
                        break
                    else:
                        print(f"El agente {agente.nombre}, no se encuentra disponible...")
            case "3":
                print("Saliendo...")
                break
            case _: print("Opcion inválida...")