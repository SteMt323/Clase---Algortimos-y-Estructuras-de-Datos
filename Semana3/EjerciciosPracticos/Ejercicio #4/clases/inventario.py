from .producto import Producto

class Inventario():
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        print(type(producto))
        self.productos.append(producto)
    
    def buscar_producto(self, codigo):
        for i in self.productos:
            if i.get_code() == codigo:
                return i
        return None
            
    def actualizar_producto(self, code, nombre = None, precio = None, cantidad = None):
        producto = self.buscar_producto(code)
        if producto:
            if nombre:
                producto.nombre = nombre
            if precio:
                producto.precio = precio
            if cantidad:
                producto.cantidad = cantidad
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")
            
    def eliminar_producto(self, code):
        producto = self.buscar_producto(code)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")
         
   
    