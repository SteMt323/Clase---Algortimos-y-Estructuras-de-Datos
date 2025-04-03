class Producto():
    def __init__(self, code: int, nombre: str, precio: float, cantidad: int):
        self.__code = code
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def get_code(self):
        return self.__code
    
    def __str__(self):
        return f"Producto(code={self.__code}, nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"