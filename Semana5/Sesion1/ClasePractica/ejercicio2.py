"""
Construir un método countVocales que determine la cantidad de vocales
en una lista de caracteres.
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def agregar(self, data):
        new_node = Node(data)
        if not self.head:
           self.head = new_node 
           return
       
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def imprimir(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
    def countVocals(self):
        vocals = ["a", "e", "i", "o", "u"]
        counter = 0
        temp = self.head
        while temp:
            if temp.data.lower() in vocals:
                counter += 1
            temp = temp.next
        return counter
    

def main():
    lista: LinkedList = LinkedList()
    
    lista.agregar("h")
    lista.agregar("o")
    lista.agregar("l")
    lista.agregar("a")
    lista.agregar("m")
    lista.agregar("u")
    lista.agregar("n")
    lista.agregar("d")
    lista.agregar("o")
    
    lista.imprimir()
    print(lista.countVocals())
    
if __name__ == "__main__":
    main()
        