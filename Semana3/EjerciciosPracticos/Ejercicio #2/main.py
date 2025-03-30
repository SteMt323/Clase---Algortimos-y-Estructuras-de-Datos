### Ejercicio 2 - Módulo de ordenamiento ###
"""
Se requiere que los estudiantes diseñen un módulo independiente que contenga
implementaciones de algoritmos de ordenamiento simples (bubble sort). El
objetivo es que, a partir de una función principal, se invoquen los métodos del
módulo para ordenar una lista de números y demostrar la correcta separación de
responsabilidades, fomentando la modularidad y la reutilización del código.
"""

import sort_algortihms

def main():
    lista = [7, 12, 2, 8, 20, 43, 56, 1, 9, 0]
    list_sort = sort_algortihms
    print(f"Lista original: \n{lista}")
    print("\nLista ordenada: ")
    print(list_sort.bubble_sort(lista))
    
if __name__ == "__main__":
    main()