---
title: Circuito RC
order: 2
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - primer-orden
  - rc
draft: false
aliases:
  - circuito RC
  - carga y descarga del condensador
  - transitorio RC
  - RC circuit
---

# Circuito RC

> [!definicion]
> El circuito **RC** de primer orden: un condensador $C$ que se **carga** o **descarga** a través de una resistencia $R$. Su variable de estado es la **tensión** $v_C$ (que no salta), y su transitorio es una exponencial con **constante de tiempo** $\tau=RC$:
> $$v_C(t)=v_C(\infty)+\big[v_C(0^+)-v_C(\infty)\big]\,e^{-t/\tau}.$$

> [!info]
> Uno de los dos circuitos de [[Transitorios Primer Orden/index| primer orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]; **dual** del [[Circuito RL]]. Se apoya en la ley y la continuidad del [[Capacitor]]. Caso particular del método de [[Respuesta Completa Primer Orden]]. Fraile Mora, cap. 4, §4.4.2.

---

## Ejemplo

> [!ejemplo]
> **Carga de un condensador.**
>
> En el circuito, $V_s=10\ \text{V}$, $R=2\ \text{k}\Omega$ y $C=1\ \mu\text{F}$, con el condensador inicialmente **descargado** ($v_C(0^-)=0$). En $t=0$ se cierra el interruptor. Hallar $v_C(t)$ e $i(t)$.
>
> ![[circuito_rc.svg|360]]
>
> *Al cerrar en $t=0$, la fuente carga el condensador a través de $R$.*
>
> **Paso 1 — Los tres datos.**
> - Valor inicial: por continuidad, $v_C(0^+)=v_C(0^-)=0$.
> - Valor final: en régimen permanente el condensador es un [[Circuitos DC en Estado Estable| abierto]], no circula corriente y toda la fuente cae en $C$: $v_C(\infty)=V_s=10\ \text{V}$.
> - Constante de tiempo: $\tau=RC=2\ \text{k}\Omega\cdot1\ \mu\text{F}=2\ \text{ms}$.
>
> **Paso 2 — Sustituir en la fórmula.**
> $$v_C(t)=10+(0-10)\,e^{-t/\tau}=10\big(1-e^{-t/2\,\text{ms}}\big)\ \text{V}.$$
>
> **Paso 3 — La corriente.** $i=C\dfrac{dv_C}{dt}=\dfrac{V_s}{R}e^{-t/\tau}$, o bien por la malla $i=(V_s-v_C)/R$:
> $$i(t)=\frac{10}{2\,\text{k}\Omega}\,e^{-t/2\,\text{ms}}=5\,e^{-t/2\,\text{ms}}\ \text{mA}.$$
>
> ![[rc_respuesta.svg|470]]
>
> *La tensión sube hacia $V_s$ (alcanza el $63\%$ en $t=\tau$); la corriente arranca en $V_s/R$ y decae.*
>
> > [!solucion]
> > $v_C(t)=10(1-e^{-t/2\,\text{ms}})\ \text{V}$, $i(t)=5\,e^{-t/2\,\text{ms}}\ \text{mA}$. En $t=\tau= 2\ \text{ms}$, $v_C=6{,}32\ \text{V}$; en $5\tau=10\ \text{ms}$, $v_C\approx10\ \text{V}$ (cargado).

---

## En qué consiste

> [!teoria] Carga y descarga
> El RC tiene dos transitorios duales entre sí:
> - **Carga:** con la fuente conectada, $v_C$ sube de $0$ a $V_s$ como $V_s(1-e^{-t/\tau})$; la corriente decae de $V_s/R$ a $0$.
> - **Descarga:** sin fuente (el condensador alimenta a $R$), $v_C$ cae de su valor inicial $V_0$ a $0$ como $V_0\,e^{-t/\tau}$; la corriente también decae.
>
> En ambos casos la **misma** $\tau=RC$ fija la rapidez. Una $R$ grande (poca corriente) o una $C$ grande (mucha carga que mover) hacen el proceso **lento**.

> [!teorema] La ecuación del RC en carga
> Por la LKV, $V_s = Ri + v_C$ con $i=C\,dv_C/dt$, de donde
> $$RC\,\frac{dv_C}{dt}+v_C = V_s,$$
> una ecuación de primer orden con $\tau=RC$ y solución $v_C=V_s+(v_C(0)-V_s)e^{-t/RC}$.

> [!demostracion]
> **Paso 1 — Plantear.** LKV en la malla: $V_s=Ri+v_C$. Sustituir $i=C\dfrac{dv_C}{dt}$: $RC\,\dfrac{dv_C}{dt}+v_C=V_s$. **Paso 2 — Homogénea.** $RC\,v_C'+v_C=0$ tiene solución $A\,e^{-t/RC}$. **Paso 3 — Particular.** Una constante $v_C=V_s$ satisface la ecuación (en permanente $v_C'=0$). **Paso 4 — General + inicial.** $v_C=V_s+A\,e^{-t/RC}$; imponiendo $v_C(0)=v_C(0^-)$ se obtiene $A=v_C(0)-V_s$, es decir $v_C=V_s+(v_C(0)-V_s)e^{-t/RC}$. $\blacksquare$

> [!algoritmo] Resolver un RC
> **Paso 1 —** $v_C(0^+)=v_C(0^-)$ (continuidad, del estado previo). **Paso 2 —** $v_C(\infty)$: con $C$ abierto en DC permanente. **Paso 3 —** $\tau=R_{eq}C$, con $R_{eq}$ la resistencia que ve el condensador (su [[Teorema de Thevenin| equivalente de Thévenin]]) con las fuentes anuladas. **Paso 4 —** sustituir en $v_C(t)=v_C(\infty)+[v_C(0^+)-v_C(\infty)]e^{-t/\tau}$.

> [!warning]
> En $\tau=R_{eq}C$, la $R_{eq}$ **no** es siempre la $R$ dibujada: es la resistencia equivalente vista desde los bornes del condensador, anulando las fuentes. Y la corriente $i$ **sí** puede saltar en $t=0$ (a $V_s/R$), aunque $v_C$ no.

## Resumen

> [!resumen]
> | Magnitud | Carga ($v_C(0)=0$) | Descarga ($v_C(0)=V_0$) |
> |:---|:---|:---|
> | $v_C(t)$ | $V_s(1-e^{-t/\tau})$ | $V_0\,e^{-t/\tau}$ |
> | $i(t)$ | $\dfrac{V_s}{R}e^{-t/\tau}$ | $-\dfrac{V_0}{R}e^{-t/\tau}$ |
> | $\tau$ | $RC$ | $RC$ |
> | en $t=\tau$ | $63\%$ de $V_s$ | $37\%$ de $V_0$ |

> [!corolario]
> El RC carga y descarga su condensador con una exponencial de $\tau=RC$. Es el comportamiento que, en su [[Circuito RL| dual]] el RL, le ocurre a la corriente del inductor; y el ladrillo de filtros y temporizadores. Su versión general es [[Respuesta Completa Primer Orden]].

> [!referencia]
> Fraile Mora, cap. 4, §4.4.2. Dual: [[Circuito RL]]. Base: [[Capacitor]], [[Constante de Tiempo]]. Método general: [[Respuesta Completa Primer Orden]].
