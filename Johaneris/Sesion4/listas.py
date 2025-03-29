'''Contro de ventas de los emppleados (3) de una emporesa de electrodopmestiucos para
un trimestre'''

#primero crear dos listas vacias

tablaVentas=[]
ventasEmpleados = []

#prtimeor se llena la tabla de los empleados 

for i in range(3):
    print(f"\nIngrese el nombre de empleado {i + 1}: ", end  = " ")
    nombre = input()
    ventasEmpleados.append(nombre)

#este for reciorere las columnasd 
for j in range(3):
    fila = []
    for k in range(3):
        print(f"\ningrese la venta del empleado {j + 1} de mes {k + 1}: ", end = " ")
        ventas = float(input())
        fila.append(ventas)
    tablaVentas.append(fila)

print("\nEmpleados: ", ventasEmpleados)
print("\nVentas: ", tablaVentas)
print("\nInformacion de ventas")
print("Nombre\tEnero\tFebrero\tMarzo")

#rn lugasr de ange nos da el indixce donde estan los nombre 
for i, nombre in enumerate(ventasEmpleados):
    print(f"{nombre}\t{tablaVentas[i][0]:,.1f}\t{tablaVentas[i][1]:,.1f}\t{tablaVentas[i][2]:,.1f}\t")
