"""
Operaciones de grafos osbre listas de adyecencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
}
"""

grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
}

"""
Vertices A, B, C
A --> ['C']
B --> []
C --> ['A']

El vértice A apunta a C y viceversa
"""

class Grafo:
    def __init__(self):
        self.grafo = {} # Será el diccionario de listas de adyecencia
        
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            print(f"El vértice '{vertice}' ya eiste.")
            
    def agregar_arista_no_direccional(self, origen, destino): # Arista no dirigido
        if origen in self.grafo[destino] or destino in self.grafo[origen]:
            print("Ya hay conexion entre los 2 vertices...")
            return
        elif origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append(destino)
            self.grafo[destino].append(origen)
        else:
            print("Faltan vertices...")
            
    def agregar_arista_direccional(self, origen, destino):
        if origen in self.grafo[destino] or destino in self.grafo[origen]:
            print("Ya habia conexion entre los vertices....")
            return
        elif origen in self.grafo and destino in self.grafo:
            self.grafo[origen].append(destino)
        else:
            print("Faltan vertices...")
            
    def eliminar_arista(self, origen, destino):
        if origen in self.grafo and destino in self.grafo:
            if destino in self.grafo[origen]:
                self.grafo[origen].remove(destino)
            if origen in self.grafo[destino]:
                self.grafo[destino].remove(origen)
            else:
                print("Faltan vertices...")
                
    def mostrar_conexiones(self):
        for vertice in self.grafo:
            print(f"{vertice} --> {self.grafo[vertice]}")
            
    def conexion(self, origen, destino) -> bool:
        if origen in self.grafo:
            return destino in self.grafo[origen]
        return False
    
def menu():
    grafo: Grafo = Grafo()
    while True:
        print("\n\n1. Agregar Vertices...")
        print("2. Agregar Aristas No Direccionales...")
        print("3. Agregar Aristas Direccionales...")
        print("4. Eliminar Aristas...")
        print("5. Mostrar Conexiones...")
        print("6. Evaluar las Conexiones....")
        print("7. Salir...")
        opc = input("Seleccione una opcion: ")
        match opc:
            case "1":
                vertice = input("Ingrese el dato: ")
                grafo.agregar_vertice(vertice)
            case "2":
                origen = input("Ingrese el vertice origen del arista: ")
                destino = input("Ingrese el vertice destino del arista: ")
                grafo.agregar_arista_no_direccional(origen, destino)
            case "3":
                origen = input("Ingrese el vertice origen del arista: ")
                destino = input("Ingrese el vertice destino del arista: ")
                grafo.agregar_arista_direccional(origen, destino)
            case "4":
                origen = input("Ingrese el vertice origen a eliminar: ")
                destino = input("Ingrese el vertice destino a eliminar: ")
                grafo.eliminar_arista(origen, destino)
            case "5":
                grafo.mostrar_conexiones()
            case "6":
                origen = input("Ingrese el vertice origen a evaluar: ")
                destino = input("Ingrese el vertice destino a evaluar: ")
                print(grafo.conexion(origen, destino))
            case "7":
                print("Saliendo...")
                break
            case _: print("Opcion invalida, ingrese denuevo...")
    
def main():
    menu()

if __name__ == "__main__":
    main()