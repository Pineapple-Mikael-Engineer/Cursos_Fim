---
title: Pivoteo Parcial Total Estabilidad
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
draft: false
aliases:
  - Pivoteo
  - Pivoting
  - Estabilidad de la eliminación Gaussiana
---

# Pivoteo Parcial y Total en Eliminación Gaussiana

> [!definicion]
> El **pivoteo** es una estrategia de intercambio de filas (y opcionalmente columnas) durante la [[Eliminacion Gaussiana]] para evitar divisiones por números pequeños y controlar la propagación del error de redondeo. El elemento que se coloca en la posición diagonal mediante estos intercambios se denomina **pivote**.

Sin pivoteo, la eliminación Gaussiana es numéricamente inestable incluso para matrices bien condicionadas. El pivoteo transforma el algoritmo en una herramienta robusta para la mayoría de aplicaciones prácticas.

---

## Motivación: ¿Por qué falla la eliminación sin pivoteo?

> [!ejemplo]
> **Fallo catastrófico sin pivoteo.**
> 
> Consideremos el sistema:
> $$\begin{pmatrix} 10^{-20} & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
> 
> En precisión doble ($u \approx 10^{-16}$), la solución exacta es $x_1 \approx 1$, $x_2 \approx 1$.
> 
> **Eliminación Gaussiana sin pivoteo:**
> 1. Multiplicador: $m_{21} = a_{21}/a_{11} = 1 / 10^{-20} = 10^{20}$.
> 2. Fila 2 actualizada: $a_{22}' = 1 - 10^{20} \cdot 1 = -10^{20}$ (el $1$ original se pierde por [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]]).
> 3. $b_2' = 2 - 10^{20} \cdot 1 = -10^{20}$.
> 4. Sustitución regresiva: $x_2 = -10^{20} / -10^{20} = 1$.
> 5. $x_1 = (1 - 1 \cdot 1) / 10^{-20} = 0$. **¡Completamente erróneo!**
> 
> **Eliminación Gaussiana con pivoteo parcial:**
> 6. Intercambiar filas (pivote $a_{21}=1$ en lugar de $a_{11}=10^{-20}$):
>    $$\begin{pmatrix} 1 & 1 \\ 10^{-20} & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
> 7. Multiplicador: $m_{21} = 10^{-20} / 1 = 10^{-20}$.
> 8. Fila 2 actualizada: $a_{22}' = 1 - 10^{-20} \cdot 1 \approx 1$.
> 9. $b_2' = 1 - 10^{-20} \cdot 2 \approx 1$.
> 10. Sustitución regresiva: $x_2 \approx 1$, $x_1 \approx 1$. **¡Correcto!**

Este ejemplo muestra que un pivote minúsculo ($10^{-20}$) genera multiplicadores enormes ($10^{20}$) que amplifican descontroladamente los errores de redondeo.

---

## Pivoteo Parcial

> [!definicion]
> En el **pivoteo parcial**, en el paso $k$ de la eliminación, se selecciona como pivote el elemento de mayor valor absoluto en la columna $k$ por debajo (e incluyendo) la diagonal:
> $$|a_{p,k}| = \max_{i \geq k} |a_{i,k}|$$
> y se intercambian las filas $k$ y $p$.

> [!proposicion]
> **Propiedades del pivoteo parcial.**
> 1. Todos los multiplicadores satisfacen $|m_{i,k}| \leq 1$.
> 2. El costo adicional es $O(n^2)$ comparaciones, despreciable frente al $O(n^3)$ de la eliminación.
> 3. Garantiza estabilidad numérica para la gran mayoría de matrices prácticas.
> 4. No requiere conocer la matriz completa a priori (aplicable en eliminación *in-place*).

> [!teoria]
> **Análisis de error hacia atrás para pivoteo parcial.**
> Si se aplica [[Eliminacion Gaussiana]] con pivoteo parcial en aritmética con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$, los factores calculados $\tilde{L}$ y $\tilde{U}$ satisfacen:
> $$\tilde{L}\tilde{U} = A + \Delta A, \quad \|\Delta A\|_\infty \leq \rho \cdot u \cdot \|A\|_\infty$$
> donde $\rho$ es el **factor de crecimiento** definido como:
> $$\rho = \frac{\max_{i,j,k} |a_{i,j}^{(k)}|}{\max_{i,j} |a_{i,j}|}$$
> siendo $a_{i,j}^{(k)}$ los elementos generados durante la eliminación.

El factor de crecimiento $\rho$ mide cuánto crecen los elementos de la matriz durante el proceso. Para pivoteo parcial, $\rho \leq 2^{n-1}$ en el peor caso teórico, pero en la práctica rara vez excede $n$ o $10$-$100$.

> [!warning]
> **¿Puede fallar el pivoteo parcial?**
> Existen ejemplos patológicos (como ciertas matrices de [[Matriz de Wilkinson|Wilkinson]]) donde $\rho \approx 2^{n-1}$, causando pérdida total de precisión. Sin embargo, estas matrices son extremadamente raras en aplicaciones prácticas. El pivoteo parcial es el método por defecto en bibliotecas como LAPACK (`dgetrf`).

---

## Pivoteo Total

> [!definicion]
> En el **pivoteo total**, en el paso $k$ se selecciona como pivote el elemento de mayor valor absoluto en toda la submatriz activa (filas $k \dots n$, columnas $k \dots n$):
> $$|a_{p,q}| = \max_{i \geq k, j \geq k} |a_{i,j}|$$
> y se intercambian la fila $k$ con la fila $p$, y la columna $k$ con la columna $q$. El intercambio de columnas debe registrarse en un vector de permutación para recuperar el orden original de las incógnitas.

> [!proposicion]
> **Propiedades del pivoteo total.**
> 1. Garantiza que todos los multiplicadores satisfacen $|m_{i,k}| \leq 1$.
> 2. Minimiza el factor de crecimiento $\rho$: se puede demostrar que $\rho \leq n^{1/2} [2 \cdot 3^{1/2} \cdots n^{1/(n-1)}]^{1/2} \approx O(n^{\frac{1}{4}\log n})$, mucho menor que $2^{n-1}$.
> 3. Es **numéricamente más estable** que el pivoteo parcial.
> 4. El costo adicional es $O(n^3)$ comparaciones, comparable al costo de la eliminación misma.

> [!info]
> **Comparativa de costos.**
> | Estrategia | Costo adicional | Factor de crecimiento $\rho$ |
> |:---|:---:|:---:|
> | Sin pivoteo | $0$ | Ilimitado (inestable) |
> | Pivoteo parcial | $O(n^2)$ | $\leq 2^{n-1}$ (típicamente $O(1)$) |
> | Pivoteo total | $O(n^3)$ | $O(n^{\frac{1}{4}\log n})$ |
> | Pivoteo por umbral (rook pivoting) | $O(n^2)$ promedio | Comparable al total |

Debido a su costo elevado, el pivoteo total rara vez se usa en la práctica. El **pivoteo parcial es el estándar industrial**.

---

## Ejemplo comparativo con matriz patológica

> [!ejemplo]
> **Matriz donde el pivoteo parcial también puede fallar.**
> 
> Consideremos la matriz de $n \times n$:
> $$A = \begin{pmatrix} 
> 1 & 0 & 0 & \cdots & 0 & 1 \\
> -1 & 1 & 0 & \cdots & 0 & 1 \\
> -1 & -1 & 1 & \cdots & 0 & 1 \\
> \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
> -1 & -1 & -1 & \cdots & 1 & 1 \\
> -1 & -1 & -1 & \cdots & -1 & 1
> \end{pmatrix}$$
> 
> ```python
> import numpy as np
> 
> def matriz_crecimiento(n):
>     A = np.tril(-np.ones((n, n)), -1) + np.eye(n)
>     A[:, -1] = 1.0
>     return A
> 
> n = 50
> A = matriz_crecimiento(n)
> x_exacto = np.ones(n)
> b = A @ x_exacto
> 
> # Pivoteo parcial (estándar)
> x_parcial = np.linalg.solve(A, b)
> error_parcial = np.linalg.norm(x_parcial - x_exacto, np.inf)
> 
> # Simulación de pivoteo total (no disponible directamente, usamos SVD como referencia)
> U, s, Vt = np.linalg.svd(A)
> x_total = Vt.T @ np.diag(1/s) @ U.T @ b
> error_total = np.linalg.norm(x_total - x_exacto, np.inf)
> 
> print(f"Error con pivoteo parcial: {error_parcial:.2e}")
> print(f"Error con referencia SVD:  {error_total:.2e}")
> print(f"Factor de crecimiento estimado: {np.linalg.norm(A, np.inf) / np.linalg.norm(np.linalg.inv(A), np.inf):.2e}")
> ```
> 
> Para $n=50$, el pivoteo parcial produce errores del orden de $10^{-10}$, mientras que un método robusto como SVD mantiene precisión completa. El factor de crecimiento $\rho$ es significativo.

---

## Rook Pivoting: Un compromiso eficiente

> [!info]
> El **rook pivoting** (o pivoteo de torre) es una estrategia intermedia propuesta por Poole y Neal (1992):
> 1. En el paso $k$, buscar el elemento de máximo valor absoluto en la primera columna de la submatriz activa.
> 2. En la fila de ese elemento, buscar el máximo valor absoluto.
> 3. Si coincide con el elemento original, es el pivote. Si no, repetir desde la columna del nuevo máximo.
> 4. Este proceso (similar al movimiento de una torre de ajedrez) converge rápidamente a un elemento grande.
> 
> **Ventajas:**
> - Costo $O(n^2)$ en promedio, comparable al pivoteo parcial.
> - Factor de crecimiento $\rho$ típicamente mucho menor que el pivoteo parcial.
> - Implementado en algunas bibliotecas especializadas.

---

## Pivoteo para matrices simétricas

Para matrices **simétricas definidas positivas**, la [[Factorizacion Cholesky Matrices Definidas Positivas|factorización de Cholesky]] es naturalmente estable **sin pivoteo**. El factor de crecimiento está acotado por $1$.

Para matrices simétricas indefinidas, se requiere **pivoteo simétrico** (intercambiar simultáneamente filas y columnas $k \leftrightarrow p$) para preservar la simetría. Esto da lugar a la factorización $P A P^T = L D L^T$, donde $D$ es diagonal por bloques (con bloques $1 \times 1$ y $2 \times 2$). Esta es la base del algoritmo de **Bunch-Kaufman**, usado en LAPACK (`dsytrf`).

---

## Pivoteo en la práctica con LAPACK

Las bibliotecas numéricas profesionales ofrecen rutinas optimizadas con pivoteo:

| Rutina LAPACK | Matriz | Pivoteo | Factorización |
|:---|:---|:---|:---|
| `dgetrf` | Densa general | Parcial | $P A = L U$ |
| `dgetc2` | Densa general | Total | $P A Q = L U$ |
| `dsytrf` | Simétrica indefinida | Simétrico | $P A P^T = L D L^T$ |
| `dpotrf` | Simétrica definida positiva | Ninguno | $A = L L^T$ (Cholesky) |

> [!ejemplo]
> **Uso de pivoteo parcial con SciPy/LAPACK.**
> ```python
> import numpy as np
> from scipy.linalg import lu
> 
> A = np.array([[1e-20, 1], [1, 1]])
> P, L, U = lu(A)  # Pivoteo parcial por defecto
> 
> print("Matriz de permutación P:")
> print(P)
> print("\nFactor L:")
> print(L)
> print("\nFactor U:")
> print(U)
> print("\nVerificación: P @ A - L @ U =")
> print(P @ A - L @ U)
> ```
> 
> Salida:
> ```
> Matriz de permutación P:
> [[0. 1.]
>  [1. 0.]]
> 
> Factor L:
> [[1.0e+00 0.0e+00]
>  [1.0e-20 1.0e+00]]
> 
> Factor U:
> [[1. 1.]
>  [0. 1.]]
> 
> Verificación: P @ A - L @ U =
> [[0. 0.]
>  [0. 0.]]
> ```

---

## Relación con otras factorizaciones

> [!info]
> **Conexiones con otras descomposiciones.**
> - La [[Factorizacion LU]] con pivoteo parcial es la base de la eliminación Gaussiana práctica.
> - La [[Factorizacion QR]] con pivoteo de columnas ($A P = Q R$) se usa para problemas de rango deficiente y mínimos cuadrados.
> - El pivoteo total en $L U$ está relacionado con la búsqueda de un [[Matching Maximo en Grafos Bipartitos|matching máximo]] en el grafo bipartito asociado a la matriz, lo que conecta con algoritmos de **escalado y permutación** previos a la factorización (ej. `mc64` en HSL).

---

## Resumen: ¿Qué estrategia usar?

| Escenario | Estrategia recomendada |
|:---|:---|
| Matrices densas generales | Pivoteo parcial (estándar) |
| Matrices mal condicionadas conocidas | Pivoteo total o rook pivoting |
| Matrices simétricas definidas positivas | Sin pivoteo ([[Factorizacion Cholesky Matrices Definidas Positivas|Cholesky]]) |
| Matrices simétricas indefinidas | Pivoteo simétrico (Bunch-Kaufman) |
| Matrices dispersas | Pivoteo parcial con estrategias de [[Relleno Matrices Dispersas|minimización de relleno]] |

> [!corolario]
> El pivoteo es la diferencia entre un algoritmo numéricamente inútil y una herramienta confiable. En eliminación Gaussiana, el pivoteo parcial proporciona un equilibrio óptimo entre estabilidad y costo computacional para la gran mayoría de aplicaciones en ingeniería y ciencias.
