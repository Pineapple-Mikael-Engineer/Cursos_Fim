---
title: Respuesta de Elementos Pasivos
tags:
  - circuitos-electricos
  - teoria
  - impedancia
draft: false
aliases:
  - respuesta de elementos pasivos
  - respuesta sinusoidal de R L C
  - reactancia inductiva y capacitiva
---

# Respuesta de Elementos Pasivos en CA

> [!definicion]
> Ante una excitación sinusoidal, cada elemento pasivo responde con una corriente senoidal de la misma
> frecuencia pero **desfasada** y **escalada** según su oposición: la **resistencia** $R$ no desfasa
> ($i$ en fase, oposición $R$); el **inductor** hace que $i$ **atrase** $90^\circ$ con oposición
> $X_L=\omega L$; el **condensador** hace que $i$ **adelante** $90^\circ$ con oposición
> $\lvert X_C\rvert=1/\omega C$.

> [!info]
> El origen físico de la [[Impedancia Compleja| impedancia]] en
> [[Impedancia y Admitancia/index| Impedancia y admitancia]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Es la versión temporal de lo que [[Fasores Electricos]] muestra con
> fasores. Fraile Mora, cap. 2, §2.6.

---

## Ejemplo

> [!ejemplo]
> **Las tres respuestas en el tiempo.**
>
> A los tres elementos se les aplica la misma tensión $v(t)=V_m\operatorname{sen}\omega t$. ¿Cómo es la
> corriente en cada uno?
>
> ![[respuesta_pasivos.svg|640]]
>
> *Resistencia: $i$ en fase con $v$. Inductor: $i$ atrasa $90^\circ$ (su pico llega después).
> Condensador: $i$ adelanta $90^\circ$ (su pico llega antes).*
>
> **Resistencia.** $i=\dfrac{v}{R}=\dfrac{V_m}{R}\operatorname{sen}\omega t$: en fase, amplitud $V_m/R$.
>
> **Inductor.** $i=\dfrac{1}{L}\!\int v\,dt=\dfrac{V_m}{\omega L}\operatorname{sen}(\omega t-90^\circ)$:
> **atrasa** $90^\circ$, amplitud $V_m/\omega L$.
>
> **Condensador.** $i=C\dfrac{dv}{dt}=\omega C V_m\operatorname{sen}(\omega t+90^\circ)$: **adelanta**
> $90^\circ$, amplitud $\omega C V_m$.
>
> > [!solucion]
> > En fase ($R$), atrasada ($L$) y adelantada ($C$). Las oposiciones son $R$, $X_L=\omega L$ y
> > $\lvert X_C\rvert=1/\omega C$: a más frecuencia, el inductor estorba **más** y el condensador
> > **menos**.

---

## En qué consiste

> [!teoria] Por qué cada uno desfasa así
> El desfase sale de la ley de cada elemento aplicada a una senoide:
> - **Resistencia** ($v=Ri$): la corriente copia a la tensión, **sin desfase**. Su oposición $R$ no
>   depende de $\omega$.
> - **Inductor** ($v=L\,di/dt$): para que la **derivada** de $i$ sea senoidal, $i$ debe ir
>   **retrasada** $90^\circ$; la oposición $X_L=\omega L$ **crece** con la frecuencia (a $\omega\to0$,
>   en CC, el inductor es un corto).
> - **Condensador** ($i=C\,dv/dt$): la corriente es la **derivada** de la tensión, luego va
>   **adelantada** $90^\circ$; la oposición $1/\omega C$ **decrece** con la frecuencia (a $\omega\to0$,
>   en CC, el condensador es un abierto).

> [!proposicion] La reactancia depende de la frecuencia
> | Elemento | Oposición | Con la frecuencia |
> |:---|:---|:---|
> | Resistencia | $R$ | constante |
> | Inductor | $X_L=\omega L$ | crece ($\propto\omega$) |
> | Condensador | $\lvert X_C\rvert=1/\omega C$ | decrece ($\propto1/\omega$) |
>
> De aquí nace el comportamiento de los filtros: el condensador deja pasar lo rápido (alta $\omega$) y
> el inductor lo lento.

> [!warning]
> El desfase es entre la corriente y la **tensión del mismo elemento**, y vale exactamente $90^\circ$
> en $L$ y $C$ **ideales** (sin pérdidas). Un inductor real tiene algo de $R$, lo que reduce el
> desfase por debajo de $90^\circ$.

## Resumen

> [!resumen]
> | Elemento | $i$ frente a $v$ | Amplitud de $i$ | Oposición |
> |:---|:---|:---|:---|
> | Resistencia | en fase | $V_m/R$ | $R$ |
> | Inductor | atrasa $90^\circ$ | $V_m/\omega L$ | $X_L=\omega L$ |
> | Condensador | adelanta $90^\circ$ | $\omega C V_m$ | $1/\omega C$ |

> [!corolario]
> Cada elemento desfasa la corriente $0^\circ$, $-90^\circ$ o $+90^\circ$ y la opone con $R$, $\omega
> L$ o $1/\omega C$. Empaquetar ambas cosas —desfase y oposición— en un complejo es justo la
> [[Impedancia Compleja]].

> [!referencia]
> Fraile Mora, cap. 2, §2.6. Se resume en la [[Impedancia Compleja]]. Versión fasorial:
> [[Fasores Electricos]].
