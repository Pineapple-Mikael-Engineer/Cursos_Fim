---
title: Resistencias en Serie y Paralelo
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - reduccion
draft: false
aliases:
  - resistencias en serie
  - resistencias en paralelo
  - resistencia equivalente
  - asociación de resistencias
  - series resistors
  - parallel resistors
  - equivalent resistance
---

# Resistencias en Serie y Paralelo $R_{eq}$

> [!definicion]
> Dos resistencias están en **serie** si comparten un nudo por el que circula la **misma corriente**; entonces se suman: $R_{eq}=\sum_k R_k$. Están en **paralelo** si comparten **ambos** nudos y por tanto soportan la **misma tensión**; entonces se suman sus conductancias: $\dfrac{1}{R_{eq}}=\sum_k \dfrac{1}{R_k}$. La **resistencia equivalente** $R_{eq}$ es la única resistencia que, vista desde los dos terminales del grupo, impone la misma relación $v$–$i$.

---

> [!info]
> Primera nota de [[Reduccion de Circuitos/index| Reducción de circuitos]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Combina la [[Resistencia y Ley de Ohm| ley de Ohm]] con [[Ley de Voltajes LKV| LKV]] y [[Ley de Corrientes LKC| LKC]]. Es la base de los repartos: el [[Divisor de Voltaje| divisor de tensión]] (serie) y el [[Divisor de Corriente| divisor de corriente]] (paralelo).

---

## Ejemplo

> [!ejemplo] Reducir una red mixta a una sola resistencia
> Buscamos la resistencia equivalente entre los terminales de la red: una $R_1=6\ \Omega$ en **serie** con el **paralelo** de $R_2=4\ \Omega$ y $R_3=4\ \Omega$.
>
> ![[serie_paralelo.svg|460]]
> Izq.: tres resistencias en serie. Der.: tres en paralelo.
>
> **Paso 1 — Resolver el paralelo $R_2\parallel R_3$.** Por ser dos resistencias en paralelo usamos el caso de dos:
> $$R_{23}=\frac{R_2 R_3}{R_2+R_3}=\frac{4\times 4}{4+4}=\frac{16}{8}=2\ \Omega.$$
> Dos resistencias iguales en paralelo dan la mitad: coherente.
>
> **Paso 2 — Sumar la serie.** $R_1$ y $R_{23}$ comparten un nudo y la misma corriente, así que están en serie:
> $$R_{eq}=R_1+R_{23}=6\ \Omega+2\ \Omega=8\ \Omega.$$
>
> La red completa se comporta, vista desde sus terminales, como una **única** resistencia de $8\ \Omega$. Si la alimentáramos con $v=24\ \text{V}$, la fuente entregaría $i=v/R_{eq}=24/8=3\ \text{A}$.

---

## En qué consiste

> [!teoria] Misma corriente vs. misma tensión
> Toda la asociación de resistencias se reduce a identificar **qué magnitud comparten** los elementos:
>
> - En **serie** los elementos van uno tras otro sin bifurcación: la **corriente** que entra en el primero es la misma que sale del último. Lo que se reparte es la **tensión**.
> - En **paralelo** los elementos cuelgan entre los **mismos dos nudos**: soportan la **misma tensión** en bornes. Lo que se reparte es la **corriente**.
>
> Confundir ambos casos es el error más frecuente de la reducción. La pregunta correcta no es "cómo están dibujadas", sino "¿comparten la corriente o comparten la tensión?".

> [!teorema] Resistencia equivalente en serie
> $n$ resistencias en serie equivalen a una sola
> $$R_{eq}=\sum_{k=1}^{n} R_k = R_1+R_2+\dots+R_n.$$
> El equivalente serie es siempre **mayor o igual** que la mayor de las resistencias.

> [!demostracion]
> **Paso 1 — Misma corriente.** Por estar en serie, la misma corriente $i$ atraviesa todas las resistencias.
>
> **Paso 2 — LKV.** La tensión total $v$ entre los terminales es, por la [[Ley de Voltajes LKV| LKV]], la suma de las caídas:
> $$v=v_1+v_2+\dots+v_n.$$
>
> **Paso 3 — Ley de Ohm.** Cada caída es $v_k=R_k\,i$. Sustituyendo:
> $$v=R_1 i+R_2 i+\dots+R_n i=\Big(\sum_k R_k\Big)\,i.$$
>
> **Paso 4 — Identificar.** Como $v=R_{eq}\,i$ por definición de equivalente, resulta $R_{eq}=\sum_k R_k$. $\blacksquare$

> [!teorema] Resistencia equivalente en paralelo
> $n$ resistencias en paralelo equivalen a una sola cuya **conductancia** es la suma de conductancias:
> $$\frac{1}{R_{eq}}=\sum_{k=1}^{n}\frac{1}{R_k},\qquad\text{equivalentemente}\qquad
> G_{eq}=\sum_{k=1}^{n} G_k.$$
> El equivalente paralelo es siempre **menor o igual** que la menor de las resistencias.

> [!demostracion]
> **Paso 1 — Misma tensión.** Por estar en paralelo, la misma tensión $v$ aparece en bornes de todas.
>
> **Paso 2 — LKC.** La corriente total $i$ que entra en el grupo se reparte, por la [[Ley de Corrientes LKC| LKC]], entre las ramas:
> $$i=i_1+i_2+\dots+i_n.$$
>
> **Paso 3 — Ley de Ohm (en conductancia).** Cada rama lleva $i_k=G_k\,v=v/R_k$. Sustituyendo:
> $$i=\frac{v}{R_1}+\frac{v}{R_2}+\dots+\frac{v}{R_n}=\Big(\sum_k \tfrac{1}{R_k}\Big)\,v.$$
>
> **Paso 4 — Identificar.** Como $i=v/R_{eq}$, resulta $\dfrac{1}{R_{eq}}=\sum_k \dfrac{1}{R_k}$. $\blacksquare$

> [!proposicion] El caso de dos resistencias en paralelo
> Para **exactamente dos** resistencias, despejar $R_{eq}$ de $1/R_{eq}=1/R_1+1/R_2$ da la fórmula del "producto sobre suma":
> $$R_{eq}=\frac{R_1 R_2}{R_1+R_2}.$$
> Es la forma más usada en la práctica. **Cuidado:** solo vale para **dos** ramas; con tres o más hay que volver a las conductancias. Como caso particular, $n$ resistencias **iguales** $R$ en paralelo dan $R_{eq}=R/n$.

> [!warning]
> Serie y paralelo solo se aplican a grupos **reconocibles** como tales. En un puente o en una red en $\Delta$/Y puede no haber **ninguna** pareja en serie ni en paralelo: en ese caso esta técnica se agota y hay que recurrir a [[Estrella Triangulo Kennelly| Kennelly]] o a mallas/nodos. Antes de sumar, comprueba siempre que el grupo comparte de verdad la corriente (serie) o la tensión (paralelo).

---

## Resumen

> [!resumen] Lo esencial
> | Asociación | Comparten | Equivalente | Tamaño de $R_{eq}$ |
> |:---|:---|:---|:---|
> | Serie | la corriente $i$ | $R_{eq}=\sum_k R_k$ | $\ge$ la mayor |
> | Paralelo | la tensión $v$ | $1/R_{eq}=\sum_k 1/R_k$ | $\le$ la menor |
> | Paralelo (dos) | la tensión $v$ | $R_{eq}=\dfrac{R_1 R_2}{R_1+R_2}$ | $\le$ la menor |
> | $n$ iguales en paralelo | la tensión $v$ | $R_{eq}=R/n$ | — |

> [!corolario]
> La **dualidad** es perfecta: lo que la serie hace con resistencias, el paralelo lo hace con conductancias. Por eso conviene pensar en serie con $R$ y en paralelo con $G=1/R$: en ambos casos "lo que se comparte se suma". Esta misma dualidad reaparece en los divisores y en la transformación de fuentes.

> [!referencia]
> Fraile Mora, cap. 1, §1.10. Continúa con el [[Divisor de Voltaje]] y el [[Divisor de Corriente]].
