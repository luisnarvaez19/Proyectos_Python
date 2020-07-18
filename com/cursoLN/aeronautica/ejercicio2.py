"""
Asignatura: Simuladores de Vuelo. Máster Ingeniería Aeronáutica ULE
Práctica 2.2.- Vuelo de un paracaidísta
Autor: Amelia Quintero Moreno
DNI: 29788260-V
Fecha: 2019-03-30

"""
import matplotlib.pyplot as plt  # Librería para gráficos
# Librerías necesarias
import numpy as np  # Librería numérica

# Constantes
R0 = (6356766)  # Radio de la Tierra en (m)
TL = (-0.0065)  # Gradiente de temperatura (º/m)
T0 = (288.15)  # Temperatura estándar a nivel del mar (ºK)
g0 = (9.80665)  # Aceleración de la gravedad a 45 grados de latitud (m/s2)
P0 = (101325.0)  # Presión a g0 (Pa)
M0 = (28.9644)  # Masa molecular del aire (Kg/mol)
Rs = (8314.32)  # Constante de gases ideales (Nm/kmol/ºK)

# Parámetros de la configuración
h0 = (3500)  # Altitud del salto (m)
h1 = (700)  # Altitud a la que se abre el paracaídas (m)
s = (1)  # Superficie de contacto con el aire (m2)
m = (75)  # Masa del paracaidísta (kg)
Cd0 = (0.6)  # Coeficiente de resistencia con el paracaídas cerrado
Cd1 = (1.7)  # Coeficiente de resistencia con el paracaídas abierto
t = [0]  # (s)
dt = (0.01)  # Intervalo de integración


# Definición de funciones
def integra(p, q, h):
    pfinal = p + (q * h)
    return pfinal


def cota_geopotencial(z):
    h = R0 * z / (R0 + z)  # Calcula la cota geopotencial (h) a partir de la cota geométrica (z)
    return h


def temperatura_aire(z):
    T = T0 + TL * cota_geopotencial(z)  # Calcula la temperatura del aire (T) a partir de cota geométrica (z)
    return T


def presion_aire(z):
    P = P0 * np.exp(((g0 * M0) / (Rs * TL)) * np.log(
        T0 / temperatura_aire(z)))  # Calcula la presión del aire (P) a partir de la cota geométrica (z)
    return P


def densidad_aire(z):
    d = (presion_aire(z) / temperatura_aire(z)) * (
                M0 / Rs)  # Calcula la densidad del aire (d) a partir de la cota geométrica (z)
    return d


# Velocidad de caída libre
v = [0]  # Velocidad vertical inicial del paracaidista 0 m/s
z = [h0]  # Altitud a la que realiza el salto h0
a = [((0.5 * densidad_aire(z[-1]) * (
            (v[-1]) ** 2) * s * Cd0) / m) - g0]  # Aceleración en caída libre teniendo en cuenta la resistencia del aire


def main():
    while z[-1] > 0:
        if z[-1] > h1:  # Tramo en caída libre (entre 3500 y 700 m)
            a_libre = ((0.5 * densidad_aire(z[-1]) * (((v[-1]) ** 2) * s * Cd0) / m) - g0)
            a.extend([a_libre])

            v_libre = integra(v[-1], a_libre, dt)
            v.extend([v_libre])

            z_libre = integra(z[-1], v[-1], dt)
            z.extend([z_libre])

            t_libre = (t[-1] + dt)
            t.extend([t_libre])

        else:  # Tramo de caída con el paracaídas abierto (entre 700 y 0 m)
            a_paraca_abierto = ((0.5 * densidad_aire(z[-1]) * (((v[-1]) ** 2) * s * Cd1) / m) - g0)
            a.extend([a_paraca_abierto])

            v_paraca_abierto = integra(v[-1], a_paraca_abierto, dt)
            v.extend([v_paraca_abierto])

            z_paraca_abierto = integra(z[-1], v[-1], dt)
            z.extend([z_paraca_abierto])

            t_paraca_abierto = (t[-1] + dt)
            t.extend([t_paraca_abierto])

    print("Aterrizaje tras", "%.2f" % t[-1], "s", ",", "a una velocidad de", "%.2f" % v[-1], "m/s")

    # Gráfica "Altura geométrica en f(t)"
    figzt = plt.figure()  # Comando para dibujar la gráfica
    figurazt = figzt.add_subplot(211)  # Comando para que la gráfica que se obtenga se dibuje en un rectángulo
    figurazt.set_xlabel('Tiempo (s)')  # Nombre del eje x
    figurazt.set_ylabel('Altura geométrica (m)')  # Nombre del eje y
    figurazt.set_title('Altura geométrica en f(t)')  # Título de la gráfica
    figurazt.plot(t, z, 'b')  # Muestra los valores obtenidos de t y z en color azul
    figzt.show()  # Muestra la gráfica obtenida

    # Gráfica "Velocidad en f(t)"
    figvt = plt.figure()  # Comando para dibujar la gráfica
    figuravt = figvt.add_subplot(211)  # Comando para que la gráfica que se obtenga se dibuje en un rectángulo
    figuravt.set_xlabel('Tiempo (s)')  # Nombre del eje x
    figuravt.set_ylabel('Velocidad (m/s)')  # Nombre del eje y
    figuravt.set_title('Velocidad en f(t)')  # Título de la gráfica
    figuravt.plot(t, v, 'r')  # Muestra los valores obtenidos de t y z en color rojo
    figvt.show()  # Muestra la gráfica obtenida


if __name__ == '__main__': main()