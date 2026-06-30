---
title: Teorema de Millman
order: 5
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - millman
draft: false
aliases:
  - teorema de Millman
  - Millman
  - Millman's theorem
---

# Teorema de Millman

> [!definicion]
> Cuando varias ramas, cada una formada por una **fuente de tensión $V_k$ en serie con una resistencia $R_k$**, se conectan **en paralelo** entre dos nodos $A$ y $B$, la tensión entre ellos es
> $$V_{AB}=\frac{\sum_k V_k/R_k}{\sum_k 1/R_k}=\frac{\sum_k V_k\,G_k}{\sum_k G_k},$$
> donde $G_k=1/R_k$ es la **conductancia** de cada rama. Es un caso particular muy cómodo del [[Analisis de Nodos| análisis de nodos]]: resuelve la red con **una sola ecuación de nodo**.

> [!info]
> Atajo de [[Teoremas/index| Teoremas de circuitos]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]); equivale a aplicar la **LKC** en el nodo $A$ tomando $B$ como referencia. Se apoya en la [[Transformacion de Fuentes| transformación de fuentes]] para llevar cada rama a la forma $V_k$–$R_k$. Fraile Mora, cap. 1, §1.16.

---

## Ejemplo

> [!ejemplo]
> **Tensión entre $A$ y $B$ por Millman.**
>
> Dos ramas en paralelo entre $A$ y $B$: la rama 1 con $V_1=10\ \text{V}$ y $R_1=2\ \Omega$; la rama 2 con $V_2=4\ \text{V}$ y $R_2=4\ \Omega$. Hallar $V_{AB}$.
>
> ![[millman.svg|470]]
>
> *Ramas (fuente + resistencia) en paralelo entre $A$ y $B$; Millman da $V_{AB}$ de un cálculo.*
>
> > [!solucion]
> > Se aplica directamente la fórmula con $G_1=1/R_1=0{,}5\ \text{S}$ y $G_2=1/R_2=0{,}25\ \text{S}$:
> > $$V_{AB}=\frac{V_1/R_1+V_2/R_2}{1/R_1+1/R_2}=\frac{10/2+4/4}{1/2+1/4}=\frac{5+1}{0{,}75}=8\ \text{V}.$$
> > De aquí, las corrientes de rama salen por Ohm: $i_1=(V_1-V_{AB})/R_1=(10-8)/2=1\ \text{A}$ y $i_2=(V_2-V_{AB})/R_2=(4-8)/4=-1\ \text{A}$ (la rama 2 absorbe corriente). Su suma es cero, como exige la LKC en $A$.
> > $$\boxed{V_{AB}=8\ \text{V}}$$

---

## En qué consiste

> [!teoria]
> Millman dice que $V_{AB}$ es el **promedio ponderado** de las tensiones de rama $V_k$, donde el peso de cada una es su conductancia $G_k=1/R_k$. Las ramas de baja resistencia (gran $G_k$) "tiran" más fuerte del nodo hacia su propia $V_k$; las de alta resistencia apenas influyen. Dos casos límite:
> - Una rama con **solo resistencia** (sin fuente) entra como $V_k=0$: arrastra $V_{AB}$ hacia cero con peso $G_k$, pero no aporta numerador.
> - Una **fuente de corriente** $I_k$ inyectada en $A$ se suma tal cual al numerador: $+I_k$ (es ya una corriente, no hay que dividir por nada).

> [!teorema]
> Para $N$ ramas $V_k$–$R_k$ en paralelo entre $A$ y $B$, la tensión del nodo $A$ respecto de $B$ es
> $$V_{AB}=\frac{\displaystyle\sum_{k=1}^{N} V_k/R_k}{\displaystyle\sum_{k=1}^{N} 1/R_k}.$$

> [!demostracion]
> Se toma $B$ como nodo de referencia ($V_B=0$) y se aplica la LKC en el nodo $A$.
>
> **Paso 1 — corriente de cada rama hacia $A$.** Por la rama $k$, de su fuente $V_k$ a través de $R_k$, la corriente que entra al nodo $A$ es, por la ley de Ohm,
> $$i_k=\frac{V_k-V_{AB}}{R_k}.$$
>
> **Paso 2 — LKC en $A$.** La suma de todas las corrientes que entran al nodo es cero:
> $$\sum_k i_k=\sum_k \frac{V_k-V_{AB}}{R_k}=0.$$
>
> **Paso 3 — despejar $V_{AB}$.** Se separa la suma y se saca $V_{AB}$ de su término:
> $$\sum_k \frac{V_k}{R_k}-V_{AB}\sum_k \frac{1}{R_k}=0
> \quad\Longrightarrow\quad
> V_{AB}\sum_k \frac{1}{R_k}=\sum_k \frac{V_k}{R_k},$$
> de donde sigue la fórmula. $\blacksquare$

> [!algoritmo]
> 1. Llevar **cada rama** a la forma "fuente de tensión $V_k$ en serie con $R_k$"; si viene como fuente de corriente, aplicar [[Transformacion de Fuentes| transformación de fuentes]].
> 2. Aplicar la fórmula $V_{AB}=\dfrac{\sum_k V_k/R_k}{\sum_k 1/R_k}$.
> 3. Con $V_{AB}$ ya conocido, obtener las corrientes de rama por Ohm: $i_k=(V_k-V_{AB})/R_k$.

> [!warning]
> El teorema **solo** aplica a ramas estrictamente **en paralelo** entre los **mismos** dos nodos $A$ y $B$. Si una rama no tiene resistencia ($R_k=0$, fuente de tensión ideal), su conductancia $G_k\to\infty$ domina la suma y **fija** $V_{AB}=V_k$ directamente: la fórmula no debe usarse, basta leer esa rama.

---

## Resumen

> [!resumen]
> | Magnitud | Expresión | En el ejemplo |
> |---|---|---|
> | Tensión del nodo | $V_{AB}=\dfrac{\sum_k V_k G_k}{\sum_k G_k}$ | $8\ \text{V}$ |
> | Conductancia de rama | $G_k=1/R_k$ | $0{,}5$ y $0{,}25\ \text{S}$ |
> | Corriente de rama | $i_k=(V_k-V_{AB})/R_k$ | $1\ \text{A}$ y $-1\ \text{A}$ |
> | Validez | ramas $V_k$–$R_k$ **en paralelo** entre $A$ y $B$ | — |

> [!corolario]
> Con dos ramas ($N=2$) la fórmula se reduce a $V_{AB}=\dfrac{V_1 G_1+V_2 G_2}{G_1+G_2}$, el promedio ponderado de dos tensiones. Si además $R_1=R_2$, queda la media aritmética $V_{AB}=(V_1+V_2)/2$.

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 1, §1.16. Relacionadas: [[Analisis de Nodos]], [[Transformacion de Fuentes]], [[Teorema de Thevenin]], [[Teoremas/index]].
