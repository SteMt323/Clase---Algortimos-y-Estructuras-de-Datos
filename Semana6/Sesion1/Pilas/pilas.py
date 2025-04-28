class Pila:
    def __init__(self):
        self.lista = []
        
    def is_void(self) -> bool:
        if any in self.lista:
            return False
        else: return True
        
    def append(self, data):
        return self.lista.append(data) 
    
    def delete(self):
        return self.lista.pop()
    
    def print_list(self):
        for i, lista in enumerate(self.lista):
            print(f"- {self.lista[i]}") 
        return
    
    def size_list(self) -> int:
        return len(self.lista)
    
def main():
    lista: Pila = Pila()
    print(f"Esta Vacio? {lista.is_void()}")
    lista.append(1)  
    lista.append(2.2)     
    lista.append("hola mundo")     
    lista.append(4)           
    lista.print_list()
    print("Eliminando ultimo elemento: ")
    lista.delete()
    lista.print_list()
    print(f"Tamaño de la lista: {lista.size_list()}")

if __name__ == "__main__":
    main()