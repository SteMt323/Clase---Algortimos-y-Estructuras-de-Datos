### Ejercicios de Funciones con Python ###
from funciones_listas import suma, menor, mayor

def main():
    lista = []
    n = int(input("Ingrese cantidad de elemntos a procesar: "))
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
        
    
    print("Los elementos de la lista son: ", lista)
    print(f"La suma de todos los elementos es: {suma(lista)}")
    print(f"El número menor de la lista es {menor(lista)}")
    print(f"El número mayor de la lista es {mayor(lista)}")
    
        
if __name__ == "__main__":
    main()