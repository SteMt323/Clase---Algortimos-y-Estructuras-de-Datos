"""
Problema#1
Una escuela de educación primaria requiere un algoritmo que muestre los datos de los
estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro
indicado; este parámetro puede ser cualquiera de los siguientes campos: carnet, nombres,
apellidos, peso, estatura, sexo, promedio.
"""
from estudiantes import estudiantes
from linked_list import LinkedList

def main():
    registro = estudiantes()
    list: LinkedList = LinkedList()
    n = int(input("Ingresar cantidad de estudiantes a registrar: "))
    for i in range(n):
        carnet = int(input("Carnet: "))
        nombres = input("Nombres")
        apellidos = input("Apellidos: ")
        peso = float(input("Peso: "))
        estatura = float(input("Estatura: "))
        sexo = input("Sexo: ")
        promedio = float(input("Promedio: "))
        new_student = registro.registro_estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)
        
        list.agregar_estudiantes(new_student)
        
    list.imprimir()
    
    print("\n")
    type_order = input("Ingrese el campo por cual ordenar: ")
    list.order_list_by_type(type_order)
    
if __name__ == "__main__":
    main()