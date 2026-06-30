---
title: Variantes Doolittle Crout Cholesky
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - factorizacion-lu
draft: false
aliases:
  - Método de Doolittle
  - Método de Crout
  - Factorización LU por variantes
---

# Variantes de la Factorización LU: Doolittle, Crout y Cholesky

> [!definicion]
> La [[Factorizacion LU]] descompone una matriz $A \in \mathbb{R}^{n \times n}$ en el producto $A = LU$. Las variantes **Doolittle** y **Crout** difieren en la asignación de la diagonal unitaria. Para matrices simétricas definidas positivas, la **factorización de Cholesky** ($A = LL^T$) es una alternativa más eficiente, estudiada en detalle en [[Factorizacion Cholesky Matrices Definidas Positivas]].

---

## 1. Variante de Doolittle

### 1.1 En qué consiste

En la factorización de Doolittle, se busca $A = LU$ con:
- $L$ triangular inferior **unitaria** ($\ell_{ii} = 1$)
- $U$ triangular superior general

**Pasos del método (para una matriz $A$ de $n \times n$):**

1. Inicializar $L$ como matriz identidad ($\ell_{ii} = 1$, $\ell_{ij} = 0$ para $i<j$) y $U$ como matriz de ceros.

2. Para $k = 1, 2, \dots, n$:
   - **Paso 2.1 (calcular fila $k$ de $U$):** Para $j = k, k+1, \dots, n$:
     $$u_{kj} = a_{kj} - \sum_{p=1}^{k-1} \ell_{kp} u_{pj}$$
   - **Paso 2.2 (calcular columna $k$ de $L$ por debajo de la diagonal):** Para $i = k+1, \dots, n$:
     $$\ell_{ik} = \frac{1}{u_{kk}} \left( a_{ik} - \sum_{p=1}^{k-1} \ell_{ip} u_{pk} \right)$$

3. El resultado es $A = L \cdot U$.

**Observaciones clave:**
- Los elementos $\ell_{ii} = 1$ ya están fijos y no se calculan.
- Se requiere $u_{kk} \neq 0$ para poder calcular $\ell_{ik}$. Si $u_{kk} = 0$, la matriz no admite factorización LU sin pivoteo (ver [[Existencia Unicidad LU Matrices No Singulares]]).
- Esta variante surge naturalmente de la [[Eliminacion Gaussiana]].

### 1.2 Ejemplo detallado

> [!ejemplo]
> **Factorización Doolittle de $A = \begin{pmatrix} 2 & -1 & 1 \\ 4 & 1 & -1 \\ -2 & 2 & 3 \end{pmatrix}$.**
>
> **$k = 1$ (primera iteración):**
> - Fila 1 de $U$: $u_{11}=2$, $u_{12}=-1$, $u_{13}=1$
> - Columna 1 de $L$ (debajo de diag): $\ell_{21}=4/2=2$, $\ell_{31}=-2/2=-1$
>
> **$k = 2$ (segunda iteración):**
> - Fila 2 de $U$:
>   - $u_{22} = a_{22} - \ell_{21}u_{12} = 1 - 2(-1) = 3$
>   - $u_{23} = a_{23} - \ell_{21}u_{13} = -1 - 2(1) = -3$
> - Columna 2 de $L$: $\ell_{32} = (a_{32} - \ell_{31}u_{12})/u_{22} = (2 - (-1)(-1))/3 = 1/3$
>
> **$k = 3$ (tercera iteración):**
> - Fila 3 de $U$: $u_{33} = a_{33} - \ell_{31}u_{13} - \ell_{32}u_{23} = 3 - (-1)(1) - (1/3)(-3) = 5$
>
> **Resultado:**
> $$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 1/3 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & -1 & 1 \\ 0 & 3 & -3 \\ 0 & 0 & 5 \end{pmatrix}$$

### 1.3 Algoritmo (implementación)

> [!algoritmo]
> **Pseudocódigo de Doolittle (sin pivoteo).**
> ```
> Entrada: A matriz n x n
> Salida: L (triangular inferior unitaria), U (triangular superior)
>
> Inicializar L = I (identidad), U = 0
> Para k = 1 hasta n:
>     Para j = k hasta n:
>         u[k][j] = a[k][j]
>         Para p = 1 hasta k-1:
>             u[k][j] = u[k][j] - l[k][p] * u[p][j]
>     Para i = k+1 hasta n:
>         l[i][k] = a[i][k]
>         Para p = 1 hasta k-1:
>             l[i][k] = l[i][k] - l[i][p] * u[p][k]
>         l[i][k] = l[i][k] / u[k][k]
> ```

> [!algoritmo]
> **Implementación en Python.**
> ```python
> import numpy as np
>
> def doolittle(A):
>     """
>     Factorización LU variante Doolittle (sin pivoteo).
>     
>     Parámetros:
>         A: matriz cuadrada (n x n)
>     
>     Retorna:
>         L: matriz triangular inferior unitaria (n x n)
>         U: matriz triangular superior (n x n)
>     """
>     n = A.shape[0]
>     L = np.eye(n)
>     U = np.zeros((n, n))
>     
>     for k in range(n):
>         # Calcular fila k de U
>         for j in range(k, n):
>             U[k, j] = A[k, j] - sum(L[k, p] * U[p, j] for p in range(k))
>         
>         # Calcular columna k de L (por debajo de la diagonal)
>         for i in range(k+1, n):
>             L[i, k] = (A[i, k] - sum(L[i, p] * U[p, k] for p in range(k))) / U[k, k]
>     
>     return L, U
>
> # Ejemplo
> A = np.array([[2., -1., 1.], [4., 1., -1.], [-2., 2., 3.]])
> L, U = doolittle(A)
> print("L:\n", L)
> print("U:\n", U)
> print("L @ U:\n", L @ U)
> ```

---

## 2. Variante de Crout

### 2.1 En qué consiste

En la factorización de Crout, se busca $A = LU$ con:
- $U$ triangular superior **unitaria** ($u_{ii} = 1$)
- $L$ triangular inferior general

**Pasos del método (para una matriz $A$ de $n \times n$):**

1. Inicializar $U$ como matriz identidad ($u_{ii} = 1$, $u_{ij} = 0$ para $i>j$) y $L$ como matriz de ceros.

2. Para $k = 1, 2, \dots, n$:
   - **Paso 2.1 (calcular columna $k$ de $L$):** Para $i = k, k+1, \dots, n$:
     $$\ell_{ik} = a_{ik} - \sum_{p=1}^{k-1} \ell_{ip} u_{pk}$$
   - **Paso 2.2 (calcular fila $k$ de $U$ a la derecha de la diagonal):** Para $j = k+1, \dots, n$:
     $$u_{kj} = \frac{1}{\ell_{kk}} \left( a_{kj} - \sum_{p=1}^{k-1} \ell_{kp} u_{pj} \right)$$

3. El resultado es $A = L \cdot U$.

**Observaciones clave:**
- Los elementos $u_{ii} = 1$ ya están fijos y no se calculan.
- Se requiere $\ell_{kk} \neq 0$ para poder calcular $u_{kj}$. Si $\ell_{kk} = 0$, la matriz no admite factorización LU sin pivoteo.
- El orden de cálculo es **columna por columna** (a diferencia de Doolittle que es fila por fila).

### 2.2 Ejemplo detallado

> [!ejemplo]
> **Factorización Crout de $A = \begin{pmatrix} 2 & -1 & 1 \\ 4 & 1 & -1 \\ -2 & 2 & 3 \end{pmatrix}$.**
>
> **$k = 1$ (primera iteración):**
> - Columna 1 de $L$: $\ell_{11}=2$, $\ell_{21}=4$, $\ell_{31}=-2$
> - Fila 1 de $U$ (a la derecha de diag): $u_{12}=a_{12}/\ell_{11}=-1/2=-0.5$, $u_{13}=1/2=0.5$
>
> **$k = 2$ (segunda iteración):**
> - Columna 2 de $L$:
>   - $\ell_{22} = a_{22} - \ell_{21}u_{12} = 1 - 4(-0.5) = 3$
>   - $\ell_{32} = a_{32} - \ell_{31}u_{12} = 2 - (-2)(-0.5) = 1$
> - Fila 2 de $U$: $u_{23} = (a_{23} - \ell_{21}u_{13})/\ell_{22} = (-1 - 4(0.5))/3 = -1$
>
> **$k = 3$ (tercera iteración):**
> - Columna 3 de $L$: $\ell_{33} = a_{33} - \ell_{31}u_{13} - \ell_{32}u_{23} = 3 - (-2)(0.5) - (1)(-1) = 5$
>
> **Resultado:**
> $$L = \begin{pmatrix} 2 & 0 & 0 \\ 4 & 3 & 0 \\ -2 & 1 & 5 \end{pmatrix}, \quad U = \begin{pmatrix} 1 & -0.5 & 0.5 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$$

### 2.3 Algoritmo (implementación)

> [!algoritmo]
> **Pseudocódigo de Crout (sin pivoteo).**
> ```
> Entrada: A matriz n x n
> Salida: L (triangular inferior), U (triangular superior unitaria)
>
> Inicializar L = 0, U = I (identidad)
> Para k = 1 hasta n:
>     Para i = k hasta n:
>         l[i][k] = a[i][k]
>         Para p = 1 hasta k-1:
>             l[i][k] = l[i][k] - l[i][p] * u[p][k]
>     Para j = k+1 hasta n:
>         u[k][j] = a[k][j]
>         Para p = 1 hasta k-1:
>             u[k][j] = u[k][j] - l[k][p] * u[p][j]
>         u[k][j] = u[k][j] / l[k][k]
> ```

> [!algoritmo]
> **Implementación en Python.**
> ```python
> import numpy as np
>
> def crout(A):
>     """
>     Factorización LU variante Crout (sin pivoteo).
>     
>     Parámetros:
>         A: matriz cuadrada (n x n)
>     
>     Retorna:
>         L: matriz triangular inferior (n x n)
>         U: matriz triangular superior unitaria (n x n)
>     """
>     n = A.shape[0]
>     L = np.zeros((n, n))
>     U = np.eye(n)
>     
>     for k in range(n):
>         # Calcular columna k de L
>         for i in range(k, n):
>             L[i, k] = A[i, k] - sum(L[i, p] * U[p, k] for p in range(k))
>         
>         # Calcular fila k de U (a la derecha de la diagonal)
>         for j in range(k+1, n):
>             U[k, j] = (A[k, j] - sum(L[k, p] * U[p, j] for p in range(k))) / L[k, k]
>     
>     return L, U
>
> # Ejemplo
> A = np.array([[2., -1., 1.], [4., 1., -1.], [-2., 2., 3.]])
> L, U = crout(A)
> print("L:\n", L)
> print("U:\n", U)
> print("L @ U:\n", L @ U)
> ```

---

## 3. La variante de Cholesky (caso especial)

Para matrices **simétricas definidas positivas** (SPD), existe una factorización más eficiente que reduce el costo a la mitad y garantiza estabilidad numérica sin pivoteo. Esta factorización se estudia en detalle en [[Factorizacion Cholesky Matrices Definidas Positivas]].

### 3.1 En qué consiste

En la factorización de Cholesky, se busca $A = L L^T$ con:
- $L$ triangular inferior con **diagonal estrictamente positiva** ($\ell_{ii} > 0$)

**Pasos del método (para una matriz SPD $A$ de $n \times n$):**

1. Inicializar $L$ como matriz de ceros.

2. Para $k = 1, 2, \dots, n$:
   - **Paso 2.1 (calcular el elemento diagonal):**
     $$\ell_{kk} = \sqrt{a_{kk} - \sum_{p=1}^{k-1} \ell_{kp}^2}$$
   - **Paso 2.2 (calcular los elementos de la columna $k$ por debajo de la diagonal):** Para $i = k+1, \dots, n$:
     $$\ell_{ik} = \frac{1}{\ell_{kk}} \left( a_{ik} - \sum_{p=1}^{k-1} \ell_{ip} \ell_{kp} \right)$$

3. El resultado es $A = L L^T$.

**Observaciones clave:**
- La matriz debe ser **simétrica** ($A = A^T$) y **definida positiva** ($x^T A x > 0$ para todo $x \neq 0$).
- No se requiere pivoteo: los $\ell_{kk}$ son automáticamente positivos (en teoría) si $A$ es SPD.
- Costo computacional: $\frac{1}{3}n^3$ FLOPs, aproximadamente la mitad de LU.

### 3.2 Ejemplo detallado

> [!ejemplo]
> **Factorización de Cholesky de $A = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}$.**
>
> Verificar que $A$ es SPD (simétrica y todos los menores principales positivos: $4 > 0$, $4\cdot10-2^2=36>0$, $\det(A)=...$).
>
> **$k = 1$ (primera iteración):**
> - $\ell_{11} = \sqrt{a_{11}} = \sqrt{4} = 2$
> - Columna 1 debajo de diag: $\ell_{21}=a_{21}/\ell_{11}=2/2=1$, $\ell_{31}=a_{31}/\ell_{11}=-2/2=-1$
>
> **$k = 2$ (segunda iteración):**
> - $\ell_{22} = \sqrt{a_{22} - \ell_{21}^2} = \sqrt{10 - 1^2} = \sqrt{9} = 3$
> - Columna 2 debajo de diag: $\ell_{32} = (a_{32} - \ell_{31}\ell_{21})/\ell_{22} = (2 - (-1)(1))/3 = 1$
>
> **$k = 3$ (tercera iteración):**
> - $\ell_{33} = \sqrt{a_{33} - \ell_{31}^2 - \ell_{32}^2} = \sqrt{6 - (-1)^2 - 1^2} = \sqrt{4} = 2$
>
> **Resultado:**
> $$L = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ -1 & 1 & 2 \end{pmatrix}$$
>
> **Verificación:** $LL^T = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix} = A$.

### 3.3 Algoritmo (implementación)

> [!algoritmo]
> **Pseudocódigo de Cholesky.**
> ```
> Entrada: A matriz SPD n x n
> Salida: L triangular inferior tal que A = L * L^T
>
> Inicializar L = 0
> Para k = 1 hasta n:
>     L[k][k] = sqrt(A[k][k] - sum_{p=1}^{k-1} L[k][p]**2)
>     Para i = k+1 hasta n:
>         L[i][k] = (A[i][k] - sum_{p=1}^{k-1} L[i][p] * L[k][p]) / L[k][k]
> ```

> [!algoritmo]
> **Implementación en Python.**
> ```python
> import numpy as np
>
> def cholesky(A):
>     """
>     Factorización de Cholesky (matriz simétrica definida positiva).
>     
>     Parámetros:
>         A: matriz SPD (n x n)
>     
>     Retorna:
>         L: matriz triangular inferior (n x n) tal que A = L @ L.T
>     """
>     n = A.shape[0]
>     L = np.zeros((n, n))
>     
>     for k in range(n):
>         # Elemento diagonal
>         s = sum(L[k, p]**2 for p in range(k))
>         L[k, k] = np.sqrt(A[k, k] - s)
>         
>         # Elementos por debajo de la diagonal
>         for i in range(k+1, n):
>             s = sum(L[i, p] * L[k, p] for p in range(k))
>             L[i, k] = (A[i, k] - s) / L[k, k]
>     
>     return L
>
> # Ejemplo
> A = np.array([[4., 2., -2.], [2., 10., 2.], [-2., 2., 6.]])
> L = cholesky(A)
> print("L:\n", L)
> print("L @ L.T:\n", L @ L.T)
> ```

> [!warning]
> **Estabilidad numérica en Cholesky.** El cálculo de la raíz cuadrada requiere que el argumento sea positivo. En aritmética de punto flotante pueden aparecer valores negativos muy pequeños debido a error de redondeo, indicando que la matriz no es SPD (o está mal condicionada). Para estos casos existe la variante $LDL^T$ que evita raíces cuadradas (ver [[Factorizacion Cholesky Matrices Definidas Positivas]]).

---

## Comparación entre las tres variantes

| Aspecto | Doolittle | Crout | Cholesky |
|:---|:---:|:---:|:---:|
| **Tipo de matriz** | General (con pivoteo) | General (con pivoteo) | SPD (sin pivoteo) |
| **Factorización** | $A = LU$ | $A = LU$ | $A = LL^T$ |
| **Diagonal unitaria** | $L$ | $U$ | No aplica |
| **Orden de cálculo** | Fila $U$ → Columna $L$ | Columna $L$ → Fila $U$ | Columna $L$ progresiva |
| **Costo** | $\frac{2}{3}n^3$ | $\frac{2}{3}n^3$ | $\frac{1}{3}n^3$ |
| **Pivoteo necesario** | Sí (estabilidad) | Sí (estabilidad) | No (automático) |
| **Almacenamiento** | $L$ (sin diag) + $U$ | $L$ + $U$ (sin diag) | $L$ |

---

## Resumen y recomendaciones

| Situación | Variante recomendada |
|:---|:---|
| Matriz densa general | Doolittle con pivoteo parcial (estándar LAPACK) |
| Implementación didáctica | Cualquiera (equivalente en costo) |
| Matriz con acceso preferente por columnas | Crout |
| Matriz simétrica definida positiva | Cholesky (ver [[Factorizacion Cholesky Matrices Definidas Positivas]]) |
| Matriz simétrica indefinida | $LDL^T$ con pivoteo de Bunch-Kaufman |

> [!corolario]
> Doolittle y Crout son dos caras de la misma moneda: la factorización [[Factorizacion LU|LU]]. La elección entre ellas es principalmente una cuestión de orden de acceso a memoria. El verdadero salto cualitativo ocurre al pasar a matrices con estructura especial, donde la [[Factorizacion Cholesky Matrices Definidas Positivas|factorización de Cholesky]] ofrece ventajas decisivas en costo (mitad) y estabilidad (sin pivoteo). Para matrices SPD, **nunca uses LU**: usa Cholesky.