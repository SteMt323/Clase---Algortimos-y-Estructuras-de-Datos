class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data): # Insertar al Final
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def prepend(self, data): # Insertar al Inicio
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def delete_inicio(self):
        if not self.head:
            print("Sin elementos en la lista...")
            return
        current = self.head
        current = current.next
        current.prev = None
        self.head = current
        
    def delete_final(self):
        if not self.head:
            print("Sin elementos en la lista...")
            return