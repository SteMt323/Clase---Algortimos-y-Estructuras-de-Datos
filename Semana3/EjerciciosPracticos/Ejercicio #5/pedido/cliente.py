class Cliente():
    def __init__(self, id: int, nombre: str, contacto: str):
        self._id = id
        self.nombre = nombre
        self.contacto = contacto
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, nuevo_id):
        return ValueError("El id no puede ser modificado")
        
    def calcular_descuento(self):
        return 0
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Contacto: {self.contacto}"
        
    
class ClienteVip(Cliente):
    def __init__(self, id, nombre, contacto):
        super().__init__(id, nombre, contacto) # super() hereda atributos de nuestra clase base
        self.tipo = "VIP"
        
    def calcular_descuento(self):
        return 0.15

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Contacto: {self.contacto}, Tipo: {self.tipo}"

