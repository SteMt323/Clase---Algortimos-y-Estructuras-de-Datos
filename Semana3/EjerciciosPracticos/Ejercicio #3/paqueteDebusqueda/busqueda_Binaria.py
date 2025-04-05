def busqueda_binaria(lista, numero):
    limite_izquierdo = 0
    limite_derechp = len(lista)-1

    #mientras que la izquierda nno pase a la derecha, se sigue buscando
    # pero si izquiera es mayor a derecha el numeo no se encuentra
    while limite_izquierdo <= limite_derechp:
    #se calcula el indice medio
        medio = (limite_derechp + limite_izquierdo) //2

        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            limite_izquierdo = medio + 1
        else:
            limite_derechp = medio - 1

    return -1
