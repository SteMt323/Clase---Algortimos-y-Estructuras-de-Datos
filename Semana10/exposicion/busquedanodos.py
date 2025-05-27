"""
Busqueda en arboles binarios con nodos
"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None 
        
class BinaryTree:
    def __init__(self):
        self.root = None 
        
    def insertion(self, data):
        new_node: Node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        self.insertion_aux(self.root, new_node)
        
    def insertion_aux(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self.insertion_aux(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insertion_aux(current.right, new_node)
                
                
    def search_node(self, data):
        return self.aux_search_node(self.root, data)
    
    def aux_search_node(self, node, data):
        if not node:
            return None
        if data == node.data:
            return node.data
        elif data < node.data:
            return self.aux_search_node(node.left, data)
        elif data > node.data:
            return self.aux_search_node(node.right, data)
        
def main():
    binary_tree: BinaryTree = BinaryTree()
    binary_tree.insertion(2)
    binary_tree.insertion(7)
    binary_tree.insertion(2)
    binary_tree.insertion(4)
    binary_tree.insertion(3)
    binary_tree.insertion(1) 
    print("Buscar el nodo con valor 7")
    print(binary_tree.search_node(8))
    
if __name__ == "__main__":
    main()