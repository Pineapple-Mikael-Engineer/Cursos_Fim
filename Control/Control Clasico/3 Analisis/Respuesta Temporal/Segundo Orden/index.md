---
title: Sistemas de Segundo Orden
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - segundo orden
  - 2do orden
  - respuesta segundo orden
---

# Sistemas de Segundo Orden

> [!definicion]
> Sistema canónico de 2.º orden con ganancia unitaria, gobernado por dos parámetros: frecuencia natural $\omega_n$ [rad/s] y razón de amortiguamiento $\zeta$ (adimensional):
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2},\qquad s_{1,2} = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2-1}.$$
> Con ganancia $K$: $G(s)=K\omega_n^2/(s^2+2\zeta\omega_n s+\omega_n^2)$ (la $K$ se añade al final por linealidad). Para $0<\zeta<1$ los polos son complejos conjugados $-\zeta\omega_n\pm j\omega_d$ con $\omega_d=\omega_n\sqrt{1-\zeta^2}$.

> [!info]
> Marco de la carpeta **Segundo Orden** dentro de [[Respuesta Temporal/index | respuesta temporal]]. Cada métrica de la respuesta subamortiguada tiene su nota hija: [[Formula General | fórmula general $y(t)$]], [[Sobrepico Mp | sobrepico $M_p$]], [[Tiempo Pico Tp | tiempo de pico $T_p$]], [[Tiempo Establecimiento Ts | tiempo de establecimiento $T_s$]] y [[Tiempo Subida Tr | tiempo de subida $T_r$]]. El sistema suele provenir de un dominio físico [[Mecanico Traslacional | masa-resorte-amortiguador]]; el caso de un solo polo está en [[Primer Orden]].

---

## Ejemplo

> [!ejemplo] Identificar parámetros y clasificar
> **Problema.** Un sistema tiene $G(s)=\dfrac{25}{s^2+6s+25}$. Hallar $\omega_n$, $\zeta$, los polos, $\omega_d$ y las métricas de respuesta.
>
> **Paso 1 — Comparar con la forma canónica.** Igualando $s^2+2\zeta\omega_n s+\omega_n^2$ con $s^2+6s+25$:
> $$\omega_n^2=25\;\Rightarrow\;\omega_n=5\ \text{rad/s},\qquad 2\zeta\omega_n=6\;\Rightarrow\;\zeta=\frac{6}{2\cdot5}=0.6.$$
>
> **Paso 2 — Clasificar.** Como $0<\zeta=0.6<1$ → **subamortiguado** (polos complejos, hay sobrepico).
>
> **Paso 3 — Polos y frecuencia amortiguada:**
> $$s_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=-3\pm j\,5\sqrt{1-0.36}=-3\pm j\,4,\qquad \omega_d=4\ \text{rad/s}.$$
>
> **Paso 4 — Métricas de respuesta** (cada fórmula se detalla en su nota hija):
> $$M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}=e^{-\pi(0.6)/0.8}=e^{-2.356}\approx0.095\;(9.5\%),$$
> $$T_p=\frac{\pi}{\omega_d}=\frac{\pi}{4}\approx0.785\ \text{s},\qquad T_s(2\%)\approx\frac{4}{\zeta\omega_n}=\frac{4}{3}\approx1.33\ \text{s}.$$
> El par dominante $-3\pm j4$ fija toda la dinámica: parte real $\sigma=\zeta\omega_n=3$ (velocidad de decaimiento) y parte imaginaria $\omega_d=4$ (oscilación).

> [!ejemplo] Curva característica
> ![[segundo_orden_escalon.svg]]
>
> Respuesta a escalón de un sistema subamortiguado: sobrepico $M_p$ en el pico $t_p$, oscilación de frecuencia $\omega_d$ y establecimiento dentro de la banda $\pm2\%$.

---

## En qué consiste

> [!teoria]
> El sistema de 2.º orden estándar tiene ganancia unitaria en DC ($G(0)=1$) y dos parámetros con interpretación geométrica directa en el plano $s$:
> - $\omega_n$ es la **distancia al origen** de los polos: $|s_{1,2}|=\omega_n$.
> - $\zeta$ fija el **ángulo** $\beta$ respecto al eje imaginario negativo: $\cos\beta=\zeta$.
> - $\sigma=\zeta\omega_n$ es la **parte real** (decaimiento, ver [[Tiempo Establecimiento Ts | $T_s$]]); $\omega_d=\omega_n\sqrt{1-\zeta^2}$ es la **parte imaginaria** (oscilación, ver [[Tiempo Pico Tp | $T_p$]]).

> [!teorema] Polos de lazo cerrado
> $$s_{1,2} = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}.$$
> La naturaleza de la raíz cuadrada (real o imaginaria) clasifica la respuesta según $\zeta$.

> [!info] Clasificación según $\zeta$
> | $\zeta$ | Tipo de polos | Respuesta |
> |---|---|---|
> | $\zeta = 0$ | Imaginarios puros ($\pm j\omega_n$) | No amortiguada (oscila) |
> | $0 < \zeta < 1$ | Complejos conjugados | Subamortiguada |
> | $\zeta = 1$ | Reales iguales ($s=-\omega_n$) | Críticamente amortiguada |
> | $\zeta > 1$ | Reales distintos y negativos | Sobreamortiguada |

> [!info] Respuesta a escalón (subamortiguada)
> Para escalón unitario y $0<\zeta<1$ (demostración completa en [[Formula General]]):
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\,\sin(\omega_d t + \theta),\qquad \theta=\arccos\zeta.$$
> De esta única expresión salen todas las métricas: $M_p$ (máximo de $y$), $T_p$ (donde $\dot y=0$), $T_s$ (envolvente) y $T_r$ (subida $10\%\to90\%$).

> [!info] Parámetros de respuesta (cada uno en su nota hija)
> | Métrica | Fórmula | Nota |
> |---|---|---|
> | Frecuencia amortiguada | $\omega_d=\omega_n\sqrt{1-\zeta^2}$ | [[Formula General]] |
> | Sobrepico | $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ | [[Sobrepico Mp]] |
> | Tiempo de pico | $T_p=\pi/\omega_d$ | [[Tiempo Pico Tp]] |
> | Tiempo de establecimiento | $T_s(2\%)\approx4/\zeta\omega_n$ | [[Tiempo Establecimiento Ts]] |
> | Tiempo de subida | $T_r\approx(\pi-\theta)/\omega_d$ | [[Tiempo Subida Tr]] |

---

## Uso en diseño

> [!regla] De especificaciones a polos deseados
> El proceso inverso fija $\zeta$ y $\omega_n$ a partir de los requisitos:
> - $M_p \to \zeta$ (el sobrepico depende solo de $\zeta$).
> - $T_s \to \zeta\omega_n$ (parte real de los polos).
> - $T_p$ o $T_r \to \omega_n$ (una vez conocido $\zeta$).
>
> Con $\zeta$ y $\omega_n$ se ubican los polos deseados $s_{1,2}=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}$ y se diseña el controlador para llevarlos allí (ver [[Lugar Raices/index | lugar de las raíces]]).

> [!info] Aproximación de orden superior
> Un sistema de orden $>2$ se aproxima como 2.º orden si tiene un **par de polos dominantes** complejos: el resto de polos debe tener parte real al menos **5 veces** más negativa que la del par dominante. Ver [[Polos Ceros | polos y ceros]].

> [!info] En MATLAB
> ```matlab
> wn = 5; zeta = 0.6;
> G = tf(wn^2, [1 2*zeta*wn wn^2]);   % 25/(s^2+6s+25)
> damp(G)        % polos, wn y zeta
> step(G)        % respuesta al escalon
> stepinfo(G)    % Mp, Tp, Ts, Tr numericos
> ```

---

## Limitaciones

> [!warning]
> 1. Las fórmulas de $M_p$, $T_p$, $T_r$ asumen sistema **subamortiguado** ($0<\zeta<1$).
> 2. Para $\zeta\ge1$ no hay sobrepico ni pico: $M_p$ y $T_p$ no aplican.
> 3. Las aproximaciones de $T_r$ y $T_s$ pierden precisión para $\zeta$ muy bajo o muy alto.
> 4. En presencia de **ceros** la respuesta puede diferir notablemente (ver [[Polos Ceros | efecto de ceros]]).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | FT estándar | $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$ |
> | Polos | $s_{1,2}=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}$ |
> | Parámetros | $\omega_n$ (distancia al origen), $\zeta$ ($\cos\beta$) |
> | Subamortiguado | $0<\zeta<1\Rightarrow$ complejos $-\zeta\omega_n\pm j\omega_d$ |
> | Salida a escalón | $y(t)=1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta)$ |
> | Métricas | $M_p$, $T_p$, $T_s$, $T_r$ (notas hijas) |

> [!corolario]
> Todo sistema de 2.º orden estándar queda descrito por $(\zeta,\omega_n)$, que fijan la posición de los polos y, a través de ellos, las cuatro métricas de respuesta. El diseño consiste en traducir las especificaciones temporales a una región del plano $s$ y ubicar allí los polos dominantes mediante [[Lugar Raices/index | lugar de las raíces]].

> [!referencia]
> - Respuesta completa $y(t)$: [[Formula General]].
> - Métricas: [[Sobrepico Mp]] · [[Tiempo Pico Tp]] · [[Tiempo Establecimiento Ts]] · [[Tiempo Subida Tr]].
> - Polos, ceros y dominancia: [[Polos Ceros]].
> - Caso de un solo polo: [[Primer Orden]].
> - Origen físico típico: [[Mecanico Traslacional]].
