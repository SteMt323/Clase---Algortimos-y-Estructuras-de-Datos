"""
Desarrollar un programa que permita al usuario gestionar una cuenta bancaria. El programa
debera utilizar un menú que permita realizar diferentes operaciones 
sobre el saldo de la cuenta

Menú de opciones:
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir

El programa debe permitir al usuario ingresar la cantidad para depositar o retirar,
actualizar el saldo y mostrar los resultados. Si se elige la opción de retiro, debe 
verificar que el saldo sea suficiente.
"""
import os

cuenta = []
cuenta.append(float(0))

def depositar_dinero():
    saldo_actual = float(0)
    if cuenta:
        saldo_actual = cuenta[0]
        
    print("________________________________________________________")
    print(f"Su saldo actual es de: {saldo_actual}")
    print("________________________________________________________")
    saldo_entrante = float(input("Ingrese la cantidad de dinero a depositar: \n"))
    cuenta[0] = (saldo_actual + saldo_entrante)
    print(f"Deposito exitoso su nuevo saldo es de: {cuenta[0]}")
    print("________________________________________________________")
    
def consultar_saldo():
    if cuenta: 
        print("________________________________________________________")
        print(f"Saldo actual: \t {cuenta[0]}")
        
def retirar_dinero():
    
    saldo_actual = float(0)
    if cuenta:
        saldo_actual = cuenta[0]
        
    print("________________________________________________________")
    saldo_retiro = float(input("Ingrese la cantidad a retirar: \n"))
    
    if saldo_retiro > saldo_actual:
        print("El dinero que intenta retirar es mayor al saldo actual de la cuenta...")
        print("Por favor intente mas tarde....")
        return False
    else: 
        cuenta[0] = (saldo_actual - saldo_retiro)
        print("________________________________________________________")
        print(f"El saldo ha sido retirado exitosamente \n Monto retirado: {saldo_retiro}")
        print("________________________________________________________")
        print(f"Saldo actual de la cuenta: {cuenta[0]}")
        print("________________________________________________________")
        return True
    
def menu():
    while True:
        print("_____Cuenta Bancaria_____")
        print("1. Consultar saldo")
        print("2. Depositar saldo")
        print("3. Retirar saldo")
        print("4. Salir")
        print("__________________________")
        opc = int(input("Seleccione una opción: "))
        
        if opc == 1:
            consultar_saldo()
            os.system("pause")
        elif opc == 2:
            depositar_dinero()
            os.system("pause")
        elif opc == 3:
            retirar_dinero()
            os.system("pause")
        elif opc == 4:
            break
        else:
            print("Opción inválida, intente nuevamente...")
            os.system("pause")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()