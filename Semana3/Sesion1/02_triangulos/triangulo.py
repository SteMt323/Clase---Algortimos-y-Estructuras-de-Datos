"""
Ejercicio 2: Desarrollar un programa que cargue los datos de un 
triángulo. Implementar un método o función para determinar el tipo 
de triangulo (equlátero, isóceles o escaleno)
"""
def tipo_triangulo(medida1: float, medida2: float, medida3: float):
    if medida1 == medida2 == medida3:
        return print("El tirangulo es equlátero")
    elif medida1 == medida2 or medida1 == medida3 or medida2 == medida3:
        return print("El tirangulo es isóceles")
    else:
        return print("El tirangulo es escaleno")

def main():
    med1 = float(input("Ingrese la medida 1: "))
    med2 =  float(input("Ingrese la medida 2: "))
    med3 = float(input("Ingrese la medida 3: "))
    tipo_triangulo(med1, med2, med3)
    
if __name__ == "__main__":
    main()
