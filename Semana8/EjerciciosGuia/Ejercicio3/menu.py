from cola_atencion import ColaAtencion
import os

def menu():
    cola: ColaAtencion = ColaAtencion()
    while True:
        print("===Menu Atencion Pacientes===")
        print("1. Registrar nuevo paciente")
        print("2. Atender paciente")
        print("3. Mostrar pacientes por atender")
        print("4. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                nombre = input("Ingrese el nombre del paciente: ")
                while True:
                    servicio = input("Ingrese el servicio del paciente: \n1. Compra\n2. Consulta\n3.Receta")
                    if servicio == "1": 
                        servicio = "Compra", 
                        break
                    elif servicio == "2": 
                        servicio = "Consulta"
                        break
                    elif servicio == "3": 
                        servicio = "Receta"
                        break
                    else: 
                        print("Opción inválida, ingrese nuevamente...")
                        os.system("pause")
                cola.agregar_cliente(nombre, servicio)
                print("Se ha agregado el paciente...")
                os.system("pause")
            case "2": 
                cola.atender_paciente()
                os.system("pause")
            case "3":
                cola.mostrar_pacientes()
                os.system("pause")
                
            case "4":
                print("Saliendo...")
                break
            
            case _:
                print("Opción inválida...")