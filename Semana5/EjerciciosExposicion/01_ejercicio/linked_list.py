class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def agregar_estudiantes(self, student):
        new_node: Node = Node(student)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def values_in_list(self) -> bool:
        if not self.head:
            return False
        return True
        
    def imprimir(self):
        if not self.values_in_list():
            print("No hay ningun registro...")
            return
            
        temp = self.head
        while temp:
            print(temp.data, end= "\n\n")
            temp = temp.next
            
    def order_list_by_type(self, campo: str):
        if not self.values_in_list():
            print("No hay registros...")
            return
        
        lista_estudiantes = []
        temp = self.head
        while temp:
            lista_estudiantes.append(temp.data)
            temp = temp.next
    
        try:
            ordenados = sorted(lista_estudiantes, key=lambda x: x[campo])
        except KeyError:
            print(f"Campo '{campo}' no válido.")
            return
    
        for estudiante in ordenados:
            print(estudiante, end="\n\n")

    

        
        
            