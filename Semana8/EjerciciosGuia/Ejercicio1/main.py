"""
Ejercicio #1: Cola de impresión compartida
Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados
envían documentos para ser impresos. Cada documento tiene un nombre, el usuario que lo
envió y el número de páginas. El sistema debe permitir agregar documentos a la co la,
procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo
actualmente. Analice con los estudiantes cómo se evita el desorden en el uso compartido de un
recurso limitado.
"""
from menu import menu

def main():
    menu()
    
if __name__ == "__main__":
    main()