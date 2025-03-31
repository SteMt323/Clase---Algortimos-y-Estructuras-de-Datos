def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total
    
def menor(lista):
    lista.sort()
    return lista[0]
    
def mayor(lista):
    lista.sort()
    return lista[-1]