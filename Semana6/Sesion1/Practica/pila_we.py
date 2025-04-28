import os
class Pila:
    def __init__(self):
        self.lista = []
        
    def append(self, data):
        return self.lista.append(data)
    
    def backforward(self):
        return self.lista.pop()
    
    def print_current_page(self):
        if not self.lista:
            return "Sin historial"
        return self.lista[-1]
    
def menu():
    pila: Pila = Pila()
    while True:
        print("__NAVEGACION DE WEB")
        print("1. Ingresar a una web")
        print("2. Retroceder")
        print("3. Mostrar Pagina Actual")
        print("4. Salir")
        opc = input("Seleccione una opciopn: ")
        match opc:
            case "1":
                data = input("Ingrese la web: ")
                pila.append(data)
                os.system("pause")
                
            case "2":
                pila.backforward()
                os.system("pause")
            case "3":
                print(pila.print_current_page())
                os.system("pause")
            case "4":
                print("Saliendo...")
                break
            
            case _:
                print("Opcion invalida...")
                os.system("pause")
                
def main():
    menu()
    
if __name__ == "__main__":
    main()