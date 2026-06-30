---
title: Factorizacion LU
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - factorizacion-matricial
  - index
draft: false
aliases:
  - Descomposición LU
  - LU decomposition
  - Factorización triangular
---

# Factorización LU

> [!definicion]
> La **factorización LU** (o descomposición LU) de una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ consiste en expresarla como el producto de dos matrices triangulares:
> $$A = L U$$
> donde $L \in \mathbb{R}^{n \times n}$ es una matriz **triangular inferior unitaria** ($\ell_{ii} = 1$) y $U \in \mathbb{R}^{n \times n}$ es una matriz **triangular superior**.

Cuando se incorpora pivoteo para garantizar estabilidad numérica, la factorización toma la forma:
$$P A = L U \quad \text{o} \quad P A Q = L U$$
donde $P$ y $Q$ son matrices de permutación que registran los intercambios de filas y columnas.

---

## Ejemplo de uso: Resolver un sistema con múltiples lados derechos

> [!ejemplo]
> **Resolver $Ax = b_1$ y $Ax = b_2$ usando factorización LU.**
> 
> Sea $A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$, $b_1 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$, $b_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$.
>
> **Paso 1: Calcular la factorización LU de $A$ (una sola vez).**
>
> Mediante eliminación (ver algoritmo más abajo) se obtiene:
> $$L = \begin{pmatrix} 1 & 0 & 0 \\ -0.5 & 1 & 0 \\ 0 & -0.6667 & 1 \end{pmatrix}, \quad 
>   U = \begin{pmatrix} 2 & -1 & 0 \\ 0 & 1.5 & -1 \\ 0 & 0 & 1.3333 \end{pmatrix}$$
>
> **Paso 2: Resolver $L y = b_1$ y luego $U x = y$ (sustitución progresiva + regresiva).**
> - Para $b_1$: $y = (1, 0.5, 1.3333)^T$, $x_1 = (1, 1, 1)^T$.
> - Para $b_2$: $y = (0, 1, 1.1667)^T$, $x_2 = (0.5, 1, 0.5)^T$.
>
> **Ventaja:** El paso 1 (costo $\frac{2}{3}n^3$) se hace una sola vez. Cada sistema adicional cuesta solo $O(n^2)$ FLOPs, en lugar de repetir la eliminación completa.

---

## Algoritmo de factorización LU (sin pivoteo)

El algoritmo básico es esencialmente la eliminación Gaussiana, pero **almacenando los multiplicadores** en la parte triangular inferior de la matriz original.

> [!algoritmo]
> **Factorización LU in-place (sin pivoteo).**
> 
> **Entrada:** Matriz $A \in \mathbb{R}^{n \times n}$. **Salida:** Matriz $A$ modificada: parte triangular superior contiene $U$, parte estrictamente inferior contiene los multiplicadores $m_{ik}$ de $L$ (los unos de la diagonal de $L$ no se almacenan).
> 
> 1. Para $k = 1, 2, \dots, n-1$:
>     - Para $i = k+1, \dots, n$:
>         - $a_{ik} \leftarrow a_{ik} / a_{kk}$  (multiplicador $m_{ik}$)
>         - Para $j = k+1, \dots, n$:
>             - $a_{ij} \leftarrow a_{ij} - a_{ik} \cdot a_{kj}$

> [!algoritmo]
> **Resolución de $Ax = b$ vía LU (con permutación).**
> 
> **Entrada:** Factores $L$, $U$, vector de permutación $\text{piv}$, lado derecho $b$. **Salida:** Solución $x$.
> 
> 2. **Aplicar permutación:** $b \leftarrow P b$ (reordenar según $\text{piv}$).
> 3. **Sustitución progresiva:** Resolver $L y = b$ para $y$.
>    $$y_1 = b_1$$
>    $$y_i = b_i - \sum_{j=1}^{i-1} \ell_{ij} y_j, \quad i = 2, \dots, n$$
> 4. **Sustitución regresiva:** Resolver $U x = y$ para $x$.
>    $$x_n = y_n / u_{nn}$$
>    $$x_i = \left( y_i - \sum_{j=i+1}^{n} u_{ij} x_j \right) / u_{ii}, \quad i = n-1, \dots, 1$$

**Costo total:** $\frac{2}{3}n^3$ FLOPs para la factorización + $n^2$ FLOPs por cada sistema adicional.

---

## Implementación práctica

> [!ejemplo]
> **Uso en Python con SciPy.**
> 
> ```python
> import numpy as np
> from scipy.linalg import lu_factor, lu_solve
> 
> A = np.array([[2., -1., 0.],
>               [-1., 2., -1.],
>               [0., -1., 2.]])
> b1 = np.array([1., 0., 1.])
> b2 = np.array([0., 1., 0.])
> 
> # Factorización (una sola vez)
> lu_fact, piv = lu_factor(A)
> 
> # Resolver para cada lado derecho
> x1 = lu_solve((lu_fact, piv), b1)
> x2 = lu_solve((lu_fact, piv), b2)
> 
> print(f"Solución 1: {x1}")  # [1. 1. 1.]
> print(f"Solución 2: {x2}")  # [0.5 1.  0.5]
> ```

| Biblioteca | Rutina | Descripción |
|:---|:---|:---|
| LAPACK | `dgetrf` | Factorización $P A = L U$ |
| LAPACK | `dgetrs` | Resolución usando factores LU |
| SciPy | `lu_factor` / `lu_solve` | Factorización y resolución |
| MATLAB | `[L, U, P] = lu(A)` | Factorización con pivoteo parcial |

---

## Motivación: ¿Por qué usar LU en lugar de eliminación Gaussiana repetida?

La [[Eliminacion Gaussiana]] resuelve $Ax = b$ en $O(n^3)$ operaciones. Pero si se necesita resolver para **múltiples lados derechos** $b_1, b_2, \dots, b_m$, repetir la eliminación desde cero costaría $O(m n^3)$.

> [!proposicion]
> **Ventaja fundamental de LU.** Resolver $m$ sistemas con la misma matriz $A$ cuesta:
> - Eliminación Gaussiana repetida: $\frac{2}{3}m n^3$ FLOPs.
> - Factorización LU + $m$ sustituciones: $\frac{2}{3}n^3 + m n^2$ FLOPs.
> 
> Para $m \geq 2$ y $n$ grande, LU es **significativamente más eficiente**.

El análisis detallado del costo computacional se desarrolla en [[Conteo Operaciones Complejidad O n3]].

---

## Existencia y unicidad (sin pivoteo)

> [!teorema]
> **Condiciones de existencia.** Una matriz $A \in \mathbb{R}^{n \times n}$ admite factorización LU (sin pivoteo) si y solo si todos sus **menores principales líderes** son no singulares:
> $$\det(A_{1:k, 1:k}) \neq 0, \quad k = 1, 2, \dots, n-1$$
> 
> Bajo esta condición, la factorización $A = LU$ con $L$ unitaria es **única**.

> [!warning]
> **¿Qué matrices NO admiten LU sin pivoteo?** Ejemplo clásico: $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. El menor principal líder $A_{1:1, 1:1} = 0$, por lo que no existe LU sin pivoteo. Sin embargo, $P A = L U$ con $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ sí existe.

La demostración completa y el análisis detallado se tratan en [[Existencia Unicidad LU Matrices No Singulares]].

---

## Factorización LU con pivoteo parcial

Para garantizar estabilidad numérica y permitir la factorización de matrices con menores principales singulares, se incorpora [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]].

> [!definicion]
> La **factorización LU con pivoteo parcial** produce:
> $$P A = L U$$
> donde $P$ es una matriz de permutación que registra los intercambios de filas realizados durante la eliminación para colocar el pivote de mayor magnitud.

El análisis de cómo el pivoteo afecta la [[Acumulacion Error Redondeo Gauss|acumulación del error]] y el factor de crecimiento es fundamental para entender la robustez del método.

---

## Variantes de la factorización LU

| Variante | Forma | Característica | Nota específica |
|:---|:---|:---|:---|
| **Doolittle** | $A = L U$ | $L$ unitaria ($\ell_{ii}=1$), $U$ general | [[Variantes Doolittle Crout Cholesky\|Ver detalles]] |
| **Crout** | $A = L U$ | $U$ unitaria ($u_{ii}=1$), $L$ general | [[Variantes Doolittle Crout Cholesky\|Ver detalles]] |
| **Cholesky** | $A = L L^T$ | Para matrices simétricas definidas positivas | [[Factorizacion Cholesky Matrices Definidas Positivas]] |

---

## Aplicaciones de la factorización LU

| Aplicación | Fórmula | Notas |
|:---|:---|:---|
| **Calcular determinante** | $\det(A) = \det(P) \cdot \prod_{i=1}^{n} u_{ii}$ | $\det(P) = (-1)^{\text{intercambios}}$ |
| **Calcular inversa** | $A^{-1} = U^{-1} L^{-1} P$ | Resolver $A X = I$ |
| **Refinamiento iterativo** | Mejora precisión de solución | Usa $LU$ precalculada |
| **Número de condición** | Estimación de $\kappa(A)$ | Usado en estimadores de LAPACK |

---

## Comparación con otras factorizaciones

| Factorización | Forma | Costo | Estabilidad | Cuándo usarla |
|:---|:---|:---:|:---:|:---|
| **LU** | $P A = L U$ | $\frac{2}{3}n^3$ | Buena con pivoteo | Sistemas cuadrados generales |
| **Cholesky** | $A = L L^T$ | $\frac{1}{3}n^3$ | Excelente | Matrices SPD ([[Factorizacion Cholesky Matrices Definidas Positivas]]) |
| **QR** | $A = Q R$ | $\frac{4}{3}n^3$ | Excelente | Sistemas sobredeterminados ([[Factorizacion QR]]) |
| **SVD** | $A = U \Sigma V^T$ | $\approx 20 n^3$ | Máxima | Análisis de rango y pseudo-inversa ([[Valores Singulares y Descomposicion SVD]]) |

---

## Limitaciones y consideraciones

> [!warning]
> **Cuándo LU puede no ser la mejor opción.**
> 
> 1. **Matrices simétricas definidas positivas:** [[Factorizacion Cholesky Matrices Definidas Positivas|Cholesky]] es el doble de rápido y más estable.
> 2. **Matrices muy mal condicionadas:** El [[Condicionamiento Numerico Numero Condicion|condicionamiento]] limita la precisión; considerar [[Valores Singulares y Descomposicion SVD|SVD]] o regularización.
> 3. **Matrices dispersas grandes:** El relleno durante LU puede hacerla inviable; usar [[Metodos Iterativos|métodos iterativos]].
> 4. **Múltiples lados derechos secuenciales:** Si los $b_k$ dependen del resultado anterior, LU sigue siendo eficiente, pero considerar si un método iterativo puede aprovechar la solución previa.

El análisis del relleno en matrices dispersas se estudia en [[Relleno Matrices Dispersas]].