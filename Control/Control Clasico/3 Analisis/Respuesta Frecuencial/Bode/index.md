---
title: Diagramas de Bode
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - bode
  - index
draft: false
aliases:
  - Bode
  - diagrama de Bode
  - Bode plot
---

# Diagramas de Bode

> [!definicion]
> El diagrama de Bode es el par de gráficas de la [[Respuesta Frecuencial/index | respuesta en frecuencia]] $G(j\omega)$ con la frecuencia en **escala logarítmica**: la **magnitud** $20\log_{10}|G(j\omega)|$ en dB y la **fase** $\angle G(j\omega)$ en grados. En escala log, los productos de factores se vuelven sumas, así que el trazo se construye sumando las contribuciones de cada factor elemental.

> [!info]
> Índice de la subsección Bode dentro de [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Se desglosa en [[Factores Basicos]] (aporte de cada término), [[Construccion Asintotica]] (sumar las rectas) y [[Correcciones]] (ajuste fino en esquinas y picos). Complementa a [[Nyquist/index | Nyquist]].

---

## Ejemplo

> [!ejemplo]
> **Lectura de un Bode de segundo orden.** Sistema $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$ con $\omega_n=10\ \text{rad/s}$ y $\zeta=0.2$.
>
> ![[bode_segundo_orden.svg|600]]
>
> **Magnitud (arriba).** En baja frecuencia $|G|\to1\ (0\text{ dB})$. Sobre $\omega_n=10$ la pendiente pasa a $-40$ dB/dec (dos polos). En la resonancia aparece un pico:
> $$M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}=\frac{1}{2(0.2)\sqrt{1-0.04}}\approx2.55\;(+8.1\text{ dB})\quad\text{en}\quad \omega_r=\omega_n\sqrt{1-2\zeta^2}\approx9.6\ \text{rad/s}.$$
>
> **Fase (abajo).** Arranca en $0^\circ$, vale $-90^\circ$ exactos en $\omega_n=10$ y tiende a $-180^\circ$ (dos polos). La transición es más brusca cuanto menor es $\zeta$.
>
> Se lee de un vistazo: ganancia DC ($0$ dB), pico resonante ($+8$ dB), pendiente de alta frecuencia ($-40$ dB/dec) y fase asintótica ($-180^\circ$). Estos pasos se sistematizan en [[Construccion Asintotica]].

---

## En qué consiste

> [!teoria] Por qué Bode es práctico
> En escala log, la magnitud en dB de un producto de factores es la **suma** de las magnitudes de cada factor, y la fase es la suma de las fases:
> $$20\log|G_1G_2\cdots|=\sum_i 20\log|G_i|,\qquad \angle(G_1G_2\cdots)=\sum_i\angle G_i.$$
> Esto permite trazar el diagrama **sumando** las contribuciones de cada [[Factores Basicos | factor básico]] (ganancia, integradores, polos, ceros, par de 2.º orden) mediante rectas asintóticas.

> [!info] De qué se compone su construcción
> - **[[Factores Basicos | Factores básicos]]:** aporte de cada término ($K$, $j\omega$, $1/j\omega$, $1+j\omega/\omega_0$, par de 2.º orden) en magnitud y fase.
> - **[[Construccion Asintotica | Construcción asintótica]]:** sumar las rectas de cada factor para el trazo aproximado.
> - **[[Correcciones | Correcciones]]:** ajustes en las frecuencias de esquina ($\pm3$ dB) y en los picos resonantes.

> [!definicion] Términos clave
> | Término | Definición |
> |---|---|
> | **Década** | factor $\times10$ en frecuencia |
> | **Octava** | factor $\times2$ en frecuencia |
> | **Frecuencia de esquina** $\omega_0$ | donde un factor cambia de pendiente ($\omega=$ polo/cero) |
> | **Pendiente** | dB/década; un polo aporta $-20$, un cero $+20$, un par de 2.º orden $\pm40$ |
> | **Ancho de banda** | frecuencia donde la magnitud cae $-3$ dB respecto a baja frecuencia |

---

## Algoritmo

> [!algoritmo] En MATLAB
> ```matlab
> wn = 10; zeta = 0.2;
> G = tf(wn^2, [1 2*zeta*wn wn^2]);
> bode(G); grid on            % magnitud y fase
> [Gm, Pm, Wpc, Wgc] = margin(G);   % margenes y cruces
> ```

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ejes | $\lvert G\rvert_{\text{dB}}$ y $\angle G$ vs $\omega$ (log) |
> | Magnitud | $20\log_{10}\lvert G(j\omega)\rvert$ |
> | Propiedad clave | productos $\to$ sumas en dB y grados |
> | Construcción | sumar [[Factores Basicos \| factores]] asintóticos |
> | Pendiente | $-20$/polo, $+20$/cero, $\pm40$ par 2.º orden (dB/dec) |
> | Ajuste | [[Correcciones \| $\pm3$ dB]] en esquinas, pico $M_r$ |

> [!corolario]
> El Bode descompone $G(j\omega)$ en magnitud y fase sobre escala logarítmica, donde la propiedad del logaritmo convierte el trazado en una suma de factores elementales. De él se leen directamente ganancia, ancho de banda y los [[Margenes MF MG | márgenes]] de estabilidad.

> [!referencia]
> - Aportes individuales: [[Factores Basicos]].
> - Trazado paso a paso: [[Construccion Asintotica]] · [[Correcciones]].
> - Lectura de estabilidad: [[Margenes MF MG]].
> - Representación complementaria: [[Nyquist/index]].
