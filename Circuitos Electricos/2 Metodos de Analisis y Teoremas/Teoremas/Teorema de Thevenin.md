---
title: Teorema de Thévenin
order: 2
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - thevenin
draft: false
aliases:
  - teorema de Thévenin
  - equivalente Thévenin
  - Thevenin
  - Thévenin's theorem
---

# Teorema de Thévenin

> [!definicion]
> **Cualquier** red lineal de dos terminales se comporta, vista desde ellos, como una **fuente de tensión $V_{Th}$ en serie con una resistencia $R_{Th}$**. La $V_{Th}$ es la **tensión en vacío** (en circuito abierto) entre los terminales; la $R_{Th}$ es la resistencia vista desde ellos con **todas las fuentes independientes anuladas** (las de tensión en cortocircuito, las de corriente abiertas). La carga conectada no distingue la red original de su equivalente.

> [!info]
> El teorema más útil de [[Teoremas/index| Teoremas de circuitos]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]). Su dual es el [[Teorema de Norton]], y se pasa de uno a otro por una [[Transformacion de Fuentes| transformación de fuente]] ($V_{Th}=I_N R_{Th}$). Es la base de la [[Maxima Transferencia de Potencia]]. Fraile Mora, cap. 1, §1.15.

---

## Ejemplo

> [!ejemplo]
> **Equivalente Thévenin visto desde $a$-$b$.**
>
> En la red, $V_s = 12\ \text{V}$, $R_1 = 6\ \Omega$ (en serie) y $R_2 = 12\ \Omega$ (entre los terminales $a$-$b$). Hallar su equivalente de Thévenin.
>
> ![[thevenin.svg|620]]
>
> *La red de la izquierda, vista desde $a$-$b$, equivale a $V_{Th}$ en serie con $R_{Th}$.*
>
> **Paso 1 — Tensión en vacío $V_{Th}$.** Sin carga en $a$-$b$ no circula corriente por fuera, así que $R_1$ y $R_2$ forman un divisor de tensión:
> $$V_{Th} = V_s\,\frac{R_2}{R_1+R_2} = 12\cdot\frac{12}{6+12} = 8\ \text{V}.$$
>
> **Paso 2 — Resistencia equivalente $R_{Th}$.** Se **anula** la fuente ($V_s$ en cortocircuito) y se mira desde $a$-$b$: $R_1$ y $R_2$ quedan **en paralelo**:
> $$R_{Th} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1+R_2} = \frac{6\cdot 12}{18} = 4\ \Omega.$$
>
> > [!solucion]
> > $V_{Th} = 8\ \text{V}$, $R_{Th} = 4\ \Omega$. Cualquier carga $R_L$ en $a$-$b$ recibe la misma corriente que en la red original: $i_L = \dfrac{V_{Th}}{R_{Th}+R_L} = \dfrac{8}{4+R_L}$. Por ejemplo, con $R_L = 4\ \Omega$, $i_L = 1\ \text{A}$.

---

## En qué consiste

> [!teoria] Por qué toda red lineal se reduce a una fuente y una resistencia
> Por **linealidad** y [[Proporcionalidad y Superposicion| superposición]], la relación entre la tensión $v$ y la corriente $i$ en los terminales de cualquier red lineal es una **recta**: $v = V_{Th} - R_{Th}\,i$. Esa recta queda fijada por dos puntos: el de **vacío** ($i=0$, donde $v=V_{Th}$) y la **pendiente** $-R_{Th}$. Cualquier circuito con esa misma recta es indistinguible, y el más simple que la produce es justamente $V_{Th}$ en serie con $R_{Th}$.

> [!algoritmo] Cómo hallar el equivalente de Thévenin
> **Paso 1 — $V_{Th}$:** desconectar la carga y calcular la **tensión en vacío** entre los terminales (con cualquier método: divisores, mallas, nodos).
>
> **Paso 2 — $R_{Th}$:** **anular las fuentes independientes** (tensión → corto, corriente → abierto) y calcular la resistencia vista desde los terminales (asociaciones serie/paralelo o $V$-$\Omega$).
>
> **Paso 3 — Con fuentes dependientes:** no se pueden anular. Se aplica una **fuente de prueba** de $1\ \text{V}$ (o $1\ \text{A}$) en los terminales y $R_{Th}=v_{\text{prueba}}/i_{\text{prueba}}$; alternativamente, $R_{Th}=V_{Th}/I_{cc}$ con $I_{cc}$ la corriente de cortocircuito.

> [!proposicion] $R_{Th}$ a partir del cortocircuito
> Si se calcula también la **corriente de cortocircuito** $I_{cc}$ (la que circula al unir $a$-$b$), entonces
> $$R_{Th}=\frac{V_{Th}}{I_{cc}}.$$
> En el ejemplo, $I_{cc}=V_s/R_1=12/6=2\ \text{A}$, y $R_{Th}=8/2=4\ \Omega$, igual que antes. Esa $I_{cc}$ es precisamente la fuente del [[Teorema de Norton| equivalente de Norton]].

> [!warning]
> Las fuentes **dependientes nunca se anulan**: dependen de variables del circuito. Y $R_{Th}$ se mide con las fuentes independientes desactivadas, **no** con la carga conectada. Olvidar uno u otro punto es el error típico.

## Resumen

> [!resumen]
> | Elemento | Cómo se obtiene |
> |:---|:---|
> | $V_{Th}$ | tensión en **vacío** entre los terminales |
> | $R_{Th}$ | resistencia vista con fuentes indep. **anuladas** |
> | $R_{Th}$ (alternativa) | $V_{Th}/I_{cc}$ |
> | con fuentes dependientes | fuente de prueba: $R_{Th}=v_p/i_p$ |
> | equivalente | $V_{Th}$ **en serie** con $R_{Th}$ |

> [!corolario]
> Thévenin convierte una red arbitrariamente complicada en dos elementos. Para estudiar el efecto de **distintas cargas** —y en particular la que extrae **máxima potencia**— basta el equivalente, sin reanalizar el circuito cada vez. → [[Maxima Transferencia de Potencia]].

> [!referencia]
> Fraile Mora, cap. 1, §1.15. Dual: [[Teorema de Norton]]. Aplicación: [[Maxima Transferencia de Potencia]]. Base teórica: [[Proporcionalidad y Superposicion]].
