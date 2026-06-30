---
title: Sistema Polifásico
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - sistema polifásico
  - sistemas polifásicos
  - polyphase system
---

# Sistema Polifásico

> [!definicion]
> Un **sistema polifásico** está formado por $n$ tensiones (o corrientes) sinusoidales de la **misma amplitud y frecuencia**, desfasadas uniformemente $360^\circ/n$ entre sí. El **monofásico** es el caso $n=1$; el **trifásico** ($n=3$, desfase $120^\circ$) es el que domina la generación y el transporte de energía por ser el de mejor compromiso entre simplicidad y prestaciones.

> [!info]
> El marco general de los [[Fundamentos Trifasicos/index| fundamentos trifásicos]] ([[7 Circuitos Trifasicos/index| capítulo 7]]): el trifásico es solo el **caso particular** más útil ($n=3$) de una familia más amplia. La generación concreta se ve en [[Generacion de Tensiones Trifasicas]] y el porqué de su predominio en [[Ventajas del Trifasico]]. Fraile Mora, cap. 3, §3.1.

---

## Ejemplo

> [!ejemplo]
> **Desfase de un sistema bifásico, trifásico y hexafásico.**
>
> ¿Qué desfase hay entre fases consecutivas en un sistema bifásico ($n=2$), trifásico ($n=3$) y hexafásico ($n=6$)?
>
> **Paso 1 — La regla.** El desfase uniforme entre fases vale, por definición,
> $$\Delta\varphi=\frac{360^\circ}{n}.$$
>
> **Paso 2 — Sustituir cada caso:**
> - Bifásico, $n=2$: $\Delta\varphi=360^\circ/2=180^\circ$.
> - Trifásico, $n=3$: $\Delta\varphi=360^\circ/3=120^\circ$.
> - Hexafásico, $n=6$: $\Delta\varphi=360^\circ/6=60^\circ$.
>
> > [!solucion]
> > $180^\circ$, $120^\circ$ y $60^\circ$ respectivamente, sin más que aplicar $\Delta\varphi=360^\circ/n$. A mayor número de fases, menor desfase entre ellas y más "lleno" queda el ciclo: por eso la potencia total se suaviza al crecer $n$.

---

## En qué consiste

> [!teoria] Por qué $n=3$ es el óptimo
> Con **una sola fase** ($n=1$) la potencia instantánea **pulsa** entre cero y un máximo dos veces por ciclo, y no existe campo magnético giratorio: un motor monofásico no arranca por sí solo. Al **aumentar $n$** ocurren dos cosas buenas: la suma de las potencias de las fases se vuelve más constante y la rectificación a continua sale más suave (menos rizado). Pero también una mala: cada fase necesita su(s) conductor(es), de modo que más fases significan **más cobre, más aislamiento y más coste**.
>
> El **trifásico es el mínimo $n$** que ya consigue lo esencial: potencia instantánea **constante** y **campo giratorio** (que permite el motor de inducción autoarrancante), y todo ello con solo **3 conductores** (o 4 con neutro). Subir a $n>3$ aporta mejoras marginales que no compensan el sobrecoste para generación y transporte. Por eso $n=3$ se impuso como estándar universal. Los sistemas de **más fases** ($n=6$, $n=12$) se reservan para **rectificación** industrial y **grandes máquinas**, donde el menor rizado sí justifica la complejidad.

> [!proposicion] La suma de las fases es cero (sistema equilibrado)
> En un sistema polifásico **equilibrado** —fases de igual amplitud y exactamente $360^\circ/n$— la suma instantánea de las $n$ tensiones (o corrientes) es **cero**:
> $$\sum_{k=0}^{n-1}V_m\operatorname{sen}\!\left(\omega t-k\,\frac{360^\circ}{n}\right)=0\quad\text{en todo instante}.$$
> En forma fasorial, los $n$ fasores tienen igual módulo y están repartidos a $360^\circ/n$: forman un **polígono regular cerrado**, cuyo vector resultante es nulo. Para $n=3$, el polígono es un triángulo equilátero; para $n=2$, dos vectores opuestos.

> [!warning]
> "Polifásico" **no** es "varias fuentes monofásicas independientes". Las fases **comparten la misma frecuencia** y guardan un **desfase fijo y coherente** entre sí; precisamente esa coherencia es la que da las ventajas (potencia constante, campo giratorio, anulación en el neutro). Además, el estándar es el **trifásico**: el bifásico ($n=2$) está hoy en **desuso** y solo aparece en contextos históricos o especiales.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |:---|:---|
> | Definición | $n$ fases iguales en amplitud y frecuencia |
> | Desfase entre fases | $\Delta\varphi=360^\circ/n$ |
> | Monofásico | $n=1$ (potencia pulsante, sin campo giratorio) |
> | Trifásico | $n=3$, desfase $120^\circ$ (estándar) |
> | Suma (equilibrado) | $\sum v_k=0$; fasores en polígono regular cerrado |

> [!corolario]
> El trifásico no es más que el polifásico de $n=3$: el **menor** número de fases que ya entrega potencia constante y campo giratorio con un mínimo de conductores. Toda la teoría del capítulo se construye sobre esa elección óptima.

> [!referencia]
> Fraile Mora, cap. 3, §3.1. Generación física: [[Generacion de Tensiones Trifasicas]]. Por qué se impuso: [[Ventajas del Trifasico]]. Marco: [[Fundamentos Trifasicos/index]], [[7 Circuitos Trifasicos/index]].
