---
title: Proporcionalidad y Superposición
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - superposicion
draft: false
aliases:
  - proporcionalidad
  - superposición
  - principio de superposición
  - linealidad
  - proportionality
  - superposition
---

# Proporcionalidad y Superposición

> [!definicion]
> En un circuito **lineal** se cumplen dos propiedades equivalentes a la linealidad:
> **(a) Proporcionalidad (homogeneidad):** si una fuente independiente se multiplica por un factor
> $k$, **todas** las respuestas (tensiones y corrientes) debidas a ella se multiplican por el mismo
> $k$.
> **(b) Superposición (aditividad):** la respuesta ante **varias** fuentes independientes es la
> **suma** de las respuestas a cada fuente actuando **sola**, con las demás **anuladas** (las fuentes
> de tensión se sustituyen por un **cortocircuito**, las de corriente por un **circuito abierto**).

> [!info]
> Es el **cimiento** de [[Teoremas/index| Teoremas de circuitos]]
> ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]): de la linealidad derivan directamente el
> [[Teorema de Thevenin]] y el [[Teorema de Norton]]. Se apoya en el manejo de
> [[Fuentes Independientes]] y del [[Divisor de Voltaje]]. Fraile Mora, cap. 1, §1.14.

---

## Ejemplo

> [!ejemplo]
> **Tensión en un nodo con dos fuentes, por superposición.**
>
> Una fuente $V_s = 12\ \text{V}$ está en serie con $R_1 = 4\ \Omega$ y llega al nodo $N$; una fuente
> de corriente $I_s = 1\ \text{A}$ **inyecta** corriente en $N$; y $R_2 = 12\ \Omega$ une $N$ con
> masa. Hallar la tensión $V_N$.
>
> ![[superposicion.svg|640]]
>
> *(a) circuito original; (b) solo $V_s$ ($I_s$ abierta); (c) solo $I_s$ ($V_s$ en corto). La
> respuesta total es la suma.*
>
> **Paso 1 — Solo $V_s$** (se **abre** la fuente de corriente $I_s$). El nodo $N$ queda alimentado por
> $V_s$ a través del divisor $R_1$-$R_2$:
> $$V_N^{(1)} = V_s\,\frac{R_2}{R_1+R_2} = 12\cdot\frac{12}{4+12} = 12\cdot\frac{12}{16} = 9\ \text{V}.$$
>
> **Paso 2 — Solo $I_s$** (se **cortocircuita** la fuente de tensión $V_s$). Con $V_s$ en corto, $R_1$
> queda de $N$ a masa, **en paralelo** con $R_2$:
> $$R_1 \parallel R_2 = \frac{R_1 R_2}{R_1+R_2} = \frac{4\cdot 12}{16} = 3\ \Omega,
> \qquad V_N^{(2)} = I_s\,(R_1 \parallel R_2) = 1\cdot 3 = 3\ \text{V}.$$
>
> **Paso 3 — Superponer.** La tensión total es la suma de ambas contribuciones:
> $$V_N = V_N^{(1)} + V_N^{(2)} = 9 + 3 = 12\ \text{V}.$$
>
> > [!solucion]
> > $V_N = 12\ \text{V}$. La corriente que circula por $R_2$ hacia masa es
> > $i_{R_2} = \dfrac{V_N}{R_2} = \dfrac{12}{12} = 1\ \text{A}$.

---

## En qué consiste

> [!teoria] Por qué funciona: la respuesta es combinación lineal de las fuentes
> En una red de resistencias y fuentes independientes, las ecuaciones de nodos (o mallas) son
> **lineales**: cada incógnita resulta ser una **combinación lineal** de los valores de las fuentes,
> $v = a_1 V_{s1} + a_2 I_{s1} + \dots$, con coeficientes $a_i$ que dependen solo de las resistencias.
> De ahí salen las dos propiedades de golpe: escalar una fuente por $k$ escala su término (**propor-
> cionalidad**), y la respuesta total es la suma de los términos individuales (**superposición**).
> **Anular** una fuente significa ponerla a su valor nulo: una fuente de tensión a $0\ \text{V}$ es un
> **cortocircuito**, y una de corriente a $0\ \text{A}$ es un **circuito abierto**. Las fuentes
> **dependientes NO se anulan**: no son entradas independientes, sino que responden a variables
> internas del circuito, así que permanecen activas en todos los subcircuitos.

> [!algoritmo] Cómo resolver por superposición
> **Paso 1 — Aislar una fuente:** dejar activa una sola fuente independiente y **anular** las demás
> (tensión → cortocircuito, corriente → circuito abierto; las dependientes se mantienen).
>
> **Paso 2 — Resolver el subcircuito:** calcular la contribución de esa fuente a la respuesta buscada
> (a menudo es trivial con [[Divisor de Voltaje| divisores]] o asociaciones serie/paralelo).
>
> **Paso 3 — Repetir y sumar:** hacer lo mismo con cada fuente independiente y **sumar** todas las
> contribuciones **con su signo** para obtener la respuesta total.

> [!warning]
> La superposición vale para magnitudes **lineales** (tensiones y corrientes), pero **NO para la
> potencia**: como $P = R\,i^2$ es **cuadrática**, la potencia total **no** es la suma de las potencias
> que daría cada fuente por separado. Hay que sumar primero las corrientes (o tensiones) y **luego**
> calcular la potencia. Además, las fuentes **dependientes nunca se anulan**.

## Resumen

> [!resumen]
> | Concepto | Regla |
> |:---|:---|
> | Proporcionalidad | fuente $\times k \Rightarrow$ respuestas debidas a ella $\times k$ |
> | Superposición | respuesta total $=$ suma de respuestas a cada fuente sola |
> | Anular fuente de tensión | sustituir por **cortocircuito** ($0\ \text{V}$) |
> | Anular fuente de corriente | sustituir por **circuito abierto** ($0\ \text{A}$) |
> | Fuentes dependientes | **no se anulan** (siempre activas) |
> | Potencia | **no** se superpone ($P=R\,i^2$ es cuadrática) |

> [!corolario]
> Como la relación tensión-corriente en los terminales de cualquier red lineal es una **recta**, dos
> números bastan para describirla por completo: de ahí nacen el [[Teorema de Thevenin]] y el
> [[Teorema de Norton]], que reducen toda la red a una fuente y una resistencia.

> [!referencia]
> Fraile Mora, cap. 1, §1.14. Consecuencias: [[Teorema de Thevenin]], [[Teorema de Norton]].
> Herramientas: [[Divisor de Voltaje]], [[Fuentes Independientes]]. Índice:
> [[Teoremas/index]].
