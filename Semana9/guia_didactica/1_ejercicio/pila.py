class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None 
        self.data = data
        
class PilaLinkedList:
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
        
    def delete_all_words(self):
        current = self.head
        while current:
            next_node = current.next
            current.prev = None
            current.next = None
            current = next_node
        self.head = None
   
    def add_phrases(self, data):
        self.delete_all_words()
        separate_words = data.split()
        for i in separate_words:
            self.prepend(i)    
        print(separate_words)
        print(f"La frase '{data}' se ha agregado")
    
    def reversed_phrases(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("")