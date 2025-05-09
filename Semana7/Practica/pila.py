from nodo import Node
from cola import Cola
# LIFO
# Last in, First Out

class Pila:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def print_pila(self):
        if not self.head:
            print("Sin elementos en la pila...")
            return
        current = self.head
        while current:
            print(current.data, end= "\n")
            current= current.next
    
    def pass_pila_cola(self):
        method_pass: Cola = Cola()
        if not self.head:
            print("Sin elementos en la pila...")
            return
        current = self.head
        while current:
            method_pass.append(current.data)
            current = current.next