from documento import Documento

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
        
class Impresora:
    def __init__(self):
        self.head = None
        
    def append(self, name, origin_user, num_pages):
        new_node: Node = Node(Documento(name, origin_user, num_pages))
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def atender_documentos(self):
        if not self.head:
            print("Sin documentos para atender...")
            return
        current = self.head
        self.head = current.next
        self.head.prev = None
        print(f"Documento {current.data.name} atendido")

    def print_documents(self):
        if not self.head:
            print("Sin documentos para atender...")
            return
        current = self.head
        counter = 1
        while current:
            print(f"""
                  Documento {counter}: 
                  - {current.data.name}
                  - {current.data.origin_user}
                  - {current.data.num_pages}
                  
                  """)
            current = current.next
            
