from linkedlist import *

def menu():
    lista: LinkedList = LinkedList
    while True:
        print("\n1. Agregar Cancion")
        print("2. Reproducir siguiente cancion")
        print("3. Reproducir cancion anterior")
        print("4. Eliminar cancion")
        print("5. Imprimir lista de reproduccion")
        print("6. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                cancion = input("Ingrese la cancion: ")
                lista.append(cancion)
            case "2": lista.move_fordward()
            case "3": lista.move_backward()
            case "4": lista.delete_song()
            case "5": lista.print_playlist_current()
            case "6": break
            case _: print("Opcion invalida...")