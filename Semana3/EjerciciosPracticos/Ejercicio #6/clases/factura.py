class Factura():
    def __init__(self):
        self._productos = []
        
    def agregar_producto(self, nombre, cantidad, precio, descuento=0):
        if cantidad <= 0 or precio <= 0:
            print("La cantidad o el precio deben ser mayores a 0")
            return
        
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": cantidad,
            "descuento": descuento
        }
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            sub = producto["cantidad"] * producto["precio"]
            descuento = sub * (producto["descuento"]/100)
            total += (sub - descuento)
        return total
    
    def generar_reporte(self):
        print("______Factura_______")
        for producto in self._productos:
            print(f"Producto: {producto["nombre"]}")
            print(f"Cantidad: {producto["cantidad"]}")
            print(f"Precio: {producto["precio"]}")
            print(f"Descuento: {producto["descuento"]}")
        print(f"Total: {round(self.calcular_total(), 2)}")
        
    def validar_info(self):
        if len(self._productos) == 0:
            print("No hay ningun producto registrado...")
            return False
        return True
        