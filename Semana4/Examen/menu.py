import os
from clases.persona import Persona
from clases.gastos import GestorGastos
from pedir_datos import agregar_usuario, mostrar_usuario, agregar_gastos

def menu():
    gestor = GestorGastos()
    usuario = agregar_usuario()
    mostrar_usuario(usuario)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("___Control de Gastos____")
        print("1. Agregar Gasto")
        print("2. Mostrar Total Gastado en el Mes")
        print("3. Mostrar Total Gastado por Categoría")
        print("4. Mostrar Gasto Promedio por Categoría")
        print("5. Listar Todos los Gastos")
        print("6. Salir...")
        opc = input("Seleccione una opción: ")

        if opc == "1":
            agregar_gastos(gestor)
            input("Gasto agregado. Presione ENTER para continuar...")

        elif opc == "2":
            mes = int(input("Ingrese el mes (1 - 12): "))
            if 1 <= mes <= 12:
                total = gestor.total_mes(mes)
                print(f"Total gastado en el mes {mes}: ${total:.2f}")
            else:
                print("Mes inválido.")
            input("Presione ENTER para continuar...")

        elif opc == "3":
            categoria = input("Ingrese la categoría: ")
            total = gestor.total_categoria(categoria)
            print(f"Total gastado en '{categoria}': ${total:.2f}")
            input("Presione ENTER para continuar...")

        elif opc == "4":
            categoria = input("Ingrese la categoría: ")
            promedio = gestor.gasto_promedio_categoria(categoria)
            print(f"Gasto promedio en '{categoria}': ${promedio:.2f}")
            input("Presione ENTER para continuar...")

        elif opc == "5":
            gestor.listar_gastos()
            input("Presione ENTER para continuar...")

        elif opc == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intente nuevamente.")
            input("Presione ENTER para continuar...")
