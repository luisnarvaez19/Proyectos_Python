"""
Crea una acción que determine si la secuencia “ala” aparece en una sucesión de caracteres
 cuyo final viene dado por un punto. También debes indicar cuantas veces aparece “ala”.

"""

def buscar_palabra (frase, buscar):
    """

    :param frase:  Frase a leer
    :param buscar: Se busca la cadena buscar dentro de la frase
    :return:  el numero de apariciones
    """
    nroapariciones = 0

    if  len(frase) < len(buscar):
        return nroapariciones
    for i in range(0,(len(frase)-len(buscar))):
        if frase[i:i+len(buscar)] == buscar:
            nroapariciones += 1

    return nroapariciones

fraseleer = input("Introduzca una frase: ")
buscarleer = input("Introduzca la palabra a buscar: ")
print(buscar_palabra(fraseleer, buscarleer))

