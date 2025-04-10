"""
Construir un método imprimeInverso que imprima los elementos de una lista
enlazada de enteros en orden inverso a partir de una posición p. (6 puntos)
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def agregar(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def imprimir(self):
        current = self.head
        if not current:
            print("Lista vacía")
            return
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        
    def reverse_list(self, position):
        # funcion recursiva
        def helper(nodo, current_position): 
            # caso base
            if not nodo:
                return
            # llamada recursiva
            helper(nodo.next, current_position + 1)
            if current_position >= position:
                print(nodo.data, end="->")
        
        helper(self.head, 1)
        print("None")

def main():
    lista: LinkedList = LinkedList()
    for i in range(1, 13):
        lista.agregar(i)
        
    print("Lista original")
    lista.imprimir()
    
    while True:
        position = int(input("Ingrese desde la posicion a revertir (no mayor a 13)"))
        if position > 13:
            print("Posicin no valida... intente nuevamente")
        else:
            print(f"Lista inversa desde la posicion {position}")
            lista.reverse_list(position)
            break
            
if __name__ == "__main__":
    main()