'''Crear un programa que simule la gestión de un inventario en una tienda. Utilizar un menú para
agregar, eliminar, modificar y consultar productos en el inventario. Cada producto tendrá un
código, nombre, cantidad y precio.
Menú de opciones:
1. Agregar producto
2. Eliminar producto
3. Modificar producto
4. Consultar producto
5. Mostrar todos los productos
6. Salir'''
import os
import time

Inventario = []

def Limpiar():
    os.system("cls")
    time.sleep(0.5)

def Agregar_datos():
    Limpiar()
    while True:
        try:
            print(
        """
        +================================+
        |¡Bienvenido al sistema de       |
        |gestion de inventarios,         |
        |agrege la cantidad de productos |
        +================================+
        """, end = "   => ")
            
            
            cantidad = int(input())
            break
        except ValueError: print("Solo numeros son admitidos")

# aqui habia un error porque estaba validando mal
    for i in range(cantidad):
        while True:
            nombre = input("ingrese el nombre del producto: ")
            if not nombre.isalpha():
                print("Ingrese solo letras: ")
            else:
                break
            
            
        while True:
            try:
                codigo = int(input("Ingrese el codigo del producto (Solo numueros): "))
            #sale del bucle si es correcto
                break
            except ValueError: print("El codigo debe ser un numero entero")

        while True:

            try:
                precio = float(input("Ingrese el precio del producto: "))
                break
            except ValueError: print("Ingrese solo numeros")
            
        InventarioProducos = [nombre,  codigo, precio]
        Inventario.append(InventarioProducos)
    print()
    print("Se agregaron los productos con exito")
    print()
    os.system("pause")
    # Limpiar()
   
    


def editar_lista():
    while True:
        Limpiar()
        print("""\t\t\tIngrese lo que desea editar
    1. Editar producto
    2. Editar Codigo
    3. Editar Precio
    4. Todos los campos
    5. Salir al menu principal""")
        opcion = int(input())
        #aqui se queda como numero pues se esta convirtiendo
        if opcion == 1:
            print("Ingrese el codigo del producto que desea editar: ", end = " ")
            codigo_producto = int(input())

            #probr asi o con la funcion enumerate la cual es una funcion incorporada que devuelve  un objeto que  se usa paraiteras sobere secuenciuas y 
            for indice, Productos_Editar in enumerate(Inventario):
                #entendi que debe ir ahi debido a que vamos a iterar sobre el dato en la lista ya que el indice ya otr      
                # ademas es el 1 porque vamos a iterar sobre el indece 1 de la lista que son los codigos    
                if Productos_Editar[1] == codigo_producto:
                    # Inventario.pop(indice)
                    print("Ingrese el nuevo nombre del producto: ", end = " ")
                    Nuevonombre_producto = input()
                    # Inventario.insert(indice, Nuevonombre_producto)
                    Inventario[indice][0] = Nuevonombre_producto
                    # print(Inventario)
            print()
            print("Se realizo con exito")
            print()
            return
        elif opcion == 2:
            print("Ingrese el codigo que desea cambiar: ", end =  ' ')
            CambiarCodigo = int(input())
            for indice2,codigo in enumerate(Inventario):
                if codigo[1] == CambiarCodigo:
                    print("Ingrese el nuevo codigo: ", end = " ")
                    NuevoCodigoProducto = int(input())
                    Inventario[indice2][1] = NuevoCodigoProducto
                    print()
                    print("Se realizo con exito")
                    print()
                else:
                    print("Ingrese un codigo valido")
            
            return
        elif opcion == 3: 
            Precio_editar = int(input("Ingrese el codigo del producto que desea editar: "))
            for indice3, precioeditar in enumerate(Inventario):
                #esa variable itera sobre el codifo de las listas
                if precioeditar[1] == Precio_editar:
                    NuevoPrecio = float(input("Ingrese el nuevo precio para el producto: "))
                    #el primer indice es loq ue representa cada lista dentro de la lista grande
                    #el segundo es lo que represenat dentro de la lista chiquita que seria el codigo
                    Inventario[indice3][2] = NuevoPrecio
            print("Se realizo con exito")
            return
        elif opcion == 4:
            EditarCampos = input("Ingrese el codigo del producto que desea editar: ")
            for indice4,  todos_campos in enumerate(Inventario):
                if todos_campos[1] == EditarCampos:
                    nuevoNombreProducto = input("Ingrese el nuevo nombre del produvto que desea editar: ")
                    Inventario[indice4][0] = nuevoNombreProducto
                    nuevoCodigoProducto = int(input("Ingrese el nuevo codigo del producto que desea editar: "))
                    Inventario[indice4][1] = nuevoCodigoProducto
                    nuevoPrecioProducto = float(input("Ingrese el nuevo precio del productoq que desea editar: "))
                    Inventario[indice4][2] = nuevoPrecioProducto
            print("Se realizo con exito")
            os.system("pause")
            return
        elif opcion == 5:
            print("regresando al menu principal")
            return
        else:
            print("Ingrese una opcion valida")
        os.system("pause")

    

def Eliminar_Producto():
    Limpiar()
    Eliminar_Elemento = int(input("Ingrese el codigo del productoq ue desea eliminar: "))
    for indice, Codigo_eliminar in enumerate(Inventario):
        if Codigo_eliminar[1] == Eliminar_Elemento:
            del Inventario[indice]
    print("Producto eliminado exisitosamente")
    os.system("pause")
    
    
    
def consultar_Producto():
    '''El operador * en Python desempaqueta una lista, es decir, separa sus elementos y los pasa individualmente a la función print()
    El operador * convierte [4, 5, 6] en print(4, 5, 6).'''
    Limpiar()
    Consultar_Productito = int(input("Ingrese el codigo del producto que desea cosultar: "))
    for indice, Codigo_Consultar in enumerate(Inventario):
        if Codigo_Consultar[1] == Consultar_Productito:
            print(*Inventario[indice])
        else:
            print("no se encuentra el producto")
        
    os.system("pause")
    

def Mostrar_TodosLosProductos():
    Limpiar()
    print("="*10, "Este es el inventario disponible ", "="*10)
    print("Producto     |   Codigo  |   Precio")
    for i in Inventario:
        print(*i, sep = "              ")
    
    os.system("pause")
    return
    

def Menu_Pincipal():
    
    while True:
        Limpiar()
        print("\t-"*4,"Bienvenido al sistema de gestion de Inventario, elija una opcion para continuar","\t-"*4)
        print('''
    1. Agregar producto
    2. Eliminar producto
    3. Modificar producto
    4. Consultar producto
    5. Mostrar todos los productos
    6. Salir''')
        eleccion = int(input())

        if eleccion == 1:
            Agregar_datos()
            
        elif eleccion == 2:
            Eliminar_Producto()
            
        elif eleccion == 3:
            editar_lista()
            
        elif eleccion == 4:
            consultar_Producto()
        elif eleccion == 5:
            Mostrar_TodosLosProductos()
        elif eleccion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, vuelvavlo a intentar")
            os.system("pause")
    
    



def main():
    Menu_Pincipal()
    


if __name__ == "__main__" :
    main()