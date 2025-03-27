"""
Calcular la nota de n estudiantes para los tres cortes 
de evaluación de asignatura algoritmos y estructura de datos
"""

def nota_final(not1, not2, not3):
    return (not1 + not2 + not3) / 3

def main():
    notas_estudiantes = dict()
    n = int(input("Ingrese la cantidad de estudiantes a evaluar: "))
    
    for i in range(n):
        print(f"Estudiante {i + 1}")
        nombre = input("Ingrese el nombre del estudiante: ")
        not1 = float(input("Ingrese la nota del primer corte: "))
        not2 = float(input("Ingrese la nota del segundo corte: "))
        not3 = float(input("Ingrese la nota del tercer corte: "))
        nota = float(nota_final(not1, not2, not3))
        nota = round(nota, 2) 
        nota_final_estudiantes = {nombre: nota}
        notas_estudiantes.update(nota_final_estudiantes)
        
    print(notas_estudiantes)
    
if __name__ == "__main__":
    main()
    