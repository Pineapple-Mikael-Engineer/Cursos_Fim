---
title: Teorema de Norton
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - norton
draft: false
aliases:
  - teorema de Norton
  - equivalente Norton
  - Norton
  - Norton's theorem
---

# Teorema de Norton

> [!definicion]
> El **dual** de Thévenin: cualquier red lineal de dos terminales equivale a una **fuente de corriente
> $I_N$ en paralelo con una resistencia $R_N$**. La $I_N$ es la **corriente de cortocircuito** entre
> los terminales; la $R_N$ es la misma resistencia que la de Thévenin, $R_N = R_{Th}$, vista con las
> fuentes independientes anuladas. Ambos equivalentes describen la misma red y se relacionan por
> $V_{Th} = I_N R_N$.

> [!info]
> Pareja del [[Teorema de Thevenin]] en [[Teoremas/index| Teoremas de circuitos]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]). Se obtiene uno del otro por una [[Transformacion de Fuentes| transformación de fuente]]. Fraile Mora, cap. 1, §1.15.

---

## Ejemplo

> [!ejemplo]
> **Equivalente Norton de la misma red.**
>
> La misma red que en [[Teorema de Thevenin| Thévenin]]: $V_s = 12\ \text{V}$, $R_1 = 6\ \Omega$,
> $R_2 = 12\ \Omega$, vista desde $a$-$b$.
>
> ![[norton.svg|620]]
>
> *La red equivale a una fuente de corriente $I_N$ en paralelo con $R_N$.*
>
> **Paso 1 — Corriente de cortocircuito $I_N$.** Se unen $a$-$b$ con un hilo: $R_2$ queda
> **cortocircuitada** (sus extremos al mismo potencial), así que toda la corriente pasa por el hilo y
> $$I_N = \frac{V_s}{R_1} = \frac{12}{6} = 2\ \text{A}.$$
>
> **Paso 2 — Resistencia equivalente $R_N$.** Idéntica a la de Thévenin: con $V_s$ en cortocircuito,
> $$R_N = R_{Th} = R_1 \parallel R_2 = 4\ \Omega.$$
>
> > [!solucion]
> > $I_N = 2\ \text{A}$, $R_N = 4\ \Omega$. Coincide con el equivalente de Thévenin:
> > $V_{Th} = I_N R_N = 2\cdot 4 = 8\ \text{V}$. Ante una carga $R_L$, el equivalente Norton reparte
> > $I_N$ entre $R_N$ y $R_L$ por el [[Divisor de Corriente| divisor de corriente]].

---

## En qué consiste

> [!teoria] La misma recta, leída al revés
> Thévenin y Norton describen la **misma recta** $v = V_{Th} - R_{Th}\,i$ de los terminales, pero la
> fijan con puntos distintos: Thévenin usa el de **vacío** ($V_{Th}$, con $i=0$) y Norton el de
> **cortocircuito** ($I_N$, con $v=0$, y $I_N = V_{Th}/R_{Th}$). Por eso son intercambiables: pasar de
> uno a otro es una [[Transformacion de Fuentes| transformación de fuente]], $V_{Th}=I_N R_N$ con la
> misma $R$.

> [!algoritmo] Cómo hallar el equivalente de Norton
> **Paso 1 — $I_N$:** **cortocircuitar** los terminales y calcular la corriente que circula por ese
> hilo.
>
> **Paso 2 — $R_N$:** anular las fuentes independientes y calcular la resistencia vista desde los
> terminales ($R_N = R_{Th}$). Con fuentes dependientes, usar fuente de prueba.
>
> **Paso 3 — Conversión:** si ya se tiene Thévenin, $I_N = V_{Th}/R_{Th}$ y $R_N = R_{Th}$ (y
> viceversa).

> [!proposicion] ¿Thévenin o Norton?
> Son equivalentes; se elige por comodidad. **Thévenin** encaja mejor con cargas en **serie** y con el
> análisis de **mallas**; **Norton**, con cargas en **paralelo** y el análisis de **nodos**. Para
> combinar varias fuentes reales en paralelo, Norton suele simplificar el álgebra.

> [!warning]
> $R_N = R_{Th}$ **siempre**: la resistencia equivalente no cambia entre los dos modelos. Lo único que
> cambia es la fuente ($V_{Th}$ en serie ↔ $I_N$ en paralelo). Y como en Thévenin, las fuentes
> **dependientes no se anulan**.

## Resumen

> [!resumen]
> | Elemento | Cómo se obtiene |
> |:---|:---|
> | $I_N$ | corriente de **cortocircuito** entre los terminales |
> | $R_N$ | $= R_{Th}$ (fuentes indep. anuladas) |
> | relación con Thévenin | $V_{Th} = I_N R_N$ |
> | equivalente | $I_N$ **en paralelo** con $R_N$ |

> [!corolario]
> Thévenin y Norton son la misma verdad —toda red lineal de dos terminales es una fuente y una
> resistencia— contada con la fuente dual. Tener ambos a mano permite elegir el que mejor encaje con
> el resto del circuito.

> [!referencia]
> Fraile Mora, cap. 1, §1.15. Dual: [[Teorema de Thevenin]]. Conversión:
> [[Transformacion de Fuentes]]. Aplicación: [[Maxima Transferencia de Potencia]].
