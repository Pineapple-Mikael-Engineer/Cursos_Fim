---
title: Sistemas de Ecuaciones No Lineales
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - index
draft: false
aliases:
  - Sistemas no lineales
  - Nonlinear systems
  - Ecuaciones no lineales multivariable
---

# Sistemas de Ecuaciones No Lineales

> [!definicion]
> Un **sistema de ecuaciones no lineales** busca $x \in \mathbb{R}^n$ tal que
> $$F(x) = 0, \qquad F: \mathbb{R}^n \to \mathbb{R}^n, \quad F = (f_1, \dots, f_n)^T,$$
> donde al menos una componente $f_i$ es no lineal. Generaliza el problema escalar $f(x) = 0$ a varias variables acopladas.

> [!info]
> A diferencia del caso de [[Sistemas Lineales/index|sistemas lineales]] $Ax = b$, no hay método directo: se resuelve iterando. Las dos familias son el [[Newton Raphson Multivariable/index|método de Newton multivariable]] (rápido, basado en linealización) y las [[Condicion Contraccion Norma Matricial|iteraciones de punto fijo]] (más simples, convergencia bajo contracción).

---

## Newton multivariable

> [!info]
> Extiende [[Newton Raphson/index|Newton escalar]] sustituyendo la derivada por la [[Matriz Jacobiana y Sistema Lineal Asociado|matriz jacobiana]] $J(x)$. Cada paso resuelve un sistema **lineal** $J(x^{(k)})\,\Delta x = -F(x^{(k)})$. Conserva la [[Convergencia Local Cuadratica|convergencia cuadrática]] local, a cambio de evaluar y factorizar $J$ en cada iteración ([[Costo Computacional Evaluacion Jacobiano|costo]]). Se desarrolla en [[Newton Raphson Multivariable/index]].

## Iteración de punto fijo multivariable

> [!info]
> Reescribe $F(x) = 0$ como $x = G(x)$ e itera $x^{(k+1)} = G(x^{(k)})$. Converge si $G$ es una **contracción** en una norma, condición que generaliza $|g'(r)| < 1$ del caso escalar mediante la norma de la jacobiana de $G$. Se trata en [[Condicion Contraccion Norma Matricial]].

---

## Ejemplo

> [!ejemplo]
> **Intersección de una circunferencia y una parábola.**
> $$F(x, y) = \begin{pmatrix} x^2 + y^2 - 4 \\ y - x^2 \end{pmatrix} = 0.$$
> Solución en el primer cuadrante: $x^2 = y$ y $y^2 + y - 4 = 0 \Rightarrow y = \frac{-1+\sqrt{17}}{2} \approx 1.5616$, $x \approx 1.2496$.
>
> Newton desde $(x_0, y_0) = (1, 1)$, con jacobiana $J = \begin{pmatrix} 2x & 2y \\ -2x & 1 \end{pmatrix}$:
>
> | $k$ | $x^{(k)}$ | $y^{(k)}$ | $\|F\|_2$ |
> |:---:|:---:|:---:|:---:|
> | 0 | 1.0000 | 1.0000 | 2.236 |
> | 1 | 1.3000 | 1.6000 | 0.250 |
> | 2 | 1.2503 | 1.5628 | $7.3\text{e-}3$ |
> | 3 | 1.2496 | 1.5616 | $4.1\text{e-}6$ |
> | 4 | 1.2496 | 1.5616 | $<10^{-12}$ |
>
> La norma del residuo decae cuadráticamente: convergencia típica de Newton multivariable cerca de la solución.

---

## La jerarquía escalar se conserva

> [!info]
> | Problema escalar | Análogo multivariable |
> |:---|:---|
> | $f(x) = 0$ | $F(x) = 0$ |
> | derivada $f'(x)$ | [[Matriz Jacobiana y Sistema Lineal Asociado\|jacobiana]] $J(x)$ |
> | Newton $x - f/f'$ | $x - J^{-1}F$ (resolver sistema lineal) |
> | $|g'(r)| < 1$ | $\|J_G\| < 1$ ([[Condicion Contraccion Norma Matricial\|contracción]]) |
> | orden cuadrático | [[Convergencia Local Cuadratica\|orden cuadrático]] |

---

## Resumen

| Tema | Nota |
|:---|:---|
| Linealización y sistema lineal por paso | [[Matriz Jacobiana y Sistema Lineal Asociado]] |
| Newton multivariable (panorama) | [[Newton Raphson Multivariable/index]] |
| Orden de convergencia | [[Convergencia Local Cuadratica]] |
| Costo de evaluar/factorizar $J$ | [[Costo Computacional Evaluacion Jacobiano]] |
| Punto fijo y contracción | [[Condicion Contraccion Norma Matricial]] |

> [!corolario]
> Los sistemas no lineales $F(x) = 0$ se resuelven iterando, sin análogo a la eliminación directa de los sistemas lineales. El método de [[Newton Raphson Multivariable/index|Newton multivariable]] linealiza con la [[Matriz Jacobiana y Sistema Lineal Asociado|jacobiana]] y hereda la [[Convergencia Local Cuadratica|convergencia cuadrática]] del caso escalar, al precio de resolver un sistema lineal por paso; las [[Condicion Contraccion Norma Matricial|iteraciones de punto fijo]] ofrecen una alternativa más barata bajo condición de contracción. Toda la jerarquía de órdenes del caso de una variable se traslada, con la derivada reemplazada por la jacobiana.
