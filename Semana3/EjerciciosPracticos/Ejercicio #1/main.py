'''Ejercicio #1: Análisis de datos de ventas
Desarrollar un programa que procese un conjunto de registros de ventas (por
ejemplo, listas de diccionarios) para extraer información relevante. Los
estudiantes deberán aplicar funciones internas como map, filter y reduce para
transformar y filtrar los datos, calculando totales y promedios. Este ejercicio
busca que los estudiantes identifiquen y aprovechen las funcionalidades nativas
de Python para la manipulación eficiente de estructuras de datos.
'''

import random
import time
import datetime
import os
from functools import reduce 

registros_totales = []




def Pedir_Registros():
    
    
    while True:
        try:
            cantidad_De_Registros = int(input("Ingrese la cantidad de registro a analizar: "))
            break
        except ValueError: print("Solo numero admitos")
    
    for i in range(cantidad_De_Registros):
        #debo generar un id por cada venta
        id_unico = random.randint(10, 100)

        while True:
            FechaDeVenta = input("Ingrese la fecha en la que se hizo la venta (DD/MM/YYYY): ")
            try:
                fecha = datetime.datetime.strptime(FechaDeVenta, "%d/%m/%Y").date()
                break
            except ValueError:
                print("La fecha es invalida")
              

        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_de_productos = int(input("Ingrese la cantidad de productos vendidas: "))
        precio_Unitario_producto = float(input("Ingrese el precio del producto: "))
        categoria_productos = input("Ingrese la categoria de los producto: ")

        registros = {
            "id": id_unico,
            "Fecha de venta": fecha,
            "Nombre":nombre_producto,
            "cantidad":cantidad_de_productos,
            "Precio":precio_Unitario_producto,
            "categoria":categoria_productos
        }

        registros_totales.append(registros)

    print(registros_totales)


def Productos_Mas_Vendidos():
    mas_vendido = list(map(lambda producto: producto["Nombre"], registros_totales))
    print(*mas_vendido)
    time.sleep(2)
    os.system("pause")

def Total_Venta():
    nombre_Producto = list(map(lambda producto: producto["Nombre"], registros_totales))
    total_ventas = list(map(lambda ventas: ventas["Precio"] * ventas["cantidad"], registros_totales))
    #zip devuelve tupplas lol
    informacionVentas = zip(nombre_Producto, total_ventas)
    # for i, productos in enumerate(informacionVentas):
    #     print(f"El total de ventas de {informacionVentas[i][0]} es de: ${informacionVentas[i][1]}")
    for i, k in informacionVentas:
        print(f"El total de ventas de {i} es de: ${k}") 





def ventas_mayores():
    mayor = list(filter( lambda producto: producto["cantidad"] * producto["Precio"] > 5000, registros_totales))
    
    if mayor:
        print()
        print("estos son los prodictos mayores a 5000: ")
        print()
        for i in mayor:
            total_ventas = i["cantidad"] * i["Precio"]
            print(f"Producto: {i["Nombre"]} y el total es de: {total_ventas}")
    else:
        print("no hay registros con mas de 5000")

def volumen():
    while True:
        print('''Elija una opcion
    1. Ver productos con menos demanda
    2. Ver productos con mas demanda
''')
        opcion = int(input())

        if opcion == 1:
            volumen_bajo = list(filter(lambda volumen: volumen["cantidad"] <= 5, registros_totales))
            if volumen_bajo:
                print()
                print("Estos son los productos con menor demanda: ")
                print()
                for i in volumen_bajo:
                    print(f"Producto: {i["Nombre"]} con la cantidad: {i["cantidad"]}")
                    print()
        elif opcion == 2:
            volumen_alto = list(filter(lambda volumenAlto: volumenAlto["cantidad"] >= 6, registros_totales))

            if volumen_alto:
                print()
                print("Estos son los productos con mayor demanda: ")
                print()
                for k in volumen_alto:
                    print(f"Producto: {i["Nombre"]} con la cantidad: {i["cantidad"]}")
                    print()

def total_ingresos():

    '''la funcion reuce lo que hace es guardar los lemenos de una lista
    en otra de maera acumulativa
    
    debe tneer un acumulador que uarde el resultdo parcial de la 
    operacion 
    reduce() lleva un acumulador que va "recordando" 
    el resultado de las iteraciones anteriores.'''
    totalIngresos = reduce(lambda contador, iterador: contador + (int(iterador["Precio"]) * iterador['cantidad']), registros_totales, 0)

    print(totalIngresos)




def Menu():
    while True:
        print("\t-"*4,"Bienvenido al sistema de gestion de ventas, elija una opcion para continuar","\t-"*4)
        print("Debe agregar datos para usar las funcionalidades del sistema")
        time.sleep(2.5)
        print("""
1. Agregar Datos 
2. Obtener los nombres de los productos vendidos
3. Total de cada venta
4. obtener las ventas mayores a 5000
5. Productos con alto o bajo volumen (demanda de los productos)
6. Total de los ingresos
7. Salir""")
        opcion = int(input())
        if opcion == 1:
            Pedir_Registros()
        elif opcion == 2:
            Productos_Mas_Vendidos()
        elif opcion == 3:
            Total_Venta()
        elif opcion == 4:
            ventas_mayores()
        elif opcion == 5:
            volumen()
        elif opcion == 6:
            total_ingresos()
        elif opcion == 7:
            print("Saliento del sistema")
            break




def main():
    Menu()
    


if __name__ == "__main__" :
    main()