import os

"""
Programa de atención al Cliente
"""
class Clinica:
    def __init__(self):
        self.paciente = []
        
    def append_registrar(self):
        name = input("Ingrese el nombre del paciente: ")
        self.paciente.append(name)
        
    def atender(self):
        if self.paciente:
            atendido = self.paciente.pop(0)
            print(f"Paciente {atendido} atendido...")
            return 
        print("Sin pacientes por atender...")
        return 
    
    def print_pacientes(self):
        if self.paciente:
            print("Lista de pacientes: ")
            for i, paciente in enumerate(self.paciente, start = 1):
                print(f"{i}. {paciente}")
            return 
        print("Sin pacientes registrados...") 
        return 
    
def menu():
    clinica: Clinica = Clinica()
    while True:
        print("1. Registrar Paciente")
        print("2. Atender Paciente")
        print("3. Mostrar Pacientes")
        print("4. Salir")
        opc = input("Ingrese una opcion: ")
        match opc:
            case "1":
                clinica.append_registrar()
                os.system("pause")
            case "2": 
                clinica.atender()
                os.system("pause")
            case "3": 
                clinica.print_pacientes()
                os.system("pause")
            case "4":
                print("Saliendo...")
                break
            case _:print("Opcion invalida, intente nuevamente...")
            
def main():
    menu()
    
if __name__ == "__main__":
    main()