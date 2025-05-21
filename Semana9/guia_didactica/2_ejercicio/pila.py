class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
        
class PilaLinkedList:
    def __init__(self):
        self.head = None
        self.split_words = []
        self.pares ={
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
    def prepend(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def sacar_elemento(self):
        if not self.head:
            return
        current = self.head
        self.head = current.next
        
    def delete_all_words(self):
        current = self.head
        while current:
            next_node = current.next
            current.prev = None
            current.next = None
            current = next_node
        self.head = None    
    
    def agregar_parentesis(self, data):
        self.delete_all_words()
        self.split_words = list(data)
        print("Se procesado la cadena...")
        self.imprimir()
        
    def match_parentesis(self) -> bool:
        for i in self.split_words:
            if i in self.pares.values():
                self.prepend(i)
            elif i in self.pares.keys():
                if self.pares[i] == self.head.data:
                    self.sacar_elemento()
        if not self.head:
            print("La cadena esta balanceada...")
            return True
        else: 
            print("La cadena no esta balanceada...")
            
    def imprimir(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next