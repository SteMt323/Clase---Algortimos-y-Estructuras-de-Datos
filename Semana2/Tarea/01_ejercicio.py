### Manejo de listas ###
"""
Crear un progrma que simule la gestión de un inventario en una tienda.
Utilizar un menú para agregar, eliminar, modificar y consultar productos en el inventario.
Cada producto tendrá un código, nombre, cantidad y precio.
"""
import os
inventario = []

"""
0 1 2 3
0 1 2 3
0 1 2 3
"""

def agregar_producto():
    codigo = int(input("Ingrese el código del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    
    producto = [codigo, nombre, cantidad, precio]
    inventario.append(producto)
    
def eliminar_producto():
    if not inventario:
        print("No hay productos en el inventario ")
        return False
    code = int(input("Ingrese el código del producto a eliminar: "))
    for i, registro in enumerate(inventario):
        if registro[0] == code:
                inventario.pop(i)
                print(f"El producto con código {code}, ha sido eliminado")
                return True 
        
    print(f"El producto con código {code}, no existe")
    return False
        
def modificar_productos():
    if not inventario:
        print("No hay productos en el inventario para modificar")
        return False
    
    code = int(input("Ingrese el código del producto a modificar: "))
    for i, registro in enumerate(inventario):
        if registro[0] == code:
                print(inventario[i])
                inventario.pop(i)
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                nuevo_producto = [code, nuevo_nombre, nueva_cantidad, nuevo_precio]
                inventario.insert(i,nuevo_producto)
                return True 

    print(f"El producto con código {code}, no existe")
    return False

def consultar_producto():
    if not inventario:
        print("No hay productos en el inventario para modificar")
        return False
    
    code = int(input("Ingrese el código del producto a consultar: "))
    for i, registro in enumerate(inventario):
        if registro[0] == code:
            print(f"Nombre:\t {registro[1]}")
            print(f"Cantidad:\t {registro[2]}")
            print(f"Precio:\t {registro[3]}")
            return True
    
    print(f"El producto con código {code}, no existe")
    return False

def mostrar_todos_productos():
    if not inventario:
        print("No hay productos en el inventario para mostrar")
        return False
    

    print("Código\t Nombre\t Cantidad\t Precio")
    for i, producto in enumerate(inventario):
        print(f"{inventario[i][0]}\t {inventario[i][1]}\t {inventario[i][2]}\t {inventario[i][3]} ")
            
        
def menu():
    while True:
        print("_____Sistema de Gestión de Inventario_____")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Modificar Producto")
        print("4. Consultar Producto")
        print("5. Mostrar todos los Productos")
        print("6. Salir")
        print("__________________________________________")
        opc = int(input("Seleccione una opción: "))
        
        if opc == 1:
            agregar_producto()
            os.system("pause")
        elif opc == 2:
            eliminar_producto()
            os.system("pause")
        elif opc == 3:
            modificar_productos()
            os.system("pause")
        elif opc == 4:
            consultar_producto()
            os.system("pause")
        elif opc == 5: 
            mostrar_todos_productos()
            os.system("pause")
        elif opc == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente denuevo")
            os.system("pause")
            
        
def main():
    menu()
    
if __name__ == "__main__":
    main()
    