from binaryTree import BinaryTree as Tree
import random as rm

class Inputs:
    def __init__(self):
        pass
    
    def agregar(self):
        tree: Tree = Tree()
        id = rm.randint(1000,9999)
        nombre = input("Ingrese el nombre del estudiante: ")
        grupo = input("Ingrese el grupo del estudiante: ")
        while True:
            nota = float(input("Ingrese la nota final del estudiante"))
            if type(nota) == float:
                break
            else: print("Nota inválida, ingrese nuevamente...")
        tree.insert(id, nombre, grupo, nota)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  