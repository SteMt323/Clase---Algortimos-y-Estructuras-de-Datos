class Node:
    def __init__(self, data):
        self.next = None
        self.data = data 
        
class LinkedList():
    def __init__(self):
        self.head
        
    def append(self, data): # Insersion al final
        new_node: Node =  Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    
    def prepend(self, data): # Insersion al inicio
        new_node: Node =  Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertion_espefic(self, index, data):
        new_node: Node =  Node(data)
        temp = self.data
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
            
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        elif index > counter:
            print("Index fuera de rango...")
            return
        else:
            current = self.head
            new_counter = 0
            while current:
                if new_counter == (index - 1):
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
                new_counter += 1

    def delete(self, data):
        if not self.head:
            print("Lista vacia....")
            return
        
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return
            
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
            
        if not temp:
            return
        
        prev.next = temp.next
        temp = None
        
        
    def search(self, data) -> bool:
        if not self.head:
            print("Lista vacia....")
            return
        
        temp = self.head
        while temp:
            if temp.data == data:
                print(temp.data)
                return True
            temp = temp.next
        print("Valor no encontrado...")
        return False
        
    def impresion(self):
        if not self.head:
            print("Lista vacia....")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")
        


        
        