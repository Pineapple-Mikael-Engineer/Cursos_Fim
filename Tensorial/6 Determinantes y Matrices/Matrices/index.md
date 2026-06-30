---
title: Matrices
order: 2
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - index
draft: false
aliases:
  - matriz
  - algebra de matrices
  - traza
  - matrices
---

# Matrices $\mathsf{A}$

> [!definicion]
> Una **matriz** $\mathsf{A}$ es un arreglo rectangular $m\times n$ de elementos $a_{ij}$ ($i$ = fila, $j$ = columna),
> $$\mathsf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},$$
> que representa un **operador lineal** (rotaciones, transformaciones) por sus efectos sobre vectores o bases. A diferencia de un determinante, sus elementos $a_{ij}$ **no se combinan entre sí**: una matriz es un arreglo ordenado, no un número.

> [!info]
> Sección **6.2** del [[../index | capítulo 6]] (Rogan & Muñoz). El álgebra matricial pertenece al álgebra lineal: las matrices son los mapas lineales del curso (transformaciones de coordenadas, diagonalización de tensores). Se desglosa en:
> - [[Operaciones Basicas]] — suma, producto por escalar, producto matricial (no conmutativo), transpuesta, unidad.
> - [[Matriz Inversa]] — $\mathsf{A}\mathsf{A}^{-1}=\mathsf{1}$, cofactores y Gauss-Jordan.
> - [[../Matrices Ortogonales]] — $\tilde{\mathsf{A}}\mathsf{A}=\mathsf{1}$ (rotaciones reales).
> - [[../Matrices Hermiticas y Unitarias]] — $\mathsf{A}^\dagger=\mathsf{A}$, $\mathsf{U}^\dagger\mathsf{U}=\mathsf{1}$.

---

## Ejemplo

> [!ejemplo]
> **Traza como invariante.** Para
> $$\mathsf{A}=\begin{pmatrix}2&5&0\\1&3&7\\4&0&-1\end{pmatrix},\qquad \operatorname{tr}(\mathsf{A})=a_{11}+a_{22}+a_{33}=2+3+(-1)=4.$$
> La traza solo mira la diagonal. Su utilidad es ser **invariante cíclico**: con
> $$\mathsf{B}=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad \mathsf{C}=\begin{pmatrix}0&1\\1&0\end{pmatrix},$$
> se tiene $\mathsf{B}\mathsf{C}=\begin{pmatrix}0&1\\2&0\end{pmatrix}$ y $\mathsf{C}\mathsf{B}=\begin{pmatrix}0&2\\1&0\end{pmatrix}$. Aunque $\mathsf{B}\mathsf{C}\neq\mathsf{C}\mathsf{B}$, ambas tienen diagonal nula y
> $$\operatorname{tr}(\mathsf{B}\mathsf{C})=0=\operatorname{tr}(\mathsf{C}\mathsf{B}).$$

---

## La traza

> [!definicion] Traza
> La **traza** de una matriz cuadrada es la suma de sus elementos diagonales,
> $$\operatorname{tr}(\mathsf{A})=\sum_i a_{ii}.$$

> [!proposicion] Propiedades de la traza
> 1. **Lineal:** $\operatorname{tr}(\mathsf{A}\pm\mathsf{B})=\operatorname{tr}(\mathsf{A})\pm\operatorname{tr}(\mathsf{B})$ y $\operatorname{tr}(\alpha\mathsf{A})=\alpha\operatorname{tr}(\mathsf{A})$.
> 2. **Cíclica:** $\operatorname{tr}(\mathsf{A}\mathsf{B})=\operatorname{tr}(\mathsf{B}\mathsf{A})$, aun cuando $\mathsf{A}\mathsf{B}\neq\mathsf{B}\mathsf{A}$.
> 3. **Triple cíclica:** $\operatorname{tr}(\mathsf{A}\mathsf{B}\mathsf{C})=\operatorname{tr}(\mathsf{B}\mathsf{C}\mathsf{A})=\operatorname{tr}(\mathsf{C}\mathsf{A}\mathsf{B})$ (rotación de los factores, **no** permutación arbitraria).
> 4. **Conmutador:** $\operatorname{tr}([\mathsf{A},\mathsf{B}])=\operatorname{tr}(\mathsf{A}\mathsf{B}-\mathsf{B}\mathsf{A})=0$.

> [!demostracion] Propiedad cíclica $\operatorname{tr}(\mathsf{A}\mathsf{B})=\operatorname{tr}(\mathsf{B}\mathsf{A})$
> **Paso 1.** Por definición de traza y de producto matricial,
> $$\operatorname{tr}(\mathsf{A}\mathsf{B})=\sum_i(\mathsf{A}\mathsf{B})_{ii}=\sum_i\sum_j a_{ij}b_{ji}.$$
> **Paso 2.** Como son sumas de escalares, se conmutan los factores y se reordenan las sumas:
> $$\sum_i\sum_j a_{ij}b_{ji}=\sum_i\sum_j b_{ji}a_{ij}=\sum_j\sum_i b_{ji}a_{ij}.$$
> **Paso 3.** La suma interna $\sum_i b_{ji}a_{ij}=(\mathsf{B}\mathsf{A})_{jj}$, de modo que
> $$\operatorname{tr}(\mathsf{A}\mathsf{B})=\sum_j(\mathsf{B}\mathsf{A})_{jj}=\operatorname{tr}(\mathsf{B}\mathsf{A}).\qquad\blacksquare$$
> Iterando con $\mathsf{A}\to\mathsf{A}\mathsf{B}$, $\mathsf{B}\to\mathsf{C}$ se obtiene la versión triple.

> [!info] Significado físico
> Para una matriz simétrica o hermítica, la traza es la **suma de los autovalores** y el determinante su **producto**; ambos son coeficientes del polinomio característico. En lenguaje tensorial la traza es la **contracción** de un tensor de segundo orden: un escalar invariante. En teoría de grupos, $\operatorname{tr}$ de una representación es el **carácter**, invariante por cambio de base.

---

## En qué consiste

> [!teoria]
> Una matriz $\mathsf{A}$ es la representación, **dependiente de la base**, de un operador lineal. El caso $n\times 1$ es un vector columna $|x\rangle$ y el $1\times n$ un vector fila $\langle x|$; el producto $\langle x|y\rangle$ recupera el producto escalar. Las matrices $m\times n$, con la suma y el producto, forman un **anillo**: hay estructura aditiva (grupo conmutativo) y multiplicativa, pero el producto **no es conmutativo** y puede ser un divisor de cero ($\mathsf{A}\mathsf{B}=\mathsf{0}$ con $\mathsf{A},\mathsf{B}\neq\mathsf{0}$), por lo que no llegan a formar un **cuerpo**. Las clases especiales (ortogonal, hermítica, unitaria, normal) se definen por la relación de $\mathsf{A}$ con su transpuesta $\tilde{\mathsf{A}}$ o su adjunta $\mathsf{A}^\dagger$.

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |---|---|
> | Matriz | arreglo $m\times n$ de $a_{ij}$; operador lineal, no $\|\mathsf{A}\|$ |
> | Estructura | las $m\times n$ forman un **anillo** (producto no conmutativo) |
> | Traza | $\operatorname{tr}(\mathsf{A})=\sum_i a_{ii}$, lineal |
> | Ciclicidad | $\operatorname{tr}(\mathsf{A}\mathsf{B})=\operatorname{tr}(\mathsf{B}\mathsf{A})$; $\operatorname{tr}([\mathsf{A},\mathsf{B}])=0$ |
> | Invariancia | traza = suma de autovalores = carácter del grupo |

> [!corolario]
> Una matriz no es un determinante: es el arreglo que representa un operador, y solo cobra vida al operar (sumar, multiplicar, invertir). El producto no conmuta —de ahí el conmutador y toda la física cuántica—, pero la **traza** sobrevive a ese desorden: invariante cíclico, suma de autovalores, contracción tensorial y carácter de grupo.

> [!referencia]
> - Cómo se opera con ellas: [[Operaciones Basicas]].
> - Cuándo y cómo se invierten: [[Matriz Inversa]].
> - El número asociado: [[../Determinantes]].
