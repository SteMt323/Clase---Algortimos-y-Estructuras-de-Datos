from cola_impresion import Impresora
import os

def menu():
    cola: Impresora = Impresora()
    while True:
        print("1. Agregar documento")
        print("2. Atender documento")
        print("3. Visualizar documentos")
        print("4. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1":
                name = input("Ingrese el nombre del documento")
                user_origin = input("Ingrese el usuario emisor")
                while True:
                    num_pages = int(input("Ingrese el número de páginas"))
                    if num_pages is int: break
                    else: print("Número inválido...")
                cola.append(name, user_origin, num_pages)
                os.system("pause")
            case "2":
                cola.atender_documentos()
                os.system("pause")
            case "3":
                cola.print_documents()
                os.system("pause")
            case "4": 
                print("Saliendo...")
                break
            case _: print("Opción inválida")