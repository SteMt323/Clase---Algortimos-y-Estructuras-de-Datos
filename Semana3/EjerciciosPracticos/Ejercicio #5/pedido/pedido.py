from cliente import Cliente, ClienteVip
class Pedido():
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        
    def calcular_venta_total(self):
        total = sum(producto["precio"] for producto in self.productos)
        descuento = self.cliente.calcular_descuento()
        total -= total * descuento
        return total
        
    def generar_pedido(self):
        print("\n------- Pedido -------")
        print(f"Cliente: {self.cliente.nombre} - {self.cliente.contacto}")
        print("Productos comprados: ")
        for i, producto in enumerate(self.productos, start=1):
            print(f"{1}: {producto["nombre"]} - ${producto["precio"]:.2f}")
        print(f"Total: ${self.calcular_venta_total():.2f}")
        
        
    # Esta funcion debería de detallar datos del cliente, lista de productos
    # y el total de la venta
    
        
    