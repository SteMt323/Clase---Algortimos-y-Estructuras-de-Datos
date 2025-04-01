from pedido.cliente import ClienteVip, Cliente
from pedido.producto import Producto
import random

def detallar_cliente():
    cliente_detalle = None
    n = input("Seleccione el tipo de cliente: \n1. Regular \n2. Vip\n")
    if n == "1":
        cliente = Cliente()
        id = random.randint(1000, 9999) 
        nombre = input("Ingrese el nombre: ")
        contacto = input("Ingrese el contacto del cliente (num - cel): ")
        cliente_detalle = cliente.agregar_cliente(id, nombre, contacto)
        
    elif n == "2":
        cliente = ClienteVip()
        id = random.randint(1000, 9999)
        nombre = input("Ingrese el nombre: ")
        contacto = input("Ingrese el contacto del cliente (num - cel): ")
        tipo = True
        cliente_detalle = cliente.agregar_cliente(id, nombre, contacto, tipo)
        
    return cliente_detalle
        
        
def elegir_productos():
    list_products = [{
        "Pc de Escritorio": 2000.20,
        "Laptop": 1500.20,
        "Mouse": 50.20,
        "Teclado": 120.20
    }]
    
    
    print("Lista de productos")
    for i in list_products:
        print(f"Producto {i + 1}:  {list_products[i]}")
    
    n = input("Seleccione cantidad de productos a elegir: ")
    p = Producto()
    selected_products = []
    for i in range(n):
        election = input("Seleccione el producto: ")
        if election == "1":
            producto = list_products[0]
            selected_products.append(p.agregar_producto(producto))
        elif election == "2":
            producto = list_products[1]
            selected_products.append(p.agregar_producto(producto))
        elif election == "3":
            producto = list_products[2]
            selected_products.append(p.agregar_producto(producto))
        elif election == "4":
            producto = list_products[3]
            selected_products.append(p.agregar_producto(producto))
        else: 
            print("No ha seleccionado ninguno de los indicados...")
            
    return selected_products
