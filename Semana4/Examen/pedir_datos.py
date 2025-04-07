from clases.gastos import GestorGastos
from clases.persona import Persona
from datetime import datetime

def agregar_gastos(gestor):
    fecha = datetime.now()
    categoria = input("Introduzca la categoría: ")
    monto = float(input("Ingrese el monto: "))
    descripcion = input("Introduzca la descripción del gasto: ")
    gestor.agregar_gasto(fecha, categoria, monto, descripcion)

def agregar_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    carrera = input("Ingrese su carrera: ")
    return Persona(nombre, edad, carrera)

def mostrar_usuario(usuario):
    print("Bienvenido....")
    print(usuario)
