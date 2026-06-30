---
title: Circuito RLC Serie
order: 1
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - segundo-orden
  - rlc
draft: false
aliases:
  - circuito RLC serie
  - RLC serie
  - series RLC circuit
---

# Circuito RLC Serie

> [!definicion]
> El **RLC serie** es el circuito de segundo orden básico: una resistencia, un inductor y un condensador **en serie**. Por la LKV, su corriente obedece una ecuación de segundo orden
> $$\frac{d^2 i}{dt^2}+2\alpha\,\frac{di}{dt}+\omega_0^2\,i=0,\qquad \alpha=\frac{R}{2L},\quad \omega_0=\frac{1}{\sqrt{LC}}.$$
> El **amortiguamiento** $\alpha$ (por $R$) y la **frecuencia natural** $\omega_0$ determinan si la respuesta oscila o no.

> [!info]
> El primer circuito de [[Transitorios Segundo Orden/index| segundo orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]; **dual** del [[Circuito RLC Paralelo]]. Las tres formas posibles de su respuesta están en [[Regimenes de Amortiguamiento]]. Fraile Mora, cap. 4, §4.6.

---

## Ejemplo

> [!ejemplo]
> **Identificar el régimen y la frecuencia.**
>
> En el RLC serie, $R=100\ \Omega$, $L=10\ \text{mH}$ y $C=1\ \mu\text{F}$. Hallar $\alpha$, $\omega_0$ y el tipo de respuesta.
>
> ![[circuito_rlc_serie.svg|420]]
>
> *Al cerrar en $t=0$, $L$ y $C$ intercambian energía mientras $R$ la amortigua.*
>
> **Paso 1 — Frecuencia natural.**
> $$\omega_0=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{10\,\text{mH}\cdot1\,\mu\text{F}}}=\frac{1}{\sqrt{10^{-8}}}=10^{4}\ \text{rad/s}.$$
>
> **Paso 2 — Amortiguamiento.**
> $$\alpha=\frac{R}{2L}=\frac{100}{2\cdot10\,\text{mH}}=5\times10^{3}\ \text{s}^{-1}.$$
>
> **Paso 3 — Comparar.** $\zeta=\alpha/\omega_0=0{,}5<1$: **subamortiguado**, oscila. Las raíces son complejas, $s=-\alpha\pm j\omega_d$, con
> $$\omega_d=\sqrt{\omega_0^2-\alpha^2}=\sqrt{10^{8}-2{,}5\times10^{7}}\approx 8{,}66\times10^{3}\ \text{rad/s}.$$
>
> > [!solucion]
> > $\alpha=5000\ \text{s}^{-1}$, $\omega_0=10^4\ \text{rad/s}$, $\zeta=0{,}5$ → **subamortiguado**. La respuesta es $i(t)=e^{-5000t}\big(A\cos\omega_d t+B\sin\omega_d t\big)$ con $\omega_d\approx 8660\ \text{rad/s}$; las constantes $A,B$ salen de las condiciones iniciales $i_L(0)$ y $v_C(0)$.

---

## En qué consiste

> [!teoria] De la LKV a la ecuación de segundo orden
> Recorriendo la malla serie, la LKV suma las tensiones de los tres elementos:
> $$L\frac{di}{dt}+Ri+\frac{1}{C}\int i\,dt = V_s.$$
> Derivando respecto al tiempo para quitar la integral y dividiendo por $L$:
> $$\frac{d^2i}{dt^2}+\frac{R}{L}\frac{di}{dt}+\frac{1}{LC}\,i=0\;\;\Longrightarrow\;\;\frac{d^2i}{dt^2}+2\alpha\frac{di}{dt}+\omega_0^2 i=0,$$
> identificando $2\alpha=R/L$ (de ahí $\alpha=R/2L$) y $\omega_0^2=1/LC$. Es una EDO lineal de segundo orden homogénea: su solución la fija la **ecuación característica**.

> [!teorema] Ecuación característica y raíces
> Proponiendo $i\propto e^{st}$, la ecuación se vuelve algebraica:
> $$s^2+2\alpha s+\omega_0^2=0 \;\Longrightarrow\; s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}.$$
> El **discriminante** $\alpha^2-\omega_0^2$ decide el régimen: $>0$ sobreamortiguado (raíces reales distintas), $=0$ crítico (raíz doble), $<0$ subamortiguado (raíces complejas conjugadas, oscila).

> [!algoritmo] Resolver un RLC serie
> **Paso 1 —** Calcular $\alpha=R/2L$ y $\omega_0=1/\sqrt{LC}$. **Paso 2 —** Comparar: el signo de $\alpha^2-\omega_0^2$ da el régimen ([[Regimenes de Amortiguamiento]]) y la forma de la respuesta natural. **Paso 3 —** Sumar la respuesta forzada (régimen permanente, con $C$ abierto y $L$ en corto). **Paso 4 —** Imponer las **dos** condiciones iniciales —$i_L(0^+)$ y $v_C(0^+)$, ambas continuas— para fijar las dos constantes.

> [!proposicion] La $R$ crítica
> El paso de no oscilar a oscilar ocurre en $\alpha=\omega_0$, es decir
> $$R_{\text{crit}}=2\sqrt{\frac{L}{C}}.$$
> Con $R>R_{\text{crit}}$ no hay oscilación (sobreamortiguado); con $R<R_{\text{crit}}$, sí (subamortiguado). En el ejemplo, $R_{\text{crit}}=2\sqrt{10\,\text{mH}/1\,\mu\text{F}}=200\ \Omega$, y como $R=100<200$, oscila.

> [!warning]
> Un circuito de segundo orden necesita **dos** condiciones iniciales: $i_L(0^+)$ **y** $v_C(0^+)$ (las dos variables de estado, ambas continuas). Con una sola no queda determinado. Y $\alpha$ depende de la topología: aquí $R/2L$; en [[Circuito RLC Paralelo| paralelo]] es $1/2RC$.

## Resumen

> [!resumen]
> | Cantidad | Expresión (serie) |
> |:---|:---|
> | EDO | $i''+2\alpha i'+\omega_0^2 i=0$ |
> | Amortiguamiento | $\alpha=R/2L$ |
> | Frecuencia natural | $\omega_0=1/\sqrt{LC}$ |
> | Característica | $s^2+2\alpha s+\omega_0^2=0$ |
> | $R$ crítica | $R_{\text{crit}}=2\sqrt{L/C}$ |
> | Condiciones iniciales | $i_L(0^+)$ y $v_C(0^+)$ |

> [!corolario]
> El RLC serie reduce todo el segundo orden a dos números: $\alpha=R/2L$ y $\omega_0=1/\sqrt{LC}$. Su [[Circuito RLC Paralelo| dual]] cambia solo la expresión de $\alpha$. Las tres respuestas posibles son el tema de [[Regimenes de Amortiguamiento]].

> [!referencia]
> Fraile Mora, cap. 4, §4.6. Dual: [[Circuito RLC Paralelo]]. Regímenes: [[Regimenes de Amortiguamiento]]. Base: [[Inductor]], [[Capacitor]].
