#!/usr/bin/env cursoLN
# coding: utf-8

# # Este programa espera que los tres ficheros de datos (uno por circuscripción) se encuentren en el mismo directorio que el cuaderno.
# 
# 
# **Pseudocódigo:**
#
'''
Preguntar el nombre de la circuscripción y almacenarla en Circuscripción
Preguntar la convocatoria y almacenarla en Convocatoria.

Si la convocatoria es 2004
     almacenar en la tabla su fichero
         para cada string de la cabecera eliminar los 5 primeros caracteres
     asignar en función de la circuscripción el código postal (CP) y el número de escaños a asignar (TotalEsc)
Si la convocatoria es 2008
     almacenar en la tabla su fichero
     asignar en función de la circuscripción el código postal (CP) y el número de escaños a asignar (TotalEsc)
Si la convocatoria es 2011
     almacenar en la tabla su fichero
     asignar en función de la circuscripción el código postal (CP) y el número de escaños a asignar (TotalEsc)

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
    PenultimoResto es ese máxiomo antes de cambiar su valor: VotosRelativos [NuevaPosicion] 
    VotosRelativos [NuevaPosicion] se actualiza con VotosCircuscripcion [NuevaPosicion] / (NDiputados [NuevaPosicion]+1)
    NDiputados [NuevaPosicion] se incrementa en 1.

#  Ya está calculado el reparto, a imprimirlo:

Para cada i que toma valores desde 0 hasta la longitud de la lista (todas las listas tienen la misma longitud)
    print ("El partido  >>>> ", Nobre del partido, "  a obtenido  >>> ", número de escaños, " escaños")

# Ya está impreso el resultado electoral, vamos a identificar quien podría haber robado el último escaño

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
Circuscripcion = input ("Que circuscripción hay que evaluar? Opciones: Alicante / Barcelona / Madrid / Sevilla / Valencia  >>>  ")
Convocatoria = input ("Que convocatoria? Opciones: 2004 / 2008 / 2011  >>>  ")


if Convocatoria == "2004" :
    TodosLosVotos = pd.read_csv("convocatoria 2004.csv",index_col="Código de Provincia") 
    for i in range(0,len(Cabecera)):
        Cabecera [i]= (Cabecera [i][5:])
    if (Circuscripcion == "Alicante"):
            TotalEsc = 11
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
if Convocatoria == "2008" :
    TodosLosVotos = pd.read_csv("convocatoria 2008.csv",index_col="Codigo de Provincia")
    if (Circuscripcion == "Alicante"):
        TotalEsc = 12
        CP=3
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
if Convocatoria == "2011" :
    TodosLosVotos = pd.read_csv("convocatoria 2011.csv",index_col="Código de Provincia") 
    if (Circuscripcion == "Alicante"):
        TotalEsc = 12
        CP=3
    elif (Circuscripcion == "Barcelona"):
        TotalEsc = 31
        CP=8
    elif (Circuscripcion == "Madrid"):
        TotalEsc = 36
        CP=28
    elif (Circuscripcion == "Sevilla"):
        TotalEsc = 12 
        CP=41
    elif (Circuscripcion == "Valencia"):
        TotalEsc = 16   
        CP=46

if Convocatoria == "1989":
    TodosLosVotos = pd.read_csv("convocatoria 1989.csv", index_col="Código de Provincia")


    #  ************************************************************************************************************
#  *  Aquí comienza el ejercicio propiamente dicho. Organizando las dos listas que contienen la información.   *     
#  ************************************************************************************************************


Cabecera = list (TodosLosVotos.columns)
VotosCircuscripcion = list(TodosLosVotos.loc[CP])          

# Elimino los datos inecesarios del principio de la lista.
# En el fichero de 2011 es necesario eliminar un campo mas que en las otras convocatorias.

del (VotosCircuscripcion [0:14])
del (Cabecera [0:14])
if Convocatoria == "2011":
    del (VotosCircuscripcion [0])
    del Cabecera [0]

# Las siguientes dos instrucciones no son necesarias. Voy a eliminar los campos que no necesito
# aunque el programa funcionaría igual si no los borrase. Queda mas limpio y ordenado simplemente

del (VotosCircuscripcion [1::2])
del (Cabecera [1::2])

# La lista VotosRelativos contiene los votos a tener en cuenta en la siguiente iteracion
# la actualizaré cada vez que asigne un escaño dividiendo los votos reales de ese partido
# que estarán en VotosCircuscripcion entre el número de esacaños ya adjudicados + 1

VotosRelativos = list (VotosCircuscripcion)

# En la lista NDiputados guardaré el número de diputados asignados a cada partido en el mismo orden
# en que figuran en las demás listas. Inicialmente todos los valores son 0. Su tamaño es el mismo que el resto de las listas.

NDiputados = [0] * len (VotosRelativos)

# El siguiente bucle realiza la asignación de los escaños.
# En la variable penultimo resto, voy a guardar los votos relativos por los que se adjudica el escaño, antes de actualizarlo
# Cuando el bucle finalice, en PenultimoResto tenfo el dato para valorar la diferencia del último escaño

for i in range (0,TotalEsc):
    NuevoMaximo = max (VotosRelativos)
    NuevaPosicion = VotosRelativos.index (NuevoMaximo)

    PenultimoResto = VotosRelativos [NuevaPosicion] 
    NDiputados [NuevaPosicion] = NDiputados [NuevaPosicion] + 1
    VotosRelativos [NuevaPosicion] = VotosCircuscripcion [NuevaPosicion] / (NDiputados [NuevaPosicion]+1)

# Presentación de los escños asignados

for i in range (0,len(VotosCircuscripcion)):
    print ("El partido  >>>> ", Cabecera [i], "  a obtenido  >>> ", NDiputados[i], " escaños")
    
# Identificación del siguiente escaño. O dicho de otra forma ¿A quien le correspondía el siguiente 
# escaño?
# NuevaPosicion todavía contiene los datos del último escaño asignado

SiguienteMaximo = max (VotosRelativos) 
SiguientePosicion = VotosRelativos.index (SiguienteMaximo)
VotosNecesarios = int ((PenultimoResto - VotosRelativos [SiguientePosicion]) * (NDiputados [SiguientePosicion]+1))+1

print ("\n\n", Cabecera [SiguientePosicion],"hubiera quitado el último escaño a",Cabecera [NuevaPosicion],"si hubiera conseguido",VotosNecesarios,"votos mas\n\n")



# In[ ]:




