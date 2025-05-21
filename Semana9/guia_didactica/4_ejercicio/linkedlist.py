from elemento import *

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class ColaLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, nombre, prioridad):
        new_node: Node = Node(elemento(nombre, prioridad))
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    def dequeque(self):
        if not self.head:
            print("Sin tareas registradas...")
            return
        
        for priority in range(1, 6):
            current = self.head
            while current:
                prev_node = current.prev
                next_node = current.next
                if current.data.prioridad == priority:
                    # Evaluar el head
                    if self.head.data.prioridad == priority:
                        self.head = next_node
                        if self.head:
                            self.head.prev = None
                        return

                    # Evaluar el tail
                    if not current.next:
                        prev_node.next = None
                        return
                    # Evaluar demas casos
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    return
                
                current = current.next
                
    def print_cola(self):
        if not self.head:
            print("Sin elementos en la lista: ")
            return
        current = self.head
        counter = 1
        while current:
            print(f"Elemento {counter}:\n- Nombre: {current.data.nombre}\n- Prioridad: {current.data.prioridad}")
            counter = counter + 1
            current = current.next 