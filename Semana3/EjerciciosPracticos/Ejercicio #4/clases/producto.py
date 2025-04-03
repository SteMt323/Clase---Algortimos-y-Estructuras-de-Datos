class Producto():
    def __init__(self, code: int, nombre: str, precio: float, cantidad: int):
        self.__code = code
        self._nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    
        