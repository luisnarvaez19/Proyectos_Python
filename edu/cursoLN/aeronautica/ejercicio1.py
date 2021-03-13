"""
Asignatura: Simuladores de Vuelo. Máster Ingeniería Aeronáutica ULE
Práctica 1.2.- Trayectoria meteorito
Autor: Amelia Quintero Moreno
DNI: 29788260-V
Fecha: 2019-03-15

"""
import matplotlib.pyplot as plt  # Librería para gráficos
# Librerías necesarias
import numpy as np  # Librería numérica

# Constantes
G = (6.67259e-11 * (3600) ** 2 / (1000) ** 3)  # km**3/(kg*h**2)
R = (6.37e+3)  # km
M = (5.976e+24)  # kg

# Coordenadas polares
r0 = (4 * R)  # Se calcula para r0=4*R y para r0=2*R (km).
phi0 = (0)
r1 = [r0]  # Se declara como lista (km)
phi1 = [phi0]

# Coordenadas cartesianas declaradas como listas
x1 = [r1[-1] * np.cos(phi1[-1])]  # km
y1 = [r1[-1] * np.sin(phi1[-1])]  # km

# Velocidades en coordenadas polares
v_r = [4000 * 3.6]  # km/h
v_phi = [-3000 * 3.6]  # km/h

# Aceleraciones de las ecuaciones diferenciales de segundo orden
a_r = [((phi1[-1] ** 2) / r1[-1]) - ((G * M) / (r1[-1] ** 2))]  # km/h**2
a_phi = [(-(v_r[-1] ** 2) / r1[-1])]  # km/h**2

# Tiempo
t = [0]  # h
dt = (5 / 3600)  # Tiempo de integración
t_fin = (100)  # Tiempo de simulación en h


# Realizar cálculos
def integra(p, q, h):
    pfinal = p + (q * h)
    return pfinal


def main():
    while (t[-1] < t_fin) and (r1[-1] > R):
        # El loop debe realizarse en tiempos menores al tiempo final y para distancias mayores al radio de la Tierra

        x2 = (r1[-1] * np.cos(phi1[-1]))
        x1.extend([x2])

        y2 = (r1[-1] * np.sin(phi1[-1]))
        y1.extend([y2])

        r2 = integra(r1[-1], v_r[-1], dt)
        r1.extend([r2])

        phi2 = integra(phi1[-1], (v_phi[-1] / r1[-1]), dt)
        phi1.extend([phi2])

        vr2 = integra(v_r[-1], a_r[-1], dt)
        v_r.extend([vr2])

        vphi2 = integra(v_phi[-1], a_phi[-1], dt)
        v_phi.extend([vphi2])

        ar2 = (((v_phi[-1] ** 2) / r1[-1]) - ((G * M) / (r1[-1] ** 2)))
        a_r.extend([ar2])

        aphi2 = (-(v_r[-1] * v_phi[-1]) / r1[-1])
        a_phi.extend([aphi2])

        t2 = (t[-1] + dt)
        t.extend([t2])

    print('Alcance (m)', x1[-1])  # Imprime el valor de x
    print('Tiempo (s)', t[-1])  # Imprime el valor de t

    # Gráfica "Distancia al centro de la Tierra (Km)"
    figrt = plt.figure()  # Comando para dibujar la gráfica
    figurart = figrt.add_subplot(211)  # Comando para que la gráfica que se obtenga se dibuje en una cuadrícula cuadrada
    figurart.set_xlabel('Tiempo (h)')  # Nombre del eje x
    figurart.set_ylabel('Distancia (km)')  # Nombre del eje y
    figurart.set_title('Distancia al centro de la Tierra (Km)')  # Título de la gráfica
    figurart.plot(t, r1, 'b')  # Dibuja los valores obtenidos de t y r en color azul
    figrt.show()  # Muestra la gráfica obtenida

    # Gráfica "Posición del meteorito"
    figxy = plt.figure()  # Comando para dibujar la gráfica
    figuraxy = figxy.add_subplot(211)  # Comando para que la gráfica que se obtenga se dibuje en una cuadrícula cuadrada
    figuraxy.set_xlabel('Coordenada x (km)')  # Nombre del eje x
    figuraxy.set_ylabel('Coordenada y (km)')  # Nombre del eje y
    figuraxy.set_title('Posición del meteorito (curva x-y)')  # Título de la gráfica
    figuraxy.plot(x1, y1, 'r')  # Dibuja los valores obtenidos de x e y en color rojo
    figxy.show()  # Muestra la gráfica obtenida

    # Gráfica "Distancia al centro de la Tierra" en coordenadas polares, tal y como pide el enunciado de la práctica
    figrphi = plt.figure()  # Comando para dibujar la gráfica
    figurarphi = figrphi.add_subplot(111,
                                     projection='polar')  # Comando para que la gráfica que se obtenga se represente en coordenadas polares
    figurarphi.set_xlabel('r (km) y phi (deg)')  # Etiqueta eje horizontal
    figurarphi.set_title('Posición del meteorito (curva r-phi)')  # Título de la gráfica
    figurarphi.plot(phi1, r1, 'g')  # Dibuja los valores obtenidos de phi y r en color verde
    figrphi.show()  # Muestra la gráfica obtenida

    # Gráfica "Distancia al centro de la Tierra" cono la ha mostrado el profesor en clase
    figrphi = plt.figure()  # Comando para dibujar la gráfica
    figurarphi = figrphi.add_subplot(
        211)  # Comando para que la gráfica que se obtenga se dibuje en una cuadrícula cuadrada
    figurarphi.set_xlabel('phi (rad)')  # Nombre del eje x
    figurarphi.set_ylabel('r(km)')  # Nombre del eje y
    figurarphi.set_title('Posición del meteorito (curva r-phi)')  # Título de la gráfica
    figurarphi.plot(phi1, r1, 'g')  # Dibuja los valores obtenidos de phi y r en color verde
    figrphi.show()  # Muestra la gráfica obtenida


if __name__ == "__main__": main()