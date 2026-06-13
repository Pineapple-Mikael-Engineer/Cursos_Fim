---
title: Problema de Valor de Frontera (PVF)
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - index
draft: false
aliases:
  - PVF
  - Problema de valor de frontera
  - Boundary value problem
  - BVP
---

# Problema de Valor de Frontera (PVF)

> [!definicion]
> Un **problema de valor de frontera** es una EDO de orden $\geq 2$ con condiciones impuestas en **dos** extremos del dominio, no en un instante inicial:
> $$y'' = f(x, y, y'), \qquad y(a) = \alpha, \quad y(b) = \beta, \qquad x \in [a, b].$$

> [!info]
> A diferencia del [[Problema Valor Inicial PVI/index|PVI]] (que integra hacia adelante en el tiempo), el PVF describe **configuraciones de equilibrio**: la deflexión estática de una viga, la temperatura estacionaria en una barra, el perfil de una membrana. No hay "tiempo" que avanzar; la solución debe satisfacer ambos extremos a la vez, lo que cambia por completo la estrategia numérica.

---

## Dos enfoques

> [!info]
> - **[[Metodo Diferencias Finitas/index|Diferencias finitas]]:** discretiza el dominio y reemplaza las derivadas por [[Aproximacion Diferencias Finitas Serie Taylor|aproximaciones]], convirtiendo el PVF en un **sistema lineal** (tridiagonal). Resuelve todos los puntos simultáneamente.
> - **[[Metodo Disparo Shooting/index|Disparo (shooting)]]:** convierte el PVF en una sucesión de [[Problema Valor Inicial PVI/index|PVI]], ajustando la pendiente inicial desconocida hasta acertar la condición del otro extremo. Reutiliza los integradores de PVI.

---

## Ejemplo

> [!ejemplo]
> **Conducción de calor estacionaria en una barra: $-T'' = q(x)/k$**, con extremos a temperatura fija $T(0)=T_0$, $T(L)=T_L$. La solución $T(x)$ es el perfil de temperatura en equilibrio. No se "integra en el tiempo": se busca la función que satisface la ecuación **y** ambos extremos.
>
> | Enfoque | Cómo procede |
> |:---|:---|
> | Diferencias finitas | discretiza $[0,L]$, resuelve un sistema tridiagonal para $T_1,\dots,T_{N-1}$ |
> | Disparo | adivina $T'(0)$, integra como PVI, corrige hasta que $T(L)=T_L$ |

---

## PVI vs PVF

> [!info]
> | | [[Problema Valor Inicial PVI/index\|PVI]] | PVF |
> |:---|:---|:---|
> | Condiciones | todas en $t_0$ | repartidas en $a$ y $b$ |
> | Interpretación | evolución temporal | equilibrio espacial |
> | Estrategia | marchar hacia adelante | resolver todo a la vez (o iterar) |
> | Existencia/unicidad | garantizada (Lipschitz) | **no** siempre (puede no haber o haber múltiples) |
> | Métodos | un paso (RK) | diferencias finitas, disparo |

> [!warning]
> A diferencia del PVI, un PVF puede **no tener solución** o tener **infinitas** (p. ej. problemas de autovalores, modos de vibración). La existencia depende de la ecuación y las condiciones; no hay un teorema tan limpio como [[Teoremas Existencia Unicidad Picard Lindelof|Picard-Lindelöf]].

---

## Resumen

| Enfoque | Subdirectorio |
|:---|:---|
| Diferencias finitas (sistema lineal) | [[Metodo Diferencias Finitas/index]] |
| Disparo (reducción a PVI) | [[Metodo Disparo Shooting/index]] |

> [!corolario]
> El problema de valor de frontera impone condiciones en dos extremos del dominio y describe configuraciones de equilibrio —vigas, temperaturas estacionarias, membranas— en vez de evolución temporal. Se ataca de dos formas: las [[Metodo Diferencias Finitas/index|diferencias finitas]] discretizan y resuelven un sistema lineal tridiagonal de una vez, mientras que el [[Metodo Disparo Shooting/index|disparo]] reduce el PVF a una sucesión de [[Problema Valor Inicial PVI/index|PVI]] ajustando la pendiente inicial. A diferencia del PVI, la existencia y unicidad no están garantizadas, lo que conecta con problemas de autovalores y modos propios.
