from cola_solicitudes import ColaSolicitudes
import os

def menu():
    cola: ColaSolicitudes = ColaSolicitudes()
    while True:
        print("\n\n=== Solicitudes de archivos ===")
        print("1. Registrar solicitud de acceso")
        print("2. Mostrar acceso de usuarios de un archivo")
        print("3. Atender solicitud actual")
        print("4. Mostar solicitudes pendientes")
        print("5. Salir")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                usuario = input("Ingrese el nombre del usuario")
                archivo = input("Ingrese el archivo de la solicitud")
                cola.append_solicitud(usuario, archivo)
                os.system("pause")
            case "2":
                archivo = input("Ingrese el archivo de solicitud a copnsultar")
                cola.mostrar_usuarios_archivo(archivo)
                os.system("pause")
            case "3":
                cola.atender_solicitud()
                os.system("pause")
            case "4":
                cola.imprimir_pendientes()
                os.system("pause")
            case "5":
                print("Saliendo...")
                break
            case _: print("Opcion invalida...")
                