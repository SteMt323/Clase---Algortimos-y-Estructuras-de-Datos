'''Ejercicio No. 3
Desarrollar un programa que se comporte como un diccionario Inglés-Español; esto es, solicitará
una palabra en inglés y escribirá la correspondiente palabra en español. Para hacer más sencillo
el ejercicio, el número de parejas de palabras estará limitado a 5. Por ejemplo, suponer que
introducimos las siguientes parejas de palabras:
book libro
green verde
mouse ratón
Una vez finalizada la introducción de las listas de palabras, pasamos al modo traducción, de
forma que si introducimos green, la respuesta ha de ser verde. Si la palabra no se encuentra, se
emitirá un mensaje que lo indique.
El programa constará de dos métodos, aparte de Main():
1. crearDiccionario(). Este método creará el diccionario.
2. traducir(). Este método realizará la labor de traducción.'''
import os

Diccionario = []



def crearDiccionario():
    print("="*20, "Bienvenido al pequeño diccionario :3", "="*20)
    while True:
        for i in range(5):
            Palabra_Ingles=input("Ingrese la palabra en ingles: ")
            Palabra_Spanish=input("Ingrese la palabra en español: ")
        # if not Palabra_Ingles.isalpha() or Palabra_Spanish.isalpha():
        #         print("Solo se pueden ingresar letras")
                
            # else:
            Diccionariochico = [Palabra_Ingles, Palabra_Spanish]
                #Siempre recordar el append
            Diccionario.append(Diccionariochico)
            print("Palabras agregadas exitosamente!")
        os.system("pause")
        return
        
    

# def traducir():
#     PalabraTraducir = input("Ingrese la palabra a traducir (Ingles a español): ")
#     for i, word in enumerate(Diccionario):
#         if PalabraTraducir == Diccionario[i][word]:
#             print(Diccionario[1])

def traducir():
    print()
    print()
    n = int(input("Ingrese cuantas palabras va a traducir, maximo 5: "))
    enuentra = False
    
    for k in range(n):
        PalabraTraducir = input("Ingrese la palabra a traducir (Ingles a español): ")
        for i in Diccionario:
            if i[0] == PalabraTraducir:
                print(f"La traduccion es: {i[1]}")
                enuentra = True
                break
        
    if not enuentra:    
        print("No se enconttro la palabra")
            

def main():
    crearDiccionario()
    traducir()


if __name__ == "__main__":
    main()






            
