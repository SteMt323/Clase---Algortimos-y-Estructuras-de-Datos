'''Desarrollar un programa que permita al usuario gestionar una cuenta bancaria. El programa
deberá utilizar un menú que permita realizar diferentes operaciones sobre el saldo de la cuenta.
Menú de opciones:
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
El programa debe permitir al usuario ingresar la cantidad para depositar o retirar, actualizar el
saldo y mostrar los resultados. Si se elige la opción de retiro, debe verificar que el saldo sea
suficiente.'''
import os
SaldoActual = 0.0
Nombre = ""

Cuenta_Bancaria =[Nombre, SaldoActual]

# el problema al usar el insert en este codigo es el siguiente, que estoy insertando valores en lugar de actualiarlo, lo que puedo hacer es pasarle ese valor a la variable

def Depositar():

    print("-"*20, "Bienvenido al Banco :3", "-"*20)
    

    while True:
        nombreUsuario = input("Ingrese su nombre: ")
        if not  nombreUsuario.isalpha():
            print("solo puede ingresar letras")
            # AQUI ESTOY ACTIALIZANDO EL VALOR EN LA POSICIO 0 DE LA LISTA EN LUGAR DE INSERTARLO
            Cuenta_Bancaria[0]= nombreUsuario
        break
    
    while True: 
        try:
            saldoNuevo = float(input("Ingrese la catidad que desea depositar: "))
            
            SaldoDeposito = SaldoActual + saldoNuevo
            # Cuenta_Bancaria.insert(1,saldoNuevo)
            Cuenta_Bancaria[1] = SaldoDeposito
            #
            break
        except ValueError: print("Solo numeros son admitidos: ")
    return

    # NuevoSaldo = [nombreUsuario, SaldoActual]

def Consultar_Dinero():
    print(f"{Cuenta_Bancaria[0]} tu saldo actual es: {Cuenta_Bancaria[1]} ")
    os.system("pause")
    return

def Retirar_Dinero():
    
    while True:
        Retiro = float(input("Ingrese el salgo que desea retirar: "))  
        if Cuenta_Bancaria[1] < Retiro:
            print("Saldo insuficiente para realizar el retiro")
        else:
            while True: 
                try:
            
                    SaldoDeRetiro -= Retiro
                    # Cuenta_Bancaria.insert(1,saldoNuevo)
                    Cuenta_Bancaria[1] = SaldoDeRetiro
                except ValueError: print("Solo numeros son admitidos: ")
                break
    

    # NuevoSaldo = [nombreUsuario, SaldoActual]

def menu_Principal():
    

    while True:
        print(""" Bienvenido al sistema de gestion bancaria
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir""")
        opcion = int(input())
        if opcion == 1:
            Consultar_Dinero()
        elif opcion == 2:
            Depositar()
        elif opcion == 3:
            Retirar_Dinero()
        elif opcion == 4:
            print("Saliento del sistema")
            break

    



def main():
    menu_Principal()


if __name__ == "__main__" :
    main()

        

