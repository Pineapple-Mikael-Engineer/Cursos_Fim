---
title: Matriz de Vandermonde y Mal Condicionamiento
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - error-numerico
draft: false
aliases:
  - Matriz de Vandermonde
  - Vandermonde matrix
  - Mal condicionamiento de Vandermonde
---

# Matriz de Vandermonde y Mal Condicionamiento

> [!definicion]
> La **matriz de Vandermonde** asociada a los nodos $x_0, \dots, x_n$ surge al plantear la [[Existencia Unicidad Polinomio Interpolador|interpolación]] en la base de monomios $p(x) = \sum_{j=0}^n c_j x^j$:
> $$V = \begin{pmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^n \\ 1 & x_1 & x_1^2 & \cdots & x_1^n \\ \vdots & & & & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^n \end{pmatrix}, \qquad V c = y.$$

> [!info]
> Aunque $V$ es no singular para nodos distintos ($\det V = \prod_{i<j}(x_j - x_i)$), su [[Condicionamiento Numerico Numero Condicion|número de condición]] crece **exponencialmente** con $n$. Por eso, resolver $Vc = y$ es una mala forma de interpolar: motiva las bases de [[Lagrange/index|Lagrange]] y [[Newton Diferencias Divididas/index|Newton]].

---

## Determinante y no singularidad

> [!teorema]
> El determinante de Vandermonde es
> $$\det V = \prod_{0 \leq i < j \leq n} (x_j - x_i).$$
> Es no nulo si y solo si los nodos son distintos, garantizando solución única del sistema.

> [!demostracion]
> Considérese $\det V$ como polinomio en $x_n$ de grado $n$. Se anula cuando $x_n = x_i$ ($i<n$), pues dos filas coinciden; luego tiene factores $(x_n - x_i)$ para $i = 0,\dots,n-1$. El cociente es el determinante de Vandermonde de orden $n$ (en $x_0,\dots,x_{n-1}$), y por inducción se obtiene el producto completo. El coeficiente director es $1$.

---

## Mal condicionamiento

> [!teorema]
> Para nodos equiespaciados en $[0, 1]$ (o $[-1,1]$), el número de condición de la matriz de Vandermonde crece exponencialmente:
> $$\kappa_2(V) \sim O\!\big(2^n\big) \quad \text{(equiespaciados)},$$
> de modo que resolver $Vc = y$ pierde $\sim n\log_{10}2 \approx 0.3\,n$ dígitos por el solo hecho de plantearlo en monomios.

> [!ejemplo]
> **Crecimiento de $\kappa_2(V)$** con nodos equiespaciados en $[0,1]$:
>
> | $n$ | $\kappa_2(V)$ aprox. | dígitos perdidos |
> |:---:|:---:|:---:|
> | 5 | $\sim 10^{3}$ | 3 |
> | 10 | $\sim 10^{6}$ | 6 |
> | 15 | $\sim 10^{10}$ | 10 |
> | 20 | $\sim 10^{13}$ | 13 |
>
> Para $n \gtrsim 16$, en doble precisión los coeficientes $c_j$ calculados son ya basura, aunque el polinomio interpolador *exista y sea único*. El problema es la **base de monomios**, no la interpolación en sí.

---

## Por qué falla la base de monomios

> [!teoria]
> Los monomios $1, x, x^2, \dots, x^n$ se parecen cada vez más entre sí en $[0,1]$ (todos crecen monótonamente, casi colineales como vectores de función). La matriz $V$ tiene columnas casi linealmente dependientes, lo que dispara $\kappa_2(V)$. Es el mismo fenómeno que arruina las [[Condicionamiento Ecuaciones Normales|ecuaciones normales]] en mínimos cuadrados: una base mal acondicionada.

> [!info]
> **Remedios.** El interpolador es único, pero la *representación* importa:
>
> | Estrategia | Efecto sobre el condicionamiento |
> |:---|:---|
> | Base de [[Formulacion Polinomios Cardinales L i x\|Lagrange]] | evita resolver el sistema por completo |
> | Base de [[Tabla Diferencias Divididas y Coeficientes\|Newton]] | sistema triangular, bien condicionado |
> | Polinomios ortogonales (Chebyshev) | $\kappa$ acotado, base casi ortonormal |
> | [[Fenomeno Runge y Nodos Chebyshev\|Nodos de Chebyshev]] | reducen $\kappa(V)$ frente a equiespaciados |

---

## Comparación de costos

> [!info]
> | Método | Costo construcción | Estabilidad |
> |:---|:---|:---|
> | Vandermonde (resolver $Vc=y$) | $\frac{2}{3}n^3$ + mal condicionado | mala |
> | [[Lagrange/index\|Lagrange]] | $O(n^2)$ por evaluación | buena |
> | [[Newton Diferencias Divididas/index\|Newton]] | $O(n^2)$ coeficientes, $O(n)$ evaluación | buena |
>
> Vandermonde es además el **más caro** ($O(n^3)$) por requerir resolver un sistema denso, frente al $O(n^2)$ de las otras bases.

---

## Relación con otras notas

> [!info]
> - El planteamiento del sistema: [[Existencia Unicidad Polinomio Interpolador]].
> - La medida de la amplificación de error: [[Condicionamiento Numerico Numero Condicion]].
> - Las bases que lo evitan: [[Formulacion Polinomios Cardinales L i x]] y [[Tabla Diferencias Divididas y Coeficientes]].
> - El mismo fenómeno en mínimos cuadrados: [[Condicionamiento Ecuaciones Normales]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Matriz | $V_{ij} = x_i^{\,j}$ |
| Determinante | $\prod_{i<j}(x_j - x_i)$ |
| No singular | nodos distintos |
| $\kappa_2(V)$ | $\sim 2^n$ (equiespaciados) |
| Causa | base de monomios casi colineal |
| Remedio | Lagrange, Newton, Chebyshev |

> [!corolario]
> La matriz de Vandermonde formaliza la interpolación en la base de monomios y prueba la unicidad vía $\det V = \prod_{i<j}(x_j-x_i)$, pero su número de condición crece exponencialmente $\kappa_2(V)\sim 2^n$ con nodos equiespaciados, haciendo inútil resolver $Vc=y$ para $n$ moderado. El defecto está en la base —los monomios son casi colineales—, no en el problema de interpolación, que sigue bien planteado. Por eso se construye el mismo polinomio en las bases de [[Lagrange/index|Lagrange]] o [[Newton Diferencias Divididas/index|Newton]], estables y más baratas, y se prefieren [[Fenomeno Runge y Nodos Chebyshev|nodos de Chebyshev]].
