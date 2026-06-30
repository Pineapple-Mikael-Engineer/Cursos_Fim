---
title: Circuito RL
order: 1
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - primer-orden
  - rl
draft: false
aliases:
  - circuito RL
  - magnetización del inductor
  - transitorio RL
  - RL circuit
---

# Circuito RL

> [!definicion]
> El circuito **RL** de primer orden: un inductor $L$ que se **magnetiza** o **desmagnetiza** a través de una resistencia $R$. Su variable de estado es la **corriente** $i_L$ (que no salta), y su transitorio es una exponencial con **constante de tiempo** $\tau=L/R$:
> $$i_L(t)=i_L(\infty)+\big[i_L(0^+)-i_L(\infty)\big]\,e^{-t/\tau}.$$

> [!info]
> El **dual** del [[Circuito RC]] ($v_C\leftrightarrow i_L$, $C\leftrightarrow L$, $RC\leftrightarrow L/R$), uno de los circuitos de [[Transitorios Primer Orden/index| primer orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Se apoya en la ley y la continuidad del [[Inductor]]. Fraile Mora, cap. 4, §4.4.1.

---

## Ejemplo

> [!ejemplo]
> **Magnetización de un inductor.**
>
> En el circuito, $V_s=10\ \text{V}$, $R=5\ \Omega$ y $L=10\ \text{mH}$, con el inductor inicialmente **desenergizado** ($i_L(0^-)=0$). En $t=0$ se cierra el interruptor. Hallar $i_L(t)$ y $v_L(t)$.
>
> ![[circuito_rl.svg|360]]
>
> *Al cerrar en $t=0$, la fuente establece la corriente en el inductor a través de $R$.*
>
> **Paso 1 — Los tres datos.**
> - Valor inicial: por continuidad, $i_L(0^+)=i_L(0^-)=0$.
> - Valor final: en régimen permanente el inductor es un [[Circuitos DC en Estado Estable| corto]], y toda la tensión cae en $R$: $i_L(\infty)=V_s/R=10/5=2\ \text{A}$.
> - Constante de tiempo: $\tau=L/R=10\ \text{mH}/5\ \Omega=2\ \text{ms}$.
>
> **Paso 2 — Sustituir en la fórmula.**
> $$i_L(t)=2+(0-2)\,e^{-t/\tau}=2\big(1-e^{-t/2\,\text{ms}}\big)\ \text{A}.$$
>
> **Paso 3 — La tensión.** $v_L=L\dfrac{di_L}{dt}=V_s\,e^{-t/\tau}$:
> $$v_L(t)=10\,e^{-t/2\,\text{ms}}\ \text{V}.$$
>
> ![[rl_respuesta.svg|470]]
>
> *La corriente sube hacia $V_s/R$ (alcanza el $63\%$ en $t=\tau$); la tensión arranca en $V_s$ y decae.*
>
> > [!solucion]
> > $i_L(t)=2(1-e^{-t/2\,\text{ms}})\ \text{A}$, $v_L(t)=10\,e^{-t/2\,\text{ms}}\ \text{V}$. En $t=\tau=2\ \text{ms}$, $i_L=1{,}26\ \text{A}$; en $5\tau=10\ \text{ms}$, $i_L\approx2\ \text{A}$.

---

## En qué consiste

> [!teoria] Magnetización y desmagnetización
> Como el RC, el RL tiene dos transitorios duales:
> - **Magnetización:** con la fuente conectada, $i_L$ sube de $0$ a $V_s/R$ como $\dfrac{V_s}{R}(1-e^{-t/\tau})$; la tensión $v_L$ decae de $V_s$ a $0$.
> - **Desmagnetización:** sin fuente, $i_L$ cae de su valor inicial $I_0$ a $0$ como $I_0\,e^{-t/\tau}$, descargando su energía en la resistencia.
>
> La **misma** $\tau=L/R$ fija la rapidez. Una $L$ grande (mucho flujo que mover) o una $R$ pequeña hacen el proceso **lento** —al revés que en el RC respecto a $R$, por la dualidad—.

> [!teorema] La ecuación del RL en magnetización
> Por la LKV, $V_s=Ri_L+v_L$ con $v_L=L\,di_L/dt$, de donde
> $$\frac{L}{R}\,\frac{di_L}{dt}+i_L=\frac{V_s}{R},$$
> de primer orden con $\tau=L/R$ y solución $i_L=\dfrac{V_s}{R}+\left(i_L(0)-\dfrac{V_s}{R}\right)e^{-t/(L/R)}$.

> [!demostracion]
> **Paso 1 — Plantear.** LKV: $V_s=Ri_L+L\dfrac{di_L}{dt}$, es decir $\dfrac{L}{R}i_L'+i_L=\dfrac{V_s}{R}$. **Paso 2 — Homogénea.** $\dfrac{L}{R}i_L'+i_L=0$ da $A\,e^{-t/(L/R)}$. **Paso 3 — Particular.** La constante $i_L=V_s/R$ satisface la ecuación en permanente. **Paso 4 — General + inicial.** $i_L=\dfrac{V_s}{R}+A\,e^{-t/(L/R)}$; con $i_L(0)=i_L(0^-)$, $A=i_L(0)-V_s/R$. $\blacksquare$ Es la dualidad exacta del [[Circuito RC| RC]].

> [!algoritmo] Resolver un RL
> **Paso 1 —** $i_L(0^+)=i_L(0^-)$ (continuidad). **Paso 2 —** $i_L(\infty)$: con $L$ en corto en DC permanente. **Paso 3 —** $\tau=L/R_{eq}$, con $R_{eq}$ la resistencia vista desde el inductor (Thévenin) con las fuentes anuladas. **Paso 4 —** sustituir en $i_L(t)=i_L(\infty)+[i_L(0^+)-i_L(\infty)]e^{-t/\tau}$.

> [!warning]
> La tensión $v_L$ **sí** puede saltar en $t=0$ (a $V_s$), aunque $i_L$ no. Y **abrir** un RL en conducción provoca un $di/dt$ enorme y una sobretensión peligrosa: por eso se protegen con diodos o redes de descarga.

## Resumen

> [!resumen]
> | Magnitud | Magnetización ($i_L(0)=0$) | Desmagnetización ($i_L(0)=I_0$) |
> |:---|:---|:---|
> | $i_L(t)$ | $\dfrac{V_s}{R}(1-e^{-t/\tau})$ | $I_0\,e^{-t/\tau}$ |
> | $v_L(t)$ | $V_s\,e^{-t/\tau}$ | $-R\,I_0\,e^{-t/\tau}$ |
> | $\tau$ | $L/R$ | $L/R$ |
> | en $t=\tau$ | $63\%$ de $V_s/R$ | $37\%$ de $I_0$ |

> [!corolario]
> El RL establece y extingue la corriente de su inductor con una exponencial de $\tau=L/R$: el espejo exacto del [[Circuito RC| RC]] con $v\leftrightarrow i$. Conocido uno, el otro sale por dualidad.

> [!referencia]
> Fraile Mora, cap. 4, §4.4.1. Dual: [[Circuito RC]]. Base: [[Inductor]], [[Constante de Tiempo]]. Método general: [[Respuesta Completa Primer Orden]].
