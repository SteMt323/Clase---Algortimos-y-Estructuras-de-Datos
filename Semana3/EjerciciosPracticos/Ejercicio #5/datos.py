from pedido.cliente import ClienteVip, Cliente
import random

def detallar_cliente():
    cliente_detalle = None
    n = input("Seleccione el tipo de cliente: \n1. Regular \n2. Vip\n")
    id = random.randint(1000, 9999) 
    nombre = input("Ingrese el nombre: ")
    contacto = input("Ingrese el contacto del cliente (num - cel): ")
    if n == "1":
        cliente_detalle = Cliente(id, nombre, contacto)
        
    elif n == "2":
        cliente_detalle = ClienteVip(id, nombre, contacto)
        
    return cliente_detalle
        
        
def elegir_productos():
    # Esta es nuestra lista de productos, contiene una lista de diccionario "nombre" "precio"
    list_products = [{
        {"nombre": "Pc de Escritorio", "precio": 2000.20},
        {"nombre": "Laptop", "precio": 1500.20},
        {"nombre": "Mouse", "precio": 50.20},
        {"nombre": "Teclado", "precio": 120.20}
    }]
    
    
    print("\nLista de productos: ")
    for i, producto in enumerate(list_products, start =1):
        print(f"Producto {1}:  {producto["nombre"]} - ${producto["precio"]:.2}")
    
    n = int(input("Seleccione cantidad de productos a elegir: "))
    
    selected_products = [] # Y aqui para poder agregar a una nueva lista los productos elegidos
    
    for _ in range(n):
        election = int(input("Seleccione el producto: "))
        if 0 <= election < len(list_products):
            selected_products.append(list_products[election])
        else: 
            print("No ha seleccionado ninguno de los indicados...")
            
    return selected_products
