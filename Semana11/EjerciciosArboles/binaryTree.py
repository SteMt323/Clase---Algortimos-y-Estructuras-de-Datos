from estudiante import Estudiante
class Node:
    def __init__(self, data: Estudiante):
        self.data = data 
        self.left = None
        self.right = None 
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, id, nombre, grupo, nota):
        new_node: Node = Node(Estudiante(id, nombre, grupo, nota))
        if not self.root:
            self.root = new_node
            return
        self.recursive_insert(self.root, new_node)
        
    def recursive_insert(self, current, new_node):
        if new_node.data.id < current.data.id:
            if current.left is None:
                current.left = new_node
            else:
                self.recursive_insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.recursive_insert(current.right, new_node)
        
    def print_inorder(self):
        self.recursive_inorder(self.root)
        
    def recursive_inorder(self, node):
        if node is not None:
            self.recursive_inorder(node.left)
            print(node.data)
            self.recursive_inorder(node.right)
            
    
    # Vamos a implementar las funciones de eliminar a ver que nota
    
    def delete_node(self, data):
        self.root = self.recursive_delete_node(self.root, data)
        
    def recursion_delete_node(self, current, data):
        if not current:
            print("Arbol vacío")
            return
        
        if data < current.data.id:
            current.left = self.recursion_delete_node(current.left, data)
        elif data > current.data.id:
            current.right = self.recursion_delete_node(current.right, data)
        else:
            # Solo si el nodo a eliminar es un nodo hoja 
            if not current.left and not current.right:
                return None
            # Con un solo nodo hijo
            elif not current.right:
                return current.left
            elif not current.left:
                return current.right
            
            # Dos nodos hijos
            else:
                sucesor = self.search_sucesor_node(current.right)
                current.data = sucesor.data
                current.right = self.recursion_delete_node(current.right, sucesor.data)
            return current
                
    def search_sucesor_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    