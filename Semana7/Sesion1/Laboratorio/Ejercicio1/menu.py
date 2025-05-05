from pila import PilaLinkedList
import os

def menu():
    pila: PilaLinkedList = PilaLinkedList()
    while True:
        print("1. Agregar Documentos")
        print("2. Revisar Documentos")
        print("3. Ver Pendientes")
        print("4. Salir")
        opc = input("Elija una de las opciones: ")
        match opc:
            case "1":
                data = input("Introduzca el nuevo pendiente: ")
                pila.push(data)
            case "2":
                if pila.delete():
                    print("Se ha revisado el primer documento de la pila de pendientes...")
                    os.system("pause")
                else: 
                    print("No se ha podido revisar el pendiente...")
                    os.system("pause")
            case "3":               
                pila.print_pila()
                os.system("pause")
            case "4": 
                print("Saliendo...") 
                break
            case _:
                print("Opción inválida")
                os.system("pause")