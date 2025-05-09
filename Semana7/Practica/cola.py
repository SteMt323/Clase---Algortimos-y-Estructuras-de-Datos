from nodo import Node
# FIFO
# First in, first out

class Cola:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next: 
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def print_cola(self):
        if not self.head:
            print("Sin elementos en la cola...")
            return
        current = self.head
        while current:
            print(current.data, end="\n")
            current = current.next