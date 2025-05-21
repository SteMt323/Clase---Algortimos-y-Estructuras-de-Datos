from pila import *

def menu():
    pila: PilaLinkedList = PilaLinkedList()
    while True: 
        print("\n1. Ingresar Cadena")
        print("2. Evaluar Balance")
        print("3. Salir")
        opc = input("Seleccionme una opcion: ")
        match opc:
            case "1": 
                cadena = input("Ingrese la cadena a evaluar: ")
                pila.agregar_parentesis(cadena)
            case "2":
                pila.match_parentesis()
            case "3": break
            case _: print("Opcion invalida")