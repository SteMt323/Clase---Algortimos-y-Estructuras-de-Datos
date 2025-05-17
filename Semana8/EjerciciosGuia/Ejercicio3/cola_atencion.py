from paciente import Paciente

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None 
        self.data = data 
        
class ColaAtencion:
    def __init__(self):
        self.head = None
        
    def agregar_cliente(self, nombre: str, servicio: str):
        new_node: Node = Node(Paciente(nombre, servicio))
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def atender_paciente(self):
        if not self.head:
            print("Sin pacientes por atender...")
            return
        current = self.head
        self.head = current.next

        print(f"Se ha atendido al paciente {current.data.nombre}")
        
    def mostrar_pacientes(self):
        if not self.head:
            print("Sin pacientes en la cola de espera")
            return
        current = self.head
        counter = 1
        while current:
            print(f"Paciente {counter}: \nNombre: {current.data.nombre}\nServicio: {current.data.servicio}")
            current = current.next
            
            