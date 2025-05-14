"""
Ejercicio #4: Simulación de atención de procesos por el microprocesador
Diseñe un programa que simule cómo un microprocesador atiende procesos en una cola de
ejecución. Cada proceso tiene un identificador, un nombre y una duración estimada en
milisegundos. A medida que el procesador queda libre, atiende al siguiente proceso en orden
de llegada (FIFO - First In, First Out). El sistema debe permitir agregar procesos a la cola,
mostrar el proceso en ejecución y visualizar los procesos pendientes.
"""
from menu import menu

def main():
    menu()
    
if __name__== "__main__":
    main()