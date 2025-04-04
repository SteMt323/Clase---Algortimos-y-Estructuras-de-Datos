from clases.factura import Factura
import os

def menu():
    factura = Factura()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("____Simulación de proceso de facturación_____")
        print("1. Agregar Productos ")
        print("2. Facturar ")
        print("3. Salir....")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precion del producto: "))
            descuento = float(input("Ingrese el descuento del producto (porcentual)"))
            factura.agregar_producto(nombre, cantidad, precio, descuento)
            os.system("pause")
        elif opc == "2":
            if factura.validar_info():
                factura.generar_reporte()
            os.system("pause")

        elif opc == "3":
            print("Saliendo....")
            break