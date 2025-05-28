"""
Algoritmo de busqueda binaria
"""

def busqueda_binaria_recursiva(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1  # No encontrado

    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif objetivo < lista[medio]:
        return busqueda_binaria_recursiva(lista, objetivo, inicio,  medio - 1)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)

numeros = [5, 12, 18, 23, 37, 45, 59, 66, 72, 88]
valor = 12
pos = busqueda_binaria_recursiva(numeros, valor, 0, len(numeros) - 1)

if pos != -1:
    print(f"Encontrado en la posición {pos}")
else:
    print("No encontrado")
