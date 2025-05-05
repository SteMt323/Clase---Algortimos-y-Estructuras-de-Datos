class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
        
class PilaDoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node: Node = Node(data)
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
            print("Sin panes horneados...")
            return
        current = self.head
        print(f"Pan para vender: {current.data}")