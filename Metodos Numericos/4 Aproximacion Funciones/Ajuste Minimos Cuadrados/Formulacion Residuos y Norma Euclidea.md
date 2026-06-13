---
title: Formulación de Residuos y Norma Euclídea
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - minimos-cuadrados
draft: false
aliases:
  - Formulación de residuos
  - Norma euclídea de mínimos cuadrados
  - Matriz de diseño
  - Least squares residuals
---

# Formulación de Residuos y Norma Euclídea

> [!definicion]
> Dado un modelo lineal en los parámetros $\phi(x; c) = \sum_{j=1}^n c_j\varphi_j(x)$ y datos $\{(x_i, y_i)\}_{i=1}^m$ con $m > n$, el **vector de residuos** es $r = Ac - y$, donde la **matriz de diseño** $A \in \mathbb{R}^{m\times n}$ tiene entradas $A_{ij} = \varphi_j(x_i)$. El ajuste minimiza la **norma euclídea** del residuo:
> $$\min_{c\in\mathbb{R}^n}\ \|Ac - y\|_2^2 = \min_c \sum_{i=1}^m \big(\textstyle\sum_j c_j\varphi_j(x_i) - y_i\big)^2.$$

> [!info]
> La elección de la norma $\|\cdot\|_2$ no es arbitraria: hace el problema **diferenciable** y **lineal** en $c$, conduce a las [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]], y tiene interpretación geométrica (proyección ortogonal) y estadística (estimador de máxima verosimilitud bajo ruido gaussiano).

---

## Por qué la norma euclídea

> [!info]
> | Norma | Problema | Propiedad |
> |:---|:---|:---|
> | $\|\cdot\|_2$ (euclídea) | mínimos cuadrados | diferenciable, lineal, único óptimo |
> | $\|\cdot\|_1$ | desviaciones absolutas | robusta a *outliers*, no diferenciable |
> | $\|\cdot\|_\infty$ | minimax (Chebyshev) | minimiza el peor error, no diferenciable |
>
> La norma $\|\cdot\|_2$ es la única que da un problema lineal con solución cerrada; las otras requieren programación lineal o métodos iterativos. De ahí su predominio.

---

## El sistema sobredeterminado

> [!teoria]
> Con $m > n$, el sistema $Ac = y$ tiene **más ecuaciones que incógnitas**: en general no tiene solución exacta (el dato $y$ no está en el espacio de columnas de $A$). Mínimos cuadrados busca el $c$ que hace $Ac$ **lo más cercano posible** a $y$, es decir, la proyección de $y$ sobre $\operatorname{col}(A)$.

> [!teorema]
> **Caracterización del minimizador (ecuación normal).** $c^*$ minimiza $\|Ac - y\|_2^2$ si y solo si el residuo es **ortogonal** al espacio de columnas de $A$:
> $$A^T(Ac^* - y) = 0 \quad\Longleftrightarrow\quad A^TA\,c^* = A^Ty.$$

> [!demostracion]
> Sea $J(c) = \|Ac - y\|_2^2 = (Ac-y)^T(Ac-y) = c^TA^TAc - 2c^TA^Ty + y^Ty$. El gradiente es
> $$\nabla J(c) = 2A^TAc - 2A^Ty.$$
> Anulándolo se obtiene $A^TAc = A^Ty$. Como $J$ es convexa (su Hessiana $2A^TA$ es semidefinida positiva), el punto crítico es un mínimo global. La condición $\nabla J = 0$ equivale a $A^Tr = 0$: el residuo es ortogonal a las columnas de $A$.

---

## Ejemplo

> [!ejemplo]
> **Ajuste de recta $y = c_0 + c_1 x$ a $(1,1),(2,2),(3,2),(4,3)$.** La matriz de diseño y el dato:
> $$A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \\ 1 & 4 \end{pmatrix}, \quad y = \begin{pmatrix} 1 \\ 2 \\ 2 \\ 3 \end{pmatrix}.$$
> El residuo $r = Ac - y$ se minimiza en $\|\cdot\|_2$. Sistema sobredeterminado ($4 > 2$): no existe recta que pase por los 4 puntos, pero sí la que minimiza $\sum r_i^2$. Su solución (vía [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]]) es $c = (0.5, 0.6)^T$, con residuo $r = (0.1, -0.3, 0.3, -0.1)^T$, que cumple $A^Tr = 0$.

---

## Interpretación geométrica

> [!teoria]
> El conjunto $\{Ac : c\in\mathbb{R}^n\}$ es el espacio de columnas $\operatorname{col}(A)$, un subespacio de $\mathbb{R}^m$ de dimensión $\leq n$. Minimizar $\|Ac - y\|_2$ equivale a hallar el punto de ese subespacio **más cercano** a $y$, que es su **proyección ortogonal** $\hat y = Ac^*$. El residuo $r = y - \hat y$ es perpendicular al subespacio: $A^Tr = 0$. Esta ortogonalidad *es* la ecuación normal.

> [!info]
> La matriz de proyección es $P = A(A^TA)^{-1}A^T$, que cumple $P^2 = P$ y $P^T = P$. Entonces $\hat y = Py$ y $r = (I-P)y$. Geometría limpia: $y$ se descompone en su sombra sobre $\operatorname{col}(A)$ más una parte ortogonal.

---

## Relación con otras notas

> [!info]
> - El sistema que caracteriza el óptimo: [[Ecuaciones Normales y Matriz Gram]].
> - Por qué resolverlo directamente es arriesgado: [[Condicionamiento Ecuaciones Normales]].
> - Los modelos concretos: [[Regresion Lineal Multiple y Polinomial]].
> - Contraste con la interpolación exacta: [[Ajuste Minimos Cuadrados/index]] y [[Interpolacion Polinomica/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Residuo | $r = Ac - y$ |
| Matriz de diseño | $A_{ij} = \varphi_j(x_i)$ |
| Objetivo | $\min \|Ac - y\|_2^2$ |
| Condición de óptimo | $A^T(Ac - y) = 0$ |
| Geometría | proyección de $y$ sobre $\operatorname{col}(A)$ |
| Por qué $\|\cdot\|_2$ | diferenciable, lineal, único |

> [!corolario]
> La formulación de mínimos cuadrados minimiza la norma euclídea del residuo $r = Ac - y$ de un sistema sobredeterminado ($m > n$), elección que hace el problema convexo y diferenciable con solución única. El minimizador se caracteriza por la ortogonalidad del residuo al espacio de columnas, $A^T(Ac-y) = 0$, que es geométricamente la proyección de $y$ sobre $\operatorname{col}(A)$ y algebraicamente las [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]] $A^TAc = A^Ty$. Esta base sustenta la [[Regresion Lineal Multiple y Polinomial|regresión]] y advierte sobre el [[Condicionamiento Ecuaciones Normales|condicionamiento]] de su resolución.
