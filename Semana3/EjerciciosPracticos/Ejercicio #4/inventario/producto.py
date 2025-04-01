
class Producto():
    def __init__(self, codigo: int, nombre: str, precio: float, cantidad_stock: int):
        self._codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, nuevo_codigo):
        return ValueError("El código nu puede ser modificado")
        