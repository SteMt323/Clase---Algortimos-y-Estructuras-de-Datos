from .producto import Producto

class Inventario():
    def __init__(self):
        self.producto = []
        
    def agregar_producto(self, producto: Producto):
        self.producto.append(producto)
        
    def buscar_producto(self, codigo: int):
        return list(filter(lambda index_product: index_product.codigo == codigo, self.producto))
    
    def actualizar_producto(self, codigo: int, nombre: str = None, precio: float = None, cantidad_stock: int = None):
        for index in self.producto:
            if index.codigo == codigo:
                if nombre is not None:
                    index.nombre = nombre
                if precio is not None:
                    index.precio = precio
                if cantidad_stock is not None:
                    index.cantidad_stock = cantidad_stock
                return True
        return False
                
    def eliminar_producto(self, codigo: int):
        for index in self.producto:
            if index.codigo == codigo:
                self.producto.remove(index)
                return True
        return False
    
    def generar_codigo(self):
        n = len(self.producto)
        return n + 1
            