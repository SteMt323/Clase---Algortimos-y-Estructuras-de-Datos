"""
Desarrollar un programa que se comporte como un diccionario Inglés - Español; esto
es, solicitará una palabra en inglés y escribirá la correspondiente palabra en español.
Para hacer más sencillo el ejercicio, el número de parejas estará limitado a 5.
Por ejemplo, suponer que introducimos las siguientes palabras:

book - libro
green - verde
mouse - ratón

Una vez finalizada la inbtroducción de las listas de palabras, pasamos al modo traducción, 
de forma que si introducimos green, la respuesta ha de ser verde. Si la palabra no se encuentra, 
se emitirá un mensaje que lo indique.

El programa copnstará de dos métodos, aparte de Main():
1. crear Diccionario(). Este método creará el diccionario.
2. traductor(). Este método realizará la labor de traducción
"""
diccionario = []
hola = "Holamundi"

def agregar_diccionario(clave, valor):
    diccionario.append([clave, valor])

def traductor(clave):
    for i in diccionario:
        if i[0] == clave:
            return i[1]
    return None

def main():
    num = 0
    while True:
        num = int(input("Introduzca la cantidad de pares de palabras a ingresar (5 max): "))
        if num <= 5:
            break
    for i in range(num):
        word = input(f"Ingrese la palabra ({i+1}) en ingles: ")
        palabra = input(f"Ingrese la palabra ({i+1}) en espanol: ")
        word.replace(" ","") # Aqui si el usuario ingresa espacios vacios, se les eliminan
        palabra.replace(" ","")
        agregar_diccionario(word, palabra)
        
    traducir = input("Traduzca la palabra de ingles a espanol: ")
    traduccion = traductor(traducir)
    if traduccion:
        print(f"La traducción de '{traducir}' es: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

        
if __name__ == "__main__":
    main()