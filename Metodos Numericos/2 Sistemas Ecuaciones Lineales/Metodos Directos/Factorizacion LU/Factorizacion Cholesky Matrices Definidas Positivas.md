---
title: Factorizacion Cholesky Matrices Definidas Positivas
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - factorizacion-matricial
draft: false
aliases:
  - Cholesky
  - Descomposición de Cholesky
  - LL^T
  - LDL^T
---

# Factorización de Cholesky para Matrices Simétricas Definidas Positivas

> [!definicion]
> La **factorización de Cholesky** es la descomposición de una matriz **simétrica definida positiva** $A \in \mathbb{R}^{n \times n}$ como:
> $$A = L L^T$$
> donde $L$ es una matriz **triangular inferior** con elementos diagonales **estrictamente positivos** ($\ell_{ii} > 0$).

Esta factorización es un caso especial de la [[Factorizacion LU]] que explota la simetría y la definición positiva para reducir el costo computacional a la mitad y garantizar estabilidad numérica **sin necesidad de pivoteo**.

---

## Matrices simétricas definidas positivas

Antes de desarrollar el algoritmo, es crucial caracterizar la clase de matrices para las que Cholesky es aplicable.

> [!definicion]
> Una matriz $A \in \mathbb{R}^{n \times n}$ es **simétrica definida positiva** (SDP) si:
> 1. $A = A^T$ (simetría).
> 2. $x^T A x > 0$ para todo vector $x \in \mathbb{R}^n$, $x \neq 0$ (definición positiva).

> [!proposicion]
> **Caracterizaciones equivalentes de matrices SDP.** Sea $A \in \mathbb{R}^{n \times n}$ simétrica. Las siguientes afirmaciones son equivalentes:
> 1. $A$ es definida positiva.
> 2. Todos los **valores propios** de $A$ son estrictamente positivos: $\lambda_i > 0$, $i = 1, \dots, n$.
> 3. Todos los **menores principales líderes** son estrictamente positivos: $\Delta_k > 0$, $k = 1, \dots, n$ (criterio de Sylvester).
> 4. Existe una matriz $B$ no singular tal que $A = B^T B$.

La última caracterización es exactamente lo que garantiza la existencia de la factorización de Cholesky con $L$ real.

> [!ejemplo]
> **Verificación de definición positiva mediante menores principales.**
> 
> $$A = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}$$
> 
> - $\Delta_1 = 4 > 0$
> - $\Delta_2 = \det\begin{pmatrix} 4 & 2 \\ 2 & 10 \end{pmatrix} = 40 - 4 = 36 > 0$
> - $\Delta_3 = \det(A) = 4(60 - 4) - 2(12 + 4) + (-2)(4 + 20) = 224 - 32 - 48 = 144 > 0$
> 
> Todos los menores principales líderes son positivos $\implies$ $A$ es SDP.

---

## Existencia y unicidad

> [!teorema]
> **Existencia y unicidad de la factorización de Cholesky.** Sea $A \in \mathbb{R}^{n \times n}$ una matriz simétrica definida positiva. Entonces:
> 1. **Existencia:** Existe una única matriz triangular inferior $L$ con $\ell_{ii} > 0$ tal que $A = L L^T$.
> 2. **Unicidad:** Si se exige $\ell_{ii} > 0$, la factorización es única.

> [!demostracion]
> **Demostración por inducción sobre $n$.**
> 
> **Caso base $n=1$:** $A = [a_{11}]$ con $a_{11} > 0$ (por definición positiva). Tomamos $L = [\sqrt{a_{11}}]$ con $\ell_{11} > 0$. Única.
> 
> **Paso inductivo:** Supongamos cierto para $n-1$. Escribimos $A$ en bloques:
> $$A = \begin{pmatrix} A_{11} & a \\ a^T & a_{nn} \end{pmatrix}$$
> 
> donde $A_{11} \in \mathbb{R}^{(n-1) \times (n-1)}$ es SDP (por ser submatriz principal de $A$).
> 
> Por hipótesis inductiva, existe $L_{11}$ triangular inferior con $\ell_{ii} > 0$ tal que $A_{11} = L_{11} L_{11}^T$.
> 
> Buscamos $L$ de la forma:
> $$L = \begin{pmatrix} L_{11} & 0 \\ \ell^T & \ell_{nn} \end{pmatrix}$$
> 
> Imponiendo $A = L L^T$:
> $$A = \begin{pmatrix} L_{11} L_{11}^T & L_{11} \ell \\ \ell^T L_{11}^T & \ell^T \ell + \ell_{nn}^2 \end{pmatrix} = \begin{pmatrix} A_{11} & a \\ a^T & a_{nn} \end{pmatrix}$$
> 
> De aquí:
> 1. $L_{11} \ell = a \implies \ell = L_{11}^{-1} a$ (sistema triangular, soluble).
> 2. $\ell^T \ell + \ell_{nn}^2 = a_{nn} \implies \ell_{nn} = \sqrt{a_{nn} - \ell^T \ell}$.
> 
> La cantidad dentro de la raíz es positiva porque $A$ es SDP (el complemento de Schur $a_{nn} - a^T A_{11}^{-1} a > 0$).
> 
> Por tanto, $\ell_{nn} > 0$ está unívocamente determinado. $\blacksquare$

---

## Algoritmo de Cholesky

La demostración anterior sugiere un algoritmo constructivo. Existen varias versiones equivalentes según el orden de recorrido de la matriz.

> [!algoritmo]
> **Algoritmo de Cholesky (versión por columnas).**
> 
> Para $k = 1, 2, \dots, n$:
> 
> 1. **Calcular elemento diagonal:**
>    $$\ell_{kk} = \sqrt{a_{kk} - \sum_{p=1}^{k-1} \ell_{kp}^2}$$
> 
> 2. **Calcular elementos por debajo de la diagonal en la columna $k$:** Para $i = k+1, \dots, n$:
>    $$\ell_{ik} = \frac{1}{\ell_{kk}} \left( a_{ik} - \sum_{p=1}^{k-1} \ell_{ip} \ell_{kp} \right)$$

> [!algoritmo]
> **Algoritmo de Cholesky (versión por filas).**
> 
> Para $i = 1, 2, \dots, n$:
> 
> 1. Para $j = 1, \dots, i-1$:
>    $$\ell_{ij} = \frac{1}{\ell_{jj}} \left( a_{ij} - \sum_{p=1}^{j-1} \ell_{ip} \ell_{jp} \right)$$
> 
> 2. Calcular elemento diagonal:
>    $$\ell_{ii} = \sqrt{a_{ii} - \sum_{p=1}^{i-1} \ell_{ip}^2}$$

Ambas versiones son algebraicamente equivalentes y tienen el mismo costo computacional. La elección depende de cómo esté almacenada la matriz en memoria (row-major vs. column-major).

> [!ejemplo]
> **Factorización de Cholesky paso a paso.**
> 
> $$A = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}$$
> 
> **$k = 1$:**
> - $\ell_{11} = \sqrt{a_{11}} = \sqrt{4} = 2$
> - $\ell_{21} = a_{21} / \ell_{11} = 2/2 = 1$
> - $\ell_{31} = a_{31} / \ell_{11} = -2/2 = -1$
> 
> **$k = 2$:**
> - $\ell_{22} = \sqrt{a_{22} - \ell_{21}^2} = \sqrt{10 - 1^2} = \sqrt{9} = 3$
> - $\ell_{32} = (a_{32} - \ell_{31}\ell_{21}) / \ell_{22} = (2 - (-1)(1)) / 3 = 3/3 = 1$
> 
> **$k = 3$:**
> - $\ell_{33} = \sqrt{a_{33} - \ell_{31}^2 - \ell_{32}^2} = \sqrt{6 - (-1)^2 - 1^2} = \sqrt{4} = 2$
> 
> Resultado:
> $$L = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ -1 & 1 & 2 \end{pmatrix}, \quad L^T = \begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$
> 
> Verificación: $L L^T = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix} = A$.

---

## Complejidad computacional

> [!teorema]
> **Costo de la factorización de Cholesky.** La factorización de Cholesky requiere aproximadamente $\frac{1}{3}n^3$ FLOPs.
> 
> **Comparación:**
> - [[Factorizacion LU|LU]] (Doolittle/Crout): $\frac{2}{3}n^3$ FLOPs.
> - Cholesky: $\frac{1}{3}n^3$ FLOPs.
> 
> Cholesky es **exactamente el doble de rápido** que LU para matrices SDP.

> [!demostracion]
> **Conteo de operaciones.**
> 
> En el paso $k$ (versión por columnas):
> - Cálculo de $\ell_{kk}$: $k-1$ multiplicaciones + $k-1$ sumas + 1 raíz cuadrada.
> - Cálculo de $\ell_{ik}$ para $i = k+1, \dots, n$: $(n-k)(k-1)$ multiplicaciones + $(n-k)(k-1)$ sumas + $(n-k)$ divisiones.
> 
> Sumando sobre $k = 1, \dots, n$:
> - Multiplicaciones y sumas: $\sum_{k=1}^{n} (n-k)(k-1) \approx \frac{n^3}{6}$ cada una.
> - Divisiones: $\sum_{k=1}^{n} (n-k) \approx \frac{n^2}{2}$.
> - Raíces cuadradas: $n$.
> 
> Total de FLOPs: $\frac{n^3}{6} + \frac{n^3}{6} + O(n^2) = \frac{n^3}{3}$.
> 
> (Las raíces cuadradas son más costosas que una multiplicación, pero son solo $n$, despreciables frente a $n^3$.)

> [!ejemplo]
> **Ahorro práctico para $n=1000$.**
> 
> - LU: $\frac{2}{3} \times 10^9 \approx 6.67 \times 10^8$ FLOPs.
> - Cholesky: $\frac{1}{3} \times 10^9 \approx 3.33 \times 10^8$ FLOPs.
> 
> Ahorro de $\approx 3.3 \times 10^8$ operaciones.

---

## Estabilidad numérica

Una propiedad notable de Cholesky es su **estabilidad sin pivoteo**.

> [!teorema]
> **Estabilidad de Cholesky.** Si $A$ es simétrica definida positiva, la factorización de Cholesky en aritmética con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$ produce un factor calculado $\tilde{L}$ que satisface:
> $$\tilde{L} \tilde{L}^T = A + \Delta A, \quad \|\Delta A\|_2 \leq c_n \cdot u \cdot \|A\|_2$$
> donde $c_n$ es una constante moderada que depende de $n$.
> 
> El **factor de crecimiento** está acotado por $1$: $\max_{i,j,k} |a_{ij}^{(k)}| \leq \max_{i,j} |a_{ij}|$.

> [!info]
> **¿Por qué Cholesky no necesita pivoteo?**
> 1. Los elementos diagonales $\ell_{kk}$ son siempre positivos y no pueden hacerse arbitrariamente pequeños en relación con la norma de $A$.
> 2. Los multiplicadores en la versión de Crout implícita son $\ell_{ik}/\ell_{kk}$, que están acotados por $1$ debido a la desigualdad de Cauchy-Schwarz en el producto interno que define $A$.
> 3. El factor de crecimiento está acotado por $1$, lo que garantiza que no hay amplificación catastrófica del error de redondeo.

Esto contrasta con la [[Acumulacion Error Redondeo Gauss|eliminación Gaussiana]] general, donde el factor de crecimiento $\rho$ puede ser grande y se requiere [[Pivoteo Parcial Total Estabilidad|pivoteo]] para controlarlo.

---

## Implementación in-place

Cholesky puede implementarse sobrescribiendo la mitad triangular inferior de $A$.

> [!algoritmo]
> **Cholesky in-place (versión por columnas).**
> 
> ```python
> import numpy as np
> 
> def cholesky_inplace(A):
>     """
>     Factorización de Cholesky in-place.
>     Al finalizar, la parte triangular inferior de A contiene L.
>     Se asume que A es simétrica definida positiva.
>     """
>     n = A.shape[0]
>     for k in range(n):
>         # Elemento diagonal
>         A[k, k] = np.sqrt(A[k, k])
>         
>         # Columna por debajo de la diagonal
>         for i in range(k+1, n):
>             A[i, k] /= A[k, k]
>         
>         # Actualizar submatriz (solo parte triangular inferior)
>         for j in range(k+1, n):
>             for i in range(j, n):
>                 A[i, j] -= A[i, k] * A[j, k]
>     
>     return A
> 
> # Ejemplo
> A = np.array([[4., 2., -2.], [2., 10., 2.], [-2., 2., 6.]])
> L = np.tril(cholesky_inplace(A.copy()))
> print("L =\n", L)
> print("L @ L.T =\n", L @ L.T)
> ```

> [!warning]
> **Precaución numérica.** En la práctica, se debe verificar que el radicando $a_{kk} - \sum \ell_{kp}^2$ sea positivo. Si es negativo o muy cercano a cero (salvo error de redondeo), la matriz no es numéricamente definida positiva, y Cholesky **fallará** con una raíz cuadrada de número negativo.

---

## Variante $LDL^T$ para matrices simétricas

Para matrices simétricas que **no son definidas positivas** (indefinidas o semidefinidas), la factorización $LL^T$ no existe (radicando negativo). Se usa la variante $LDL^T$.

> [!definicion]
> La **factorización $LDL^T$** descompone una matriz simétrica $A$ como:
> $$A = L D L^T$$
> donde $L$ es triangular inferior unitaria ($\ell_{ii}=1$) y $D$ es una matriz **diagonal** (con elementos positivos, negativos o cero).

> [!algoritmo]
> **Algoritmo $LDL^T$ (sin raíces cuadradas).**
> 
> Para $k = 1, 2, \dots, n$:
> 
> 1. **Calcular elemento diagonal de $D$:**
>    $$d_{kk} = a_{kk} - \sum_{p=1}^{k-1} \ell_{kp}^2 d_{pp}$$
> 
> 2. **Calcular columna $k$ de $L$ por debajo de la diagonal:** Para $i = k+1, \dots, n$:
>    $$\ell_{ik} = \frac{1}{d_{kk}} \left( a_{ik} - \sum_{p=1}^{k-1} \ell_{ip} \ell_{kp} d_{pp} \right)$$

**Ventajas de $LDL^T$:**
1. No requiere raíces cuadradas.
2. Aplicable a matrices simétricas indefinidas.
3. La matriz $D$ revela la inercia de $A$: número de elementos positivos, negativos y nulos en la diagonal de $D$ coincide con el número de valores propios positivos, negativos y nulos de $A$ (Ley de Inercia de Sylvester).

> [!ejemplo]
> **Factorización $LDL^T$ de una matriz simétrica indefinida.**
> 
> $$A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & -1 \\ 0 & -1 & 1 \end{pmatrix}$$
> 
> **$k = 1$:**
> - $d_{11} = a_{11} = 1$
> - $\ell_{21} = a_{21}/d_{11} = 2/1 = 2$
> - $\ell_{31} = a_{31}/d_{11} = 0/1 = 0$
> 
> **$k = 2$:**
> - $d_{22} = a_{22} - \ell_{21}^2 d_{11} = 3 - 4 \cdot 1 = -1$
> - $\ell_{32} = (a_{32} - \ell_{31}\ell_{21}d_{11}) / d_{22} = (-1 - 0) / (-1) = 1$
> 
> **$k = 3$:**
> - $d_{33} = a_{33} - \ell_{31}^2 d_{11} - \ell_{32}^2 d_{22} = 1 - 0 - 1 \cdot (-1) = 2$
> 
> Resultado:
> $$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$
> 
> Verificación: $LDL^T = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & -1 \\ 0 & -1 & 1 \end{pmatrix} = A$.
> 
> La diagonal de $D$ tiene signos $(+, -, +)$: dos positivos, uno negativo $\implies$ $A$ tiene dos valores propios positivos y uno negativo (indefinida).

---

## Pivoteo en $LDL^T$: Algoritmo de Bunch-Kaufman

Para matrices simétricas indefinidas, $LDL^T$ sin pivoteo puede ser numéricamente inestable si algún $d_{kk}$ es muy pequeño.

> [!info]
> **Pivoteo simétrico.** Para preservar la simetría, los intercambios deben aplicarse simultáneamente a filas y columnas:
> $$P A P^T = L D L^T$$
> donde $P$ es una matriz de permutación.

El algoritmo estándar es el de **Bunch-Kaufman**, que usa bloques $1 \times 1$ y $2 \times 2$ en $D$ para manejar pivotes pequeños. Está implementado en LAPACK como `dsytrf`.

---

## Cholesky para matrices banda

Cuando $A$ es SDP y además tiene estructura de banda, el factor $L$ hereda la estructura.

> [!proposicion]
> **Cholesky para matrices banda.** Si $A$ es SDP con ancho de banda $b$ ($a_{ij} = 0$ para $|i-j| > b$), entonces $L$ también tiene ancho de banda $b$.
> 
> **Costo:** $O(n b^2)$ FLOPs, en lugar de $O(n^3)$.
> 
> **Aplicación típica:** Sistemas tridiagonales SDP provenientes de [[Metodo Diferencias Finitas|diferencias finitas]] o [[Splines Cubicos Naturales Sujetos|splines cúbicos]].

> [!ejemplo]
> **Cholesky para matriz tridiagonal SDP.**
> 
> $$A = \begin{pmatrix} d_1 & e_1 & 0 & \cdots \\ e_1 & d_2 & e_2 & \cdots \\ 0 & e_2 & d_3 & \ddots \\ \vdots & \vdots & \ddots & \ddots \end{pmatrix}$$
> 
> ```python
> def cholesky_tridiagonal(d, e):
>     n = len(d)
>     L_diag = np.zeros(n)
>     L_sub = np.zeros(n-1)
>     
>     L_diag[0] = np.sqrt(d[0])
>     for i in range(n-1):
>         L_sub[i] = e[i] / L_diag[i]
>         L_diag[i+1] = np.sqrt(d[i+1] - L_sub[i]**2)
>     
>     return L_diag, L_sub
> ```

---

## Aplicaciones de la factorización de Cholesky

| Aplicación | Descripción |
|:---|:---|
| **Sistemas $Ax = b$ con $A$ SDP** | Resolver vía $L y = b$, $L^T x = y$ (costo $n^2$ por sistema después de factorizar). |
| **Generación de muestras normales multivariadas** | Si $x \sim \mathcal{N}(0, I)$, entonces $y = L x \sim \mathcal{N}(0, A)$ donde $A = L L^T$. |
| **Mínimos cuadrados por ecuaciones normales** | $A^T A x = A^T b$, con $A^T A$ SDP (aunque inestable para problemas mal condicionados; preferir [[Factorizacion QR]]). |
| **Precondicionador para gradiente conjugado** | $M = L L^T \approx A$ acelera la convergencia de [[Gradiente Conjugado]]. |
| **Cálculo de determinante** | $\det(A) = (\det(L))^2 = \prod_{i=1}^n \ell_{ii}^2$, luego $\det(A) = \prod_{i=1}^n \ell_{ii}^2$. |

---

## Comparativa final con LU

| Aspecto | [[Factorizacion LU\|LU]] (Doolittle/Crout) | Cholesky |
|:---|:---:|:---:|
| **Hipótesis** | No singular | Simétrica definida positiva |
| **Costo** | $\frac{2}{3}n^3$ | $\frac{1}{3}n^3$ |
| **¿Requiere pivoteo?** | Sí (parcial) | No |
| **Almacenamiento** | $n^2$ | $n(n+1)/2$ (mitad) |
| **Estabilidad** | Buena con pivoteo | Excelente sin pivoteo |

> [!corolario]
> Si una matriz es simétrica definida positiva, **siempre** se debe usar Cholesky en lugar de LU. Se obtiene el doble de velocidad, la mitad de almacenamiento, y estabilidad garantizada sin necesidad de pivoteo.
