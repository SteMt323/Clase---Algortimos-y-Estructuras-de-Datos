class estudiantes:
    def __init__(self):
        self.diccionario = dict()
        
        
    def registro_estudiante(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio) -> dict:
        self.diccionario = {
            "carnet": carnet,
            "nombres": nombres,
            "apellidos": apellidos,
            "peso": peso,
            "estatura": estatura,
            "sexo": sexo,
            "promedio": promedio
        }
        return self.diccionario