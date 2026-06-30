---
title: Ecuaciones Independientes de Kirchhoff
order: 3
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - kirchhoff
  - topologia
draft: false
aliases:
  - Ecuaciones Independientes
  - Número de ecuaciones de Kirchhoff
  - Árbol y enlaces
  - Independent Kirchhoff equations
---

# Ecuaciones Independientes de Kirchhoff

> [!definicion]
> No todas las ecuaciones de Kirchhoff que se pueden escribir son **independientes**. Para un circuito de $n$ nodos y $b$ ramas:
> $$\underbrace{n-1}_{\text{LKC independientes}} \;+\; \underbrace{b-n+1}_{\text{LKV independientes}} \;=\; b.$$
> Hay exactamente $n-1$ ecuaciones de [[Ley de Corrientes LKC]] independientes (una por cada nodo salvo uno) y $b-n+1$ ecuaciones de [[Ley de Voltajes LKV]] independientes (una por cada malla básica). En total, $b$ ecuaciones: justo las que faltan para cerrar el sistema con las $b$ relaciones de los elementos.

> [!info]
> Tercera nota de la sección [[Leyes de Kirchhoff/index| Leyes de Kirchhoff]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Responde *cuántas* ecuaciones de [[Ley de Corrientes LKC]] y [[Ley de Voltajes LKV]] hay que escribir y *cuáles* elegir. El vocabulario (nodo, rama, malla, lazo, árbol) se desarrolla en [[Definiciones Topologicas]]. Fraile Mora, cap. 1, §1.9.

---

## Ejemplo

> [!ejemplo]
> **Circuito de $b = 6$ ramas y $n = 4$ nodos: ¿cuántas ecuaciones independientes?**
>
> **Paso 1 — LKC independientes.** Una por nodo, salvo uno:
> $$n - 1 = 4 - 1 = 3 \text{ ecuaciones LKC}.$$
> La ecuación del cuarto nodo es combinación lineal de las otras tres y no aporta información nueva.
>
> **Paso 2 — LKV independientes (mallas básicas).**
> $$b - n + 1 = 6 - 4 + 1 = 3 \text{ ecuaciones LKV}.$$
>
> **Paso 3 — Total y cierre del sistema.**
> $$3 + 3 = 6 = b.$$
> El circuito tiene $2b = 12$ incógnitas (una $v$ y una $i$ por rama). Las $b = 6$ relaciones de los elementos ($v = Ri$ en cada resistencia, valores de fuentes) aportan otras $6$ ecuaciones. En total $6 + 6 = 12$ ecuaciones para $12$ incógnitas:
>
> > [!solucion]
> > $3$ ecuaciones LKC $+$ $3$ ecuaciones LKV $=6$ ecuaciones de Kirchhoff independientes, que junto a las $6$ relaciones de elemento determinan por completo el circuito.

---

## En qué consiste

> [!teoria] Por qué sobra una LKC y por qué hay $b-n+1$ mallas
> **La LKC redundante.** Si se escribe $\sum_k i_k = 0$ en *todos* los $n$ nodos y se suman todas las ecuaciones, cada corriente de rama aparece dos veces —entrante en un nodo, saliente en el otro— y se cancela. La suma total es $0=0$: una identidad. Por tanto, la ecuación de cualquier nodo es combinación de las demás, y solo $n-1$ son independientes.
>
> **El conteo de mallas.** El número de lazos independientes de un grafo conexo es su **número de circuitos** (o *nulidad*), $b - n + 1$. Cada lazo independiente añade una rama de cierre a un esqueleto sin lazos; ese esqueleto es el **árbol**.

> [!definicion] Árbol, ramas de árbol y enlaces
> Dado el grafo del circuito ($n$ nodos, $b$ ramas):
> - **Árbol:** subconjunto de ramas que conecta todos los nodos **sin formar ningún lazo**. Tiene exactamente $n-1$ ramas, llamadas **ramas de árbol** (*twigs*).
> - **Coárbol (enlaces):** las $b-(n-1) = b-n+1$ ramas restantes, llamadas **enlaces** (*links*) o cuerdas. Forman el **coárbol**.
>
> Cada **enlace**, al añadirse al árbol, cierra **exactamente un lazo independiente** (lazo fundamental). De ahí salen las $b-n+1$ ecuaciones LKV independientes.

> [!algoritmo] Elegir un conjunto independiente de ecuaciones
> **Paso 1 — Contar.** Determinar $n$ (nodos) y $b$ (ramas). Calcular $n-1$ y $b-n+1$.
>
> **Paso 2 — Nodo de referencia.** Elegir un nodo como **referencia** (masa) y escribir LKC en los otros $n-1$ nodos. Esas $n-1$ ecuaciones son independientes por construcción.
>
> **Paso 3 — Elegir un árbol.** Seleccionar $n-1$ ramas que conecten todos los nodos sin lazos. Las $b-n+1$ ramas sobrantes son los **enlaces**.
>
> **Paso 4 — Lazos fundamentales.** Por cada enlace, formar el lazo único que cierra con ramas del árbol y escribir su LKV. Esas $b-n+1$ ecuaciones son independientes.
>
> **Paso 5 — Cerrar.** Añadir las $b$ relaciones de elemento. El sistema de $2b$ ecuaciones para $2b$ incógnitas queda determinado.

---

> [!proposicion] Relación con los métodos sistemáticos
> Los dos métodos del capítulo 2 son la implementación directa de este conteo:
> - El [[Analisis de Nodos]] usa las $n-1$ ecuaciones LKC, tomando los potenciales de nodo como incógnitas.
> - El [[Analisis de Mallas]] usa las $b-n+1$ ecuaciones LKV, tomando las corrientes de malla como incógnitas.
>
> Conviene el de **menor número de ecuaciones**: nodos si $n-1 < b-n+1$, mallas en caso contrario.

> [!warning]
> Las fórmulas $n-1$ y $b-n+1$ suponen un **grafo conexo**. Si el circuito tiene $s$ partes separadas (subgrafos inconexos), el número de mallas independientes es $b - n + s$ y el de LKC independientes es $n - s$. Para un circuito de una sola pieza, $s=1$ y se recuperan las fórmulas usuales.

---

## Resumen

> [!resumen]
> | Magnitud | Fórmula |
> |:---|:---|
> | LKC independientes | $n - 1$ |
> | LKV independientes (mallas básicas) | $b - n + 1$ |
> | Total ecuaciones de Kirchhoff | $b$ |
> | Ramas de árbol (*twigs*) | $n - 1$ |
> | Enlaces / cuerdas (*links*) | $b - n + 1$ |
> | Incógnitas del circuito | $2b$ ($v$ e $i$ por rama) |
> | Caso inconexo ($s$ partes) | LKC $n-s$, mallas $b-n+s$ |

> [!corolario]
> El árbol separa las ramas en dos grupos que reparten el trabajo: las $n-1$ ramas de árbol fijan los $n-1$ potenciales independientes (LKC), y los $b-n+1$ enlaces fijan los $b-n+1$ lazos independientes (LKV). Sumadas, dan las $b$ ecuaciones que, con las relaciones de elemento, resuelven cualquier red.

> [!referencia]
> Fraile Mora, cap. 1, §1.9 (independencia de las ecuaciones). Leyes: [[Ley de Corrientes LKC]], [[Ley de Voltajes LKV]]. Vocabulario de grafo: [[Definiciones Topologicas]].
