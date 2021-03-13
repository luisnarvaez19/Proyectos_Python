import numpy as np

#Constantes
G=(6.67259e-11*(3600)**2/(1000)**3) #km**3/(kg*h**2)
R=(6.37e+3) #km
M=(5.976e+24) #kg

#Coordenadas polares
r0=(4*R) #Se calcula para r0=4*R y para r0=2*R (km).
phi0=(0)

r1=[r0] #Se declara como lista (km)
phi1=[phi0]

#Coordenadas cartesianas declaradas como listas
x1=[r1[-1]*np.cos(phi1[-1])] #km
y1=[r1[-1]*np.sin(phi1[-1])] #km

x1.extend(y1)
print(f"x1 es: {x1} ")
print(f"y1 es: {y1} ")

# CONSTANTES
G = 6.67259E-11 / 1E9  # Constante de gravitación universal, en km^3/(kg*s^2)
MT = 5.976E24  # Masa de la Tierra, en kg
RT = 6370  # Radio de la Tierra, en km
t_fin = 100 * 60 * 60  # 100 horas, en s (rango de estudio del problema)
h = 5  # Paso de integración, para la función integral()

# CONDICIONES INICIALES
r0 = 4 * RT  # Posición inicial a 4 veces el Radio de la Tierra, en km
phi0 = 0  # Posición inicial en el eje del Ecuador, en rad
vr0 = 4  # Valor inicial de velocidad tangencial, en km/s
vphi0 = -3  # Valor inicial de velocidad normal, en km/s

# GENERACIÓN DE LISTAS (se crean con los valores iniciales)
t = [0]  # Creo una lista para almacenar valores de tiempo, en s
r = [r0]  # Creo una lista para almacenar valores de posición, en km
phi = [phi0]  # Creo una lista para almacenar valores de ángulo, en rad
x = [r[-1] * np.cos(phi[-1])]  # Creo una lista para almacenar valores de la coordenada x, en km
y = [r[-1] * np.sin(phi[-1])]  # Creo una lista para almacenar valores de la coordenada y, en km

print(f"x es: {x} ")