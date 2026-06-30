---
title: Ecuaciones Normales y Matriz de Gram
order: 2
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - minimos-cuadrados
  - algebra-lineal-numerica
draft: false
aliases:
  - Ecuaciones normales
  - Matriz de Gram
  - Normal equations
  - Gram matrix
---

# Ecuaciones Normales y Matriz de Gram

> [!definicion]
> Las **ecuaciones normales** del problema de [[Formulacion Residuos y Norma Euclidea|mínimos cuadrados]] $\min_c\|Ac-y\|_2^2$ son el sistema lineal cuadrado
> $$A^TA\,c = A^Ty,$$
> donde $G = A^TA \in \mathbb{R}^{n\times n}$ es la **matriz de Gram** de las columnas de $A$, con entradas $G_{jk} = \varphi_j^T\varphi_k = \sum_i \varphi_j(x_i)\varphi_k(x_i)$.

> [!info]
> Las ecuaciones normales convierten un sistema sobredeterminado $m\times n$ en uno cuadrado $n\times n$, resoluble por [[Factorizacion Cholesky Matrices Definidas Positivas|Cholesky]] (la matriz de Gram es simétrica definida positiva si $A$ tiene rango completo). Son elegantes, pero su [[Condicionamiento Ecuaciones Normales|condicionamiento]] obliga a usarlas con cautela.

---

## Propiedades de la matriz de Gram

> [!proposicion]
> Sea $G = A^TA$ con $A \in \mathbb{R}^{m\times n}$, $m \geq n$:
> 1. **Simétrica:** $G^T = (A^TA)^T = A^TA = G$.
> 2. **Semidefinida positiva:** $c^TGc = \|Ac\|_2^2 \geq 0$.
> 3. **Definida positiva** $\Leftrightarrow$ $A$ tiene **rango completo** ($n$ columnas linealmente independientes).
> 4. **No singular** $\Leftrightarrow$ rango$(A) = n$, en cuyo caso la solución $c = G^{-1}A^Ty$ es única.

> [!demostracion]
> **Propiedad 3.** $c^TGc = \|Ac\|^2 = 0 \Leftrightarrow Ac = 0$. Si $A$ tiene rango completo, $Ac = 0 \Rightarrow c = 0$, luego $G$ es definida positiva. Si $A$ tiene rango deficiente, existe $c\neq0$ con $Ac=0$ y $G$ es solo semidefinida (singular).

---

## Derivación

> [!teorema]
> El minimizador de $\|Ac - y\|_2^2$ satisface las ecuaciones normales. Equivalentemente, la matriz de Gram codifica los productos internos de las funciones base y el lado derecho $A^Ty$ los productos con los datos.

> [!demostracion]
> Del [[Formulacion Residuos y Norma Euclidea|gradiente nulo]] $\nabla J(c) = 2A^TAc - 2A^Ty = 0$ se sigue $A^TAc = A^Ty$. La interpretación: la fila $j$ del sistema es $\varphi_j^T(Ac) = \varphi_j^T y$, es decir, la proyección del residuo sobre cada función base $\varphi_j$ es nula. Cada ecuación impone ortogonalidad del residuo a una dirección del modelo.

---

## Ejemplo

> [!ejemplo]
> **Recta a $(1,1),(2,2),(3,2),(4,3)$.** Con $A = \begin{psmallmatrix}1&1\\1&2\\1&3\\1&4\end{psmallmatrix}$, $y=(1,2,2,3)^T$:
> $$G = A^TA = \begin{pmatrix} 4 & 10 \\ 10 & 30 \end{pmatrix}, \qquad A^Ty = \begin{pmatrix} 8 \\ 23 \end{pmatrix}.$$
> Ecuaciones normales:
> $$\begin{pmatrix} 4 & 10 \\ 10 & 30 \end{pmatrix}\begin{pmatrix} c_0 \\ c_1 \end{pmatrix} = \begin{pmatrix} 8 \\ 23 \end{pmatrix} \;\Rightarrow\; c_0 = 0.5,\ c_1 = 0.6.$$
> La recta de ajuste es $y = 0.5 + 0.6x$, coherente con la [[Formulacion Residuos y Norma Euclidea|formulación]].

---

## Resolución por Cholesky

> [!algoritmo]
> **Mínimos cuadrados por ecuaciones normales.**
>
> ```
> 1. Formar G = AᵀA            (O(mn²))
> 2. Formar b = Aᵀy            (O(mn))
> 3. Cholesky G = LLᵀ          (O(n³/3), G simétrica definida positiva)
> 4. Resolver L z = b          (sustitución directa)
> 5. Resolver Lᵀ c = z         (sustitución regresiva)
> ```
>
> Costo total $\approx mn^2 + n^3/3$. Es el método más rápido, pero también el de **peor condicionamiento**.

> [!warning]
> Formar $G = A^TA$ **eleva al cuadrado** el número de condición: $\kappa_2(A^TA) = \kappa_2(A)^2$. Para $A$ mal condicionada, las ecuaciones normales pierden el doble de dígitos que un método basado en QR. El análisis y la alternativa están en [[Condicionamiento Ecuaciones Normales]].

---

## Relación con otras notas

> [!info]
> - El problema que estas ecuaciones resuelven: [[Formulacion Residuos y Norma Euclidea]].
> - La factorización que las resuelve: [[Factorizacion Cholesky Matrices Definidas Positivas]].
> - El peligro de su condicionamiento y la alternativa QR: [[Condicionamiento Ecuaciones Normales]].
> - Su aplicación a modelos concretos: [[Regresion Lineal Multiple y Polinomial]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Sistema | $A^TAc = A^Ty$ |
| Matriz de Gram | $G = A^TA$, $G_{jk} = \varphi_j^T\varphi_k$ |
| Propiedades | simétrica, SDP si rango completo |
| Resolución | Cholesky, $O(mn^2 + n^3/3)$ |
| Riesgo | $\kappa(A^TA) = \kappa(A)^2$ |

> [!corolario]
> Las ecuaciones normales $A^TAc = A^Ty$ reducen el problema sobredeterminado de mínimos cuadrados a un sistema cuadrado con la matriz de Gram $G = A^TA$, simétrica y definida positiva cuando $A$ tiene rango completo, lo que permite resolverlo eficientemente por [[Factorizacion Cholesky Matrices Definidas Positivas|Cholesky]]. Cada ecuación expresa la ortogonalidad del residuo a una función base. Su elegancia tiene un precio: formar $A^TA$ eleva al cuadrado el número de condición, defecto analizado en [[Condicionamiento Ecuaciones Normales]] que motiva la factorización QR como alternativa estable.
