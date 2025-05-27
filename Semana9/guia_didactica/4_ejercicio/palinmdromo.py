class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
class L:
    def __init__(self):
        self.head = None
        self.list_word = []
        
    def preprend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        new_node.next = self.head
        self.head = new_node
        
    def dequeque(self):
        current = self.head
        while current:
            self.list_word.append(current.data)
            current = current.next
        return self.list_word
    
    def is_match(self, list_words = []) -> bool:
        self.dequeque()
        is_match = False 
        for i, elemento in enumerate(self.list_word):
            if elemento == list_words[i]:
                is_match = True
            if elemento != list_words[i]:
                is_match = False 
        return is_match

def main():
    pila = L() 
    lista = list("radara")
    for i in lista:
        pila.preprend(i.lower())
    print(pila.is_match(lista))
    
if __name__ == "__main__":
    main()