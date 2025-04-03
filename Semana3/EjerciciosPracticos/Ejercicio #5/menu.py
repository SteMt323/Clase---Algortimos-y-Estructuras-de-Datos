from pedido.pedido import Pedido
from datos import detallar_cliente, elegir_productos

def menu():
    while True:
        print("___Procesamientos de pedidos y clientes____")
        print("1. Facturar Pedido")
        print("2. Salir...")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            cliente = detallar_cliente()
            productos = elegir_productos()
            pedido = Pedido(cliente, productos)
            
            pedido.generar_pedido()
        elif opc == "2":
            print("Saliendo... ")
            break
        else: 
            print("Opoción inválida, intente nuevamente... ")
        