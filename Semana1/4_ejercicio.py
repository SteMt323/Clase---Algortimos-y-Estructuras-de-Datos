"""
Cálculo de salarios semanales de los empleados de una empresa, sabiendo que 
estos se calculan en base a las horas semanales trabajadas y deacuerdo a un
precio especificado por cada hora. Si se pasan de 48 horas semanales, las 
horas extraordinarias se pagarán a razón de dos veces la hora ordinaria.

Variables:
- horas_semanales: horas trabajadas por el empleado en una semana
- precio_hora: precio por hora trabajada
- horas_extraordinarias: horas trabajadas por el empleado en una semana que superan las 48 horas
- nombre_empleado
"""

nombre = input("Escriba el nombre del empleado: ")
horas_semanales = float(input("Escriba el número de horas trabajadas por semana: "))
precio_hora = float(input("Escriba el precio por hora trabajada: "))

if horas_semanales <= 48:
    salario_semanal = float(horas_semanales * precio_hora)
    print(f"El salario semanal de {nombre} por {horas_semanales} horas trabajadas es de: {salario_semanal}")
elif horas_semanales > 48:
    horas_extraordinarias = float(horas_semanales - 48)
    salario_semanal = float((48 * precio_hora) + (horas_extraordinarias * precio_hora))
    print(f"El salario semanal de {nombre} por {horas_semanales} horas trabajadas es {salario_semanal}")
    