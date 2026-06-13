---
title: Determinantes
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - determinantes
draft: false
aliases:
  - determinante
  - regla de Cramer
  - eliminacion de Gauss
  - determinants
---

# Determinantes

> [!definicion]
> El **determinante** de orden $n$ es el escalar
> $$D_n=\sum_{i,j,k\dots}\varepsilon_{ijk\dots}\,a_{1i}a_{2j}a_{3k}\dots,$$
> con $\varepsilon$ el [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]] ($+1$ permutación par, $-1$ impar, $0$ índice repetido). Cada término es un producto de **un** elemento de cada fila y cada columna, con signo según la paridad de la permutación.

> [!info]
> Primera sección del [[index | capítulo 6]] (libro, cap. 6.1). Nace de la condición para que un sistema lineal tenga solución no trivial, y generaliza el **producto triple** $(\vec a\times\vec b)\cdot\vec c$. Su valor decide la [[Matrices/Matriz Inversa | invertibilidad]] de una matriz ($|\mathsf{A}|\neq0$).

---

## Ejemplo

> [!ejemplo]
> **Desarrollo por cofactores (Laplace).** El determinante de orden 3 se expande por una fila:
> $$D_3=\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}=a_1\begin{vmatrix}b_2&b_3\\c_2&c_3\end{vmatrix}-a_2\begin{vmatrix}b_1&b_3\\c_1&c_3\end{vmatrix}+a_3\begin{vmatrix}b_1&b_2\\c_1&c_2\end{vmatrix}=\sum_{j}a_j\,c_{1j}.$$
> El **cofactor** $c_{1j}=(-1)^{1+j}M_{1j}$ usa la **menor** $M_{1j}$ (el determinante que queda al borrar la fila 1 y la columna $j$). Es muy útil cuando hay muchos ceros: para
> $$D=\begin{vmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{vmatrix},$$
> expandiendo dos veces por la fila superior se llega a $D=\begin{vmatrix}0&1\\-1&0\end{vmatrix}=1$ (una de las matrices de Dirac).

> [!ejemplo]
> **Regla de Cramer.** Para $3x+2y+z=11$, $2x+3y+z=13$, $x+y+4z=12$, con $|\mathsf{A}|=18\neq0$, cada incógnita es un cociente de determinantes (reemplazando la columna correspondiente por el término independiente):
> $$x=\frac{1}{18}\begin{vmatrix}11&2&1\\13&3&1\\12&1&4\end{vmatrix}=1,\quad y=\frac{1}{18}\begin{vmatrix}3&11&1\\2&13&1\\1&12&4\end{vmatrix}=3,\quad z=\frac{1}{18}\begin{vmatrix}3&2&11\\2&3&13\\1&1&12\end{vmatrix}=2.$$

> [!ejemplo]
> **Eliminación de Gauss (mejor para cómputo).** El mismo sistema se triangulariza eliminando incógnitas:
> $$\begin{aligned}&3x+2y+z=11\\&2x+3y+z=13\\&x+y+4z=12\end{aligned}\ \xrightarrow{\text{elim. }x,y}\ \begin{aligned}&x+\tfrac23y+\tfrac13z=\tfrac{11}3\\&y+\tfrac15z=\tfrac{17}5\\&54z=108\end{aligned}\ \Rightarrow\ z=2,\ y=3,\ x=1.$$
> Una forma triangular requiere solo $n-1$ multiplicaciones (vs $n!$ términos del determinante), por eso es la elegida en computación.

---

## Propiedades

> [!proposicion] Propiedades del determinante
> Se siguen de la antisimetría de $\varepsilon_{ijk\dots}$:
> 1. **Antisimetría:** intercambiar dos filas (o columnas) cambia el signo.
> 2. **Filas/columnas iguales o proporcionales** $\Rightarrow$ determinante $0$.
> 3. **Fila o columna de ceros** $\Rightarrow$ determinante $0$.
> 4. **Multiplicar una fila por $k$** multiplica el determinante por $k$.
> 5. **Sumar a una fila un múltiplo de otra** no altera el determinante:
> $$\begin{vmatrix}a_1+ka_2&a_2&a_3\\b_1+kb_2&b_2&b_3\\c_1+kc_2&c_2&c_3\end{vmatrix}=\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}.$$
> 6. **Producto:** $|\mathsf{A}\mathsf{B}|=|\mathsf{A}|\,|\mathsf{B}|$.

> [!demostracion] Por qué la propiedad 5 no cambia el determinante
> Por linealidad en la primera columna, el determinante de la izquierda se separa en dos:
> $$\begin{vmatrix}a_1+ka_2&a_2&a_3\\ \vdots\end{vmatrix}=\begin{vmatrix}a_1&a_2&a_3\\ \vdots\end{vmatrix}+k\begin{vmatrix}a_2&a_2&a_3\\ \vdots\end{vmatrix}.$$
> El segundo determinante tiene la **primera y segunda columna iguales** ($a_2$), así que por la propiedad 2 vale **cero**. Queda solo el primero. $\blacksquare$ Esta es la base de la eliminación de Gauss.

> [!warning] El determinante es mal condicionado numéricamente
> Por los signos alternados puede haber **cancelaciones**: un determinante de elementos grandes puede dar un valor pequeño, con gran error relativo. Para sistemas grandes (200 incógnitas → $200!$ términos) la regla de Cramer es inviable; se usa **Gauss** o **Gauss-Jordan**.

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |---|---|
> | Definición | $D_n=\sum\varepsilon_{ijk\dots}a_{1i}a_{2j}a_{3k}\dots$ |
> | Cofactor | $c_{ij}=(-1)^{i+j}M_{ij}$; $D=\sum_j a_{ij}c_{ij}$ |
> | Cramer | $x_i=\dfrac{\|\mathsf{A}_i\|}{\|\mathsf{A}\|}$ (columna $i$ reemplazada) |
> | Antisimetría | swap filas $\to$ signo; filas iguales $\to 0$ |
> | Producto | $\|\mathsf{A}\mathsf{B}\|=\|\mathsf{A}\|\|\mathsf{B}\|$ |
> | Cómputo | Gauss (triangular), no Cramer |

> [!corolario]
> El determinante condensa en un número la información sobre la solubilidad de un sistema y la invertibilidad de una matriz. Se calcula por cofactores (a mano, aprovechando ceros) o por eliminación de Gauss (en máquina). Su antisimetría —heredada de $\varepsilon_{ijk}$— genera todas sus propiedades y es la razón de las cancelaciones que lo hacen delicado numéricamente.

> [!referencia]
> - El símbolo que lo define: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita]].
> - Inversa vía cofactores y Gauss-Jordan: [[Matrices/Matriz Inversa]].
> - Operaciones con matrices: [[Matrices/index]].
