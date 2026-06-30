---
title: Teoremas de Circuitos
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - index
draft: false
aliases:
  - teoremas de circuitos
  - teoremas de redes
---

# Teoremas de Circuitos

> [!definicion]
> Los **teoremas de circuitos** son consecuencias de la **linealidad** que permiten resolver una **parte** de la red sin plantear todo el sistema de [[Metodos de Analisis/index| mallas o nodos]]. Los cuatro esenciales: **superposición** (la respuesta a varias fuentes es la suma de las respuestas a cada una), **Thévenin** y **Norton** (todo lo que ve una carga por dos terminales es una sola fuente equivalente con una resistencia), y **máxima transferencia de potencia** (cuánta potencia puede entregar esa fuente equivalente).

> [!info]
> Tercera sección del [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Se apoyan en las [[Leyes de Kirchhoff/index| leyes de Kirchhoff]] y en la [[Reduccion de Circuitos/index| reducción]]. Como todo el capítulo, se reutilizan tal cual en [[5 Circuitos AC Sinusoidal y Fasores/index| régimen sinusoidal]] con $Z$ en vez de $R$. Fraile Mora, cap. 1, §1.14-1.16.

---

## La linealidad lo permite todo

> [!teoria] El cimiento: superposición
> Un circuito es **lineal** si sus elementos lo son (la resistencia cumple $v=Ri$, una recta). En un sistema lineal, la respuesta a una suma de causas es la suma de las respuestas: ese es el **principio de superposición**. De él se derivan todos los demás teoremas.
>
> - **Superposición.** Para hallar una corriente o tensión, se calcula la contribución de **cada fuente por separado** (anulando las demás: las de tensión se cortocircuitan, las de corriente se abren) y se **suman**. Útil cuando hay varias fuentes y solo interesa una magnitud. → [[Proporcionalidad y Superposicion]].

> [!teoria] Reducir todo a una fuente y una resistencia
> El resultado más potente: **cualquier** red lineal vista desde **dos terminales** se comporta como una **única fuente con una única resistencia**. Hay dos formas, equivalentes entre sí por una [[Transformacion de Fuentes| transformación de fuente]]:
>
> - **Thévenin:** una fuente de tensión $V_{Th}$ (la tensión en vacío) **en serie** con una resistencia $R_{Th}$. → [[Teorema de Thevenin]].
> - **Norton:** una fuente de corriente $I_{N}$ (la corriente de cortocircuito) **en paralelo** con la misma resistencia $R_{N}=R_{Th}$. → [[Teorema de Norton]].
>
> Con ello, una carga "no ve" la maraña interna del circuito, solo su equivalente. Y la pregunta de **cuánta potencia** recibe esa carga tiene respuesta inmediata: la **máxima transferencia** ocurre cuando $R_L=R_{Th}$. → [[Maxima Transferencia de Potencia]].

> [!teoria] Un atajo para ramas en paralelo
> Cuando varias ramas (cada una, una fuente con su resistencia) se conectan **en paralelo** entre dos nodos, el **teorema de Millman** da directamente la tensión entre ellos sin plantear el sistema. Es un caso particular muy cómodo del análisis de nodos. → [[Teorema de Millman]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Teorema | Para qué sirve |
> |:---|:---|
> | [[Proporcionalidad y Superposicion]] | descomponer la respuesta fuente a fuente (linealidad) |
> | [[Teorema de Thevenin]] | equivalente de dos terminales: $V_{Th}$ en serie con $R_{Th}$ |
> | [[Teorema de Norton]] | equivalente dual: $I_N$ en paralelo con $R_N$ |
> | [[Maxima Transferencia de Potencia]] | la carga óptima $R_L=R_{Th}$ y la potencia máxima |
> | [[Teorema de Millman]] | tensión de varias ramas en paralelo, de un cálculo |

> [!corolario]
> Los teoremas no sustituyen a mallas y nodos: los **complementan**. Cuando interesa una sola magnitud, el efecto de una sola fuente, o el comportamiento visto por una carga, un teorema da la respuesta con mucho menos trabajo que resolver el circuito entero.

> [!referencia]
> Fraile Mora, cap. 1, §1.14-1.16. Anterior: [[Metodos de Analisis/index| Métodos de análisis]]. Cierra el [[2 Metodos de Analisis y Teoremas/index| capítulo 2]].
