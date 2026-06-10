---
title: Circuito RLC Paralelo
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - segundo-orden
  - rlc
draft: false
aliases:
  - circuito RLC paralelo
  - RLC paralelo
  - parallel RLC circuit
---

# Circuito RLC Paralelo

> [!definicion]
> El **RLC paralelo** —una resistencia $R$, un inductor $L$ y un condensador $C$ conectados **en
> paralelo** y excitados por una **fuente de corriente**— es el **dual** del
> [[Circuito RLC Serie| RLC serie]]. Por la LKC, su **tensión común** $v$ obedece una ecuación de
> segundo orden
> $$\frac{d^2 v}{dt^2}+2\alpha\,\frac{dv}{dt}+\omega_0^2\,v=0,\qquad \alpha=\frac{1}{2RC},\quad \omega_0=\frac{1}{\sqrt{LC}}.$$
> La frecuencia natural $\omega_0$ es **la misma** que en serie, pero el amortiguamiento $\alpha$ tiene
> **otra fórmula**: $1/2RC$ en vez de $R/2L$.

> [!info]
> El segundo circuito de [[Transitorios Segundo Orden/index| segundo orden]] del
> [[3 Almacenamiento y Transitorios/index| capítulo 3]]; **dual** del [[Circuito RLC Serie]]. Sus tres
> respuestas posibles están en [[Regimenes de Amortiguamiento]]. Fraile Mora, cap. 4, §4.6.

---

## Ejemplo

> [!ejemplo]
> **Identificar el régimen y la frecuencia.**
>
> En el RLC paralelo, $R=100\ \Omega$, $L=10\ \text{mH}$ y $C=1\ \mu\text{F}$. Hallar $\alpha$,
> $\omega_0$ y el tipo de respuesta.
>
> ![[circuito_rlc_paralelo.svg|420]]
>
> *$R$, $L$ y $C$ en paralelo bajo una fuente de corriente; la tensión común $v$ es la incógnita.*
>
> **Paso 1 — Frecuencia natural.**
> $$\omega_0=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{10\,\text{mH}\cdot1\,\mu\text{F}}}=\frac{1}{\sqrt{10^{-8}}}=10^{4}\ \text{rad/s}.$$
> Es **idéntica** a la del serie: solo depende de $L$ y $C$.
>
> **Paso 2 — Amortiguamiento.**
> $$\alpha=\frac{1}{2RC}=\frac{1}{2\cdot100\ \Omega\cdot1\,\mu\text{F}}=\frac{1}{2\times10^{-4}}=5\times10^{3}\ \text{s}^{-1}.$$
>
> **Paso 3 — Comparar.** $\zeta=\alpha/\omega_0=0{,}5<1$: **subamortiguado**, oscila. Las raíces son
> complejas, $s=-\alpha\pm j\omega_d$, con
> $$\omega_d=\sqrt{\omega_0^2-\alpha^2}=\sqrt{10^{8}-2{,}5\times10^{7}}\approx 8{,}66\times10^{3}\ \text{rad/s}.$$
>
> > [!solucion]
> > $\alpha=5000\ \text{s}^{-1}$, $\omega_0=10^4\ \text{rad/s}$, $\zeta=0{,}5$ → **subamortiguado**. La
> > tensión es $v(t)=e^{-5000t}\big(A\cos\omega_d t+B\sin\omega_d t\big)$ con
> > $\omega_d\approx 8660\ \text{rad/s}$; las constantes $A,B$ se fijan con las condiciones iniciales
> > $v_C(0^+)$ e $i_L(0^+)$.

---

## En qué consiste

> [!teoria] La dualidad serie–paralelo
> El RLC paralelo es el **dual** del serie: se obtiene intercambiando las variables y elementos
> conjugados. Donde el serie tiene LKV, malla, corriente $i$ y $\alpha=R/2L$, el paralelo tiene LKC,
> nodo, tensión $v$ y $\alpha=1/2RC$. La estructura de la ecuación —y por tanto los regímenes— es la
> misma; solo cambia **qué** combinación de elementos hace de amortiguamiento. Por eso $\omega_0$
> coincide y $\alpha$ no.

> [!teorema] De la LKC a la ecuación de segundo orden
> Aplicando la LKC en el nodo superior (referencia abajo), las corrientes de los tres elementos suman
> la de la fuente:
> $$i_R+i_L+i_C=I_s\;\;\Longrightarrow\;\;\frac{v}{R}+\frac{1}{L}\int v\,dt+C\frac{dv}{dt}=I_s.$$
> Derivando respecto al tiempo para quitar la integral y dividiendo por $C$:
> $$\frac{d^2v}{dt^2}+\frac{1}{RC}\frac{dv}{dt}+\frac{1}{LC}\,v=0\;\;\Longrightarrow\;\;\frac{d^2v}{dt^2}+2\alpha\frac{dv}{dt}+\omega_0^2 v=0,$$
> identificando $2\alpha=1/RC$ (de ahí $\alpha=1/2RC$) y $\omega_0^2=1/LC$. La **ecuación
> característica** $s^2+2\alpha s+\omega_0^2=0$ da las raíces $s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$,
> y el signo del discriminante decide el régimen igual que en serie.

> [!proposicion] La $R$ crítica (¡al revés que en serie!)
> El paso de no oscilar a oscilar ocurre en $\alpha=\omega_0$, es decir $\dfrac{1}{2RC}=\dfrac{1}{\sqrt{LC}}$,
> de donde
> $$R_{\text{crit}}=\frac{1}{2}\sqrt{\frac{L}{C}}.$$
> **Atención a la dualidad:** en paralelo una $R$ **pequeña** amortigua MÁS (más corriente se desvía
> por la resistencia), justo al revés que en serie, donde es una $R$ **grande** la que amortigua más.
> Con $R<R_{\text{crit}}$ no hay oscilación (sobreamortiguado); con $R>R_{\text{crit}}$, sí. En el
> ejemplo, $R_{\text{crit}}=\tfrac{1}{2}\sqrt{10\,\text{mH}/1\,\mu\text{F}}=50\ \Omega$, y como
> $R=100>50$, oscila.

> [!warning]
> No usar $\alpha=R/2L$: **esa es la fórmula del serie**. En paralelo $\alpha=1/2RC$. Como en todo
> circuito de segundo orden, hacen falta **dos** condiciones iniciales —las variables de estado
> $v_C(0^+)$ e $i_L(0^+)$, ambas continuas— para determinar las dos constantes de la respuesta.

## Resumen

> [!resumen]
> | Cantidad | Serie | Paralelo |
> |:---|:---|:---|
> | Ley aplicada | LKV (malla) | LKC (nodo) |
> | Incógnita | corriente $i$ | tensión $v$ |
> | EDO | $i''+2\alpha i'+\omega_0^2 i=0$ | $v''+2\alpha v'+\omega_0^2 v=0$ |
> | Amortiguamiento | $\alpha=R/2L$ | $\alpha=1/2RC$ |
> | Frecuencia natural | $\omega_0=1/\sqrt{LC}$ | $\omega_0=1/\sqrt{LC}$ |
> | $R$ crítica | $R_{\text{crit}}=2\sqrt{L/C}$ | $R_{\text{crit}}=\tfrac12\sqrt{L/C}$ |
> | Efecto de $R$ | $R$ grande amortigua más | $R$ pequeña amortigua más |
> | Condiciones iniciales | $i_L(0^+)$ y $v_C(0^+)$ | $v_C(0^+)$ e $i_L(0^+)$ |

> [!corolario]
> El RLC paralelo comparte $\omega_0=1/\sqrt{LC}$ con su [[Circuito RLC Serie| dual]] y solo cambia el
> amortiguamiento a $\alpha=1/2RC$. Como $\alpha^2-\omega_0^2$ se interpreta igual, las tres respuestas
> posibles son las mismas de [[Regimenes de Amortiguamiento]]; lo que se invierte es el papel de $R$.

> [!referencia]
> Fraile Mora, cap. 4, §4.6. Dual: [[Circuito RLC Serie]]. Regímenes:
> [[Regimenes de Amortiguamiento]]. Base: [[Inductor]], [[Capacitor]].
