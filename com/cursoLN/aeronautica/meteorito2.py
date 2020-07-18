# -*- coding: utf-8 -*-
"""
ENRIQUE CABEZAS CASTAÑO
PRÁCTICA 1.2 - TRAYECTORIA DE UN METEORITO
FECHA: 03/09/2019
"""

import time

import matplotlib.pyplot as plt
import numpy as np

# Use 1: Explicit start / stop
# start
start_time = time.time()
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
# t = [0]  # Creo una lista para almacenar valores de t, en s
t = np.array([0])
# r = [r0]  # Creo una lista para almacenar valores de posición, en km
r = np.array([r0])
# phi = [phi0]  # Creo una lista para almacenar valores de ángulo, en rad
phi = np.array([phi0])
# x = [r[-1] * np.cos(phi[-1])]  # Creo una lista para almacenar valores de la coordenada x, en km
x = np.array([r[-1] * np.cos(phi[-1])])
# y = [r[-1] * np.sin(phi[-1])]  # Creo una lista para almacenar valores de la coordenada y, en km
y = np.array([r[-1] * np.sin(phi[-1])])
# v_r = [vr0]  # v_r == r_dot (Velocidad tangencial), en km/s
v_r = np.array([vr0])
# v_phi = [vphi0]  # v_phi == r*phi_dot (Velocidad normal), en km/s
v_phi = np.array([vphi0])
# a_r = [(r[-1] * (v_phi[-1] / r[-1]) ** 2) - (G * MT / r[
#   -1] ** 2)]  # a_r = (v_r)_dot = r_dot_dot // Primera ecuación diferencial de segundo orden del problema
a_r = np.array([(r[-1] * (v_phi[-1] / r[-1]) ** 2) - (G * MT / r[-1] ** 2)])
#a_phi = [-(2 * v_r[-1] * (v_phi[-1] / r[-1])) / r[
#    -1]]  # a_phi = phi_dot_dot // Segunda ecuación diferencial de segundo orden del problema
a_phi = np.array([-(2 * v_r[-1] * (v_phi[-1] / r[-1])) / r[-1]])
# DEFINICIÓN DE LA FUNCIÓN INTEGRAL
def integral(p, q, h):
    p_siguiente = p + q * h
    return p_siguiente


# DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
def main():
    global x, y, r, t, v_r, a_r, v_phi, phi, a_phi
    while t[-1] <= t_fin and r[-1] >= RT:
        x1 = r[-1] * np.cos(phi[-1])
        # x.extend([x1])  # Va añadiendo los valores de las iteraciones a la lista x
        x = np.append(x, x1)
        y1 = r[-1] * np.sin(phi[-1])
        # y.extend([y1])  # Va añadiendo los valores de las iteraciones a la lista y
        y = np.append(y, y1)
        r1 = integral(r[-1], v_r[-1], h)  # Uso la función integral
        # r.extend([r1])  # Va añadiendo los valores de las iteraciones a la lista r
        r = np.append(r, r1)
        phi1 = integral(phi[-1], (v_phi[-1] / r[-1]), h)  # Uso la función integral
        # phi.extend([phi1])  # Va añadiendo los valores de las iteraciones a la lista phi
        phi = np.append(phi, phi1)
        v_r1 = integral(v_r[-1], a_r[-1], h)  # Uso la función integral
        # v_r.extend([v_r1])  # Va añadiendo los valores de las iteraciones a la lista v_r
        v_r = np.append(v_r, v_r1)
        v_phi1 = integral(v_phi[-1], (r[-1] * a_phi[-1]), h)  # Uso la función integral
        # v_phi.extend([v_phi1])  # Va añadiendo los valores de las iteraciones a la lista v_phi
        v_phi = np.append(v_phi, v_phi1)
        a_r1 = ((r[-1] * (v_phi[-1] / r[-1]) ** 2) - (G * MT / r[-1] ** 2))
        # a_r.extend([a_r1])  # Va añadiendo los valores de las iteraciones a la lista a_r
        a_r = np.append(a_r, a_r1)
        a_phi1 = (-(2 * v_r[-1] * (v_phi[-1] / r[-1])) / r[-1])
        # a_phi.extend([a_phi1])  # Va añadiendo los valores de las iteraciones a la lista a_phi
        a_phi = np.append(a_phi, a_phi1)
        t1 = t[-1] + h
        # t.extend([t1])  # Va añadiendo los valores de las iteraciones a la lista t
        t = np.append(t, t1)
    print(f"El alcance es: {r[-1]}")
    print(f"El t es: {t[-1]/3600}")
    # stop
    print("--- %s seconds ---" % (time.time() - start_time))

    # GENERACIÓN DE GRÁFICAS
    fig_rt = plt.figure()
    figura_rt = fig_rt.add_subplot(311)
    figura_rt.set_xlabel("Tiempo (h)")
    figura_rt.set_ylabel("Distancia (km)")
    figura_rt.set_title("rancia al centro de la Tierra")
    figura_rt.plot(t, r, "b")
    #fig_rt.show


    # fig_rt = plt.figure()
    figura_rt = fig_rt.add_subplot(312)
    figura_rt.set_xlabel("Tiempo (h)")
    figura_rt.set_ylabel("Distancia (km)")
    figura_rt.set_title("Posiciones del meteorito en coordenadas cartesianas")
    figura_rt.plot(x, y, "g")
    # fig_rt.show

    # fig_rt = plt.figure()
    figura_rt = fig_rt.add_subplot(313)
    figura_rt.set_xlabel("Tiepo (h)")
    figura_rt.set_ylabel("Distancia (km)")
    figura_rt.set_title("Posiciones del meteorito en coordenadas polares")
    figura_rt.plot(r, phi, "y")
    fig_rt.show
    plt.show()

if __name__ == "__main__": main()