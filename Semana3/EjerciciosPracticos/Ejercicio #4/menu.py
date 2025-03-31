from inventario.inventario import Inventario
from inventario.producto import Producto
from helpers import validations
import os

def menu():
    inventario = Inventario()
    while True:
        print("______Sistema de Gestión de Productos e Inventario______")
        print("1. Agregar Producto")
        print("2. Buscar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            #code
            cod = inventario.generar_codigo()
            nombre = input("Ingrese el nombre del producto")
            precio = float(input("Ingrese el precio del producto"))
            cantidad = int(input("Ingrese la cantidad del producto"))
            if validations.int_evaluation(cantidad) and validations.float_evaluation(precio):
        
                producto = Producto(cod, nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("El producto se ha agregado al inventario...")
            else:
                print("Los datos no se han ingresado correctamente, intente denuevo...")
            os.system("pause")
        elif opc == "2":
            # code
            cod = int(input("Ingrese el codigo del producto a buscar: "))
            inventario.buscar_producto(cod)
            os.system("pause")
        elif opc == "3":
            # code
            cod = int(input("Ingrese el codigo del producto a modificar: "))
            if inventario.buscar_producto(cod):
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto"))
                if validations.float_evaluation(nuevo_precio) and validations.int_evaluation(nueva_cantidad):
                    inventario.actualizar_producto(cod, nuevo_nombre, nuevo_precio, nueva_cantidad)
                    print("El producto se actualizo correctamente...")
                else: 
                    print("No se ha podido hacer cambios, intente nuevamente...")
    
            os.system("pause")
        elif opc == "4":
            # code
            cod = int(input("Ingrese el codigo del producto a eliminar: "))
            if inventario.eliminar_producto(cod):
                print("Producto eliminado")
            else: 
                print("Producto no eliminado, intente nuevamente....")
            os.system("pause")
        elif opc == "5":
            # code
            print("Saliendo...")
            break
        else: 
            print("Opción inválida, intente nuevamente...")
            os.system("pause")
            
