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
            Cuenta_Bancaria.insert(0, nombreUsuario)
        else:
            break

        

    while True: 
        try:
            saldoNuevo = float(input("Ingrese la catidad que desea depositar: "))
            
            SaldoActual += saldoNuevo
            Cuenta_Bancaria.insert(1,saldoNuevo)
            #
            break
        except ValueError: print("Solo numeros son admitidos: ")

    # NuevoSaldo = [nombreUsuario, SaldoActual]
    


def Consultar_Dinero():
    while True:
        print(f"su saldo es: {Cuenta_Bancaria[1]} ")
        break



def main():
    Consultar_Dinero()


if __name__ == "__main__" :
    main()