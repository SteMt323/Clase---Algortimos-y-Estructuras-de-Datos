from cola_procesos import ProcesosCola
import os
import random
def menu():
    cola: ProcesosCola = ProcesosCola()
    while True:
        print("=== Atención de Procesos ===")
        print("1. Agregar un nuevo proceso")
        print("2. Atender y ver proceso actual")
        print("3. Ver procesos pendientes")
        print("4. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                name = input("Ingrese el nombre del proceso: ")
                id = random.randint(1, 9999)
                while True:
                    duracion = float(input("Ingrese la duracion en milisegundos: "))
                    if duracion.is_integer: break
                    else: print("Duración inválida, ingrese nuevamente....")
                cola.agregar_procesos(id, name, duracion)
                os.system("pause")
            case "2":
                cola.atender_proceso()
                os.system("pause")
                
            case "3":
                cola.procesos_pendientres()
                os.system("pause")
                
            case "4":
                print("Saliendo...")
                break
            case _: print("Opcion invalida...")