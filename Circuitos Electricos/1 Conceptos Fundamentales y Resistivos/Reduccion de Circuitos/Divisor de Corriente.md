---
title: Divisor de Corriente
order: 3
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - reduccion
draft: false
aliases:
  - divisor de corriente
  - regla del divisor de corriente
  - current divider
  - current divider rule
---

# Divisor de Corriente $i_k=i\,\dfrac{G_k}{\sum_j G_j}$

> [!definicion]
> En un conjunto de resistencias en **paralelo**, la corriente total $i$ que entra se **reparte** entre las ramas en **proporción directa a su conductancia**:
> $$i_k=i\,\frac{G_k}{\displaystyle\sum_j G_j},\qquad G_k=\frac{1}{R_k}.$$
> La rama de **menor resistencia** (mayor conductancia) se lleva la **mayor** corriente. Es la regla dual del [[Divisor de Voltaje| divisor de tensión]] y evita recalcular la tensión común cada vez.

---

> [!info]
> Tercera nota de [[Reduccion de Circuitos/index| Reducción de circuitos]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es consecuencia directa de las [[Resistencias en Serie y Paralelo| resistencias en paralelo]], deducida con [[Ley de Corrientes LKC| LKC]] y la ley de Ohm. Su dual para resistencias en serie es el [[Divisor de Voltaje]].

---

## Ejemplo

> [!ejemplo] Repartir $9\ \text{A}$ entre dos resistencias en paralelo
> Una corriente $i=9\ \text{A}$ entra en el paralelo de $R_1=2\ \Omega$ y $R_2=4\ \Omega$. Queremos $i_1$ e $i_2$ **sin** calcular la tensión común.
>
> ![[divisor_corriente.svg|340]]
> Divisor de corriente: $i_1=i\,\dfrac{R_2}{R_1+R_2}$.
>
> **Paso 1 — Usar la forma de dos ramas.** Para dos resistencias en paralelo, la corriente de una rama es proporcional a la resistencia de **la otra**:
> $$i_1=i\,\frac{R_2}{R_1+R_2}=9\ \text{A}\times\frac{4}{2+4}=9\times\frac{4}{6}=6\ \text{A}.$$
>
> **Paso 2 — La otra rama.** Por simetría (o por LKC):
> $$i_2=i\,\frac{R_1}{R_1+R_2}=9\times\frac{2}{6}=3\ \text{A},\qquad i_1+i_2=6+3=9\ \text{A}=i.\;\checkmark$$
>
> La rama de **menor** resistencia ($R_1=2\ \Omega$) se lleva la **mayor** corriente ($6\ \text{A}$): el doble que la rama de $4\ \Omega$, como anuncia la regla.

---

## En qué consiste

> [!teoria] La tensión es común; la corriente, no
> En un grupo en paralelo todas las ramas comparten la **misma** tensión $v$, pero distinta corriente, porque $i_k=G_k\,v$ y cada conductancia es distinta. El divisor de corriente expresa esa tensión común en función de la corriente total y la sustituye: así se obtiene cada $i_k$ directamente desde $i$, sin pasar por $v$.

> [!teorema] Regla del divisor de corriente
> Para $n$ resistencias en paralelo recorridas por una corriente total $i$, la corriente de la rama $R_k$ es
> $$i_k=i\,\frac{G_k}{G_1+G_2+\dots+G_n}=i\,\frac{1/R_k}{\displaystyle\sum_j 1/R_j}.$$

> [!demostracion]
> **Paso 1 — Tensión común.** Las ramas en paralelo equivalen a $G_{eq}=\sum_j G_j$, así que la tensión común es
> $$v=\frac{i}{G_{eq}}=\frac{i}{\sum_j G_j}.$$
>
> **Paso 2 — Ley de Ohm en la rama $k$.** La corriente por $R_k$ es $i_k=G_k\,v$.
>
> **Paso 3 — Sustituir.** Reemplazando $v$:
> $$i_k=G_k\cdot\frac{i}{\sum_j G_j}=i\,\frac{G_k}{\sum_j G_j}.\qquad\blacksquare$$

> [!proposicion] El caso de dos resistencias
> Con solo dos ramas conviene escribir todo en resistencias. Como $G_1=1/R_1$ y $G_2=1/R_2$, al simplificar las fracciones aparece la resistencia de **la rama contraria** en el numerador:
> $$i_1=i\,\frac{R_2}{R_1+R_2},\qquad i_2=i\,\frac{R_1}{R_1+R_2}.$$
> **Cuidado con el cruce:** la corriente de $R_1$ lleva $R_2$ arriba. Esta inversión es justo lo contrario del divisor de tensión, donde la rama propia va en el numerador.

> [!warning]
> El cruce de subíndices solo es válido para **dos** ramas. Con tres o más resistencias en paralelo no hay atajo: hay que volver a la forma en **conductancias**, $i_k=i\,G_k/\sum_j G_j$. Aplicar la fórmula de "la resistencia contraria" a tres ramas da un resultado incorrecto.

---

## Resumen

> [!resumen] Lo esencial
> | Magnitud | Expresión | Comentario |
> |:---|:---|:---|
> | Corriente general | $i_k=i\,\dfrac{G_k}{\sum_j G_j}$ | proporcional a $G_k$ |
> | Dos resistencias | $i_1=i\,\dfrac{R_2}{R_1+R_2}$ | la resistencia **contraria** arriba |
> | Tres o más | usar conductancias | no hay atajo en $R$ |

> [!corolario]
> Divisor de tensión y divisor de corriente son **duales**: el de tensión reparte $v$ entre resistencias en serie con peso $R_k$; el de corriente reparte $i$ entre ramas en paralelo con peso $G_k$. Cambiar $v\leftrightarrow i$, serie$\leftrightarrow$paralelo y $R\leftrightarrow G$ convierte una regla en la otra. Recordar esa simetría basta para no equivocar nunca el numerador.

> [!referencia]
> Fraile Mora, cap. 1, §1.10. Ver [[Resistencias en Serie y Paralelo]] y el dual [[Divisor de Voltaje]].
