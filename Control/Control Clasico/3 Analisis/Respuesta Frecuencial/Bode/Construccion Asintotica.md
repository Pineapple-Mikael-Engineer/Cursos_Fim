---
title: Construcción Asintótica de Bode
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - bode
draft: false
aliases:
  - construcción asintótica
  - asíntotas de Bode
  - trazado de Bode
---

# Construcción Asintótica de Bode

> [!definicion]
> La construcción asintótica traza el [[index | Bode]] de $G(j\omega)$ aproximando cada [[Factores Basicos | factor]] por rectas: se parte de la asíntota de baja frecuencia ($K/(j\omega)^N$) y en cada **frecuencia de esquina** (polo o cero) se cambia la pendiente $\mp20$ dB/dec ($\pm40$ por par de 2.º orden). La fase se suma factor a factor. El resultado se afina luego en [[Correcciones]].

> [!info]
> Núcleo operativo de la subsección [[index | Bode]] en [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Usa los ladrillos de [[Factores Basicos]] y se corrige con [[Correcciones]]. La pendiente inicial la fija el [[Tabla Tipos | tipo del sistema]] $N$.

---

## Ejemplo

> [!ejemplo]
> **Trazar el Bode asintótico de $G(s)=\dfrac{100\,(s+1)}{s\,(s+10)(s+100)}$ paso a paso.**
>
> ![[bode_construccion_asintotica.svg|600]]
>
> **Paso 1 — Forma de Bode** (normalizar cada factor a $1+s/\omega_0$):
> $$G(s)=\frac{100\,(s+1)}{s\,(s+10)(s+100)}=\frac{100}{10\cdot100}\cdot\frac{1+s}{s\,(1+s/10)(1+s/100)}=\frac{0.1\,(1+s/1)}{s\,(1+s/10)(1+s/100)}.$$
> Ganancia $K=0.1$, un integrador ($N=1$), cero en $\omega=1$, polos en $\omega=10$ y $\omega=100$.
>
> **Paso 2 — Frecuencias de esquina ordenadas:** $1$ (cero, $+20$), $10$ (polo, $-20$), $100$ (polo, $-20$).
>
> **Paso 3 — Asíntota de baja frecuencia.** Para $\omega\to0$, $G\approx0.1/(j\omega)$: pendiente $-20$ dB/dec. En $\omega=1$ pasa por $20\log(0.1)=-20$ dB.
>
> **Paso 4 — Acumular pendientes esquina a esquina:**
>
> | Tramo | Pendiente | Cómo se obtiene |
> |---|---|---|
> | $\omega<1$ | $-20$ dB/dec | integrador solo |
> | $1<\omega<10$ | $\;\;0$ dB/dec | $+20$ del cero cancela el integrador |
> | $10<\omega<100$ | $-20$ dB/dec | entra el polo en $10$ |
> | $\omega>100$ | $-40$ dB/dec | entra el polo en $100$ |
>
> **Paso 5 — Nivel en cada esquina** (partiendo de $-20$ dB en $\omega=1$):
> - de $\omega=1$ a $\omega=10$: pendiente $0\Rightarrow$ sigue en $-20$ dB en $\omega=10$.
> - de $\omega=10$ a $\omega=100$: $-20$ dB/dec sobre 1 década $\Rightarrow -20-20=-40$ dB en $\omega=100$.
>
> **Paso 6 — Fase** (suma de aportes; integrador $-90^\circ$ fijo):
>
> | $\omega$ | cero $+\arctan\omega$ | polo$_{10}$ $-\arctan\frac{\omega}{10}$ | polo$_{100}$ $-\arctan\frac{\omega}{100}$ | integrador | total |
> |---|---|---|---|---|---|
> | $1$ | $+45^\circ$ | $-5.7^\circ$ | $-0.6^\circ$ | $-90^\circ$ | $-51^\circ$ |
> | $10$ | $+84^\circ$ | $-45^\circ$ | $-5.7^\circ$ | $-90^\circ$ | $-57^\circ$ |
> | $100$ | $+89^\circ$ | $-84^\circ$ | $-45^\circ$ | $-90^\circ$ | $-130^\circ$ |
>
> Fase de alta frecuencia: exceso polos$-$ceros $=3-1=2\Rightarrow\angle G\to-180^\circ$. Las rectas asintóticas (segmentos) aproximan la curva real suave; las mayores desviaciones están en las esquinas, donde se aplica [[Correcciones | la corrección de $\pm3$ dB]].

---

## En qué consiste

> [!regla] Trazado de la magnitud asintótica
> 1. Escribir $G(s)$ en **forma de Bode** (factores $1+s/\omega_0$, ganancia $K$ visible).
> 2. Identificar las **frecuencias de esquina** (polos y ceros) y ordenarlas.
> 3. Trazar la **asíntota de baja frecuencia**: la marca $K/(j\omega)^N$ (ganancia + integradores).
> 4. En cada esquina, **cambiar la pendiente**: $-20$ dB/dec por polo, $+20$ por cero, $\pm40$ por par de 2.º orden.
> 5. Acumular las pendientes hacia altas frecuencias.

> [!regla] Trazado de la fase
> 1. Sumar la fase de cada [[Factores Basicos | factor]].
> 2. Cada polo/cero simple transiciona $\mp90^\circ$ a lo largo de $\pm1$ década alrededor de su esquina ($\mp45^\circ$ en la esquina).
> 3. Verificar la fase de alta frecuencia: $\angle G\to-90^\circ(N_p-N_z)$ por el exceso polos$-$ceros.

> [!teorema] Asíntota de baja frecuencia
> Para $\omega\to0$, $G(j\omega)\approx\dfrac{K}{(j\omega)^N}$ (con $N=$ nº de integradores, **tipo** del sistema):
> - Pendiente inicial: $-20N$ dB/dec.
> - En $\omega=1$: pasa por $20\log K$ dB (si $N=0$, recta horizontal en $20\log K$).
>
> El [[Tabla Tipos | tipo del sistema]] $N$ fija la pendiente de partida y el [[Error Estacionario/index | error estacionario]].

> [!info] Frecuencia de cruce de ganancia
> La frecuencia $\omega_{gc}$ donde la magnitud cruza $0$ dB se estima sobre las asíntotas; ahí se lee el [[Margenes MF MG | margen de fase]]. Sobre un tramo de $-20$ dB/dec que parte de $K_0$ dB en $\omega_a$: $\omega_{gc}\approx\omega_a\cdot10^{K_0/20}$.

---

## Algoritmo

> [!algoritmo] En MATLAB
> ```matlab
> G = tf(100*[1 1], conv([1 0],conv([1 10],[1 100])));  % 100(s+1)/[s(s+10)(s+100)]
> bode(G); grid on
> [Gm, Pm, Wpc, Wgc] = margin(G);   % margenes y frecuencias de cruce
> ```

---

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | 1 | forma de Bode ($1+s/\omega_0$, $K$ visible) |
> | 2 | listar y ordenar esquinas |
> | 3 | asíntota baja frecuencia $K/(j\omega)^N$ |
> | 4 | cambiar pendiente en cada esquina |
> | 5 | acumular niveles hasta alta frecuencia |
> | 6 | sumar fase factor a factor |

> [!corolario]
> Trazar un Bode asintótico es ordenar las frecuencias de esquina, salir con la asíntota $K/(j\omega)^N$ y quebrar la pendiente $\pm20$ (o $\pm40$) dB/dec en cada una, sumando la fase aparte. La curva real coincide salvo cerca de las esquinas, donde [[Correcciones]] añade los $\pm3$ dB y el pico resonante.

> [!referencia]
> - Aporte de cada factor: [[Factores Basicos]].
> - Ajuste fino en esquinas y picos: [[Correcciones]].
> - Pendiente inicial y tipo: [[Tabla Tipos]] · [[Error Estacionario/index]].
> - Lectura de márgenes: [[Margenes MF MG]].
