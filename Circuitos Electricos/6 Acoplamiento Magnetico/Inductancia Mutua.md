---
title: Inductancia Mutua
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - inductancia mutua
  - inducción mutua
  - mutual inductance
---

# Inductancia Mutua $\;M$

> [!definicion]
> La **inductancia mutua** $M$ (en henrios) cuantifica el acoplamiento entre dos bobinas: una corriente variable $i_1$ en la primera **induce** en la segunda una tensión
> $$v_2=M\,\frac{di_1}{dt},$$
> y recíprocamente. Es **simétrica** ($M_{12}=M_{21}=M$). Cuando ambas bobinas llevan corriente, sus tensiones combinan la autoinducción y la mutua:
> $$v_1=L_1\frac{di_1}{dt}\pm M\frac{di_2}{dt},\qquad v_2=L_2\frac{di_2}{dt}\pm M\frac{di_1}{dt}.$$

> [!info]
> El concepto central del [[6 Acoplamiento Magnetico/index| acoplamiento magnético]]. Extiende la [[Autoinduccion| autoinducción]] al par de bobinas; el **signo** $\pm M$ lo fija la [[Regla de los Puntos]], y su tamaño relativo, el **coeficiente de acoplamiento** $k$ (más abajo). Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **Tensión inducida en el secundario abierto.**
>
> Dos bobinas acopladas con $L_1=2\ \text{H}$, $L_2=8\ \text{H}$ y $M=3\ \text{H}$. Por el primario circula $i_1=4t\ \text{A}$ (es decir $di_1/dt=4\ \text{A/s}$) y el secundario está **abierto** ($i_2=0$). Hallar $v_1$ y $v_2$.
>
> ![[inductancia_mutua.svg|470]]
>
> *La corriente $i_1$ crea un flujo; parte enlaza la segunda bobina (flujo mutuo $M$) e induce $v_2$ aunque por ella no circule corriente. Los **puntos** marcan la polaridad relativa.*
>
> **Paso 1 — Tensión en el primario** (su propia autoinducción):
> $$v_1=L_1\frac{di_1}{dt}=2\cdot4=8\ \text{V}.$$
>
> **Paso 2 — Tensión inducida en el secundario** (solo mutua, pues $i_2=0$):
> $$v_2=M\frac{di_1}{dt}=3\cdot4=12\ \text{V}.$$
>
> > [!solucion]
> > $v_1=8\ \text{V}$, $v_2=12\ \text{V}$. Hay tensión en el secundario **sin corriente** en él: la induce el flujo del primario. El acoplamiento es $k=M/\sqrt{L_1L_2}=3/\sqrt{16}=0{,}75$.

---

## En qué consiste

> [!teoria] De dónde sale $M$
> La corriente $i_1$ crea un flujo magnético; una **fracción** de ese flujo atraviesa la segunda bobina. Por la ley de Faraday, si ese flujo cambia, induce tensión en la segunda: la constante de proporcionalidad entre $v_2$ y $di_1/dt$ es la inductancia mutua $M$. Que sea **simétrica** ($M_{12}=M_{21}$) es un resultado profundo (se deduce de la energía): el acoplamiento "se ve igual" desde cualquiera de las dos bobinas.

> [!teorema] Las ecuaciones del par acoplado
> Para dos bobinas acopladas, las tensiones son la suma de la autoinducción (por la propia corriente) y la mutua (por la corriente de la otra):
> $$\boxed{\;v_1=L_1\,i_1'\pm M\,i_2',\qquad v_2=\pm M\,i_1'+L_2\,i_2'\;}$$
> donde $i'=di/dt$ y el signo $\pm$ lo da la [[Regla de los Puntos]]. En régimen sinusoidal, $d/dt\to j\omega$, así que la reactancia mutua es $j\omega M$ ([[Acoplamiento Magnetico Fasorial]]).

> [!proposicion] Coeficiente de acoplamiento $k$
> No todo el flujo se comparte: $M$ está acotada por las autoinductancias, $M\le\sqrt{L_1 L_2}$ (la cota se **demuestra** por energía en [[Energia en Bobinas Acopladas]]). El cociente adimensional
> $$k=\frac{M}{\sqrt{L_1 L_2}}\in[0,1]$$
> mide qué **fracción del flujo** se comparte: $k\to0$ bobinas casi independientes (núcleo de aire, $k\sim0{,}01$–$0{,}5$); $k\to1$ **acoplamiento perfecto** (núcleo ferromagnético, $k\sim0{,}99$; todo el flujo enlaza ambas bobinas). En el límite $k=1$, $M=\sqrt{L_1L_2}$ y la relación de transformación queda fijada por las espiras, $V_2/V_1=\sqrt{L_2/L_1}=N_2/N_1$ (puente con el [[Transformador Ideal]]). Un cálculo que dé $k>1$ señala datos incompatibles.

> [!warning]
> La inductancia mutua **no** es un elemento aparte: es un **acoplamiento** entre dos inductores. Sus unidades son henrios, como $L$. Y el término mutuo puede **sumar o restar** según los puntos: nunca escribir las ecuaciones sin fijar antes el convenio de puntos.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Tensión inducida (secundario abierto) | $v_2=M\,di_1/dt$ |
> | Ecuaciones del par | $v_1=L_1 i_1'\pm M i_2'$, $v_2=\pm M i_1'+L_2 i_2'$ |
> | Simetría | $M_{12}=M_{21}=M$ |
> | Cota | $M\le\sqrt{L_1L_2}$ |
> | Reactancia mutua (CA) | $j\omega M$ |

> [!corolario]
> La inductancia mutua abre un canal de energía entre dos bobinas que no se tocan: la corriente de una induce tensión en la otra. Con su signo (puntos) y su intensidad ($k$), queda descrito cualquier par acoplado —y, en el límite, el transformador—.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Base: [[Autoinduccion]]. Signo: [[Regla de los Puntos]]. Energía y cota de $M$: [[Energia en Bobinas Acopladas]].
