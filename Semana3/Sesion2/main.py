from clase_empleado import Empleado

def main():
    empleados = []
    n = int(input("Ingrese la cantiodad de empleados a ingresar: "))
    
    print("\nIngrese los datops de los empleados...")
    for i in range(n):
        nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
        salario_bruto = float(input(f"Ingrese el salario bruto del empleado {i + 1}: "))
        empleado = Empleado(nombre, salario_bruto)
        empleados.append(empleado)
        
        
    print("Datos empleados")
    for i in empleados:     
        print(f"{i.get_nombre()}: {round(i.get_salario_neto(), 2)}")
        
if __name__ == "__main__":
    main()
        