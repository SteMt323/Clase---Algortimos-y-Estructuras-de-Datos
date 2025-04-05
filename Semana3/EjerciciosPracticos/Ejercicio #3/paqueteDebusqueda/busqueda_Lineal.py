def busqueda_lineal(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            #devuelve la posicion del numero encontrado lol
            return i
    return -1 