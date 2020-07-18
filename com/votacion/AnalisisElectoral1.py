#!/usr/bin/env cursoLN
# coding: utf-8


def Buscar(provincia):
    '''
        Esta funcion busca en la lista de Provincias, si la provincia dada por el usuario existe,
        en cuyo caso calcula los escaños
        :param    provincia:
        :return:  El indice o posición de la provincia dentro del arreglo Provincia
    '''
    '''
        Hacer un ciclo hasta que se termine la lista de Provincias:
            Buscar en la lista de provincias la que se llame igual a la recibida como parametro (if)
    '''
    for i in range(52):
        if Provincias[i].rstrip() == provincia:
            return i
    return -1

'''   FIN DE LA FUNCION:  Buscar   '''


def Imprimir(lista, partidos,limite):
    '''
        Imprime los partidos y los diputados y o escaños alcanzados
        :param lista:    Lista de diputados
        :param partidos: Lista de Partidos
        :param limite:   Limite de la lista de votos o de votantes
        :return:         No devuelve nada, lo que hace es imprimir
    '''

    for i in range(0, len(limite)):
        if lista[i] > 0:
            print("El partido  >>>> ", partidos[i], "  ha obtenido  >>> ", lista[i], " escaños")

'''   FIN DE LA FUNCION: Imprimir   '''



def CalculoEscaños(VotosCircuscripcion, TotalEsc, Circunscripcion ):
    '''
        Esta función calcula los escaños para la Provincia en particular dado los votos, el total de escaños
        de la Provincia y el nombre de la provincia en cuestion
        :param VotosCircuscripcion:   El número de votos de la Provincia para todos los partidos
        :param TotalEsc:        El numero total de Escaños de la provinci en cuestión
        :param Circunscripcion: La Provincia de la cual se calculan los escaños
        :return:  no devuelve nada
    '''
    '''
        Esta parte del codigo se convirtio en una funcion para poder ser llamada varias veces
        El siguiente bucle realiza la asignación de los escaños.
        En la variable penultimo resto, voy a guardar los votos relativos por los que se adjudica el escaño, antes de actualizarlo
        Cuando el bucle finalice, en PenultimoResto tengo el dato para valorar la diferencia del último escaño

        Reparto de escaños
        Para cada valor de i entre 0 y TotalEsc
        NuevoMaximo es el maximo valor de VotosRelativos
        NuevaPosicion es el indice donde se encuentra ese máximo dentro de VotosRelativos.
        PenultimoResto es ese máximo antes de cambiar su valor: VotosRelativos [NuevaPosicion]
        VotosRelativos [NuevaPosicion] se actualiza con VotosCircuscripcion [NuevaPosicion] / (NDiputados [NuevaPosicion]+1)
        NDiputados [NuevaPosicion] se incrementa en 1.

        Ya está calculado el reparto, a imprimirlo:

        Para cada i que toma valores desde 0 hasta la longitud de la lista (todas las listas tienen la misma longitud)
        print ("El partido  >>>> ", Nombre del partido, "  ha obtenido  >>> ", número de escaños, " escaños")
    '''
    PartidosStr = "PSOE,PP,IU,CDS,CIU,EAJ-PNV,RUIZ-MATEOS,HB,PA,LV-LV,UV,EA,LVE,EE,PTE-UC,ERC,PST,PAR,AIC,PCPE,BNG,CG,UPV,PSG-EG,AV-MEC,FE-JONS,ACN,VERDE,CSD,PH,PNG-PG,AR,EX.U.,PSM-ENE,PORE,IGC,PAS,PED,FPG,PAM,GRM,UNA,UA-CH.A,ENV-URV,PREPAL,UB,CEU,SEV,MV,ACI,PANCAL,COA,ARDE,PEE-(LV),R. X C.,FE (I),TAGOROR,PRGU,PRB,PNEM,P.PR.,PCE-(M.L.),LKI-EMK"
    Partidos = PartidosStr.split(",")

    # La lista VotosRelativos contiene los votos a tener en cuenta en la siguiente iteracion
    # la actualizaré cada vez que asigne un escaño dividiendo los votos reales de ese partido
    # que estarán en VotosCircuscripcion entre el número de escaños ya adjudicados + 1
    #  VotosRelativos = list (VotosCircuscripcion)

    VotosRelativos=list(VotosCircuscripcion)
    NDiputados = [0] * len(VotosRelativos)
    for i in range(0, TotalEsc):
        NuevoMaximo = max(VotosRelativos)
        NuevaPosicion = VotosRelativos.index(NuevoMaximo)

        # En estas instrucciones se analizan los empates (2da entrega).  Como el NuevoMaximo se puede repetir
        # se cuenta cuentas veces existe. Si cuantosMax es mayor que 1, es porque hay repetidos.
        cuantosMax = VotosRelativos.count(NuevoMaximo)

        Repetidos = []
        VotosMayores = []
        posicion = 0
        # Aqui se maneja el caso de los repetidos
        # Se crea un while para encontrar todos los repetidos. Se guardan en una lista
        # todos los repetidos que haya. Se usa posicion para encontrar todos los repetidos
        # Se guardan en VotosMayores, las votaciones iniciales, para asi poder saber cual obtuvo la
        # mayor votacion inicialmente y seleccionarlo

        if cuantosMax > 1:  # Es que hay repetidos
            while posicion + 1 < len(VotosRelativos):
                indice = VotosRelativos.index(NuevoMaximo, posicion)
                Repetidos.append(indice)
                posicion = indice + 1
            for i in Repetidos:
                VotosMayores.append(VotosCircuscripcion[i])
            NuevoMaximo2 = max(VotosMayores)
            NuevaPosicion = VotosMayores.index[NuevoMaximo2]

        # Una vez seleccionado cual es el partido se hacen las siguientes 3 instrucciones

        PenultimoResto = VotosRelativos[NuevaPosicion]
        NDiputados[NuevaPosicion] = NDiputados[NuevaPosicion] + 1
        VotosRelativos[NuevaPosicion] = VotosCircuscripcion[NuevaPosicion] / (NDiputados[NuevaPosicion] + 1)

    print(f'\n\nEl resultado de la asignación de escaños para la Circunscripcion de {Circunscripcion.rstrip()} es: \n')

    #  Imprime los partidos y cuantos diputados lograron
    Imprimir(NDiputados, Partidos, VotosCircuscripcion)


    # Identificación del siguiente escaño. O dicho de otra forma ¿A quien le correspondía el siguiente
    # escaño?
    # NuevaPosicion todavía contiene los datos del último escaño asignado
    '''
    Ya está impreso el resultado electoral, vamos a identificar quien podría haber robado el último escaño

    SiguienteMaximo = valor del máximo de los votos relativos (las listas están preparadas para asignar el siguiente escaño)
    SiguientePosicion es el ídice del SiguienteMaximo
    VotosNecesarios valdrá int ((PenultimoResto - VotosRelativos [SiguientePosicion]) * (NDiputados [SiguientePosicion]+1))+1

    # Y mostramos el resultado

    imprimir ("\n\n", siguiente partido,"hubiera quitado el último escaño a", ultimo partido,"si hubiera conseguido",VotosNecesarios,"votos mas\n\n")
'''

    SiguienteMaximo = max(VotosRelativos)
    SiguientePosicion = VotosRelativos.index(SiguienteMaximo)
    VotosNecesarios = int(
        (PenultimoResto - VotosRelativos[SiguientePosicion]) * (NDiputados[SiguientePosicion] + 1)) + 1

    print("\n\n", Partidos[SiguientePosicion], "hubiera quitado el último escaño a", Partidos[NuevaPosicion],
          "si hubiera conseguido", VotosNecesarios, "votos mas\n\n")

    #  ¿Con que % de votos hubiese cambiado el ganador de los resultados?
    #  Se copia la lista Ndiputados en secmax para poder modificarla y saber el max
    #  despues que el primer max se ha eliminado (calculo del segundo max)

    ganador = max(NDiputados)
    indganador = NDiputados.index(ganador)
    secmax = NDiputados.copy()
    secmax.remove(ganador)
    segundo = max(secmax)
    indsegundo = NDiputados.index(segundo)

    # (VotosCircuscripcion[indganador] - VotosCircuscripcion[indsegundo] + 1)  Esta instrucción representa la diferencia de votos
    # entre el primer lugar y el segundo Y el + 1 se se suma a la diferencia para que gane las votaciones el segundo
    porcentaje = ((VotosCircuscripcion[indganador] - VotosCircuscripcion[indsegundo] + 1) * 100) / VotosCircuscripcion[
        indganador]
    print(f'El porcentaje de votos, que hubiese cambiado el ganador de los resultados, es: {round(porcentaje, 2)} %\n\n')


'''   FIN DE LA FUNCION:  CalculoEscaños  '''


def CalculoEspaña():
    '''
        Realiza el calculo de Escaños para España
        No recibe entradas, ni produce salidas
        :return: No devuelve nada
    '''

    #  ¿Cual hubiese sido el reparto de escaños si España fuese una única circunscripción?
    #  Se le coloco a la fila del archivo circunscripcion1989.csv, el numero 1378 para poder traer la fila de los resultados totales
    Cabecera = list(TodosLosVotos.columns)
    VotosCircuscripcion = list(TodosLosVotos.loc[1378])
    del (VotosCircuscripcion[0:14])
    del (Cabecera[0:14])

    # Las siguientes dos instrucciones no son necesarias. Voy a eliminar los campos que no necesito
    # aunque el programa funcionaría igual si no los borrase. Queda mas limpio y ordenado simplemente

    del (VotosCircuscripcion[1::2])
    del (Cabecera[1::2])

    print(f'CASO ESPAÑA: En este caso se supone que España es una única circunscripcion, se suman todos los votos\n')
    print(f' y todos los escaños.\n')

    CalculoEscaños(VotosCircuscripcion, 350, "España")  # 350:  Este el el total de escaños en España y la Provincia se llama España


'''   FIN DE LA FUNCION:  CalculoEspana   '''

#
#  Todas las circunscripciones   Todas las circunscripciones     Todas las circunscripciones
#

def CalculoTodas():
    '''
        Esta funcion calcula los escaños para todas las Circunscripciones o Provincias
        :return:
    '''
    ''' 
        Se realiza un ciclo, en donde se recorreran las 52 Provincias
            Para cada Provincia se hace la limpieza necesaria de los datos y
            se calculan los escaños
    '''

    print(f'CASO TODAS LAS CIRCUNSCRIPCIONES: Son un total de 52\n')

    for i in range(52):

        VotosCircuscripcion = list(TodosLosVotos.loc[Codigos[i]])
        del (VotosCircuscripcion[0:14])
        del (VotosCircuscripcion[1::2])

        CalculoEscaños(VotosCircuscripcion, Escaños[i], Provincias[i])

'''   FIN DE LA FUNCION:  CalculoTodas   '''



'''     INICIO DEL PROGRAMA PRINCIPAL     '''

import pandas as pd
'''
    Se crean las listas de Provincias, Códigos de Provincias y Escaños
    que guardaran los datos que su nombre indica
    VotosCircuscripcion es la lista con los votos de cada partido
    Eliminar 14 elementos del principio de Cabecera y de VotosCircuscripcion
    Eliminar los elementos con indice impar de Cabecera y de VotosCircuscripcion
    VotosRelativos comienza siendo idéntica a VotosCircuscripcion
    NDiputados tiene el mismo número de elementos que las anteriores. Inicialmente todos valen 0.
'''
#  Provincias o Circunscripciones
TodosLosVotos = pd.read_csv("convocatoria1989.csv",  index_col="Código de Provincia")
Provincias=TodosLosVotos['Nombre de Provincia'].tolist()
Provincias=Provincias[: len(Provincias) - 2]
provincia = ""

# Los Codigos representan los CP: Código de Provincia
CodigosStr="4, 11, 14, 18, 21, 23, 29, 41, 22, 44, 50, 33, 7, 35, 38, 39, 2, 13, 16, 19, 45, 5, 9, 24, 34, 37, 40, 42, 47, 49, 8, 17, 25, 43, 6, 10, 15, 27, 32, 36, 28, 31, 1, 20, 48, 30, 26, 3, 12, 46, 51, 52"
CodigosStr2=CodigosStr.split(",")
Codigos=[]
for i in CodigosStr2:
    Codigos.append(int(i))

# Los escaños que corresponden a cada Provincia
Escaños = [5,9,7,7,5,6,10,12,3,3,7,9,6,7,7,5,4,5,3,3,5,3,4,5,3,4,3,3,5,3,32,5,4,5,6,5,9,5,5,8,33,5,4,7,10,9,4,10,5,16,1,1]

Convocatoria = "1989"  # Este fue el archivo csv que nos tocó
'''
    Mientras el usuario no desee finalizar hacer:
        Se pide el nombre de la provincia
        Se verifica por medio de una funcion que dicha provincia existe
            Si es España se llama a una funcion que calcule los escaños de España
            (Estas funciones serán explicadas posteriormente)
            Si es Todas  se llama a una funcion que calcule los escaños de Todas
            Sino son los casos anteriores se calculan los escaños para la provincia determinada de la siguiente forma:
                En la funcion buscar se devuelve el indice de la provincia que como explicaremos en las estructura de datos
                corresponde al indice del codigo de la provincia y al de los escaños
                Finalmente se llamara a la funcion CalculaEscaÑos con los siguientes parámetros:
                CalculoEscaños(VotosCircuscripcion, Escaños[indice],Provincias[indice])
                
                # ¿Cual hubiese sido el reparto de escaños de cada circuscripción si el segundo y el tercer partidos
                # mas votados hubiesen ido en coalición?
                
                
                
                
        sino existe se envia error al usuario 
'''
while provincia != "fin":
    print("<<<   INSTRUCCIONES DE USO   >>>\n")
    print("Escriba la Circunscripción que desee evaluar, debe incluir los acentos, para Cádiz, si escribe Cadiz no la encontrará.\n")
    print("Para todas escriba Todas, y para España como una sola Circunscripcion escriba: España\n")
    print("Si desea salir escriba fin.\n")
    provincia = input("Que circuscripción hay que evaluar?  >>>  ")
    indice=0
    indice=Buscar(provincia)
    if (provincia=="fin"):
        break
    elif (provincia == "España"):
        CalculoEspaña()
    elif (provincia == "Todas"):
        CalculoTodas()
    elif (indice == -1):
        print(f'No se encontró la Circunscripcion: {provincia}')
    else:
        CP = Codigos[indice]
        Cabecera = list(TodosLosVotos.columns)
        VotosCircuscripcion = list(TodosLosVotos.loc[CP])
        del (VotosCircuscripcion [0:14])
        del (Cabecera [0:14])

# Las siguientes dos instrucciones no son necesarias. Voy a eliminar los campos que no necesito
# aunque el programa funcionaría igual si no los borrase. Queda mas limpio y ordenado simplemente

        del (VotosCircuscripcion [1::2])
        del (Cabecera [1::2])

        CalculoEscaños(VotosCircuscripcion, Escaños[indice],Provincias[indice])

        '''
                ¿Cual hubiese sido el reparto de escaños de cada circuscripción si el segundo y el tercer partidos
                mas votados hubiesen ido en coalición? (pregunta a resolver)

                Se suman los votos del segundo y tercer partido
                Se ruedan las filas de derecha a izquierda para eliminar la columna 3
                Esto se hace para la cabecera y para los votos
                Finalmente se manda a Calcular los escaños de nuevo 
                # CalculoEscaños(VotosCircuscripcion, Escaños[indice], Provincias[indice])
        '''

        VotosSuma = VotosCircuscripcion.copy()
        VotosSuma[1] += VotosSuma[2]
        Cabcoalicion = Cabecera.copy()

        for i in range(2, len(VotosCircuscripcion)-1):
            VotosSuma[i] = VotosSuma[i+1]
            Cabcoalicion[i] = Cabcoalicion[i+1]
        VotosSuma[len(VotosCircuscripcion)-1] = 0
        Cabcoalicion[len(VotosCircuscripcion)-1] = 'Votos.nulos'


        Cabecera = Cabcoalicion.copy()
        VotosCircuscripcion = VotosSuma.copy()

        print('CASO COALICION:  En este caso hay coalición entre el partido 2 y 3 y los votos se suman en el partido 2.')

        CalculoEscaños(VotosCircuscripcion, Escaños[indice], Provincias[indice])


