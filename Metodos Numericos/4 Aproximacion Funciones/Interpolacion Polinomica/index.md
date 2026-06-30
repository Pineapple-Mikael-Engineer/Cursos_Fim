---
title: Interpolación Polinómica
order: 1
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - index
draft: false
aliases:
  - Interpolación polinómica
  - Polynomial interpolation
---

# Interpolación Polinómica

> [!definicion]
> Dados $n+1$ nodos distintos $x_0, x_1, \dots, x_n$ con valores $y_i = f(x_i)$, el **polinomio interpolador** es el único polinomio $p_n$ de grado $\leq n$ tal que
> $$p_n(x_i) = y_i, \qquad i = 0, 1, \dots, n.$$

> [!info]
> El polinomio interpolador **existe y es único** (sea cual sea la base usada para construirlo). Las distintas formulaciones —[[Lagrange/index|Lagrange]], [[Newton Diferencias Divididas/index|Newton con diferencias divididas]], Vandermonde— producen el *mismo* polinomio, pero difieren en costo y estabilidad.

---

## Existencia, unicidad y representación

> [!info]
> El teorema de [[Existencia Unicidad Polinomio Interpolador|existencia y unicidad]] garantiza que el problema está bien planteado. La construcción directa por la [[Matriz Vandermonde Mal Condicionamiento|matriz de Vandermonde]] es teóricamente válida pero numéricamente peligrosa, lo que motiva las bases de Lagrange y Newton.

## Las dos bases prácticas

> [!info]
> - **[[Lagrange/index|Base de Lagrange]]:** explícita, sin resolver sistemas; ideal para teoría y para deducir fórmulas de [[Integracion Numerica Newton Cotes/index|cuadratura]].
> - **[[Newton Diferencias Divididas/index|Base de Newton]]:** incremental (añadir un nodo cuesta $O(n)$), evaluación eficiente por [[Forma Anidada y Eficiencia Algoritmo Horner|Horner]], y da acceso directo al [[Error Interpolacion Formula Cauchy|error]].

## El límite de la interpolación polinómica

> [!warning]
> Aumentar el grado **no** garantiza mejor aproximación: con nodos equiespaciados aparece el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]] (oscilaciones crecientes en los extremos). La solución es usar nodos de Chebyshev o cambiar a [[Interpolacion Tramos Splines/index|splines]].

---

## Ejemplo

> [!ejemplo]
> **Interpolar $(0,1), (1,2), (2,5)$ con $p_2$.** Las tres bases dan el mismo polinomio $p_2(x) = x^2 + 1$:
>
> | Base | Construcción |
> |:---|:---|
> | Vandermonde | resolver $\begin{psmallmatrix}1&0&0\\1&1&1\\1&2&4\end{psmallmatrix}c = \begin{psmallmatrix}1\\2\\5\end{psmallmatrix}$ → $c = (1,0,1)$ |
> | Lagrange | $1\cdot L_0 + 2\cdot L_1 + 5\cdot L_2$ |
> | Newton | $1 + 1\cdot(x-0) + 1\cdot(x-0)(x-1)$ |
>
> Verificación: $p_2(0)=1$, $p_2(1)=2$, $p_2(2)=5$. ✓

---

## Resumen

| Tema | Nota |
|:---|:---|
| Existencia y unicidad | [[Existencia Unicidad Polinomio Interpolador]] |
| Construcción directa y su mal condicionamiento | [[Matriz Vandermonde Mal Condicionamiento]] |
| Base de Lagrange | [[Lagrange/index]] |
| Base de Newton (diferencias divididas) | [[Newton Diferencias Divididas/index]] |
| Límite: oscilación y nodos óptimos | [[Fenomeno Runge y Nodos Chebyshev]] |

> [!corolario]
> La interpolación polinómica produce el único polinomio de grado $\leq n$ que pasa por $n+1$ datos; su [[Existencia Unicidad Polinomio Interpolador|existencia y unicidad]] no dependen de la base, pero la construcción sí: la [[Matriz Vandermonde Mal Condicionamiento|vía Vandermonde]] es inestable, y las bases de [[Lagrange/index|Lagrange]] y [[Newton Diferencias Divididas/index|Newton]] la reemplazan por su claridad y eficiencia. La interpolación de grado alto sobre nodos equiespaciados sufre el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]], razón por la que en la práctica se prefieren [[Interpolacion Tramos Splines/index|splines]] o nodos de Chebyshev.
