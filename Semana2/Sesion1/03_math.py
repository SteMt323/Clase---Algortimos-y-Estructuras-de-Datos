"""
Elabore un programa para calcular la quinta potencia, la raíz cuadrada, el
exponencial, el logaritmo natural y el valor absoluto de un número introducido por el
teclado
"""

import math

numero = float(input("Introduce un número: "))

# Calcular la quinta potencia
quinta_potencia = math.pow(numero, 5)

# Calcular la raíz cuadrada 
if numero >= 0:
    raiz_cuadrada = math.sqrt(numero)
else:
    raiz_cuadrada = "No definida (número negativo)"

# Calcular el exponencial
exponencial = math.exp(numero)

# Calcular el logaritmo natural 
if numero > 0:
    logaritmo_natural = math.log(numero)
else:
    logaritmo_natural = "No definido (número no positivo)"

# Calcular el valor absoluto
valor_absoluto = abs(numero)

# Mostrar los resultados
print(f"Quinta potencia: {quinta_potencia}")
print(f"Raíz cuadrada: {raiz_cuadrada}")
print(f"Exponencial: {exponencial}")
print(f"Logaritmo natural: {logaritmo_natural}")
print(f"Valor absoluto: {valor_absoluto}")