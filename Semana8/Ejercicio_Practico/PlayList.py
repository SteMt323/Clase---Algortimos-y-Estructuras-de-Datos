import os

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data 
        
class PlayList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        new_node.prev = current
        
        
    def escuchado(self):
        if not self.head:
            print("Sin musicas en la playlist...")
            return
        current = self.head
        self.head = current.next 
        
    def print(self):
        if not self.head:
            print("Sin musicas en la playlist...")
            return
        current = self.head
        counter = 1
        while current:
            print(f"{counter}. {current.data}")
            counter += 1
            current = current.next 
            
def menu():
    playlist: PlayList = PlayList()
    while True:
        print("___ Cola de PlayList___")
        print("1. Agregar Música")
        print("2. Pasar Música")
        print("3. Ver PlayList")
        print("4. Salir")
        opc = input("Seleccione una opcion: ")
        match opc: 
            case "1": 
                data = input("Ingrese la cancion: ")
                playlist.append(data)
                os.system("pause")
            case "2":
                playlist.escuchado()
                os.system("pause")
            case "3":
                playlist.print()
                os.system("pause")
            case "4":
                print("Saliendo...")
                break
            case _: print("Opcion invalida")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()