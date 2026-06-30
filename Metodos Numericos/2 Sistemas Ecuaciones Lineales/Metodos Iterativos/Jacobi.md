---
title: Método de Jacobi
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - jacobi
draft: false
aliases:
  - Jacobi
  - Método de Jacobi
  - Jacobi iteration
---

# Método de Jacobi

> [!definicion]
> El **método de Jacobi** es un método iterativo para resolver $Ax = b$. Se basa en descomponer $A = D - E - F$ donde:
> - $D$ es la matriz diagonal de $A$ ($d_{ii} = a_{ii}$, $d_{ij}=0$ para $i \neq j$)
> - $-E$ es la parte estrictamente triangular inferior
> - $-F$ es la parte estrictamente triangular superior
>
> La iteración se define tomando $M = D$, lo que produce:
> $$D y^{(k+1)} = (E + F) y^{(k)} + b$$

---

## Forma algebraica (componente a componente)

Para cada componente $i = 1, \dots, n$, la ecuación $i$-ésima del sistema $Ax = b$ es:
$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{ii}x_i + \cdots + a_{in}x_n = b_i$$

Despejando $x_i$:
$$x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} x_j \right)$$

Esto sugiere la iteración de Jacobi:
$$y_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} y_j^{(k)} \right), \quad i = 1, 2, \dots, n$$

> [!info]
> **Característica clave:** Todas las componentes $y_i^{(k+1)}$ se calculan usando **exclusivamente** valores de la iteración anterior $y_j^{(k)}$. Esto permite actualizar todas las componentes en paralelo.

---

## Forma vectorial (matricial)

Definiendo:
- $D = \operatorname{diag}(a_{11}, a_{22}, \dots, a_{nn})$
- $L = -E$ (triangular inferior con ceros en la diagonal)
- $U = -F$ (triangular superior con ceros en la diagonal)

Entonces $A = D - L - U$. La iteración de Jacobi en forma matricial es:
$$D y^{(k+1)} = (L + U) y^{(k)} + b$$

Multiplicando por $D^{-1}$:
$$y^{(k+1)} = \underbrace{D^{-1}(L + U)}_{T_J} y^{(k)} + \underbrace{D^{-1}b}_{c_J}$$

> [!info]
> **Forma alternativa:** Como $L + U = D - A$, se tiene:
> $$T_J = D^{-1}(D - A) = I - D^{-1}A$$
> $$c_J = D^{-1}b$$

---

## Ejemplo

> [!ejemplo]
> Resuélvase $Ax = b$ con:
> $$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}, \qquad b = \begin{pmatrix} 6 \\ 2 \\ 14 \end{pmatrix}$$
>
> La solución exacta es $x = (2, 2, 4)^T$.
>
> **Forma algebraica.**
>
> $$y_1^{(k+1)} = \frac{6 - (-1) y_2^{(k)}}{4} = \frac{6 + y_2^{(k)}}{4}$$
> $$y_2^{(k+1)} = \frac{2 - (-1) y_1^{(k)} - (-1) y_3^{(k)}}{4} = \frac{2 + y_1^{(k)} + y_3^{(k)}}{4}$$
> $$y_3^{(k+1)} = \frac{14 - (-1) y_2^{(k)}}{4} = \frac{14 + y_2^{(k)}}{4}$$
>
> **Forma vectorial.**
>
> $$D = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \quad L + U = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$
>
> $$T_J = D^{-1}(L+U) = \begin{pmatrix} 0 & 1/4 & 0 \\ 1/4 & 0 & 1/4 \\ 0 & 1/4 & 0 \end{pmatrix}, \quad c_J = D^{-1}b = \begin{pmatrix} 6/4 \\ 2/4 \\ 14/4 \end{pmatrix} = \begin{pmatrix} 1.5 \\ 0.5 \\ 3.5 \end{pmatrix}$$
>
> **Iteración desde $y^{(0)} = (0, 0, 0)^T$.**
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ | $y_3^{(k)}$ | $\|y^{(k)} - x\|_\infty$ |
> |:---|:---:|:---:|:---:|:---:|
> | 0 | 0.000 | 0.000 | 0.000 | 4.000 |
> | 1 | 1.500 | 0.500 | 3.500 | 1.500 |
> | 2 | 1.625 | 1.750 | 3.625 | 0.375 |
> | 3 | 1.9375 | 1.8125 | 3.9375 | 0.1875 |
> | 4 | 1.953125 | 1.96875 | 3.953125 | 0.046875 |
> | 5 | 1.9921875 | 1.9765625 | 3.9921875 | 0.0234375 |
>
> **Verificación del radio espectral.**
>
> Los autovalores de $T_J$ satisfacen $\det(T_J - \lambda I) = -\lambda (\lambda^2 - 1/8) = 0$, por lo tanto $\lambda = 0, \pm 1/\sqrt{8} \approx \pm 0.3536$. Entonces $\rho(T_J) \approx 0.3536 < 1$, lo que garantiza convergencia.

---

## Algoritmo

> [!algoritmo]
> **Jacobi en pseudocódigo.**
> ```
> función jacobi(A, b, y0, tol, max_iter)
>     n = tamaño(A)
>     y = y0
>     para k = 1 hasta max_iter
>         para i = 1 hasta n
>             suma = b[i]
>             para j = 1 hasta n
>                 si j != i
>                     suma = suma - A[i][j] * y[j]
>             y_nuevo[i] = suma / A[i][i]
>         si ||y_nuevo - y|| < tol * ||y_nuevo||
>             retornar y_nuevo, k
>         y = y_nuevo
>     retornar y, max_iter
> ```

> [!algoritmo]
> **Implementación en Python.**
> ```python
> import numpy as np
> 
> def jacobi(A, b, y0, tol=1e-10, max_iter=1000):
>     n = len(b)
>     y = y0.copy()
>     
>     for k in range(max_iter):
>         y_new = np.zeros_like(y)
>         for i in range(n):
>             suma = b[i]
>             for j in range(n):
>                 if j != i:
>                     suma -= A[i, j] * y[j]
>             y_new[i] = suma / A[i, i]
>         
>         if np.linalg.norm(y_new - y) < tol * np.linalg.norm(y_new):
>             return y_new, k + 1
>         y = y_new
>     
>     return y, max_iter
> 
> A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 4.]])
> b = np.array([6., 2., 14.])
> y0 = np.zeros(3)
> sol, iters = jacobi(A, b, y0)
> print(f"Solución: {sol}")
> print(f"Iteraciones: {iters}")
> ```

---

## Matriz de iteración y radio espectral

> [!teorema]
> La matriz de iteración de Jacobi es:
> $$T_J = D^{-1}(L+U) = I - D^{-1}A$$
>
> El método converge para cualquier $y^{(0)}$ si y solo si $\rho(T_J) < 1$.

El estudio detallado del radio espectral se desarrolla en [[Criterio Radio Espectral Convergencia]].

---

## Condiciones de convergencia

> [!teorema] [Diagonal dominante estricta]
> Si $A$ es **estrictamente diagonal dominante** por filas:
> $$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i$$
> entonces el método de Jacobi converge.

> [!teorema] [Matrices simétricas definidas positivas]
> Si $A$ es simétrica definida positiva, entonces el método de Jacobi converge si y solo si $2D - A$ es definida positiva.

La demostración se encuentra en [[Teorema Diagonal Dominante Estricta]].

---

## Ventajas y desventajas

| Ventajas | Desventajas |
|:---|:---|
| Fácil de implementar | Convergencia lenta para muchas matrices |
| Altamente paralelizable (cada componente se actualiza independientemente) | Requiere $a_{ii} \neq 0$ para todo $i$ |
| No requiere almacenamiento adicional significativo | Puede no converger si $A$ no cumple condiciones suficientes |
| El error disminuye monótonamente en ciertas normas | El método de [[Gauss Seidel]] suele converger más rápido |

---

## Resumen

| Elemento | Descripción |
|:---|:---|
| Forma algebraica | $y_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} y_j^{(k)} \right)$ |
| Forma vectorial | $y^{(k+1)} = D^{-1}(L+U) y^{(k)} + D^{-1}b$ |
| Matriz de iteración | $T_J = I - D^{-1}A$ |
| Condición de convergencia | $\rho(T_J) < 1$ |
| Condición suficiente | Diagonal dominante estricta |
| Paralelismo | Completo (todas las componentes se actualizan simultáneamente) |

> [!corolario]
> El método de Jacobi es el punto de partida natural para el estudio de métodos iterativos. Su simplicidad permite entender el marco de iteración de punto fijo, mientras que su análisis de convergencia motiva condiciones como la diagonal dominante. La comparación con [[Gauss Seidel]] muestra cómo el uso inmediato de valores actualizados puede acelerar la convergencia, tema desarrollado en [[Comparacion Asintotica Convergencia Jacobi]].