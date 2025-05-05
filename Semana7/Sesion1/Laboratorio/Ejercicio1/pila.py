class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class PilaLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node: Node= Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def delete(self) -> bool:
        if not self.head:
            return False
        else:
            current = self.head
            self.head = current.next
            return True
        
    def print_pila(self):
        if not self.head:
            print("Sin pendientes...")
            return
        current = self.head
        counter = 1
        print("LISTA DE PENDIENTES")
        while current:
            print(f"{counter}. {current.data}", end="\n")
            current = current.next