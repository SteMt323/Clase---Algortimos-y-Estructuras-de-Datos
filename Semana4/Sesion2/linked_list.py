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
        
    def eliminar(self, data):
        current = self.head
        
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
            
        if not current:
            return
        
        prev.next = current.next
        current = None
        
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
        
        
def menu():
    lista = LinkedList()
    while True:
        print("----Menu de opciones----")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Modificar")
        print("5. Imprimir")
        print("6. Salir")
        opc = input("Seleccione una de las opciones:  ")
        
        if opc == "1":
            try:
                data = int(input("Ingrese un número entero:´\n"))
                lista.agregar(data)
                print("Elemento agregado...")
                
            except ValueError:
                print("Elemento no agregado, ingrese de nuevo... ")
                
        elif opc == "5":
            lista.imprimir()
            
        elif opc == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente...")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()