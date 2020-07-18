#!/usr/bin/env cursoLN
# coding: utf-8
'''
Preguntar el nombre de la circuscripción y almacenarla en Circuscripción
Preguntar la convocatoria y almacenarla en Convocatoria.

Cabecera es la lista con los nombres de los partidos
VotosCircuscripcion es la lista con los votos de cada partido

Eliminar 14 elementos del principio de Cabecera y de VotosCircuscripcion
Si la convocatoria es 2011
    Eliminar 1 elemento mas del principio de Cabecera y de VotosCircuscripcion
Eliminar los elementos con indice impar de Cabecera y de VotosCircuscripcion

VotosRelativos comienza siendo idéntica a VotosCircuscripcion
NDiputados tiene el mismo número de elementos que las anteriores. Inicialmente todos valen 0.
'''
# Reparto de escaños
'''
Para cada valor de i entre 0 y TotalEsc
    NuevoMaximo es el maximo valor de VotosRelativos
    NuevaPosicion es el indice donde se encuentra ese máximo dentro de VotosRelativos.
    PenultimoResto es ese máximo antes de cambiar su valor: VotosRelativos [NuevaPosicion] 
    VotosRelativos [NuevaPosicion] se actualiza con VotosCircuscripcion [NuevaPosicion] / (NDiputados [NuevaPosicion]+1)
    NDiputados [NuevaPosicion] se incrementa en 1.

#  Ya está calculado el reparto, a imprimirlo:

Para cada i que toma valores desde 0 hasta la longitud de la lista (todas las listas tienen la misma longitud)
    print ("El partido  >>>> ", Nombre del partido, "  ha obtenido  >>> ", número de escaños, " escaños")
'''
def CalculoEscaños():
    '''
       Esta parte del codigo se convirtio en una funcion para poder ser llamada varias veces
       El siguiente bucle realiza la asignación de los escaños.
       En la variable penultimo resto, voy a guardar los votos relativos por los que se adjudica el escaño, antes de actualizarlo
       Cuando el bucle finalice, en PenultimoResto tengo el dato para valorar la diferencia del último escaño
    '''

    for i in range(0, TotalEsc):
        NuevoMaximo = max(VotosRelativos)
        NuevaPosicion = VotosRelativos.index(NuevoMaximo)
        # En estas instrucciones se analizan los empates (2da entrega).  Como el NuevoMaximo se puede repetir
        # se cuenta cuentas veces existe. Si cuantos es mayor que 1, es porque hay repetidos.
        cuantos = VotosRelativos.count(NuevoMaximo)

        repetidos = []
        # Se crea un while para encontrar todos los repetidos. Se guardan en una lista
        # todos los repetidos que haya. Se usa posicion para encontrar todos los repetidos
        # Se guardan en VotosMayores, las votaciones iniciales, para asi poder saber cual obtuvo la
        # mayor votacion inicialmente y seleccionarlo
        if cuantos > 1:
            while (posicion + 1 < len(valores)):
                indice = VotosRelativos.index(NuevoMaximo)
                repetidos.append(indice)
                posicion = indice + 1
            for i in repetidos:
                VotosMayores = VotosCircuscripcion[i]
            NuevoMaximo2 = max(VotosMayores)
            NuevaPosicion = VotosMayores.index[NuevoMaximo2]

        # Una vez seleccionado cual es el partido se hacen las siguientes 3 instrucciones

        PenultimoResto = VotosRelativos[NuevaPosicion]
        NDiputados[NuevaPosicion] = NDiputados[NuevaPosicion] + 1
        VotosRelativos[NuevaPosicion] = VotosCircuscripcion[NuevaPosicion] / (NDiputados[NuevaPosicion] + 1)

    for i in range(0, len(VotosCircuscripcion)):
        print("El partido  >>>> ", Cabecera[i], "  ha obtenido  >>> ", NDiputados[i], " escaños")

    # Identificación del siguiente escaño. O dicho de otra forma ¿A quien le correspondía el siguiente
    # escaño?
    # NuevaPosicion todavía contiene los datos del último escaño asignado

    SiguienteMaximo = max(VotosRelativos)
    SiguientePosicion = VotosRelativos.index(SiguienteMaximo)
    VotosNecesarios = int(
        (PenultimoResto - VotosRelativos[SiguientePosicion]) * (NDiputados[SiguientePosicion] + 1)) + 1

    print("\n\n", Cabecera[SiguientePosicion], "hubiera quitado el último escaño a", Cabecera[NuevaPosicion],
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


'''   FIN DE LA FUNCION CalculoEscaños

 
Ya está impreso el resultado electoral, vamos a identificar quien podría haber robado el último escaño

SiguienteMaximo = valor del máximo de los votos relativos (las listas están preparadas para asignar el siguiente escaño)
SiguientePosicion es el ídice del SiguienteMaximo
VotosNecesarios valdrá int ((PenultimoResto - VotosRelativos [SiguientePosicion]) * (NDiputados [SiguientePosicion]+1))+1

# Y mostramos el resultado

imprimir ("\n\n", siguiente partido,"hubiera quitado el último escaño a", ultimo partido,"si hubiera conseguido",VotosNecesarios,"votos mas\n\n")

# In[ ]:

"""

Esta primera parte no forma parte del ejercicio.
Pide los datos de convocatoria y circuscripción y prepara las variables
para que esta respuesta sea válida para todos los ejercicios.

"""

Las siguientes instrucciones cambian el texto votosXXX por XXX para una mejor presentación de 
los resultados para el caso de la convocatoria 2004 que tenía un formato diferente para 
el nombre de los partidos. No era obligatoria, pero mejora la presentación de los resultados

Además asignan el número correcto de escaños a cada circuscripción en cada convocatoria, 
que ha cambiado a lo largo del tiempo. También asignan el valor adecuado al CP (Código Postal).

'''


import pandas as pd

PartidosStr="PARTIDO SOCIALISTA OBRERO ESPAÑOL,,PARTIDO POPULAR,,IZQUIERDA UNIDA,,CENTRO DEMOCRATICO Y SOCIAL,,CONVERGENCIA I UNIO,,EUZKO ALDERDI JELTZALEA-PARTIDO NACIONALISTA VASCO,,AGRUPACION RUIZ-MATEOS,,HERRI BATASUNA,,PARTIDO ANDALUCISTA,,LOS VERDES-LISTA VERDE,,UNIO VALENCIANA,,EUSKO ALKARTASUNA,,LOS VERDES ECOLOGISTAS,,EUSKADIKO EZKERRA,,PARTIDO TRABAJADORES DE ESPAÑA-UNIDAD COMUNISTA,,ESQUERRA REPUBLICANA DE CATALUNYA,,PARTIDO SOCIALISTA DE LOS TRABAJADORES,,PARTIDO ARAGONES REGIONALISTA,,AGRUPACIONES INDEPENDIENTES DE CANARIAS,,PARTIDO COMUNISTA DE LOS PUEBLOS DE ESPAÑA,,BLOQUE NACIONALISTA GALEGO,,COALICION GALEGA,,UNITAT DEL POBLE VALENCIA,,PARTIDO SOCIALISTA GALEGO-ESQUERDA GALEGA,,ALTERNATIVA VERDA-MOVIMENT ECOLOG. DE CATALUNYA,,FALANGE ESPAÑOLA DE LAS J.O.N.S.,,ASAMBLEA CANARIA NACIONALISTA,,VERTICE ESPAÑOL REIVINDICAC. DESARROLLO ECOLOGICO,,COALICION SOCIALDEMOCRATA,,PARTIDO HUMANISTA,,PARTIDO NACIONALISTA GALEGO-PARTIDO GALEGUISTA,,ALIANZA POR LA REPUBLICA,,EXTREMADURA UNIDA,,COALICION ELECTORAL ESQUERRA NACIONALISTA,,PARTIDO DE LOS OBREROS REVOLUCIONARIOS DE ESPAÑA,,INDEPENDIENTES DE GRAN CANARIA,,PARTIU ASTURIANISTA,,UNIDAD CENTRISTA-P.E.D.,,FRENTE POPULAR GALEGA,,PARTIDO REGIONAL DE MADRID,,GRUPO DE RADICALES EN MADRID,,UNIDA NACIONALISTA ASTURIANA,,UNION ARAGONESISTA-CHUNTA ARAGONESISTA,,ESQUERRA NACIONALISTA VALENCIANA - URV,,PARTIDO REGIONALISTA DEL PAIS LEONES,,UNIO BALEAR,,PARTIDO CEUTA UNIDA,,SIETE ESTRELLAS VERDES,,MOVIMIENTO VERDE,,AGRUPACION CIUDADANA INDEPENDIENTE,,PARTIDO NACIONALISTA DE CASTILLA Y LEON,,COALICION ALICANTINISTA ALICANTON,,ACCION REPUBLICANA DEMOCRATICA ESPAÑOLA,,PARTIDO ECOLOGISTA DE EUSKADI (LISTA VERDE),,RADICALES POR CANTABRIA,,FALANGE ESPAÑOLA INDEPENDIENTE,,TAGOROR O ASAMBLEA CONEJERA DE LANZAROTE,,PARTIDO REGIONALISTA DE GUADALAJARA,,PARTIDO RADICAL BALEAR,,PARTIDO NACIONALISTA ESPAÑOL DE MELILLA,,PARTIDO PROVERISTA,,PARTIDO COMUNISTA DE ESPAÑA (MARXISTA-LENINISTA),,COALICION ELECTORAL LKI-EMK"
PartidosStr=PartidosStr.replace(",,",",")
Partidos=PartidosStr.split(",")


Circuscripcion = input("Que circuscripción hay que evaluar? Opciones: Alicante / Barcelona / Madrid / Sevilla / Valencia  >>>  ")
#Convocatoria = input("Que convocatoria? Opciones: 1989  >>>  ")

# Este fue el archivo csv que nos tocó

Convocatoria = "1989"

if Convocatoria == "1989":
#    columnas=("Nombre de Comunidad","Código de Provincia","Nombre de Provincia")
    TodosLosVotos = pd.read_csv("convocatoria1989.csv",  index_col="Código de Provincia")
    if (Circuscripcion == "Alicante"):
            TotalEsc = 9
            CP = 3
    elif (Circuscripcion == "Barcelona"):
            TotalEsc = 31
            CP=8
    elif (Circuscripcion == "Madrid"):
            TotalEsc = 35
            CP=28
    elif (Circuscripcion == "Sevilla"):
            TotalEsc = 12
            CP=41
    elif (Circuscripcion == "Valencia"):
            TotalEsc = 16
            CP=46

#  ************************************************************************************************************
#  *  Aquí comienza el ejercicio propiamente dicho. Organizando las dos listas que contienen la información.   *
#  ************************************************************************************************************
Cabecera = list (TodosLosVotos.columns)
VotosCircuscripcion = list(TodosLosVotos.loc[CP])
del (VotosCircuscripcion [0:14])
del (Cabecera [0:14])

# Las siguientes dos instrucciones no son necesarias. Voy a eliminar los campos que no necesito
# aunque el programa funcionaría igual si no los borrase. Queda mas limpio y ordenado simplemente


del (VotosCircuscripcion [1::2])
del (Cabecera [1::2])

# La lista VotosRelativos contiene los votos a tener en cuenta en la siguiente iteracion
# la actualizaré cada vez que asigne un escaño dividiendo los votos reales de ese partido
# que estarán en VotosCircuscripcion entre el número de escaños ya adjudicados + 1

VotosRelativos = list (VotosCircuscripcion)

# En la lista NDiputados guardaré el número de diputados asignados a cada partido en el mismo orden
# en que figuran en las demás listas. Inicialmente todos los valores son 0. Su tamaño es el mismo que el resto de las listas.

NDiputados = [0] * len(VotosRelativos)

print(f'\n\nEl resultado de la asignación de escaños para la Circuscripcion de {Circuscripcion} es: \n')
CalculoEscaños()


# ¿Cual hubiese sido el reparto de escaños de cada circuscripción si el segundo y el tercer partidos
# mas votados hubiesen ido en coalición?

VotosSuma = VotosCircuscripcion.copy()
VotosSuma[1] += VotosSuma[2]
Cabcoalicion = Cabecera.copy()

for i in range(2, len(VotosCircuscripcion)-1):
    VotosSuma[i] = VotosSuma[i+1]
    Cabcoalicion[i] = Cabcoalicion[i+1]
VotosSuma[len(VotosCircuscripcion)-1] = 0
Cabcoalicion[len(VotosCircuscripcion)-1] = 'Votos.nulos'


VotosRelativos = VotosSuma.copy()
Cabecera = Cabcoalicion.copy()
VotosCircuscripcion = VotosSuma.copy()
NDiputados = [0] * len(VotosRelativos)

print('En este caso hay coalición entre el partido 2 y 3 y los votos se suman en el partido 2.')
print(f'\n\nEl resultado de la asignación de escaños para la Circuscripcion de {Circuscripcion} es: \n')

CalculoEscaños()

#  ¿Cual hubiese sido el reparto de escaños si España fuese una única circunscripción?
#  Se le coloco a la fila el numero 1378 para poder traer la fila de los resultados totales
Cabecera = list (TodosLosVotos.columns)
VotosCircuscripcion = list(TodosLosVotos.loc[1378])

del (VotosCircuscripcion [0:14])
del (Cabecera [0:14])

# Las siguientes dos instrucciones no son necesarias. Voy a eliminar los campos que no necesito
# aunque el programa funcionaría igual si no los borrase. Queda mas limpio y ordenado simplemente


del (VotosCircuscripcion [1::2])
del (Cabecera [1::2])

VotosRelativos = list (VotosCircuscripcion)
NDiputados = [0] * len(VotosRelativos)
TotalEsc = 350     #  Este el el total de escaños en España

print(f'En este caso se supone que España es una única circunscripcion, se suman todos los votos\n')
print(f' y todos los escaños.\n')
print(f'\n\nEl resultado de la asignación de escaños para la Circuscripcion España es: \n')

CalculoEscaños()
#
#  Todas las circunscripciones   Todas las circunscripciones     Todas las circunscripciones


# TodosLosVotos = pd.read_csv("convocatoria1989.csv",  index_col="Código de Provincia")
Provincias=TodosLosVotos['Nombre de Provincia'].tolist()
Provincias=Provincias[: len(Provincias) - 2]
print(Provincias)
# Los Codigos representan los CP: Código de Provincia
CodigosStr="4, 11, 14, 18, 21, 23, 29, 41, 22, 44, 50, 33, 7, 35, 38, 39, 2, 13, 16, 19, 45, 5, 9, 24, 34, 37, 40, 42, 47, 49, 8, 17, 25, 43, 6, 10, 15, 27, 32, 36, 28, 31, 1, 20, 48, 30, 26, 3, 12, 46, 51, 52"
CodigosStr2=CodigosStr.split(",")
Codigos=[]
for i in CodigosStr2:
    Codigos.append(int(i))
print(Codigos)
Escaños = [5,9,7,7,5,6,10,12,3,3,7,9,6,7,7,5,4,5,3,3,5,3,4,5,3,4,3,3,5,3,32,5,4,5,1,10,5,16,6,5,9,5,5,8,4,33,1,9,5,4,7,10]

for i in range(52):

    Circuscripcion=Provincias[i]

    VotosCircuscripcion = list(TodosLosVotos.loc[Codigos[i]])
    del (VotosCircuscripcion[0:14])
    del (VotosCircuscripcion[1::2])
    print(f'Voy por la {Circuscripcion} que es la {i}, con CP: {Codigos[i]} Escaños: {Escaños[i]} y {len(VotosCircuscripcion)}')
    print(VotosCircuscripcion)

    VotosRelativos = list (VotosCircuscripcion)
    NDiputados = [0] * len(VotosRelativos)
    TotalEsc = Escaños[i]

    CalculoEscaños()

