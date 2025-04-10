"""
Implementar un método que recibe una lista de enteros L y un número entero n de
forma que modifique la lista mediante el borrado de todos los elementos de la lista
que tengan este valor. (8 puntos)

L = lista de enteros
n = numero a borrar de la lista

Objetivo: Borrar todos los elementos de la lista que coincidan con la variable "n"
"""

class Node():
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
        
    def eliminar(self, data) -> bool:
        current: Node = self.head
        prev: Node = None
        
        while current != None:
            if current.data == data:
                if prev != None: prev.next = current.next
            else:
                prev = current
                
            current = current.next
        
    def buscar(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
        
    def imprimir(self):
        current = self.head
        if not current:
            print("La lista esta vacía...")
            return
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        
# Definir el método
def remover_dato(lista: LinkedList, dato: int):
    # Eliminamos el dato
    lista.eliminar(dato)

# Creamos la lista
lista: LinkedList = LinkedList()

lista.agregar(5)
lista.agregar(8)
lista.agregar(14)
lista.agregar(28)
lista.agregar(8)
lista.agregar(8)

print("Lista inicial:")
lista.imprimir()

dato_a_borrar = int(input("Ingrese el dato a eliminar: "))

print(f"Dato a borrar: {dato_a_borrar}")
remover_dato(lista, dato_a_borrar)

print("Nueva lista: ")
lista.imprimir()