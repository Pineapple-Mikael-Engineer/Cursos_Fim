---
title: Análisis de Nodos
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - nodos
draft: false
aliases:
  - análisis de nodos
  - método de nodos
  - tensiones de nodo
  - nodal analysis
---

# Análisis de Nodos

> [!definicion]
> El **análisis de nodos** elige un nodo de **referencia** (masa) y toma como incógnitas las
> **tensiones de los demás nodos** respecto a él; luego plantea la **LKC** en cada uno. Como toda
> tensión de rama es una **diferencia** de tensiones de nodo, la **LKV queda satisfecha de antemano**;
> solo hay que imponer la LKC. Resultan $n-1$ ecuaciones, el mínimo. Es el **dual** del
> [[Analisis de Mallas| análisis de mallas]].

> [!info]
> El otro método central de [[Metodos de Analisis/index| Métodos de análisis]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]). Es la [[Ley de Corrientes LKC| LKC]] aplicada de forma
> sistemática. Cuando una fuente de tensión une dos nodos se recurre al [[Nodos con Fuentes de Voltaje| supernodo]]. Fraile Mora, cap. 1, §1.13.

---

## Ejemplo

> [!ejemplo]
> **Dos nodos con fuentes de corriente.**
>
> Hallar las tensiones de los nodos $1$ y $2$. Datos: fuentes de corriente $I_{s1}=5\ \text{A}$ (entra
> al nodo $1$) e $I_{s2}=1\ \text{A}$ (entra al nodo $2$); resistencias $R_1=1\ \Omega$ (nodo $1$ a
> masa), $R_2=2\ \Omega$ (entre los nodos $1$ y $2$) y $R_3=1\ \Omega$ (nodo $2$ a masa).
>
> ![[analisis_nodos.svg|470]]
>
> *Nodo de referencia (masa) abajo. Incógnitas: las tensiones $V_1$ y $V_2$. Cada rama resistiva lleva
> una corriente $V/R$ o $(V_1-V_2)/R$.*
>
> **Paso 1 — Referencia e incógnitas.** El nodo inferior es la masa ($V=0$). Incógnitas: $V_1$, $V_2$.
>
> **Paso 2 — LKC en el nodo $1$** (lo que entra por la fuente sale por las resistencias):
> $$I_{s1} = \frac{V_1}{R_1} + \frac{V_1-V_2}{R_2} \;\Longrightarrow\; 5 = V_1 + \frac{V_1-V_2}{2}.$$
>
> **Paso 3 — LKC en el nodo $2$.**
> $$I_{s2} = \frac{V_2}{R_3} + \frac{V_2-V_1}{R_2} \;\Longrightarrow\; 1 = V_2 + \frac{V_2-V_1}{2}.$$
>
> **Paso 4 — Resolver.** Multiplicando por $2$ y ordenando, $3V_1 - V_2 = 10$ y $-V_1 + 3V_2 = 2$:
> $$V_1 = 4\ \text{V}, \qquad V_2 = 2\ \text{V}.$$
>
> > [!solucion]
> > $V_1 = 4\ \text{V}$, $V_2 = 2\ \text{V}$. De ahí, cualquier corriente de rama: por $R_2$,
> > $i_{R_2}=(V_1-V_2)/R_2 = (4-2)/2 = 1\ \text{A}$; por $R_1$, $V_1/R_1 = 4\ \text{A}$; por $R_3$,
> > $V_2/R_3 = 2\ \text{A}$.

---

## En qué consiste

> [!teoria] Por qué la LKV se cumple sola
> Si a cada nodo le asignamos un potencial $V_k$ respecto a la masa, la tensión de la rama entre los
> nodos $j$ y $k$ es, por definición, $V_j - V_k$. Al recorrer cualquier lazo, esas diferencias se
> **cancelan telescópicamente** y su suma es cero: la LKV se cumple **sola**. Solo queda imponer la
> LKC en cada nodo, escribiendo cada corriente de rama como $(\,V_j - V_k\,)/R$ con la ley de Ohm.

> [!algoritmo] Método de nodos (fuentes de corriente)
> **Paso 1 — Elegir la masa.** Un nodo de referencia, $V=0$ (conviene el de más ramas). Quedan $n-1$
> incógnitas.
>
> **Paso 2 — LKC en cada nodo.** Igualar la corriente **inyectada** por las fuentes a la que **sale**
> por las resistencias. La corriente que sale del nodo $k$ por una resistencia a otro nodo $j$ es
> $(V_k - V_j)/R$; a masa, $V_k/R$.
>
> **Paso 3 — Resolver** el sistema lineal para las tensiones de nodo.
>
> **Paso 4 — Magnitudes de rama.** Cualquier corriente o tensión se obtiene de las $V_k$ con la ley de
> Ohm.

> [!proposicion] La matriz de conductancias (atajo por inspección)
> El sistema $G\,\mathbf{V} = \mathbf{i}_s$ se escribe **por inspección**, dual al de mallas:
> $$\begin{cases} G_{kk} = \text{suma de conductancias conectadas al nodo } k \\ G_{jk} = -\,(\text{conductancia entre los nodos } j \text{ y } k) \\ i_{s,k} = \text{corriente neta inyectada por fuentes en el nodo } k \end{cases}$$
> $G$ es **simétrica** sin fuentes dependientes. En el ejemplo (con $G=1/R$):
> $G_{11}=\tfrac{1}{R_1}+\tfrac{1}{R_2}=1{,}5$, $G_{22}=\tfrac{1}{R_3}+\tfrac{1}{R_2}=1{,}5$,
> $G_{12}=G_{21}=-\tfrac{1}{R_2}=-0{,}5$.

> [!warning]
> El análisis de nodos en su forma directa supone **fuentes de corriente**. Una fuente de tensión
> entre dos nodos (sin resistencia en serie) impide escribir la LKC de cada uno por separado: hay que
> agruparlos en un [[Nodos con Fuentes de Voltaje| supernodo]]. Si está en serie con una resistencia,
> conviene primero una [[Transformacion de Fuentes| transformación de fuente]].

## Resumen

> [!resumen]
> | Aspecto | Nodos |
> |:---|:---|
> | Incógnita | tensión de nodo $V_k$ |
> | Ley impuesta | LKC ($\sum i = 0$ por nodo) |
> | Ley automática | LKV |
> | Nº de ecuaciones | $n-1$ |
> | Sistema | $G\,\mathbf{V}=\mathbf{i}_s$, $G$ simétrica |
> | Conductancia propia / mutua | $G_{kk}=\sum G_{\text{nodo}}$ / $G_{jk}=-G_{\text{entre } j,k}$ |

> [!corolario]
> Nodos y mallas resuelven el mismo circuito con el mismo esfuerzo conceptual, pero distinto número de
> ecuaciones. Contar $n-1$ frente a $b-n+1$ ([[Ramas y Mallas Independientes| topología]]) decide
> cuál conviene: aquí, con menos nodos que mallas, nodos sería el camino corto.

> [!referencia]
> Fraile Mora, cap. 1, §1.13. Dual: [[Analisis de Mallas]]. Caso especial:
> [[Nodos con Fuentes de Voltaje]]. Con fuentes dependientes: [[Ecuaciones de Restriccion]].
