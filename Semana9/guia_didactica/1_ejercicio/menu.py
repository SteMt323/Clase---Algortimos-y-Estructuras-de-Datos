from pila import PilaLinkedList

def menu():
    pila: PilaLinkedList = PilaLinkedList()
    while True:
        print("\n1. Ingrese una frase ")
        print("2. Invertir la frase ")
        print("3. Salir")
        opc = input("Seleccione: ")
        match opc:
            case "1":
                phrase = input("Ingrese una frase: ",)
                pila.add_phrases(phrase)
                
            case "2":
                pila.reversed_phrases()
                
            case "3": break
            case _: print("Eleccion inválida...")