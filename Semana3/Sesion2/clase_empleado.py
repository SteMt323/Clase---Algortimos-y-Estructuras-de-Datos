
class Empleado():
    def __init__(self, nombre: str, salario_bruto: float):
        self.__nombre = nombre
        self.__salario_bruto = salario_bruto
        
        
    def get_nombre(self):
        return self.__nombre
        
    def get_salario_neto(self):
        from salario_neto import salario_neto
        return salario_neto(self.__salario_bruto)