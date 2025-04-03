from clases.producto import Producto
from clases.inventario import Inventario
import os

def menu():
    inventario = Inventario()
    while True:
        print("___Sistema de gestión de inventario___")
        print("1. Agregar producto ")
        print("2. Buscar producto ")
        print("3. Modificar producto ")
        print("4. Eliminar producto ")
        print("5. Salir... ")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            code = int(input("Ingrese el código: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock del producto: "))
            producto = Producto(code, nombre, precio, cantidad)
            inventario.agregar_producto(producto)
            os.system("pause")
        elif opc == "2":
            code = int(input("Ingrese el codigo del producto a buscar: "))
            inventario.buscar_producto(code)
            os.system("pause")
        elif opc == "3":
            code = int(input("Ingrese el codigo del producto a modificar: "))
            nombre = input("Ingrese el código del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock del producto: "))
            inventario.actualizar_producto(code, nombre, precio, cantidad)
            os.system("pause")
        elif opc == "4":
            code = int(input("Ingrese el codigo del producto a eliminar: "))
            inventario.eliminar_producto(code)
            os.system("pause")
        elif opc == "5":
            print("Saliendo...")
            break
        else: 
            print("Opción inválida...")
            os.system("pause")
            