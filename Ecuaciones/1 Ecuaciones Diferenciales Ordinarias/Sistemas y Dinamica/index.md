---
title: Sistemas y Dinámica
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - index
draft: false
aliases:
  - sistemas de EDO
  - sistemas dinámicos
  - plano de fase
  - systems of ODEs
---

# Sistemas y Dinámica

> [!definicion]
> Un **sistema de EDO** acopla varias funciones incógnitas. En forma normal de primer orden,
> $$\dot{\mathbf{x}}=\mathbf{f}(t,\mathbf{x}),\qquad \mathbf{x}=(x_1,\dots,x_n)^{\!\top}.$$
> El caso **lineal** $\dot{\mathbf{x}}=A\mathbf{x}$ (con $A$ matriz) se resuelve con **álgebra
> lineal**: autovalores y autovectores de $A$. El estudio **cualitativo** —el **plano de fase**:
> equilibrios, estabilidad, retratos— describe el comportamiento aun cuando no haya fórmula.

> [!info]
> Cuarto bloque del [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Generaliza las
> [[Lineales de Orden Superior/index| lineales de orden superior]] (toda EDO de orden $n$ **es** un
> sistema de $n$ ecuaciones de primer orden) y es la antesala de la teoría de
> [[Estabilidad de Lyapunov| estabilidad]] y del caos. La [[Exponencial de una Matriz| exponencial de matriz]] $e^{At}$ es el análogo vectorial del factor $e^{rt}$ escalar.

---

## Por qué todo se reduce a un sistema de primer orden

> [!teoria]
> Cualquier EDO de orden $n$, $y^{(n)}=g(t,y,\dots,y^{(n-1)})$, se vuelve un **sistema de primer
> orden** nombrando las derivadas como nuevas variables: $x_1=y,\ x_2=y',\ \dots,\ x_n=y^{(n-1)}$,
> de modo que
> $$\dot x_1=x_2,\quad \dot x_2=x_3,\quad\dots,\quad \dot x_n=g(t,x_1,\dots,x_n).$$
> Por eso el lenguaje de sistemas es el **marco universal**: en él caben las ecuaciones de orden
> superior, los modelos con varias cantidades acopladas (depredador-presa, circuitos con varias
> mallas, reacciones químicas) y la mecánica ($\dot q=\partial H/\partial p,\ \dot p=-\partial
> H/\partial q$). Y el [[Existencia y Unicidad Picard| teorema de Picard]] se enuncia directamente para el sistema $\dot{\mathbf{x}}=\mathbf{f}(t,\mathbf{x})$.

> [!teoria] Las dos mitades del bloque
> 1. **Sistemas lineales** $\dot{\mathbf{x}}=A\mathbf{x}$: se resuelven **exactamente**. Probando
>    $\mathbf{x}=\mathbf{v}\,e^{\lambda t}$ aparece el problema de autovalores
>    $(A-\lambda I)\mathbf{v}=\mathbf{0}$ ([[Sistemas Lineales Autovalores| autovalores]]); la
>    solución general se empaqueta en la [[Matriz Fundamental| matriz fundamental]] o en
>    [[Exponencial de una Matriz| $e^{At}$]], y la fuente se vence con
>    [[Variacion de Parametros Sistemas| variación de parámetros]].
> 2. **Análisis cualitativo**: el [[Puntos de Equilibrio y Plano de Fase| plano de fase]] clasifica
>    los **equilibrios** (nodo, foco, centro, silla) por los autovalores; la
>    [[Estabilidad de Lyapunov| estabilidad de Lyapunov]] y la
>    [[Linealizacion y Hartman-Grobman| linealización]] extienden el retrato a sistemas **no
>    lineales** cerca de sus equilibrios; [[Ciclos Limite y Poincare-Bendixson| Poincaré-Bendixson]]
>    gobierna lo que puede pasar en el plano (ciclos límite).

---

## Mapa del bloque

> [!info]
> | Nota | Aporte |
> |---|---|
> | [[Forma Matricial y Eliminacion\|Forma Matricial y Eliminación]] | escribir $\dot{\mathbf{x}}=A\mathbf{x}$; reducir un sistema a una sola EDO |
> | [[Matriz Fundamental\|Matriz Fundamental]] | columnas = soluciones independientes; wronskiano matricial |
> | [[Sistemas Lineales Autovalores\|Sistemas Lineales por Autovalores]] | $\mathbf{x}=\mathbf{v}e^{\lambda t}$; casos real/complejo/repetido |
> | [[Exponencial de una Matriz\|Exponencial de una Matriz]] | $e^{At}$; $\mathbf{x}=e^{At}\mathbf{x}_0$; forma de Jordan |
> | [[Variacion de Parametros Sistemas\|Variación de Parámetros (sistemas)]] | sistema no homogéneo $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}$ |
> | [[Puntos de Equilibrio y Plano de Fase\|Puntos de Equilibrio y Plano de Fase]] | nodo, foco, centro, silla |
> | [[Estabilidad de Lyapunov\|Estabilidad de Lyapunov]] | estable / asintótico / inestable; función de Lyapunov |
> | [[Linealizacion y Hartman-Grobman\|Linealización y Hartman-Grobman]] | no lineal ≈ lineal cerca del equilibrio |
> | [[Ciclos Limite y Poincare-Bendixson\|Ciclos Límite y Poincaré-Bendixson]] | oscilaciones autosostenidas en 2D |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\dot{\mathbf{x}}=\mathbf{f}(t,\mathbf{x})$; lineal $\dot{\mathbf{x}}=A\mathbf{x}$ |
> | Solución lineal | autovalores de $A$; $\mathbf{x}=e^{At}\mathbf{x}_0$ |
> | Equilibrio | $\mathbf{f}(\mathbf{x}_*)=0$; tipo según autovalores |
> | Estabilidad | signo de las partes reales de los autovalores; [[Estabilidad de Lyapunov\|Lyapunov]] |
> | No lineal | [[Linealizacion y Hartman-Grobman\|linealizar]] cerca del equilibrio |

> [!corolario]
> Un sistema lineal **se resuelve** con el espectro de $A$: cada autovalor dicta un modo
> $e^{\lambda t}$ (decaimiento/crecimiento por la parte real, rotación por la imaginaria), igual que
> las raíces características en una sola ecuación. Y cuando no hay fórmula —el caso no lineal—, el
> **plano de fase** sigue contando la historia: hacia qué equilibrios va el sistema y si son estables.

> [!referencia]
> - El método de cálculo: [[Sistemas Lineales Autovalores]].
> - La imagen cualitativa: [[Puntos de Equilibrio y Plano de Fase]].
> - De dónde viene todo: [[Concepto General de ODE]].
