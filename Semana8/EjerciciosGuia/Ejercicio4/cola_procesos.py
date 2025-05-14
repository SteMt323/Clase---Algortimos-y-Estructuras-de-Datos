from procesos import Procesos

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class ProcesosCola:
    def __init__(self):
        self.head = None
        
    def agregar_procesos(self, id, name, duracion):
        new_node: Node = Node(Procesos(id, name, duracion))
        if not self.head:
            self.head = new_node
            print(f"Proceso {name} se ha agregado")
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        print(f"Proceso {name} se ha agregado")
        
    def atender_proceso(self):
        if not self.head:
            print("Sin procesos en la pila de pendientes...")
            return
        current = self.head
        self.head.next = current.next
        self.head.prev = None
        print(f"Proceso Actual: {current.data.name}")
        
    def procesos_pendientres(self):
        if not self.head:
            print("Sin procesos pendientes...")
            return
        current = self.head
        counter = 1
        while current: 
            print(f"\n\nProceso {counter}:\n- Id: {current.data.id} \n- Nombre: {current.data.name}\n- Tiempo: {current.data.duracion} mm")
            current = current.next
        