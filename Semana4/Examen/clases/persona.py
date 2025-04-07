class Persona():
    def __init__(self, nombre: str, edad: int, carrera: str):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}"