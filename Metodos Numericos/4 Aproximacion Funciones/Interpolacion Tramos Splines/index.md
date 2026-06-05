---
title: Interpolación por Tramos (Splines)
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
  - index
draft: false
aliases:
  - Splines
  - Interpolación por tramos
  - Spline interpolation
---

# Interpolación por Tramos (Splines)

> [!definicion]
> Un **spline** de grado $m$ es una función definida a tramos por polinomios de grado $m$ sobre cada subintervalo $[x_i, x_{i+1}]$, empalmados con cierta continuidad ($C^{m-1}$ en los nodos internos). Interpola los datos $\{(x_i, y_i)\}$ usando muchos polinomios de **grado bajo** en lugar de uno de grado alto.

> [!info]
> Los splines evitan por construcción el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]: al mantener el grado bajo (típicamente $3$) y aumentar solo el número de tramos, la aproximación converge de forma estable. Son el estándar para interpolar muchos puntos, en gráficos por computadora (curvas de Bézier/B-splines) y en CAD.

---

## Jerarquía por suavidad

> [!info]
> - **[[Splines Lineales Continuidad C0|Splines lineales]] ($C^0$):** rectas que unen puntos consecutivos. Continuos pero con esquinas; convergencia $O(h^2)$.
> - **[[Splines Cubicos Naturales Sujetos|Splines cúbicos]] ($C^2$):** cúbicas por tramo con primera y segunda derivada continuas. Suaves, sin oscilación; convergencia $O(h^4)$.

## Construcción de splines cúbicos

> [!info]
> El acoplamiento de las condiciones de continuidad $C^2$ produce un [[Condiciones Continuidad C2 y Sistema Tridiagonal|sistema tridiagonal]] para las segundas derivadas en los nodos, resoluble en $O(n)$. La elección de condiciones de frontera (natural, sujeto) cierra el sistema.

## Por qué splines y no polinomios

> [!info]
> El spline cúbico es, entre todas las interpolantes $C^2$, el de **[[Propiedad Minima Curvatura|mínima curvatura]]** (energía de flexión mínima), de donde su nombre y suavidad. Su [[Convergencia y Estabilidad vs Polinomios Grado Alto|convergencia estable]] contrasta con la divergencia de los polinomios de grado alto.

---

## Ejemplo

> [!ejemplo]
> **Cuatro puntos $(0,0), (1,1), (2,0), (3,1)$.**
>
> | Interpolante | Comportamiento |
> |:---|:---|
> | Polinomio único $p_3$ | una cúbica global, puede oscilar al añadir puntos |
> | Spline lineal | tres segmentos rectos, con esquinas en $x=1,2$ |
> | Spline cúbico natural | curva suave $C^2$ con $S''=0$ en los extremos |
>
> Al refinar (más puntos), el spline cúbico mantiene la forma sin oscilar; el polinomio único degenera.

---

## Resumen

| Tema | Nota |
|:---|:---|
| Splines lineales $C^0$ | [[Splines Lineales Continuidad C0]] |
| Splines cúbicos (natural/sujeto) | [[Splines Cubicos Naturales Sujetos]] |
| Sistema tridiagonal de continuidad $C^2$ | [[Condiciones Continuidad C2 y Sistema Tridiagonal]] |
| Propiedad de mínima curvatura | [[Propiedad Minima Curvatura]] |
| Convergencia vs polinomios de grado alto | [[Convergencia y Estabilidad vs Polinomios Grado Alto]] |

> [!corolario]
> Los splines interpolan con polinomios de grado bajo empalmados con continuidad, sustituyendo el grado por el número de tramos y evitando así el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]. Los [[Splines Lineales Continuidad C0|lineales]] son simples pero angulosos ($O(h^2)$); los [[Splines Cubicos Naturales Sujetos|cúbicos]] son suaves ($C^2$, $O(h^4)$) y se construyen resolviendo un [[Condiciones Continuidad C2 y Sistema Tridiagonal|sistema tridiagonal]] en $O(n)$. Su [[Propiedad Minima Curvatura|mínima curvatura]] y su [[Convergencia y Estabilidad vs Polinomios Grado Alto|convergencia estable]] los hacen el método de referencia para interpolar muchos datos.
