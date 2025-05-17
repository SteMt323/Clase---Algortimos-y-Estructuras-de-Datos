from solicitud import Solicitud

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
        
class ColaSolicitudes:
    def __init__(self):
        self.head = None
        
    def append_solicitud(self, usuario: str, archivo: str):
        new_node: Node = Node(Solicitud(usuario, archivo))
        if not self.head:
            self.head = new_node
            print("Solicitud agregada a la cola de espera...")
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print("Solicitud agregada a la cola de espera...")
        
    def mostrar_usuarios_archivo(self, archivo: str):
        if not self.head:
            print("Sin solicitudes en la cola de espera...")
            return
        access: bool = False
        current = self.head
        print(f"Solicitudes de usuarios del archivo: {archivo}")
        while current:
            if current.data.archivo == archivo:
                print(f"\nEl usuario {current.data.usuario}: {current.data.archivo}")
                access = True
            current = current.next
        if access == False:
            print(f"Ningún usuario a accedido al archivo {archivo}")
            return
        else: return
        
    def atender_solicitud(self):
        if not self.head:
            print("Soin solicitudes en la lista de espera...")
            return
        
        current = self.head
        self.head = current.next
        self.head.prev = None
        print(f"La soplicitud del usuario {current.data.usuario}, ya se ha atendido...")
        return
    
    def imprimir_pendientes(self):
        if not self.head:
            print("Sin solicitudes en la cola de espera...")
            return
        current = self.head
        counter = 1
        print("Cola de Espera: ")
        while current:
            print(f"\nSolicitud {counter}:\n- Usuario: {current.data.usuario}\n- Archivo: {current.data.archivo}")
            current = current.next
                    
                
            
                    