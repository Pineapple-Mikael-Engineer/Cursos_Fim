---
title: Diagrama Polar
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - nyquist
draft: false
aliases:
  - diagrama polar
  - lugar polar
  - polar plot
---

# Diagrama Polar

> [!definicion]
> El **diagrama (o lugar) polar** es la curva que describe $L(j\omega)=G(j\omega)H(j\omega)$ en el plano complejo al variar $\omega$ de $0$ a $\infty$. Cada punto se ubica por su **magnitud** $|L(j\omega)|$ (distancia al origen) y su **fase** $\angle L(j\omega)$ (ángulo desde el eje real positivo). Su reflejo conjugado más, si hace falta, un arco infinito forman el [[Criterio Nyquist | diagrama de Nyquist]] completo.

> [!info]
> Pertenece a la subcarpeta [[Nyquist/index | Nyquist]] de [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Usa los mismos datos que [[Bode/index | Bode]] ($|L|$ y $\angle L$ para cada $\omega$); el conteo de estabilidad sobre la curva se hace en [[Criterio Nyquist]] y su distancia a $-1$ se mide en [[Margenes MF MG | Márgenes]].

---

## Ejemplo

> [!ejemplo]
> **Trazado paso a paso de $L(s)=\dfrac{K}{s(s+1)(s+2)}$ (tomamos $K=6$).** Hallar inicio, fin y cruces con los ejes.
>
> ![[nyquist_polar_tipo1.svg|550]]
>
> **Paso 1 — Sustituir $s=j\omega$ y racionalizar.** Multiplicando los factores del denominador,
> $$L(j\omega)=\frac{K}{j\omega(j\omega+1)(j\omega+2)}=\frac{K}{-3\omega^2 + j\,\omega(2-\omega^2)}.$$
> Multiplicando por el conjugado del denominador y con $D=9\omega^4+\omega^2(2-\omega^2)^2$:
> $$L(j\omega)=\frac{K\big[-3\omega^2 - j\,\omega(2-\omega^2)\big]}{D}
> \;\Rightarrow\;
> \operatorname{Re}=\frac{-3K\omega^2}{D},\quad
> \operatorname{Im}=\frac{-K\omega(2-\omega^2)}{D}.$$
>
> **Paso 2 — Inicio $\omega\to0^+$.** Hay un integrador ($N=1$), así que $|L|\to\infty$. La fase parte de
> $$\angle L = -90^\circ - \arctan\tfrac{\omega}{1} - \arctan\tfrac{\omega}{2}\;\xrightarrow{\omega\to0}\;-90^\circ.$$
> La rama viene del infinito asintótica a una vertical (parte real tiende a un valor finito negativo, $-9K/4$).
>
> **Paso 3 — Fin $\omega\to\infty$.** $|L|\to0$ y la fase suma los tres polos:
> $$\angle L \to -90^\circ-90^\circ-90^\circ=-270^\circ.$$
> La curva entra al origen tangente a $-270^\circ$ (equivalente a $+90^\circ$).
>
> **Paso 4 — Corte con el eje real** ($\operatorname{Im}=0$): el numerador $-K\omega(2-\omega^2)=0$ da $\omega_{pc}=\sqrt2$ rad/s. Allí
> $$\operatorname{Re}=\frac{-3K\omega^2}{9\omega^4}=\frac{-K}{3\omega^2}=\frac{-K}{6}.$$
> Con $K=6$ el cruce es $L(j\sqrt2)=-1$. El lugar corta el eje real **negativo** en $-K/6$.
>
> **Paso 5 — Lectura para estabilidad.** Ese cruce $-K/6$ es justo lo que el [[Criterio Nyquist | criterio]] compara con $-1$: estable mientras $K/6<1$, es decir $K<6$; con $K=6$ pasa por $-1$ (marginal) y con $K>6$ rodea $-1$ (inestable).

---

## En qué consiste

> [!teoria]
> El lugar polar es la lista ordenada de los fasores $L(j\omega)$. Para esbozarlo no se calculan todos los puntos: bastan el inicio ($\omega\to0$), el fin ($\omega\to\infty$) y los cruces con los ejes, uniéndolos con fase monótona decreciente en sistemas de [[Sistemas Fase Minima | fase mínima]].

> [!regla] Puntos clave para esbozar el lugar polar
> 1. **$\omega\to0$:** evaluar $L(j0^+)$. Si hay $N$ integradores, $|L|\to\infty$ con fase $-90^\circ N$; si $N=0$, parte de un real finito.
> 2. **$\omega\to\infty$:** $|L|\to0$ con fase $-90^\circ(n-m)$ ($n,m$ = grados de denominador y numerador).
> 3. **Cortes con el eje real:** resolver $\operatorname{Im}\{L(j\omega)\}=0$ y evaluar $\operatorname{Re}$ ahí.
> 4. **Cortes con el eje imaginario:** resolver $\operatorname{Re}\{L(j\omega)\}=0$ y evaluar $\operatorname{Im}$ ahí.
> 5. Unir respetando la fase monótona decreciente.

> [!teorema] Inicio y fin del lugar
> | Tipo $N$ | $L(j0^+)$ | Forma cerca de $\omega=0$ |
> |---|---|---|
> | $0$ | $K$ (real finito) | parte de un punto en el eje real positivo |
> | $1$ | $\infty\,\angle{-90^\circ}$ | viene del infinito asintótico a una vertical |
> | $2$ | $\infty\,\angle{-180^\circ}$ | viene del infinito asintótico al eje real negativo |
>
> En $\omega\to\infty$, $L\to0$ entrando al origen con ángulo $-90^\circ(n-m)$.

---

## De polar a Nyquist completo

> [!info]
> El diagrama de Nyquist añade al lugar polar ($\omega:0\to\infty$):
> - su **reflejo conjugado** ($\omega:-\infty\to0$), simétrico respecto al eje real;
> - un **arco de radio infinito** que rodea los polos en el origen (si los hay), cerrando el contorno.
>
> El conteo de rodeos a $-1$ se hace sobre esta curva cerrada (ver [[Criterio Nyquist]]).

---

## En MATLAB

> [!info]
> ```matlab
> K = 6;
> L = tf(K, conv([1 1 0], [1 2]));   % K / (s(s+1)(s+2))
> nyquist(L)                          % lugar polar + conjugado
> [re, im] = nyquist(L, sqrt(2));     % punto del cruce real: ~ -1
> ```

---

## Resumen

> [!resumen]
> | Punto del trazado | Cómo se obtiene |
> |---|---|
> | Inicio $\omega\to0$ | $|L|$, fase $-90^\circ N$ ($N$ integradores) |
> | Fin $\omega\to\infty$ | $L\to0$, fase $-90^\circ(n-m)$ |
> | Corte eje real | $\operatorname{Im}\{L\}=0$ → evaluar $\operatorname{Re}$ |
> | Corte eje imaginario | $\operatorname{Re}\{L\}=0$ → evaluar $\operatorname{Im}$ |
> | Ejemplo $K/[s(s+1)(s+2)]$ | cruza eje real en $-K/6$ a $\omega=\sqrt2$ |

> [!corolario]
> Trazar el lugar polar se reduce a fijar tres rasgos —de dónde sale, a dónde llega y dónde cruza los ejes— y unirlos con fase decreciente. El cruce con el eje real negativo es el dato clave: comparado con $-1$ entrega directamente el [[Criterio Nyquist | criterio de estabilidad]] y los [[Margenes MF MG | márgenes]].

> [!referencia]
> - Conteo de estabilidad sobre esta curva: [[Criterio Nyquist]].
> - Distancia al punto $-1$: [[Margenes MF MG]].
> - Misma data en ejes cartesianos: [[Bode/index]].
> - Monotonía de fase: [[Sistemas Fase Minima]].
