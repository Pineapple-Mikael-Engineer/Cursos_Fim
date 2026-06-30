---
title: Métodos en Régimen Fasorial
order: 1
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - métodos en régimen fasorial
  - análisis de circuitos AC
  - mallas y nodos en CA
---

# Métodos en Régimen Fasorial

> [!definicion]
> En régimen permanente sinusoidal, los **métodos de análisis** son los mismos que en CC, aplicados con fasores e impedancias: la **ley de Ohm** $\overline{V}=Z\,\overline{I}$, las **leyes de Kirchhoff** ($\sum\overline{I}=0$, $\sum\overline{V}=0$), los **divisores**, el **análisis de mallas y nodos** y los **teoremas de Thévenin/Norton/superposición** valen letra por letra, cambiando números reales por complejos.

> [!info]
> El núcleo del [[Analisis Fasorial/index| análisis fasorial]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Aplica las [[Impedancia y Admitancia/index| impedancias]] con los [[2 Metodos de Analisis y Teoremas/index| métodos del capítulo 2]]. Fraile Mora, cap. 2, §2.8.

---

## Ejemplo

> [!ejemplo]
> **Resolver un RL serie en CA.**
>
> Una fuente $\overline{V}=100\angle0^\circ\ \text{V}$ (eficaz) alimenta una resistencia $R=3\ \Omega$ en serie con un inductor de reactancia $X_L=4\ \Omega$. Hallar la corriente y las tensiones de cada elemento.
>
> ![[circuito_ac.svg|360]]
>
> *Mismo circuito que en CC, pero con fuente senoidal e impedancias: se resuelve con la ley de Ohm compleja.*
>
> **Paso 1 — Impedancia total.** $Z=R+jX_L=3+j4=5\angle53^\circ\ \Omega$ (ver [[Impedancia Compleja]]).
>
> **Paso 2 — Corriente (ley de Ohm).**
> $$\overline{I}=\frac{\overline{V}}{Z}=\frac{100\angle0^\circ}{5\angle53^\circ}=20\angle(-53^\circ)\ \text{A}.$$
>
> **Paso 3 — Tensiones de rama.**
> $$\overline{V}_R=R\,\overline{I}=3\cdot20\angle(-53^\circ)=60\angle(-53^\circ)\ \text{V},$$
> $$\overline{V}_L=jX_L\,\overline{I}=4\angle90^\circ\cdot20\angle(-53^\circ)=80\angle37^\circ\ \text{V}.$$
>
> > [!solucion]
> > $\overline{I}=20\angle(-53^\circ)\ \text{A}$ (atrasa $53^\circ$ a la tensión: carga inductiva). Verificación de la LKV: $\overline{V}_R+\overline{V}_L=(36-j48)+(64+j48)=100\angle0^\circ=\overline {V}$. **Las tensiones se suman como vectores** ([[Diagramas Fasoriales]]).

---

## En qué consiste

> [!teoria] El diccionario CC → CA
> Resolver un circuito de CA es traducir el procedimiento de CC término a término:
>
> | Análisis resistivo (CC) | Análisis fasorial (CA) |
> |:---|:---|
> | ley de Ohm $v=Ri$ | $\overline{V}=Z\,\overline{I}$ |
> | LKC $\sum i=0$, LKV $\sum v=0$ | $\sum\overline{I}=0$, $\sum\overline{V}=0$ |
> | $R_{eq}$ serie/paralelo | $Z_{eq}$ serie/paralelo |
> | divisores de $v$ e $i$ | divisores con $Z$ |
> | matriz $R$ (mallas), $G$ (nodos) | matriz $Z$, $Y$ (complejas) |
> | Thévenin $V_{Th}$, $R_{Th}$ | $\overline{V}_{Th}$, $Z_{Th}$ |
>
> Lo único que cambia es que las operaciones son entre **números complejos**.

> [!algoritmo] Resolver un circuito en régimen fasorial
> **Paso 1 —** Pasar fuentes y respuestas a **fasores** (módulo eficaz, fase) y elementos a **impedancias** $Z$. **Paso 2 —** Elegir el método (divisores, mallas, nodos, Thévenin…) **como en CC**, planteando las ecuaciones con $Z$ y fasores. **Paso 3 —** Resolver el sistema **complejo** (sumas en rectangular, productos/cocientes en polar). **Paso 4 —** Volver al tiempo si se pide: $\overline{V}=V\angle\varphi\Rightarrow v(t)=\sqrt2\,V \operatorname{sen}(\omega t+\varphi)$.

> [!proposicion] Thévenin y superposición en CA
> El [[Teorema de Thevenin| equivalente de Thévenin]] vale igual: $\overline{V}_{Th}$ es la tensión en vacío y $Z_{Th}$ la impedancia vista con las fuentes anuladas. La [[Proporcionalidad y Superposicion| superposición]] también, **con una salvedad**: si hay fuentes de **distinta frecuencia**, se resuelve cada frecuencia por separado (cada una tiene sus propias impedancias) y se suman las respuestas **en el tiempo**, no en fasores.

> [!warning]
> Todos los fasores e impedancias de un mismo cálculo deben ser **a la misma frecuencia**. Las sumas se hacen en forma **rectangular** y los productos/cocientes en **polar**. Y el resultado es un fasor: para la senoide, recordar el factor $\sqrt2$ y la frecuencia $\omega$.

## Resumen

> [!resumen]
> | Paso | Acción |
> |:---|:---|
> | 1 | fuentes/respuestas → fasores; elementos → $Z$ |
> | 2 | método de CC con $Z$ y fasores |
> | 3 | resolver el sistema complejo |
> | 4 | volver al tiempo si hace falta |
> | Ley de Ohm | $\overline{I}=\overline{V}/Z$ |

> [!corolario]
> El análisis fasorial no añade métodos: reutiliza **todos** los del capítulo 2 con álgebra compleja. Dominar la aritmética de complejos y la impedancia es cuanto separa resolver un circuito de CA de uno de CC.

> [!referencia]
> Fraile Mora, cap. 2, §2.8. Usa: [[Impedancia Compleja]], [[Analisis de Mallas]], [[Analisis de Nodos]], [[Teorema de Thevenin]]. Apoyo gráfico: [[Diagramas Fasoriales]].
