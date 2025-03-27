"""
Calcular la nota de n estudiantes para los tres cortes 
de evaluación de asignatura algoritmos y estructura de datos
"""

def promedio(not1, not2, not3):
    return (not1 + not2 + not3) / 3

n = int(input("Ingrese la cantidad de estudiantes a evaluar: "))

i= 0
while i < n:
    i += 1
    nombre = input(f"Ingrese el nombre del estudiante {i}: ")
    nota1 = float(input(f"Ingrese la primera nota del estudiante {i}: "))
    nota2 = float(input(f"Ingrese la segunda nota del estudiante {i}: "))
    nota3 = float(input(f"Ingrese la tercera nota del estudiante {i}: "))
    
    nota_final = round(promedio(nota1, nota2, nota3))
    if float(nota_final) < 60:
        print("Reprobado")
    elif float(nota_final) >= 60 and float(nota_final)<= 69:
        print("Regular")
    elif float(nota_final) >= 70 and float(nota_final)<= 79:
        print("Bueno")
    elif float(nota_final) >= 80 and float(nota_final)<= 89:
        print("Muy Bueno")
    elif float(nota_final) >= 90 and float(nota_final)<= 100:
        print("Excelente")
    else:
        print("Número inválido")
        