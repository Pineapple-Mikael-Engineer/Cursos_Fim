---
title: Determinantes y Matrices
order: 7
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - index
draft: false
aliases:
  - determinantes y matrices
  - capitulo 6 tensorial
  - algebra matricial
  - determinants and matrices
---

# Determinantes y Matrices

> [!definicion]
> Una **matriz** $\mathsf{A}$ es un arreglo $m\times n$ de elementos $a_{ij}$ ($i$ fila, $j$ columna) que representa un **operador lineal** (rotaciones, transformaciones). Su **determinante** $|\mathsf{A}|$ es el escalar
> $$|\mathsf{A}|=\sum_{i,j,k\dots}\varepsilon_{ijk\dots}\,a_{1i}a_{2j}a_{3k}\dots,$$
> que decide la existencia de inversa ($|\mathsf{A}|\neq0$) y de solución de sistemas lineales.

> [!info]
> Es el **capítulo 6** del libro (Rogan & Muñoz, Parte I; basado en Arfken & Weber cap. 3). Da el soporte algebraico de las [[Introduccion a Tensores/Transformaciones entre Sistemas/index | transformaciones]] (que son matrices) y de la [[Introduccion a Tensores/Diagonalizacion de Tensores/index | diagonalización de tensores]]. Se desglosa en:
> - [[Determinantes]] — definición, propiedades, regla de Cramer, Gauss (cap. 6.1).
> - [[Matrices/index | Matrices]] — operaciones, traza, inversa (cap. 6.2).
> - [[Matrices Ortogonales]] — $\tilde{\mathsf{A}}\mathsf{A}=1$, rotaciones (cap. 6.3).
> - [[Matrices Hermiticas y Unitarias]] — $\mathsf{A}^\dagger=\mathsf{A}$, $\mathsf{U}^\dagger\mathsf{U}=1$ (cap. 6.4).
> - [[Diagonalizacion de Matrices]] — semejanza, autovalores (cap. 6.5).
> - [[Matrices Normales]] — $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$ (cap. 6.6).

---

## Ejemplo

> [!ejemplo]
> **Una matriz es un operador, su determinante un número.** La rotación de coordenadas en 2D
> $$\begin{pmatrix}x'_1\\x'_2\end{pmatrix}=\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi\\-\operatorname{sen}\varphi&\cos\varphi\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}$$
> es una **matriz** $\mathsf{A}$ que actúa sobre el vector. Su **determinante** vale
> $$|\mathsf{A}|=\cos^2\varphi-(-\operatorname{sen}^2\varphi)=\cos^2\varphi+\operatorname{sen}^2\varphi=1,$$
> lo que expresa que la rotación **conserva áreas** (y es invertible). Composición de dos rotaciones = producto de matrices; deshacer una rotación = matriz inversa. Toda la geometría de las transformaciones se vuelve álgebra de matrices.

---

## En qué consiste

> [!teoria]
> El capítulo distingue dos objetos que a menudo se confunden:
> - El **determinante** $|\mathsf{A}|$ es **un número** (combinación lineal de productos de elementos, con signos de Levi-Civita). Sus elementos *sí* se combinan entre sí.
> - La **matriz** $\mathsf{A}$ es **un arreglo** de números que representa un operador; sus elementos $a_{ij}$ **no** se combinan entre sí hasta que se opera con ella.
>
> Las matrices forman un **anillo** (suma y producto, pero el producto no es conmutativo: $\mathsf{A}\mathsf{B}\neq\mathsf{B}\mathsf{A}$). Las clases especiales —ortogonales, hermíticas, unitarias, normales— se definen por su relación con la **transpuesta** $\tilde{\mathsf{A}}$ o la **adjunta** $\mathsf{A}^\dagger$, y son justamente las que aparecen en física (rotaciones, observables cuánticos, simetrías).

> [!info] Clases de matrices del capítulo
> | Clase | Definición | Aparece en |
> |---|---|---|
> | Ortogonal | $\tilde{\mathsf{A}}\mathsf{A}=1$ ($\tilde{\mathsf{A}}=\mathsf{A}^{-1}$) | rotaciones reales |
> | Hermítica | $\mathsf{A}^\dagger=\mathsf{A}$ | observables cuánticos |
> | Unitaria | $\mathsf{U}^\dagger\mathsf{U}=1$ | evolución cuántica |
> | Normal | $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$ | diagonalizables |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Determinantes]] | $\|\mathsf{A}\|$, propiedades, Cramer, Gauss |
> | [[Matrices/index]] | operaciones, traza, inversa |
> | [[Matrices Ortogonales]] | $\tilde{\mathsf{A}}\mathsf{A}=1$ |
> | [[Matrices Hermiticas y Unitarias]] | $\mathsf{A}^\dagger=\mathsf{A}$, $\mathsf{U}^\dagger\mathsf{U}=1$ |
> | [[Diagonalizacion de Matrices]] | semejanza, autovalores |
> | [[Matrices Normales]] | $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$ |

> [!corolario]
> Determinantes y matrices son la maquinaria de cálculo de todo el curso: las transformaciones tensoriales son matrices, la condición de tensor se verifica con ellas y la diagonalización (ejes principales) es un problema de autovalores matricial. El determinante decide la invertibilidad; la traza es un invariante; y las clases ortogonal/hermítica/unitaria capturan las simetrías de la física.

> [!referencia]
> - Operaciones y notación de índices: [[1 Algebra Lineal y Notacion/Algebra Lineal para Tensores]].
> - Diagonalización de tensores (versión geométrica): [[Introduccion a Tensores/Diagonalizacion de Tensores/index]].
> - Matrices de transformación: [[Introduccion a Tensores/Transformaciones entre Sistemas/Matriz de Transformacion]].
