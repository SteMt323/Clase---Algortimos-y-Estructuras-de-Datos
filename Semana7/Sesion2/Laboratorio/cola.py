import os

class Cola:
    def __init__(self):
        self.lista = []
        
    def is_void(self) -> bool:
        if self.lista:
            return False
        else: return True
    
    def enqueque(self, data):
        if len(self.lista) < 5:
            self.lista.append(data)
            return True
        else: return False
    
    def dequeque(self):
        if len(self.lista) > 0:
            self.lista.pop(0)
            return True
        else: return False
            
    def print_queque(self):
        if len(self.lista) != 0:
            for i in self.lista:
                print(i)
            return 
        else: 
            print("Lista vacía")
            return
    
    def cantidad_lista(self) -> int:
        return len(self.lista)
    
def menu():
    queque: Cola = Cola()
    while True:
        print("\n")
        print("1. Agregar Cliente")
        print("2. Atender Cliente")
        print("3. Consultar Clientes") 
        print("4. Mostrar Clientes")
        print("5. Mostrar Cantidad de la Lista")
        print("5. Salir")
        opc = input("Elija una opción: ")
        match opc:
            case "1": 
                nombre = input("Ingrese el nombre del cliente: ")
                if queque.enqueque(nombre): print("Se ha registrado el cliente")
                else: print("Se ha excedido el tamaño de la lista.")
                os.system("pause")
            case "2": 
                if queque.dequeque(): print("Se ha atendido al primer cliente")
                else: print("No se ha podido atender al primer cliente")
                os.system("pause")
            case "3": 
                if queque.is_void(): print("La lista de clientes esta vacia...")
                else: print("La lista de clientes esta llena") 
                os.system("pause")
            case "4": 
                print("Lista de Clientes: ")
                queque.print_queque()
                os.system("pause")
            case "5":
                print(f"Cantidad: {queque.cantidad_lista()}")
            case "6": 
                print("Saliendo...")
                break
            case _: print("Opción inválida")

def main():
    menu()
    
if __name__ == "__main__":
    main()