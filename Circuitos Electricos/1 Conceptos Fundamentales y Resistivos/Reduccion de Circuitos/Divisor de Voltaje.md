---
title: Divisor de Voltaje
order: 2
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - reduccion
draft: false
aliases:
  - divisor de tensión
  - divisor de voltaje
  - regla del divisor de tensión
  - voltage divider
  - voltage divider rule
---

# Divisor de Voltaje $v_k=v\,\dfrac{R_k}{\sum_j R_j}$

> [!definicion]
> En un conjunto de resistencias en **serie**, la tensión total $v$ aplicada se **reparte** entre ellas en **proporción directa a su resistencia**:
> $$v_k=v\,\frac{R_k}{\displaystyle\sum_j R_j}.$$
> La resistencia más grande se lleva la mayor parte de la tensión. Es la regla que evita recalcular la corriente cada vez que se quiere una caída concreta en una rama serie.

---

> [!info]
> Segunda nota de [[Reduccion de Circuitos/index| Reducción de circuitos]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es consecuencia directa de las [[Resistencias en Serie y Paralelo| resistencias en serie]], deducida con [[Ley de Voltajes LKV| LKV]] y la ley de Ohm. Su dual para resistencias en paralelo es el [[Divisor de Corriente]].

---

## Ejemplo

> [!ejemplo] Repartir $12\ \text{V}$ entre dos resistencias en serie
> Una fuente $v=12\ \text{V}$ alimenta a $R_1=8\ \Omega$ en serie con $R_2=4\ \Omega$. Queremos la tensión $v_2$ en bornes de $R_2$ **sin** calcular la corriente.
>
> ![[divisor_tension.svg|320]]
> Divisor de tensión: $v_2=v\,\dfrac{R_2}{R_1+R_2}$.
>
> **Paso 1 — Aplicar la regla.** Con dos resistencias en serie:
> $$v_2=v\,\frac{R_2}{R_1+R_2}=12\ \text{V}\times\frac{4}{8+4}=12\times\frac{4}{12}=4\ \text{V}.$$
>
> **Paso 2 — Comprobar.** La caída en $R_1$ debe completar la fuente:
> $$v_1=v\,\frac{R_1}{R_1+R_2}=12\times\frac{8}{12}=8\ \text{V},\qquad v_1+v_2=8+4=12\ \text{V}=v.\;\checkmark$$
>
> La resistencia doble ($R_1=8\ \Omega$) se lleva el doble de tensión ($8\ \text{V}$): el reparto es proporcional a la resistencia, tal como anuncia la fórmula.

---

## En qué consiste

> [!teoria] La corriente es común; la tensión, no
> En una rama serie todas las resistencias llevan la **misma** corriente $i$, pero **distinta** tensión, porque $v_k=R_k\,i$ y cada $R_k$ es diferente. El divisor de tensión no es más que escribir esa corriente común en términos de la tensión total y sustituirla: así se obtiene cada $v_k$ directamente desde $v$, sin pasar por $i$.

> [!teorema] Regla del divisor de tensión
> Para $n$ resistencias en serie sometidas a una tensión total $v$, la caída en la resistencia $R_k$ es
> $$v_k=v\,\frac{R_k}{R_1+R_2+\dots+R_n}=v\,\frac{R_k}{\displaystyle\sum_j R_j}.$$

> [!demostracion]
> **Paso 1 — Corriente de la rama.** Las resistencias en serie equivalen a $R_{eq}=\sum_j R_j$, de modo que la corriente común es
> $$i=\frac{v}{R_{eq}}=\frac{v}{\sum_j R_j}.$$
>
> **Paso 2 — Ley de Ohm en la rama $k$.** La tensión en $R_k$ es $v_k=R_k\,i$.
>
> **Paso 3 — Sustituir.** Reemplazando $i$:
> $$v_k=R_k\cdot\frac{v}{\sum_j R_j}=v\,\frac{R_k}{\sum_j R_j}.\qquad\blacksquare$$

> [!proposicion] El caso de dos resistencias
> Con solo $R_1$ y $R_2$ en serie la regla se escribe como una fracción simple:
> $$v_2=v\,\frac{R_2}{R_1+R_2},\qquad v_1=v\,\frac{R_1}{R_1+R_2}.$$
> Las dos fracciones suman $1$, así que $v_1+v_2=v$ siempre. Es la forma que más se usa al diseñar referencias de tensión.

> [!warning]
> La fórmula vale para las resistencias **realmente en serie y sin carga** en el punto de toma. Si se conecta una carga $R_L$ en paralelo con $R_2$ (es decir, se **extrae corriente** de la salida), el reparto cambia: hay que sustituir $R_2$ por $R_2\parallel R_L$, lo que **reduce** la tensión de salida respecto al valor en vacío. Un divisor solo entrega exactamente $v_2$ mientras su salida esté en circuito abierto.

---

## Resumen

> [!resumen] Lo esencial
> | Magnitud | Expresión | Comentario |
> |:---|:---|:---|
> | Caída general | $v_k=v\,\dfrac{R_k}{\sum_j R_j}$ | proporcional a $R_k$ |
> | Dos resistencias | $v_2=v\,\dfrac{R_2}{R_1+R_2}$ | fracciones suman $1$ |
> | Con carga $R_L$ | usar $R_2\parallel R_L$ | la salida baja |

> [!corolario]
> El divisor de tensión es la lectura "en serie" de la equivalencia: una vez que sabes que el grupo es serie y conoces $R_{eq}$, cada caída sale por simple proporción. Su dual exacto, para grupos en paralelo, es el [[Divisor de Corriente]], donde lo que se reparte es la corriente y el peso lo lleva la conductancia.

> [!referencia]
> Fraile Mora, cap. 1, §1.10. Ver [[Resistencias en Serie y Paralelo]] y el dual [[Divisor de Corriente]].
