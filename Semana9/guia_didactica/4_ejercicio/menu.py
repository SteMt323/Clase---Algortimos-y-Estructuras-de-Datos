from linkedlist import *

def menu():
    lista: ColaLinkedList = ColaLinkedList()
    while True:
        print("1. Agregar Elementos")
        print("2. Desencolar segun prioridad")
        print("3. Mostrar toda la cola")
        print("4. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                nombre = input("Escriba el nombre del elemento: ")
                while True:
                    prioridad = int(input("Escriba la prioridad (1-5): "))
                    if prioridad in range (1,6):
                        break
                    else: print("Prioridad inválida...")
                lista.append(nombre, prioridad)
            case "2":
                lista.dequeque()
            case "3":
                lista.print_cola()
            case "4": break
            case _: print("Opcion invalida...")