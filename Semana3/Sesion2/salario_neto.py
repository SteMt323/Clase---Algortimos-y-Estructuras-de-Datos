### Modulo ###

def salario_neto(salario_bruto: float):
    inss = salario_bruto * 0.07
    ir = (salario_bruto - inss) * 0.15
    salario_neto = salario_bruto - inss - ir
    return salario_neto