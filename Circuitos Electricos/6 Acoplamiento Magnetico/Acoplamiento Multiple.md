---
title: Acoplamiento Múltiple
order: 4
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - acoplamiento múltiple
  - matriz de inductancias
  - multiple coupling
  - inductance matrix
---

# Acoplamiento Múltiple $\;[L]$

> [!definicion]
> Cuando **más de dos** bobinas están acopladas, cada una induce tensión en **todas** las demás. El sistema se ordena en una **matriz de inductancias** $[L]$, **simétrica**, con las **autoinductancias** $L_{kk}$ en la diagonal y las **inductancias mutuas** $M_{jk}$ fuera de ella:
> $$\mathbf{v}=[L]\,\frac{d\mathbf{i}}{dt},\qquad
> [L]=\begin{pmatrix} L_1 & \pm M_{12} & \pm M_{13}\\ \pm M_{12} & L_2 & \pm M_{23}\\ \pm M_{13} & \pm M_{23} & L_3\end{pmatrix}.$$
> Cada fila es la ecuación de una bobina; el signo de cada término mutuo lo fija la regla de los puntos de **ese par**.

> [!info]
> Generaliza la [[Inductancia Mutua]] a $n$ bobinas, dentro de [[6 Acoplamiento Magnetico/index| Inducción magnética]] ([[6 Acoplamiento Magnetico/index| capítulo 6]]). Los **signos** fuera de la diagonal los da la [[Regla de los Puntos]], aplicada par a par. La matriz $[L]$ se integra directamente en el [[Analisis de Mallas| análisis de mallas]] (y de nodos), sustituyendo $j\omega[L]$ en régimen sinusoidal. Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **Tensión de una bobina en un sistema de tres acopladas.**
>
> Tres bobinas con $L_1=L_2=L_3=4\ \text{H}$ y mutuas $M_{12}=2\ \text{H}$, $M_{13}=1\ \text{H}$, $M_{23}=3\ \text{H}$ (todas con signo $+$ según los puntos). En cierto instante las derivadas de las corrientes valen $i_1'=2\ \text{A/s}$, $i_2'=1\ \text{A/s}$, $i_3'=0\ \text{A/s}$. Escribir la tensión de la **bobina 1**.
>
> **Paso 1 — Tomar la primera fila de $[L]$.** La ecuación de la bobina 1 reúne su autoinducción más las mutuas con las otras dos:
> $$v_1=L_1\,i_1'+M_{12}\,i_2'+M_{13}\,i_3'.$$
>
> **Paso 2 — Sustituir los valores:**
> $$v_1=4\cdot 2+2\cdot 1+1\cdot 0=8+2+0=10\ \text{V}.$$
>
> > [!solucion]
> > $v_1=10\ \text{V}$: la **autoinducción** aporta $8\ \text{V}$ y la **mutua de la bobina 2** otros $2\ \text{V}$; la bobina 3 no contribuye porque $i_3'=0$. La misma matriz $[L]$ daría $v_2$ y $v_3$ tomando sus filas respectivas.

---

## En qué consiste

> [!teoria] Una fila por bobina
> Cada **fila** de $[L]$ es la ecuación de una bobina:
> $$v_k=\sum_j L_{kj}\,i_j',$$
> donde $L_{kk}$ es la **autoinductancia** (término diagonal, por la propia corriente) y $L_{kj}=\pm M_{kj}$ son las **mutuas** (términos fuera de la diagonal, por las corrientes de las demás). El signo de cada mutua lo da la [[Regla de los Puntos]] del par $(k,j)$. Es, simplemente, la forma compacta de las ecuaciones acopladas: se escriben todas a la vez como un producto matriz–vector.

> [!proposicion] Simetría y carácter de la matriz
> La matriz $[L]$ es **simétrica**, $M_{jk}=M_{kj}$, porque el acoplamiento "se ve igual" desde cualquiera de las dos bobinas. Además, por ser la energía magnética $W=\tfrac12\,\mathbf{i}^{\mathsf T}[L]\,\mathbf{i}\ge 0$, la matriz es **definida positiva**. Encaja sin cambios en mallas y nodos: en corriente alterna basta reemplazar $[L]$ por $j\omega[L]$ ([[Acoplamiento Magnetico Fasorial]]).

> [!proposicion] Cuántas mutuas hay
> En $n$ bobinas, el número de inductancias mutuas **distintas** es
> $$\binom{n}{2}=\frac{n(n-1)}{2}.$$
> Cada par puede acoplarse o no: los pares que **no** se acoplan tienen $M=0$, es decir, **ceros** en la posición correspondiente de $[L]$. Para $n=3$ hay $3$ mutuas ($M_{12}$, $M_{13}$, $M_{23}$); para $n=4$, ya $6$.

> [!warning]
> Cada $M_{jk}$ lleva su **propio** signo según los puntos de **ese** par: no asumir que todos los términos mutuos comparten signo. Y la matriz $[L]$ es **simétrica** siempre, $M_{jk}=M_{kj}$, de modo que el signo de la posición $(j,k)$ es el mismo que el de la posición $(k,j)$.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Ecuación matricial | $\mathbf{v}=[L]\,\mathbf{i}'$ |
> | Fila $k$ | $v_k=\sum_j L_{kj}\,i_j'$ |
> | Diagonal | autoinductancias $L_{kk}$ |
> | Fuera de la diagonal | mutuas $\pm M_{jk}$ (signo por puntos) |
> | Simetría | $M_{jk}=M_{kj}$ |
> | N.º de mutuas | $n(n-1)/2$ |
> | Régimen sinusoidal | $[L]\to j\omega[L]$ |

> [!corolario]
> El acoplamiento múltiple no añade física nueva: es la [[Inductancia Mutua]] aplicada a cada par y reunida en una sola matriz $[L]$, simétrica y definida positiva. Con ella, un sistema de $n$ bobinas acopladas se trata como un único bloque que entra directamente en el [[Analisis de Mallas| análisis de mallas]].

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Base: [[Inductancia Mutua]]. Signos: [[Regla de los Puntos]]. Aplicación: [[Analisis de Mallas]]. Contexto: [[6 Acoplamiento Magnetico/index| Inducción magnética]].
