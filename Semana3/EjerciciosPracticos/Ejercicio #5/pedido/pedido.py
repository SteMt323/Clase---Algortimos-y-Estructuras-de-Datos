from cliente import Cliente, ClienteVip
from producto import Producto
class Pedido():
    def __init__(self, cliente, productos: Producto):
        self.cliente = cliente
        self.productos = productos
        
    def calcular_venta_total(self):
        total = sum(producto.precio for producto in self.productos)
        if self.cliente.tipo != None:
            descuento = self.cliente.descuento()
            total -= total * (descuento / 100)
            return total
        else:
            return total
        
    def generar_pedido(self):
        print("Pedido: ")
        print(f"Cliente: {self.cliente.nombre} - {self.cliente.contacto}")
        print("Productos comprados: ")
        for i in self.productos:
            print(f"Producto {i+1}: {i.producto}")
        print(f"Total: ${self.venta_total()}")
        
        
    # Esta funcion debería de detallar datos del cliente, lista de productos
    # y el total de la venta
    
        
    