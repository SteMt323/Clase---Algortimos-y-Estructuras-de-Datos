class Pila:
    def __init__(self):
        self.lista = []
        
    def append(self, data):
        return self.lista.append(data)
    
    def pop_function(self):
        return self.lista.pop()
    
    def print(self):
        n = len(self.lista)
        for i in reversed(self.lista):
            print(i) 
        return
    
    def estado(self) -> bool:
        if self.lista: return True
        else: return False 
    
def main():
    pila: Pila = Pila()
    pila.append("a")
    pila.append("b")
    pila.append("c")
    pila.append("d")
    pila.print()
    print("\n")
    pila.pop_function()
    pila.print()
    
if __name__ == "__main__":
    main()