---
title: Interpolación de Lagrange
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - lagrange
  - index
draft: false
aliases:
  - Interpolación de Lagrange
  - Lagrange interpolation
  - Forma de Lagrange
---

# Interpolación de Lagrange

> [!definicion]
> La **forma de Lagrange** del [[Existencia Unicidad Polinomio Interpolador|polinomio interpolador]] expresa $p_n$ como combinación de los **polinomios cardinales** $L_i$:
> $$p_n(x) = \sum_{i=0}^n y_i\, L_i(x), \qquad L_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j}.$$
> Cada $L_i$ vale $1$ en su nodo $x_i$ y $0$ en los demás: $L_i(x_k) = \delta_{ik}$.

> [!info]
> Su virtud es ser **explícita**: no requiere resolver ningún sistema lineal, a diferencia de [[Matriz Vandermonde Mal Condicionamiento|Vandermonde]]. Los coeficientes son directamente los valores $y_i$. Es la base preferida para deducir teoría y fórmulas de [[Integracion Numerica Newton Cotes/index|cuadratura]].

---

## Estructura: dos piezas

> [!info]
> - **[[Formulacion Polinomios Cardinales L i x|Polinomios cardinales]] $L_i(x)$:** su construcción, la propiedad $L_i(x_k)=\delta_{ik}$ y la partición de la unidad $\sum_i L_i \equiv 1$.
> - **[[Costo Computacional Evaluacion Directa|Costo de evaluación]]:** por qué la forma ingenua cuesta $O(n^2)$ por punto, y cómo la forma baricéntrica la reduce a $O(n)$.

---

## Ejemplo

> [!ejemplo]
> **Interpolar $(0,1), (1,3), (2,2)$ con Lagrange.**
> $$L_0 = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{(x-1)(x-2)}{2}, \quad L_1 = \frac{(x-0)(x-2)}{(1)(−1)} = -x(x-2), \quad L_2 = \frac{x(x-1)}{2}.$$
> $$p_2(x) = 1\cdot L_0 + 3\cdot L_1 + 2\cdot L_2 = -\tfrac{3}{2}x^2 + \tfrac{7}{2}x + 1.$$
> Verificación: $p_2(0)=1$, $p_2(1)=3$, $p_2(2)=2$. ✓

---

## Ventajas y limitaciones

> [!info]
> **Ventajas.**
> - Explícita, sin resolver sistemas.
> - Ideal para demostraciones (existencia, error, cuadratura).
> - La forma baricéntrica es estable y rápida ($O(n)$ por evaluación).

> [!warning]
> **Limitaciones.**
> - **No es incremental:** añadir un nodo obliga a recalcular *todos* los $L_i$ (cada uno cambia de grado). En cambio, [[Newton Diferencias Divididas/index|Newton]] solo añade un término.
> - La forma directa (no baricéntrica) cuesta $O(n^2)$ por punto y es numéricamente pobre.

---

## Resumen

| Tema | Nota |
|:---|:---|
| Polinomios cardinales $L_i$, propiedades | [[Formulacion Polinomios Cardinales L i x]] |
| Costo de evaluación y forma baricéntrica | [[Costo Computacional Evaluacion Directa]] |

> [!corolario]
> La interpolación de Lagrange escribe el polinomio interpolador como $\sum_i y_i L_i(x)$ con los polinomios cardinales $L_i(x_k)=\delta_{ik}$, una forma explícita que evita resolver el sistema de [[Matriz Vandermonde Mal Condicionamiento|Vandermonde]] y es insuperable para la teoría. Su debilidad —no ser incremental y la versión directa $O(n^2)$ por punto— se aborda con la [[Costo Computacional Evaluacion Directa|forma baricéntrica]] y, cuando se requiere agregar nodos, con la base de [[Newton Diferencias Divididas/index|Newton]].
