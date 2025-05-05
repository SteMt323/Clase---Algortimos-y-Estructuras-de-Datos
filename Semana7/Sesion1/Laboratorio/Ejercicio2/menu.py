from pila import PilaDoubleLinkedList
import os

def menu():
    pila: PilaDoubleLinkedList = PilaDoubleLinkedList()
    while True:
        print("1. Agregar Panes a la Bandeja")
        print("2. Vender Pan")
        print("3. Ver Pan Listo para Vender (peek)")
        print("4. Salir")
        opc = input("Elija una de las opciones: ")
        match opc:
            case "1":
                data = input("Introduzca el pan: ")
                pila.push(data)
            case "2":
                if pila.pop():
                    print("Se ha vendido el primer pan de la pila de la bandeja...")
                    os.system("pause")
                else: 
                    print("No se ha podido vender el pan...")
                    os.system("pause")
            case "3":               
                pila.peek()
                os.system("pause")
            case "4": 
                print("Saliendo...") 
                break
            case _:
                print("Opción inválida")
                os.system("pause")