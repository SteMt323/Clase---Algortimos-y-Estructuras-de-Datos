from pila import PilaDoubleLinkedList
import os

def menu():
    pila: PilaDoubleLinkedList = PilaDoubleLinkedList()
    while True:
        print("1. Agregar Paciente")
        print("2. Eliminar Paciente Actual")
        print("3. Mirar Paciente en Procedimiento")
        print("4. Salir")
        opc = input("Elija una de las opciones: ")
        match opc:
            case "1":
                nombre = input("Introduzca el nombre del paciente: ")
                while True:
                    edad = int(input("Introduzca la edad del paciente: "))
                    if edad in range(18, 66): break
                    else: print("Edad inválida, introduzca nuevamente...")
                tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
                pila.push(nombre, edad, tipo_sangre)
            case "2":
                if pila.pop():
                    print("Se ha eliminado el paciente actual del registro...")
                    os.system("pause")
                else: 
                    print("No se ha podido eliminar el paciente...")
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