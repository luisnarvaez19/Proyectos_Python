import  pandas as pd

def buscar(provincia):

    for i in range(52):
        if Provincias[i].rstrip() == provincia:
            return i
    return 0

valores=[500,200,100,1000,900,300, 1000]
nuevo=max(valores)
print(nuevo)
# print(valores.index(nuevo))
print(valores.count(nuevo))
#print(valores.index(nuevo,4))
print(f'La long de la lista es: {len(valores)}')
posicion=0
while (posicion+1<len(valores)):
    valor = valores.index(nuevo, posicion)
    print(valor)
    posicion=valor+1
ganador=max(valores)
print(f'el ganador: {ganador}')
cuenta=valores.count(ganador)
secmax=valores
print(secmax)
if cuenta>1:
    while cuenta>0:
        secmax.remove(ganador)
        cuenta-=1
print(secmax)
PartidosStr="PARTIDO SOCIALISTA OBRERO ESPAÑOL,,PARTIDO POPULAR,,IZQUIERDA UNIDA,,CENTRO DEMOCRATICO Y SOCIAL,,CONVERGENCIA I UNIO,,EUZKO ALDERDI JELTZALEA-PARTIDO NACIONALISTA VASCO,,AGRUPACION RUIZ-MATEOS,,HERRI BATASUNA,,PARTIDO ANDALUCISTA,,LOS VERDES-LISTA VERDE,,UNIO VALENCIANA,,EUSKO ALKARTASUNA,,LOS VERDES ECOLOGISTAS,,EUSKADIKO EZKERRA,,PARTIDO TRABAJADORES DE ESPAÑA-UNIDAD COMUNISTA,,ESQUERRA REPUBLICANA DE CATALUNYA,,PARTIDO SOCIALISTA DE LOS TRABAJADORES,,PARTIDO ARAGONES REGIONALISTA,,AGRUPACIONES INDEPENDIENTES DE CANARIAS,,PARTIDO COMUNISTA DE LOS PUEBLOS DE ESPAÑA,,BLOQUE NACIONALISTA GALEGO,,COALICION GALEGA,,UNITAT DEL POBLE VALENCIA,,PARTIDO SOCIALISTA GALEGO-ESQUERDA GALEGA,,ALTERNATIVA VERDA-MOVIMENT ECOLOG. DE CATALUNYA,,FALANGE ESPAÑOLA DE LAS J.O.N.S.,,ASAMBLEA CANARIA NACIONALISTA,,VERTICE ESPAÑOL REIVINDICAC. DESARROLLO ECOLOGICO,,COALICION SOCIALDEMOCRATA,,PARTIDO HUMANISTA,,PARTIDO NACIONALISTA GALEGO-PARTIDO GALEGUISTA,,ALIANZA POR LA REPUBLICA,,EXTREMADURA UNIDA,,COALICION ELECTORAL ESQUERRA NACIONALISTA,,PARTIDO DE LOS OBREROS REVOLUCIONARIOS DE ESPAÑA,,INDEPENDIENTES DE GRAN CANARIA,,PARTIU ASTURIANISTA,,UNIDAD CENTRISTA-P.E.D.,,FRENTE POPULAR GALEGA,,PARTIDO REGIONAL DE MADRID,,GRUPO DE RADICALES EN MADRID,,UNIDA NACIONALISTA ASTURIANA,,UNION ARAGONESISTA-CHUNTA ARAGONESISTA,,ESQUERRA NACIONALISTA VALENCIANA - URV,,PARTIDO REGIONALISTA DEL PAIS LEONES,,UNIO BALEAR,,PARTIDO CEUTA UNIDA,,SIETE ESTRELLAS VERDES,,MOVIMIENTO VERDE,,AGRUPACION CIUDADANA INDEPENDIENTE,,PARTIDO NACIONALISTA DE CASTILLA Y LEON,,COALICION ALICANTINISTA ALICANTON,,ACCION REPUBLICANA DEMOCRATICA ESPAÑOLA,,PARTIDO ECOLOGISTA DE EUSKADI (LISTA VERDE),,RADICALES POR CANTABRIA,,FALANGE ESPAÑOLA INDEPENDIENTE,,TAGOROR O ASAMBLEA CONEJERA DE LANZAROTE,,PARTIDO REGIONALISTA DE GUADALAJARA,,PARTIDO RADICAL BALEAR,,PARTIDO NACIONALISTA ESPAÑOL DE MELILLA,,PARTIDO PROVERISTA,,PARTIDO COMUNISTA DE ESPAÑA (MARXISTA-LENINISTA),,COALICION ELECTORAL LKI-EMK"
PartidosStr=PartidosStr.replace(",,",",")
Partidos=PartidosStr.split(",")
print(Partidos)
print(len(Partidos))
Escaños = [5,9,7,7,5,6,10,12,3,3,7,9,6,7,7,5,4,5,3,3,5,3,4,5,3,4,3,3,5,3,32,5,4,5,1,10,5,16,6,5,9,5,5,8,4,33,1,9,5,4,7,10]
print(len(Escaños))
TodosLosVotos = pd.read_csv("convocatoria1989.csv")
Codigosf=TodosLosVotos["Código de Provincia"].tolist()
print(Codigosf)
Codigosf=Codigosf[: len(Codigosf) - 2]
Codigos=[]
for i in Codigosf:
    Codigos.append(int(i))
print(Codigos)
PartidosStr="PSOE,PP,IU,CDS,CIU,EAJ-PNV,RUIZ-MATEOS,HB,PA,LV-LV,UV,EA,LVE,EE,PTE-UC,ERC,PST,PAR,AIC,PCPE,BNG,CG,UPV,PSG-EG,AV-MEC,FE-JONS,ACN,VERDE,CSD,PH,PNG-PG,AR,EX.U.,PSM-ENE,PORE,IGC,PAS,PED,FPG,PAM,GRM,UNA,UA-CH.A,ENV-URV,PREPAL,UB,CEU,SEV,MV,ACI,PANCAL,COA,ARDE,PEE-(LV),R. X C.,FE (I),TAGOROR,PRGU,PRB,PNEM,P.PR.,PCE-(M.L.),LKI-EMK"
Partidos=PartidosStr.split(",")
print(len(Partidos))
Provincias=TodosLosVotos['Nombre de Provincia'].tolist()
Provincias=Provincias[: len(Provincias) - 2]
print(Provincias)
provincia=input("Introduzca la provincia que quiere buscar: ")
indice=0
indice=buscar(provincia)
print(indice)
if (indice == 0):
    print(f'No se encontró la Circunscripcion: {provincia}')
else:
    print(f'La provincia es: {Provincias[indice]}')
# if provincia in Provincias:
#     print("Si")
# else:
#     print("No")
# print(Provincias.index(provincia))
Provincias=[i.rstrip() for i in Provincias]
print(Provincias)
Escaños = [5,9,7,7,5,6,10,12,3,3,7,9,6,7,7,5,4,5,3,3,5,3,4,5,3,4,3,3,5,3,32,5,4,5,6,5,9,5,5,8,33,5,4,7,10,9,4,10,5,16,1,1]
print(len(Escaños))
fruits = ['apple', 'banana', 'cherry','banana']

x = fruits.index("banana", 1)

print(x)
