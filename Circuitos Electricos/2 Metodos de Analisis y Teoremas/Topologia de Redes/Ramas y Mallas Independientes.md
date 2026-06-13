---
title: Ramas y Mallas Independientes
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - topologia
draft: false
aliases:
  - ramas y mallas independientes
  - ecuaciones independientes de circuitos
  - número de mallas
  - árbol y eslabones
---

# Ramas y Mallas Independientes $\;n-1\;$ y $\;b-n+1$

> [!definicion]
> En una red de $b$ ramas y $n$ nodos, el número de ecuaciones **independientes** de cada tipo lo fija
> el **árbol** del grafo: hay $n-1$ **ramas de árbol** —y por tanto $n-1$ ecuaciones de **nodo** (LKC)
> independientes— y $b-n+1$ **eslabones** —y por tanto $b-n+1$ ecuaciones de **malla** (LKV)
> independientes—. En total, $b$ ecuaciones, justo las que faltan para cerrar el sistema.

> [!info]
> El conteo central de la [[Topologia de Redes/index| topología]], en el
> [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Usa el vocabulario de
> [[Definiciones Topologicas]] y justifica por qué el [[Analisis de Nodos]] plantea $n-1$ ecuaciones y
> el [[Analisis de Mallas]] plantea $b-n+1$. Fraile Mora, cap. 1, §1.7.2.

---

## Ejemplo

> [!ejemplo]
> **Contar sobre el grafo: árbol y eslabones.**
>
> El grafo tiene $n=4$ nodos y $b=6$ ramas. Elegimos como **árbol** las tres ramas que van al nodo
> central $O$ —$OA$, $OB$, $OC$— dibujadas con trazo grueso: conectan los cuatro nodos y **no forman
> ningún lazo**. Las tres ramas restantes —$AB$, $BC$, $CA$— son los **eslabones** (a trazos):
>
> ![[arbol_eslabones.svg|600]]
>
> *Árbol (grueso): $n-1 = 3$ ramas. Eslabones (a trazos): $b-n+1 = 3$. Cada eslabón cierra un lazo
> distinto con el árbol.*
>
> **Conteo.**
> $$\text{ramas de árbol}=n-1=4-1=3,\qquad \text{eslabones}=b-n+1=6-4+1=3.$$
>
> Hay entonces **3 ecuaciones de nodo** (LKC) y **3 ecuaciones de malla** (LKV) independientes:
> $3+3=6=b$, exactamente las ecuaciones que aporta Kirchhoff para las $6$ corrientes de rama.

---

## En qué consiste

> [!teoria] Por qué el árbol cuenta las ecuaciones
> Un **árbol** conecta los $n$ nodos sin cerrar lazos. Construirlo es ir uniendo nodos: el primer nodo
> no necesita rama; cada rama nueva del árbol incorpora **exactamente un nodo nuevo**. Para enganchar
> los $n$ nodos hacen falta, pues, $n-1$ ramas. Cada una de esas ramas de árbol define un **corte** que
> separa el grafo en dos, y la LKC sobre ese corte es una ecuación de nodo independiente: de ahí las
> $n-1$ ecuaciones de nodo.
>
> Los **eslabones** son las ramas que sobran: $b-(n-1)=b-n+1$. Si se añade un eslabón al árbol, como el
> árbol ya conectaba todo, ese eslabón **cierra un lazo** (y solo uno). Cada lazo así formado contiene
> un eslabón que no está en ningún otro, de modo que las ecuaciones de malla correspondientes son
> **independientes**: de ahí las $b-n+1$ ecuaciones de malla.

> [!teorema] Conteo topológico de ecuaciones
> En un grafo **conexo** de $b$ ramas y $n$ nodos:
> $$\text{ramas de árbol}=n-1,\qquad \text{eslabones}=b-n+1,$$
> y estos números son, respectivamente, el de ecuaciones de **nodo** (LKC) y de **malla** (LKV)
> linealmente **independientes**.

> [!demostracion]
> **Paso 1 — Ramas de árbol $=n-1$ (inducción).** Un árbol con un solo nodo tiene $0$ ramas: cumple
> $n-1=0$. Supóngase cierto para $k$ nodos ($k-1$ ramas). Para conectar un nodo más sin formar lazos se
> añade **una** rama (si se añadieran dos, se cerraría un lazo): el árbol pasa a $k+1$ nodos y
> $(k-1)+1=k$ ramas, que es $(k+1)-1$. Por inducción, un árbol de $n$ nodos tiene $n-1$ ramas.
>
> **Paso 2 — Eslabones $=b-n+1$.** Los eslabones son todas las ramas menos las de árbol:
> $b-(n-1)=b-n+1$.
>
> **Paso 3 — Independencia.** Cada rama de árbol define un corte que la separa del resto; la LKC sobre
> ese corte involucra a esa rama de árbol y no a las demás de árbol, así que las $n-1$ ecuaciones son
> independientes. Dualmente, cada eslabón cierra un lazo que contiene **solo a ese** eslabón entre los
> de su clase; las $b-n+1$ ecuaciones de malla son por ello independientes. $\blacksquare$

> [!algoritmo] Elegir las ecuaciones independientes
> **Paso 1 — Contar.** Determinar $n$ (nodos) y $b$ (ramas) del circuito.
>
> **Paso 2 — Nodos.** Elegir un nodo como **referencia** (masa) y plantear LKC en los otros $n-1$:
> esas son las ecuaciones del [[Analisis de Nodos]].
>
> **Paso 3 — Mallas.** En un circuito **plano**, las $b-n+1$ **ventanas** (mallas) son siempre un
> conjunto independiente: plantear LKV en cada una es el [[Analisis de Mallas]].

> [!proposicion] ¿Mallas o nodos?
> Conviene el método que dé **menos** ecuaciones: nodos si $n-1 < b-n+1$, mallas en caso contrario. Por
> eso, antes de calcular, el conteo topológico también **elige el método más corto**.

> [!warning]
> El conteo $n-1$ y $b-n+1$ vale para un grafo **conexo**. Si la red tiene $s$ partes separadas, las
> ecuaciones de nodo son $n-s$. Además, recuérdese ([[Definiciones Topologicas]]) que solo los **nodos
> principales** cuentan: los secundarios (conexiones en serie) no añaden ecuación.

## Resumen

> [!resumen]
> | Cantidad | Fórmula | Significa |
> |:---|:---|:---|
> | Ramas de árbol | $n-1$ | ecuaciones de **nodo** (LKC) independientes |
> | Eslabones | $b-n+1$ | ecuaciones de **malla** (LKV) independientes |
> | Total Kirchhoff | $(n-1)+(b-n+1)=b$ | cierran el sistema con las $b$ de los elementos |
> | Mallas (red plana) | $b-n+1$ | número de **ventanas** |

> [!corolario]
> Antes de escribir una sola ecuación, la topología ya dice **cuántas** habrá ($n-1$ de nodo, $b-n+1$
> de malla) y **cuál método conviene**. Esa es la razón de empezar el análisis sistemático por aquí.

> [!referencia]
> Fraile Mora, cap. 1, §1.7.2. Aplicación directa: [[Analisis de Nodos]] y [[Analisis de Mallas]].
