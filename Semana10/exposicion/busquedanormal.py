"""
Busqque en arboles binarios con listas
"""

def buscar_en_arbol(arbol, valor, indice=0):
    if indice >= len(arbol) or arbol[indice] is None:
        return False

    if arbol[indice] == valor:
        return True
    elif valor < arbol[indice]:
        return buscar_en_arbol(arbol, valor, 2 * indice + 1)  # Izquierda
    else:
        return buscar_en_arbol(arbol, valor, 2 * indice + 2)  # Derecha

arbol = [50, 30, 70, 20, 40, 60, 80]

# Búsquedas
print(buscar_en_arbol(arbol, 60))  # True
print(buscar_en_arbol(arbol, 90))  # False
