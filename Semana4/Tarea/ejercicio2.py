"""
Construir un método cantVocales que determine la cantidad de vocales
almacenadas en una lista de caracteres. (6 puntos)


Objetivo: Determinar la cantidad de vocales dentro de una lista
{a, e, i, o, u}
"""

class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def agregar(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    
    def count_vocals(self):
        vocals = ["a", "e", "i", "o", "u"]
        current = self.head
        counter = 0
        while current:
            if current.data.lower() in vocals:
                counter += 1
            current = current.next
        return counter
    
    def imprimir(self):
        current = self.head
        if not current:
            print("Lista vacía")
            return
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
def main():
    lista: LinkedList = LinkedList()
    lista.agregar("a")
    lista.agregar("d")
    lista.agregar("i")
    lista.agregar("d")
    lista.agregar("a")
    lista.agregar("s")
    
    print("Lista: ")
    lista.imprimir()
    
    print("Contando las vocales")
    print(lista.count_vocals())
    
if __name__ == "__main__":
    main()
    
    