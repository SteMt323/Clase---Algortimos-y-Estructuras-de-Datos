class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        
    # Utilizo una lista doblemente enlazada circular
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail = new_node
        self.current = new_node
        
    def print_playlist_current(self):
        if not self.head:
            print("Sin listas registradas...")
            return
        current = self.head
        while current:
            if current == self.current:
                break 
            while True:
                print(f"- {current.data}", end = "\n")
                current = current.prev
                if current == self.current:
                    break
        print(f"Cancion actual: {self.current.data}")
        
    def move_fordward(self):
        if not self.head:
            print("Sin canciones registradas...")
            return
        current = self.head
        while current:
            if current == self.current:
                self.current = current.next
                return
            current = current.next
        print("No se puede avanzar...")
        
    def move_backward(self):
        if not self.head:
            print("Sin canciones registradas...")
            return
        current = self.head
        while current:
            if current == self.current:
                self.current = current.prev
                return
            current = current.prev
        print("No se puede retroceder...")
        
    def delete_song(self):
        if not self.head:
            print("Sin canciones registradas...")
            return
        current = self.head
        # Si solo hay una cancion
        if current.next == current and current.prev == current:
            self.head = None
            self.tail = None
            self.current = None
            
        # Si la cancion a eliminar es el head
        if current == self.current:
            next_node = self.head.next
            self.head = next_node
            self.head.prev = self.tail
            self.tail.next = self.head
            self.current = next_node
            return
        
        # Si la cancion a eliminar es la tail
        if self.current == self.tail:
            prev_node = self.tail.prev
            prev_node.next = self.head
            self.head.prev = prev_node
            self.tail = prev_node
            self.current = self.head
            return
        
        # Demas casos
        next_node = self.current.next
        prev_node = self.current.prev
        
        prev_node.next = next_node
        next_node.prev = prev_node
        self.current = next_node            