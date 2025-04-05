


from paqueteDebusqueda import busqueda_lineal, busqueda_binaria


listaa = [1, 2, 4, 6, 7, 8,23, 26,66]

print("La lista de numeros es de: ", listaa)

numero0 = int(input("Digame el numero a buscar: "))

#strip quita los espacios en blandp

tipoDeBusqueda = input("Que busqueda usara? (Lineal|binaria): ").strip().lower()

if tipoDeBusqueda == "lineal":
    resultado = busqueda_lineal(listaa, numero0)
elif tipoDeBusqueda == "binaria":
    resultado = busqueda_binaria(listaa, numero0)
else:
    print("la busqueda no es valida")
    resultado = -1

if resultado != -1:
    print("EL elemento se encontro en la posicion: ", resultado)
else:
    print("Elemento no fue encontrado")
