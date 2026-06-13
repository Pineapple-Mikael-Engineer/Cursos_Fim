---
title: Ecuaciones Diferenciales Ordinarias
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - index
draft: false
aliases:
  - EDOs
  - Ecuaciones diferenciales ordinarias
  - ODE
  - Integración numérica de EDOs
---

# Ecuaciones Diferenciales Ordinarias

> [!definicion]
> Una **ecuación diferencial ordinaria** (EDO) relaciona una función desconocida con sus derivadas respecto a una única variable independiente. En forma normal de primer orden,
> $$\frac{dy}{dt} = f(t, y), \qquad y(t)\in\mathbb{R}^m,$$
> y la resolución numérica genera una sucesión $y_0, y_1, \dots$ que aproxima $y(t)$ en instantes $t_n = t_0 + nh$.

> [!info]
> Las EDOs son **el lenguaje de los sistemas físicos**: la segunda ley de Newton $m\ddot{x} = F$, los circuitos $L\ddot q + R\dot q + q/C = V(t)$, la desintegración radiactiva $\dot N = -\lambda N$, la cinética química, la mecánica orbital y los modelos de poblaciones son todos EDOs. Resolverlas numéricamente es **simular**: avanzar el estado del sistema en el tiempo.

---

## Dos problemas según las condiciones

> [!info]
> - **[[Problema Valor Inicial PVI/index|Problema de valor inicial (PVI)]]:** se conoce el estado en un instante $t_0$ y se **integra hacia adelante** en el tiempo. Es el caso de la simulación dinámica: dado dónde está el sistema ahora, predecir su evolución.
> - **[[Problema Valor Frontera PVF/index|Problema de valor de frontera (PVF)]]:** se imponen condiciones en **dos** extremos del dominio (no en un instante inicial). Aparece en problemas estacionarios: deflexión de una viga, distribución de temperatura en equilibrio, trayectorias con extremos fijos.

---

## Mapa del capítulo

> [!info]
> **Parte 1 — PVI ([[Problema Valor Inicial PVI/index]]).** Existencia y unicidad de la solución; métodos de un paso ([[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]], [[Metodos Serie Taylor Orden Superior|Taylor]], [[Metodos Runge Kutta/index|Runge-Kutta]]); control [[Control Paso Adaptativo RK45 Dormand Prince|adaptativo]] del paso; [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]]; [[Sistemas EDO y Orden Superior/index|sistemas y orden superior]]; [[Rigidez Stiffness Problemas Ingenieria|rigidez]]; e [[Integradores Simplecticos Conservacion|integradores simplécticos]] que conservan invariantes físicos.

> [!info]
> **Parte 2 — PVF ([[Problema Valor Frontera PVF/index]]).** El método de [[Metodo Diferencias Finitas/index|diferencias finitas]] (discretización a un sistema lineal) y el método de [[Metodo Disparo Shooting/index|disparo]] (reducir el PVF a una sucesión de PVI).

---

## Ejemplo: el oscilador armónico

> [!ejemplo]
> **Masa-resorte $m\ddot{x} = -kx$.** Reescribiendo como sistema de primer orden con $v = \dot x$:
> $$\dot x = v, \qquad \dot v = -\tfrac{k}{m}x.$$
> Dado el estado inicial $(x_0, v_0)$, un método numérico avanza $(x_n, v_n)$ paso a paso. La solución exacta es una elipse en el plano de fases $(x, v)$ (energía constante); un buen integrador debe **mantener** esa elipse cerrada y no dejar que el sistema gane o pierda energía artificialmente — exactamente lo que distingue a los [[Integradores Simplecticos Conservacion|métodos simplécticos]].

---

## Las preguntas centrales

> [!teoria]
> Todo método de EDOs se juzga por tres propiedades, formalizadas en el [[Consistencia Estabilidad Convergencia Lax|teorema de Lax]]:
> - **Consistencia:** el método aproxima localmente la ecuación ([[Error Local Truncamiento vs Error Global Acumulado|error de truncamiento]] $\to 0$).
> - **Estabilidad:** los errores no se amplifican sin control ([[Regiones Estabilidad Absoluta A Estabilidad|región de estabilidad]]).
> - **Convergencia:** la solución numérica tiende a la exacta cuando $h\to 0$.
>
> Consistencia + estabilidad ⟹ convergencia. Para sistemas físicos, una cuarta propiedad importa: la **conservación** de invariantes (energía, momento), que solo garantizan los integradores geométricos.

---

## Resumen

| Parte | Subdirectorio |
|:---|:---|
| Valor inicial (simulación dinámica) | [[Problema Valor Inicial PVI/index]] |
| Valor de frontera (problemas estacionarios) | [[Problema Valor Frontera PVF/index]] |

> [!corolario]
> Las EDOs modelan la dinámica de prácticamente todo sistema físico, y resolverlas numéricamente equivale a simularlas. El [[Problema Valor Inicial PVI/index|problema de valor inicial]] integra el estado hacia adelante en el tiempo —la simulación por excelencia— mientras que el [[Problema Valor Frontera PVF/index|problema de valor de frontera]] resuelve configuraciones de equilibrio con condiciones en dos extremos. Todo método se evalúa por consistencia, estabilidad y convergencia; para sistemas físicos conservativos se añade la fidelidad geométrica de los [[Integradores Simplecticos Conservacion|integradores simplécticos]]. Estas técnicas se apoyan en la [[5 Diferenciacion Integracion Numerica/index|diferenciación e integración numérica]] y en la resolución de [[2 Sistemas Ecuaciones Lineales/index|sistemas lineales]] (métodos implícitos y de frontera).
