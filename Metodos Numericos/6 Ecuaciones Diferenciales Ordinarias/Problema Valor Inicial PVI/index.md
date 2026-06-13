---
title: Problema de Valor Inicial (PVI)
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - index
draft: false
aliases:
  - PVI
  - Problema de valor inicial
  - Initial value problem
  - IVP
---

# Problema de Valor Inicial (PVI)

> [!definicion]
> Un **problema de valor inicial** consiste en una EDO de primer orden con el estado conocido en un instante inicial:
> $$\frac{dy}{dt} = f(t, y), \qquad y(t_0) = y_0, \qquad t \in [t_0, t_f].$$
> Resolverlo numéricamente es generar $y_1, y_2, \dots, y_N$ que aproximen $y(t_1), \dots, y(t_N)$, **avanzando** desde la condición inicial.

> [!info]
> El PVI es la **simulación dinámica**: dado el estado actual de un sistema físico, predecir su evolución temporal. La mayoría de los métodos son de **un paso** (calculan $y_{n+1}$ solo a partir de $y_n$): Euler, Taylor y Runge-Kutta. Su calidad se mide por el orden de convergencia y la región de estabilidad.

---

## Existencia y unicidad

> [!info]
> Antes de aproximar, conviene saber que la solución existe y es única: lo garantiza el [[Teoremas Existencia Unicidad Picard Lindelof|teorema de Picard-Lindelöf]] bajo la condición de Lipschitz de $f$. Sin unicidad, "la" solución numérica no tendría sentido.

## Métodos de un paso

> [!info]
> - **[[Metodos Taylor Euler/index|Euler y Taylor]]:** los métodos fundamentales. Euler ($O(h)$) es el ladrillo conceptual; las series de Taylor suben el orden a costa de derivadas analíticas.
> - **[[Metodos Runge Kutta/index|Runge-Kutta]]:** logran alto orden evaluando $f$ en puntos intermedios, **sin** derivadas. RK4 es el caballo de batalla; los métodos adaptativos (RK45) controlan el error automáticamente.

## Sistemas, rigidez y conservación

> [!info]
> - **[[Sistemas EDO y Orden Superior/index|Sistemas y orden superior]]:** toda EDO de orden $n$ (como $m\ddot x = F$) se reduce a un sistema de primer orden, y los métodos se aplican vectorialmente. Incluye los [[Integradores Simplecticos Conservacion|integradores simplécticos]] para sistemas conservativos.
> - **[[Rigidez Stiffness Problemas Ingenieria|Rigidez]]:** sistemas con escalas de tiempo muy dispares exigen métodos implícitos; la estabilidad, no la precisión, limita el paso.

---

## Ejemplo

> [!ejemplo]
> **Desintegración radiactiva $\dot N = -\lambda N$, $N(0)=N_0$** (solución exacta $N(t)=N_0 e^{-\lambda t}$). Con $\lambda=1$, $N_0=1$, $h=0.5$:
>
> | $t_n$ | Exacta $e^{-t}$ | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler]] | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] |
> |:---:|:---:|:---:|:---:|
> | 0.0 | 1.0000 | 1.0000 | 1.0000 |
> | 0.5 | 0.6065 | 0.5000 | 0.6065 |
> | 1.0 | 0.3679 | 0.2500 | 0.3679 |
> | 1.5 | 0.2231 | 0.1250 | 0.2231 |
>
> Euler ($O(h)$) acumula error visible; RK4 ($O(h^4)$) reproduce la exacta a 4 cifras con el mismo paso. La elección del método marca la diferencia entre una simulación fiel y una que se desvía.

---

## Cómo se evalúa un método de PVI

> [!info]
> | Propiedad | Pregunta | Nota |
> |:---|:---|:---|
> | Orden | ¿qué tan rápido converge? | [[Error Local Truncamiento vs Error Global Acumulado]] |
> | Estabilidad | ¿qué pasos $h$ son seguros? | [[Regiones Estabilidad Absoluta A Estabilidad]] |
> | Costo | ¿cuántas evaluaciones de $f$ por paso? | [[Construccion General Etapas s y Orden p]] |
> | Conservación | ¿preserva energía/momento? | [[Integradores Simplecticos Conservacion]] |

---

## Resumen

| Tema | Nota |
|:---|:---|
| Existencia y unicidad | [[Teoremas Existencia Unicidad Picard Lindelof]] |
| Métodos de Euler y Taylor | [[Metodos Taylor Euler/index]] |
| Métodos de Runge-Kutta | [[Metodos Runge Kutta/index]] |
| Sistemas, orden superior, conservación | [[Sistemas EDO y Orden Superior/index]] |
| Rigidez | [[Rigidez Stiffness Problemas Ingenieria]] |

> [!corolario]
> El problema de valor inicial integra una EDO desde un estado conocido hacia adelante en el tiempo: es la simulación dinámica de sistemas físicos. Tras asegurar [[Teoremas Existencia Unicidad Picard Lindelof|existencia y unicidad]], se aplican métodos de un paso —[[Metodos Taylor Euler/index|Euler/Taylor]] y sobre todo [[Metodos Runge Kutta/index|Runge-Kutta]]— juzgados por su orden, [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]] y costo. Los sistemas físicos de orden superior se reducen a [[Sistemas EDO y Orden Superior/index|sistemas de primer orden]], y los casos [[Rigidez Stiffness Problemas Ingenieria|rígidos]] o [[Integradores Simplecticos Conservacion|conservativos]] exigen métodos especializados.
