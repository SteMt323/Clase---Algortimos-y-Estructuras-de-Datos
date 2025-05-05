from paciente import Paciente

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class PilaDoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, nombre, edad, tipo_sangre):
        new_node: Node = Node(Paciente(nombre, edad, tipo_sangre))
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def pop(self) -> bool:
        if not self.head: 
            return False
        current = self.head
        self.head = current.next
        return True
    
    def peek(self):
        if not self.head:
            print("Sin pacientes registrados...")
            return
        current = self.head
        print("Paciente Actual: ")
        print(f"Nombre: {current.data.nombre}")
        print(f"Edad: {current.data.edad}")
        print(f"Tipo de Sangre: {current.data.tipo_sangre}")