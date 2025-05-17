from llamada import Llamada
from agente import Agente
class Node: 
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
        
class ColaLlamadas:
    def __init__(self):
         self.head = None
         
    def agregar_llamada_cola(self, cliente: str, motivo:str):
        new_node: Node = Node(Llamada(cliente, motivo))
        if not self.head:
            self.head = new_node
            print(f"Se ha registrado al cliente {cliente}" )
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Se ha agregado al cliente {cliente}")

    def atender_llamada(self):
        if not self.head:
            print("No hay clientes por atender...")
            return
        current = self.head
        self.head = current.next
        self.head.prev = None
        print(f"Atendiendo a {current.data.cliente}")
        
        