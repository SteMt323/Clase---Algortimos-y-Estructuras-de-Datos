class Cliente():
    lista_cliente = []
    def __init__(self, id: int, nombre: str, contacto: str):
        self._id = id
        self.nombre = nombre
        self.contacto = contacto
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, nuevo_id):
        print("El id no puede ser modificado")
        
    def agregar_cliente(self):
        Cliente.lista_cliente.append({"id": self.id, "nombre": self.nombre, "contacto": self.contacto})
        
    
class TipoCliente(Cliente):
    def __init__(self, id, nombre, contacto, tipo):
        super().__init__(id, nombre, contacto) # super() hereda atributos de nuestra clase base
        self.tipo = tipo
        
    def agregar_cliente(self):
        Cliente.lista_cliente.append({
            "id": self.id,
            "nombre": self.nombre,
            "contacto": self.contacto,
            "tipo": self.tipo
        })
        
    def descuento(self):
        if self.tipo == "regular":
            descuento = 0
        elif self.tipo == "bronce":
            descuento = 0.10
        elif self.tipo == "plata":
            descuento = 0.15
        elif self.tipo == "oro":
            descuento = 0.20
        else:
            descuento = 0
        return descuento
