"""
Control de Ventas de los empleados (3) de una empresa 
de electrodomésticos para un trimestre
"""

# Inicialización de variables
tabla_empleados = []
tabla_ventas = []


def cargar_empleados():
    for i in range(3):
        empleado = input(f"\nIngrese el nombre del empleado {i+1}: ")
        tabla_empleados.append(empleado)
        
def cargar_ventas():
    for i in range(3):
        ventas = []
        for j in range(3):
            venta = float(input(f"\nIngrese la venta del empleado {i+1} en el mes {j+1}:"))
            ventas.append(venta)
        tabla_ventas.append(ventas)
        
def impresion_ventas():
    print(f"\nNombre\t Mes1\t Mes2\t Mes3")
    for i in range(3):
        print(f"{tabla_empleados[i]}:\t {round(tabla_ventas[i][0], 2)}\t {round(tabla_ventas[i][1], 2)}\t {round(tabla_ventas[i][2], 2)}")
            
def main():
    cargar_empleados()
    cargar_ventas()
    impresion_ventas()
    
if __name__ == "__main__":
    main()