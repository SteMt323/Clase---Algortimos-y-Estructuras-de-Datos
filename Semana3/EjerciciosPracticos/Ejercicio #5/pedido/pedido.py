from cliente import Cliente, TipoCliente

class Pedido():
    def __init__(self):
        self.cliente = TipoCliente
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def venta_total(self):
        total = sum(producto.precio for producto in self.productos)
        if self.cliente.tipo != "regular":
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
            print(f"{i.nombre}: ${round(i.precio, 2)}")
        print(f"Total: ${self.venta_total()}")
        
        
    # Esta funcion debería de detallar datos del cliente, lista de productos
    # y el total de la venta
    
        
    