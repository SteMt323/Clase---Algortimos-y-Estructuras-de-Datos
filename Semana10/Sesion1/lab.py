#Arbol

def insertar(arbol, valor):
    if arbol is None:
        return [valor, None, None]
    elif valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    else:
        arbol[2] = insertar(arbol[2], valor)
    return arbol

def inorden(arbol):
    if arbol is not None:
        inorden(arbol[1])
        print(arbol[0], end="")
        inorden(arbol[2])
        
def preorden(arbol):
    if arbol is not None:
        print(arbol[0], end="")
        preorden(arbol[1])
        preorden(arbol[2])
        
def postorden(arbol):
    if arbol is not None:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end="")
        
valores = [1,2,3,4,5,6,7]
arbol = None
for valor in valores:
    arbol = insertar(arbol, valor)
    
print("Inorden: ")
inorden(arbol)
print("preorden: ")
preorden(arbol)
print("postorden: ")
postorden(arbol)