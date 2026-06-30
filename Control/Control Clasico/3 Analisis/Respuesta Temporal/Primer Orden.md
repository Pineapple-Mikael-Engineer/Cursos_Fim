---
title: Sistemas de Primer Orden
order: 1
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - primer orden
  - 1er orden
  - respuesta primer orden
---

# Sistemas de Primer Orden

> [!definicion]
> Un sistema de primer orden tiene un único polo real y función de transferencia $G(s)=\dfrac{K}{\tau s+1}$, con **ganancia estática** $K=G(0)$ y **constante de tiempo** $\tau$ [s]. Su polo es $s=-1/\tau$ (estable si $\tau>0$). La respuesta al escalón unitario es monótona, sin sobrepico:
> $$y(t)=K\left(1-e^{-t/\tau}\right),\qquad t\ge 0.$$

> [!info]
> Es el caso más simple de [[Respuesta Temporal/index | respuesta temporal]], hermano de [[Segundo Orden/index | segundo orden]] y base para [[Reduccion Orden | reducir]] sistemas de [[Orden Superior | orden superior]] con un [[Polos Ceros#Polos dominantes | polo dominante]]. Parámetros clave: $K$ ([[Ganancia Estatica | ganancia estática]]) y $\tau$ (constante de tiempo).

---

## Ejemplo

> [!ejemplo] Horno térmico de primer orden
> Un horno se modela con $G(s)=\dfrac{50}{10s+1}$, entrada $u(t)$ = voltaje [V], salida $y(t)$ = temperatura [°C]. Se aplica un escalón $u(t)=2\,\mathbf{1}(t)$.
>
> ![[primer_orden_escalon.svg]]
>
> **Paso 1 — Identificar parámetros.** Comparando con $\dfrac{K}{\tau s+1}$:
> $$K=50,\qquad \tau=10\ \text{s},\qquad \text{polo en } s=-\tfrac{1}{\tau}=-0.1.$$
>
> **Paso 2 — Valor final** (por linealidad o [[Teorema Valor Inicial Final | TVF]]):
> $$y(\infty)=K\,u_{ss}=50\cdot 2=100\ \text{°C}.\qquad
> \lim_{s\to0}s\cdot\frac{50}{10s+1}\cdot\frac{2}{s}=\frac{100}{1}=100\ \text{°C}.$$
>
> **Paso 3 — Respuesta temporal** ($U(s)=2/s$):
> $$Y(s)=\frac{50}{10s+1}\cdot\frac{2}{s}=\frac{100}{s}-\frac{100}{s+0.1}
> \;\Longrightarrow\; y(t)=100\left(1-e^{-t/10}\right).$$
>
> **Paso 4 — Tiempo al 95 % (criterio del 5 %).** $95\%$ de $100$ es $95$:
> $$1-e^{-t/10}=0.95\Rightarrow e^{-t/10}=0.05\Rightarrow t=-10\ln(0.05)=10(2.996)\approx 29.96\ \text{s}\approx 3\tau.$$
>
> **Paso 5 — Tiempo al 63 % y 98 %** (puntos característicos):
> $$t=\tau=10\ \text{s}\to y=63.2\ \text{°C};\qquad t=4\tau=40\ \text{s}\to y=98.2\ \text{°C}.$$
>
> **Paso 6 — Tiempo de subida (10 %→90 %).**
> $$t_r\approx 2.2\,\tau=22\ \text{s}.$$
>
> **Paso 7 — Error ante rampa $u(t)=3t$.** Sistema [[Error Estacionario/index | tipo 0]] ($K_v=\lim_{s\to0}sG(s)=0$):
> $$e_{ss}=\lim_{s\to0}sE(s)=\lim_{s\to0}\frac{10s+1}{10s+51}\cdot\frac{3}{s}\to\infty.$$
> No puede seguir una rampa (le falta un integrador).

---

## En qué consiste

> [!teoria] Respuesta al escalón unitario
> Con $U(s)=1/s$, por fracciones parciales:
> $$Y(s)=\frac{K}{\tau s+1}\cdot\frac{1}{s}=\frac{K}{s}-\frac{K}{s+1/\tau}
> \;\Longrightarrow\; y(t)=K\left(1-e^{-t/\tau}\right).$$
> El término $-Ke^{-t/\tau}$ es el **transitorio** (decae con $\tau$) y $K$ es el **régimen permanente**. La tabla muestra la fracción del valor final alcanzada en múltiplos de $\tau$:
>
> | $t$ | $y(t)/K$ |
> |-----|----------|
> | $0$ | $0$ |
> | $\tau$ | $1-e^{-1}\approx 0.632$ |
> | $2\tau$ | $1-e^{-2}\approx 0.865$ |
> | $3\tau$ | $1-e^{-3}\approx 0.950$ |
> | $4\tau$ | $1-e^{-4}\approx 0.982$ |
> | $5\tau$ | $1-e^{-5}\approx 0.993$ |
> | $\infty$ | $1$ |

> [!teorema] Tiempo de establecimiento $t_s$
> Tiempo en que la respuesta entra y permanece en la banda del $\pm\%$ alrededor de $y(\infty)$.

> [!demostracion]
> **Paso 1.** El error respecto al valor final es $|y(t)-y(\infty)|=Ke^{-t/\tau}$.
>
> **Paso 2.** Imponer la banda: $Ke^{-t/\tau}\le \tfrac{\%}{100}K\Rightarrow e^{-t/\tau}\le\tfrac{\%}{100}$.
>
> **Paso 3.** Tomar $\ln$ y despejar (el $-1$ invierte la desigualdad):
> $$\boxed{\,t_s=-\tau\ln\!\left(\tfrac{\%}{100}\right).}$$

> [!info] Criterios de banda
> | Criterio | $\%$ | $-\ln(\%/100)$ | $t_s$ |
> |----------|------|----------------|-------|
> | $\pm 5\%$ | $5$ | $2.996$ | $3\tau$ |
> | $\pm 2\%$ | $2$ | $3.912$ | $4\tau$ |
> | $\pm 1\%$ | $1$ | $4.605$ | $4.6\tau$ |
>
> **Regla práctica:** $t_s(2\%)=4\tau$ (la más usada en control clásico).

> [!teorema] Tiempo de subida $t_r$ (10 %→90 %)
> $$t_r=t_{90}-t_{10}=\tau\big[\ln(10)-\ln(0.9)\big]=\tau\ln\!\left(\tfrac{10}{0.9}\right)\approx 2.197\,\tau\approx 2.2\,\tau.$$

> [!info] Respuesta a otras señales de prueba
> | Entrada | Respuesta | $e_{ss}$ |
> |------|-----|-----|
> | [[Impulso \| impulso]] | $y(t)=\frac{K}{\tau}e^{-t/\tau}$ | — |
> | [[Rampa \| rampa]] | $y(t)=K\left(t-\tau+\tau e^{-t/\tau}\right)$ | $K\tau$ |
> | [[Parabola \| parábola]] | $y(t)=K\left(\frac{t^2}{2}-\tau t+\tau^2-\tau^2 e^{-t/\tau}\right)$ | $\infty$ |

> [!info] En MATLAB
> ```matlab
> K=50; tau=10;
> G = tf(K, [tau 1]);   % 50/(10s+1)
> step(2*G)             % respuesta al escalon de 2 V
> stepinfo(G)           % t_s, t_r, valor final
> ```

---

## Limitaciones

> [!warning]
> 1. Los sistemas reales rara vez son de primer orden puro.
> 2. En la práctica se aproximan por primer orden si existe un [[Polos Ceros#Polos dominantes | polo dominante]] (ver [[Reduccion Orden]]).
> 3. La respuesta no tiene sobrepico: no modela sistemas subamortiguados (ver [[Segundo Orden/index | segundo orden]]).

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | FT | $G(s)=\dfrac{K}{\tau s+1}$ |
> | Polo | $s=-1/\tau$ (estable si $\tau>0$) |
> | Respuesta escalón | $y(t)=K(1-e^{-t/\tau})$ |
> | $y(\tau)$ | $0.632\,K$ (63 %) |
> | $t_s(2\%)$ | $4\tau$ |
> | $t_r$ (10–90 %) | $2.2\tau$ |
> | Sobrepico | ninguno |

> [!corolario]
> Un sistema de primer orden queda totalmente descrito por $K$ y $\tau$: la ganancia fija el valor final $y(\infty)=K\,u_{ss}$ y la constante de tiempo fija la velocidad (63 % en $\tau$, asentado en $4\tau$). Sin polos complejos no hay oscilación ni sobrepico; cuando un sistema mayor tiene un polo mucho más lento que los demás, se comporta como uno de primer orden (ver [[Reduccion Orden]]).

> [!referencia]
> - Forma general: [[Funcion Transferencia/index]] · [[Ganancia Estatica]].
> - Dinámica con dos polos: [[Segundo Orden/index]].
> - Polo dominante y aproximación: [[Polos Ceros]] · [[Reduccion Orden]].
> - Valor final y error: [[Teorema Valor Inicial Final]] · [[Error Estacionario/index]].
> - Señales de prueba: [[Escalon]] · [[Rampa]] · [[Parabola]] · [[Impulso]].
