---
title: Eliminacion Gaussiana
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - index
draft: false
aliases:
  - Gaussian Elimination
  - Eliminación de Gauss
  - Método de eliminación gaussiana
---

# Eliminación Gaussiana

> [!definicion]
> La **eliminación Gaussiana** es un algoritmo fundamental del álgebra lineal numérica que transforma un sistema de ecuaciones lineales $Ax = b$ en uno equivalente $Ux = c$ donde $U$ es una matriz triangular superior, mediante operaciones elementales de fila. La solución se obtiene posteriormente por **sustitución regresiva**.

El método, atribuido a Carl Friedrich Gauss (aunque usado siglos antes en China), es la base de la mayoría de los resolvedores directos modernos y constituye el punto de partida para entender la [[Factorizacion LU]].

---

## Visión general del algoritmo

Dado un sistema $Ax = b$ con $A \in \mathbb{R}^{n \times n}$ no singular, la eliminación Gaussiana procede en $n-1$ etapas:

1. **Fase de eliminación (forward elimination):** Para $k = 1, 2, \dots, n-1$, se elimina la incógnita $x_k$ de las ecuaciones $k+1, \dots, n$ restando múltiplos adecuados de la fila $k$.
2. **Fase de sustitución regresiva (back substitution):** Se resuelve $Ux = c$ desde $x_n$ hasta $x_1$.

> [!teoria]
> **Complejidad computacional.**
> La eliminación Gaussiana requiere aproximadamente $\frac{2}{3}n^3 + O(n^2)$ operaciones de punto flotante. Este costo $O(n^3)$ la hace prohibitiva para sistemas extremadamente grandes ($n > 10^5$), donde se prefieren [[Metodos Iterativos|métodos iterativos]].

---

## Algoritmo básico sin pivoteo

El algoritmo en su forma más simple asume que todos los pivotes $a_{kk}^{(k)}$ son no nulos.

> [!algoritmo]
> **Eliminación Gaussiana sin pivoteo.**
> 
> **Entrada:** Matriz $A \in \mathbb{R}^{n \times n}$, vector $b \in \mathbb{R}^n$.
> **Salida:** Vector solución $x \in \mathbb{R}^n$.
> 
> 1. Para $k = 1, 2, \dots, n-1$:
>     - Para $i = k+1, \dots, n$:
>         - $m_{ik} = a_{ik} / a_{kk}$
>         - Para $j = k+1, \dots, n$:
>             - $a_{ij} = a_{ij} - m_{ik} \cdot a_{kj}$
>         - $b_i = b_i - m_{ik} \cdot b_k$
> 2. $x_n = b_n / a_{nn}$
> 3. Para $i = n-1, n-2, \dots, 1$:
>     - $x_i = \left( b_i - \sum_{j=i+1}^{n} a_{ij} x_j \right) / a_{ii}$

> [!warning]
> **Limitaciones del algoritmo sin pivoteo.**
> 4. Falla si algún pivote $a_{kk}^{(k)} = 0$, incluso si la matriz es no singular.
> 5. Es numéricamente inestable si algún pivote es muy pequeño, como se ilustra en [[Pivoteo Parcial Total Estabilidad]].
> 6. La [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]] en la actualización $a_{ij} - m_{ik} a_{kj}$ puede destruir la precisión.

---

## Estabilidad numérica y pivoteo

La eliminación Gaussiana sin pivoteo es inherentemente inestable para muchas matrices prácticas. El **pivoteo** corrige esta deficiencia.

> [!info]
> **Estrategias de pivoteo.**
> - **[[Pivoteo Parcial Total Estabilidad|Pivoteo parcial]]:** Intercambiar filas para colocar el mayor elemento de la columna como pivote. Es el estándar industrial.
> - **[[Pivoteo Parcial Total Estabilidad|Pivoteo total]]:** Intercambiar filas y columnas para colocar el mayor elemento de toda la submatriz como pivote. Más estable pero más costoso.
> - **Rook pivoting:** Estrategia intermedia con buen balance costo-estabilidad.

El análisis detallado del factor de crecimiento y las cotas de error se desarrolla en [[Pivoteo Parcial Total Estabilidad]].

---

## Relación con la factorización LU

La eliminación Gaussiana está íntimamente ligada a la [[Factorizacion LU]].

> [!proposicion]
> **Equivalencia con LU.**
> Los multiplicadores $m_{ik}$ generados durante la eliminación forman una matriz triangular inferior unitaria $L$ tal que:
> $$A = L U$$
> donde $U$ es la matriz triangular superior resultante de la eliminación.
> 
> Si se aplica pivoteo parcial, la factorización es $PA = LU$, donde $P$ es una matriz de permutación.

Esta conexión es fundamental porque:
- Permite reutilizar la factorización para múltiples vectores $b$ (costo $O(n^2)$ por sistema adicional).
- Es la base de algoritmos eficientes para calcular [[Determinante y Matriz Inversa|determinantes]] e [[Determinante y Matriz Inversa|inversas]].
- Facilita el [[Analisis Error Directos|análisis de error]] hacia atrás.

---

## Sustitución regresiva y progresiva

Una vez obtenido el sistema triangular $Ux = c$ (o $Ly = b$ en el contexto LU), la solución se obtiene por sustitución.

> [!algoritmo]
> **Sustitución regresiva (Back Substitution).**
> 
> Dado $U \in \mathbb{R}^{n \times n}$ triangular superior no singular y $c \in \mathbb{R}^n$:
> 
> 1. $x_n = c_n / u_{nn}$
> 2. Para $i = n-1, n-2, \dots, 1$:
>     $$x_i = \frac{c_i - \sum_{j=i+1}^{n} u_{ij} x_j}{u_{ii}}$$
> 
> **Complejidad:** $\frac{n^2}{2} + O(n)$ operaciones.

> [!algoritmo]
> **Sustitución progresiva (Forward Substitution).**
> 
> Dado $L \in \mathbb{R}^{n \times n}$ triangular inferior unitaria y $b \in \mathbb{R}^n$:
> 
> 1. $y_1 = b_1$
> 2. Para $i = 2, 3, \dots, n$:
>     $$y_i = b_i - \sum_{j=1}^{i-1} \ell_{ij} y_j$$
> 
> **Complejidad:** $\frac{n^2}{2} + O(n)$ operaciones.

---

## Análisis de error

El error en la solución calculada $\tilde{x}$ por eliminación Gaussiana con pivoteo parcial satisface una cota de error hacia atrás.

> [!teorema]
> **Estabilidad hacia atrás (Wilkinson, 1961).**
> Sea $\tilde{x}$ la solución calculada mediante eliminación Gaussiana con pivoteo parcial en aritmética con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$. Entonces $\tilde{x}$ es la solución exacta de un sistema perturbado:
> $$(A + \Delta A)\tilde{x} = b, \quad \|\Delta A\|_\infty \leq \rho \cdot u \cdot \|A\|_\infty$$
> donde $\rho$ es el **factor de crecimiento**.

> [!corolario]
> **Error hacia adelante.**
> Combinando con el [[Condicionamiento Numerico Numero Condicion|número de condición]] $\kappa_\infty(A)$:
> $$\frac{\|\tilde{x} - x\|_\infty}{\|x\|_\infty} \leq \frac{\rho \cdot u \cdot \kappa_\infty(A)}{1 - \rho \cdot u \cdot \kappa_\infty(A)}$$
> 
> Para matrices bien condicionadas ($\kappa \approx 1$) y pivoteo parcial ($\rho$ moderado), la eliminación Gaussiana produce soluciones con precisión cercana a $u$.

---

## Variantes y optimizaciones

> [!info]
> **Implementaciones modernas.**
> - **Eliminación de Gauss-Jordan:** Continúa la eliminación hasta obtener una matriz diagonal (o identidad). Requiere $\approx n^3$ operaciones, más que la Gaussiana estándar. Se usa principalmente para calcular inversas.
> - **Eliminación por bloques:** Aprovecha la jerarquía de memoria del hardware (caché) operando sobre submatrices. Esencial para alto rendimiento en bibliotecas como LAPACK.
> - **Eliminación para matrices banda:** Explota la estructura dispersa para reducir complejidad a $O(n \cdot b^2)$ donde $b$ es el ancho de banda.
> - **Eliminación para matrices simétricas:** Variantes como la [[Factorizacion Cholesky Matrices Definidas Positivas|factorización de Cholesky]] ($A = LL^T$) o la factorización $LDL^T$ para matrices indefinidas.

---

## Ejemplo ilustrativo paso a paso

> [!ejemplo]
> **Resolver $Ax = b$ con eliminación Gaussiana y pivoteo parcial.**
> 
> $$A = \begin{pmatrix} 2 & 1 & -1 \\ -3 & -1 & 2 \\ -2 & 1 & 2 \end{pmatrix}, \quad b = \begin{pmatrix} 8 \\ -11 \\ -3 \end{pmatrix}$$
> 
> **Paso 1: Pivoteo parcial en columna 1.**
> Mayor valor absoluto en columna 1: $|-3| = 3$ en fila 2. Intercambiar fila 1 y fila 2.
> 
> Matriz aumentada después del intercambio:
> $$\begin{pmatrix} -3 & -1 & 2 & | & -11 \\ 2 & 1 & -1 & | & 8 \\ -2 & 1 & 2 & | & -3 \end{pmatrix}$$
> 
> **Paso 2: Eliminación en columna 1.**
> - $m_{21} = 2/(-3) = -2/3$
> - $m_{31} = -2/(-3) = 2/3$
> 
> Fila 2: $(2, 1, -1, 8) - (-2/3)(-3, -1, 2, -11) = (0, 1/3, 1/3, 2/3)$
> Fila 3: $(-2, 1, 2, -3) - (2/3)(-3, -1, 2, -11) = (0, 5/3, 2/3, 13/3)$
> 
> Matriz resultante:
> $$\begin{pmatrix} -3 & -1 & 2 & | & -11 \\ 0 & 1/3 & 1/3 & | & 2/3 \\ 0 & 5/3 & 2/3 & | & 13/3 \end{pmatrix}$$
> 
> **Paso 3: Pivoteo parcial en columna 2.**
> Mayor valor absoluto en subcolumna 2: $|5/3| = 5/3$ en fila 3. Intercambiar fila 2 y fila 3.
> 
> Matriz después del intercambio:
> $$\begin{pmatrix} -3 & -1 & 2 & | & -11 \\ 0 & 5/3 & 2/3 & | & 13/3 \\ 0 & 1/3 & 1/3 & | & 2/3 \end{pmatrix}$$
> 
> **Paso 4: Eliminación en columna 2.**
> - $m_{32} = (1/3)/(5/3) = 1/5$
> 
> Fila 3: $(0, 1/3, 1/3, 2/3) - (1/5)(0, 5/3, 2/3, 13/3) = (0, 0, 1/5, -1/5)$
> 
> Matriz triangular superior:
> $$\begin{pmatrix} -3 & -1 & 2 & | & -11 \\ 0 & 5/3 & 2/3 & | & 13/3 \\ 0 & 0 & 1/5 & | & -1/5 \end{pmatrix}$$
> 
> **Paso 5: Sustitución regresiva.**
> - $x_3 = (-1/5) / (1/5) = -1$
> - $x_2 = (13/3 - (2/3)(-1)) / (5/3) = (13/3 + 2/3) / (5/3) = 15/5 = 3$
> - $x_1 = (-11 - (-1)(3) - 2(-1)) / (-3) = (-11 + 3 + 2) / (-3) = -6 / (-3) = 2$
> 
> Solución: $x = (2, 3, -1)^T$.

---

## Limitaciones y alternativas

A pesar de su ubicuidad, la eliminación Gaussiana tiene limitaciones importantes.

> [!warning]
> **Cuándo NO usar eliminación Gaussiana.**
> 1. **Sistemas muy grandes y dispersos:** El [[Relleno Matrices Dispersas|relleno]] durante la eliminación destruye la dispersidad, haciendo el método inviable en memoria y tiempo.
> 2. **Sistemas mal condicionados:** Si $\kappa(A) \gg 1/u$, ningún método directo puede dar precisión aceptable (Ver [[Condicionamiento Numerico Numero Condicion]]).
> 3. **Múltiples lados derechos secuenciales:** Si se requiere resolver $Ax = b_i$ para muchos $b_i$ que se generan uno tras otro, es mejor usar [[Factorizacion LU]] explícitamente o métodos iterativos.
> 4. **Sistemas sobredeterminados o subdeterminados:** Requieren enfoques como [[Factorizacion QR]] o [[Valores Singulares y Descomposicion SVD|SVD]].

Para estos casos, existen alternativas como:
- [[Metodos Iterativos]] ([[Jacobi]], [[Gauss Seidel]], [[Gradiente Conjugado]]).
- Métodos de [[Factorizacion QR]] para mínimos cuadrados.
- [[Metodo Disparo Shooting]] y [[Metodo Diferencias Finitas]] para problemas de contorno.

---

## Implementaciones en bibliotecas estándar

| Biblioteca | Rutina | Descripción |
|:---|:---|:---|
| LAPACK | `dgesv` | Resuelve $Ax = b$ con pivoteo parcial |
| LAPACK | `dgetrf` | Calcula $PA = LU$ |
| LAPACK | `dgetrs` | Resuelve $Ax = b$ usando $LU$ precalculada |
| MATLAB | `A \ b` | Backslash: pivoteo parcial para matrices cuadradas |
| NumPy/SciPy | `numpy.linalg.solve` | Basado en `dgesv` de LAPACK |
| Eigen (C++) | `PartialPivLU` | Factorización LU con pivoteo parcial |

> [!ejemplo]
> **Uso en Python con NumPy.**
> ```python
> import numpy as np
> 
> A = np.array([[2.0, 1.0, -1.0],
>               [-3.0, -1.0, 2.0],
>               [-2.0, 1.0, 2.0]])
> b = np.array([8.0, -11.0, -3.0])
> 
> x = np.linalg.solve(A, b)
> print(f"Solución: {x}")
> ```
> 
> Salida: `Solución: [ 2.  3. -1.]`
