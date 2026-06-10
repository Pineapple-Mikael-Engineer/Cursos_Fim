---
title: Transformación de Fuentes
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - reduccion
draft: false
aliases:
  - transformación de fuentes
  - equivalencia de fuentes
  - fuente de tensión a corriente
  - source transformation
---

# Transformación de Fuentes $V_s=I_s R$

> [!definicion]
> Una **fuente de tensión real** ($V_s$ en **serie** con una resistencia $R$) y una **fuente de
> corriente real** ($I_s$ en **paralelo** con la misma $R$) son **indistinguibles** vistas desde sus
> dos terminales si
> $$I_s=\frac{V_s}{R}\qquad\Longleftrightarrow\qquad V_s=I_s\,R.$$
> **Transformar una fuente** es sustituir una por la otra. Es la herramienta que permite **combinar**
> fuentes y resistencias hasta dejar el circuito en la forma más cómoda para resolver.

---

> [!info]
> Cuarta nota de [[Reduccion de Circuitos/index| Reducción de circuitos]], en el
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Solo tiene sentido para
> [[Fuentes Reales| fuentes reales]] (con resistencia interna), no para fuentes ideales. Es un caso
> particular de la equivalencia de [[Resistencias en Serie y Paralelo| terminales]] y la semilla del
> [[Teorema de Norton| equivalente de Norton]] del capítulo 2.

---

## Ejemplo

> [!ejemplo] Resolver una carga con las dos formas equivalentes
> Una fuente de tensión real $V_s=10\ \text{V}$ con resistencia interna $R=5\ \Omega$ alimenta una
> carga $R_L=5\ \Omega$. La resolvemos primero tal cual y luego con su fuente de corriente
> equivalente, para comprobar que la carga "ve" lo mismo.
>
> ![[transformacion_fuentes.svg|460]]
> Equivalencia: fuente de tensión $V_s$–$R$ serie ↔ fuente de corriente $I_s=V_s/R$–$R$ paralelo.
>
> **Paso 1 — Forma de tensión.** $V_s$, $R$ y $R_L$ están en serie:
> $$I_L=\frac{V_s}{R+R_L}=\frac{10}{5+5}=1\ \text{A},\qquad V_L=I_L R_L=1\times 5=5\ \text{V}.$$
>
> **Paso 2 — Transformar la fuente.** La fuente de corriente equivalente vale
> $$I_s=\frac{V_s}{R}=\frac{10}{5}=2\ \text{A}\quad\text{en paralelo con } R=5\ \Omega.$$
>
> **Paso 3 — Forma de corriente.** Ahora $R$ y $R_L$ quedan en paralelo y $I_s$ se reparte entre
> ellas. Por el [[Divisor de Corriente| divisor de corriente]]:
> $$I_L=I_s\,\frac{R}{R+R_L}=2\times\frac{5}{5+5}=1\ \text{A},\qquad V_L=I_L R_L=5\ \text{V}.$$
>
> **Misma corriente y misma tensión en la carga** ($1\ \text{A}$, $5\ \text{V}$) por ambos caminos: la
> transformación es exacta. La carga no puede distinguir qué fuente la alimenta.

---

## En qué consiste

> [!teoria] Misma recta $v$–$i$ en los terminales
> Una fuente real, sea de tensión o de corriente, presenta en sus terminales una relación $v$–$i$ que
> es una **recta**. Dos fuentes reales son equivalentes si esa recta es la **misma**: igual tensión en
> vacío (circuito abierto) e igual corriente en cortocircuito. La resistencia $R$ — idéntica en ambas
> formas — fija la **pendiente** de esa recta. Por eso al transformar **no cambia** el valor de $R$;
> solo cambia la forma de describir la misma fuente.

> [!teorema] Equivalencia de fuentes reales
> Vistas desde sus terminales, son equivalentes:
> $$\underbrace{V_s\ \text{en serie con}\ R}_{\text{fuente de tensión real}}
> \qquad\Longleftrightarrow\qquad
> \underbrace{I_s=\frac{V_s}{R}\ \text{en paralelo con}\ R}_{\text{fuente de corriente real}}.$$
> La resistencia $R$ es **la misma** en ambas; lo único que cambia es serie$\to$paralelo y
> $V_s\leftrightarrow I_s R$.

> [!demostracion]
> **Paso 1 — Recta de la fuente de tensión.** Con $V_s$ en serie con $R$, la tensión en los terminales
> bajo una corriente de salida $i$ es, por LKV,
> $$v=V_s-R\,i.$$
>
> **Paso 2 — Recta de la fuente de corriente.** Con $I_s$ en paralelo con $R$, la corriente de
> $R$ es $I_s-i$ (LKC), y su tensión es la de los terminales:
> $$v=R\,(I_s-i)=R I_s-R\,i.$$
>
> **Paso 3 — Igualar.** Ambas rectas tienen la misma pendiente $-R$. Coinciden en todo punto si y solo
> si los términos independientes son iguales:
> $$V_s=R I_s\quad\Longleftrightarrow\quad I_s=\frac{V_s}{R}.$$
> Cumplida esa condición, los dos circuitos imponen idéntica $v$ para toda $i$: son
> indistinguibles. $\blacksquare$

> [!proposicion] Para qué sirve
> Su utilidad práctica es **encadenar simplificaciones**: tras transformar, fuentes y resistencias que
> antes estaban "atravesadas" quedan en serie o en paralelo y pueden **combinarse**. Varias fuentes de
> corriente en paralelo se suman directamente; varias de tensión en serie también. Alternar
> transformaciones con asociaciones serie/paralelo suele reducir un circuito a una sola fuente y una
> sola resistencia.

> [!warning]
> La transformación **solo describe bien los terminales externos**: la corriente o la potencia
> **internas** de $R$ **no** coinciden entre las dos formas (en una, $R$ ve la corriente de carga; en
> la otra, la de reparto). No la apliques a una fuente **ideal**: una de tensión ideal tiene $R=0$
> (sería $I_s=\infty$) y una de corriente ideal tiene $R\to\infty$; en ambos casos la equivalencia no
> está definida.

---

## Resumen

> [!resumen] Lo esencial
> | Concepto | Fuente de tensión real | Fuente de corriente real |
> |:---|:---|:---|
> | Estructura | $V_s$ en **serie** con $R$ | $I_s$ en **paralelo** con $R$ |
> | Conversión | $V_s=I_s R$ | $I_s=V_s/R$ |
> | Resistencia | $R$ (la misma) | $R$ (la misma) |
> | En vacío | $v=V_s$ | $v=I_s R$ |
> | En cortocircuito | $i=V_s/R$ | $i=I_s$ |

> [!corolario]
> La transformación de fuentes es el "serie$\leftrightarrow$paralelo" aplicado a las fuentes: lo que
> para resistencias era reducir, para fuentes es **cambiar de forma sin alterar los terminales**.
> Llevada a su límite — reducir todo lo demás a una sola $R$ — produce directamente el
> [[Teorema de Norton| equivalente de Norton]] (y, por su dual, el de Thévenin).

> [!referencia]
> Fraile Mora, cap. 1, §1.11. Ver [[Fuentes Reales]], [[Resistencias en Serie y Paralelo]] y el
> [[Teorema de Norton]].
