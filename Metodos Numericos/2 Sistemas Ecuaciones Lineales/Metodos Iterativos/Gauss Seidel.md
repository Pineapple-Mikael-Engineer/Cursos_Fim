---
title: Método de Gauss-Seidel
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - gauss-seidel
draft: false
aliases:
  - Gauss-Seidel
  - Método de Gauss-Seidel
  - Gauss-Seidel iteration
---

# Método de Gauss-Seidel

> [!definicion]
> El **método de Gauss-Seidel** es un método iterativo para resolver $Ax = b$. Al igual que Jacobi, se basa en la descomposición $A = D - L - U$, donde:
> - $D$ es la matriz diagonal de $A$
> - $-L$ es la parte estrictamente triangular inferior
> - $-U$ es la parte estrictamente triangular superior
>
> La iteración se define tomando $M = D - L$, lo que produce:
> $$(D - L) y^{(k+1)} = U y^{(k)} + b$$

---

## Forma algebraica (componente a componente)

Para cada componente $i = 1, \dots, n$, la ecuación $i$-ésima del sistema $Ax = b$ es:
$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{ii}x_i + \cdots + a_{in}x_n = b_i$$

Despejando $x_i$:
$$x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j - \sum_{j=i+1}^{n} a_{ij} x_j \right)$$

La diferencia con Jacobi es que Gauss-Seidel utiliza **los valores ya actualizados** de $x_1, \dots, x_{i-1}$ en la misma iteración:

$$y_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} y_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} y_j^{(k)} \right), \quad i = 1, 2, \dots, n$$

> [!info]
> **Característica clave:** Cada componente $y_i^{(k+1)}$ se calcula usando:
> - Los valores ya actualizados $y_1^{(k+1)}, \dots, y_{i-1}^{(k+1)}$ (de la misma iteración)
> - Los valores anteriores $y_{i+1}^{(k)}, \dots, y_n^{(k)}$ (de la iteración previa)
>
> Esto **no** permite paralelizar completamente, pero acelera la convergencia.

---

## Forma vectorial (matricial)

Con la partición $A = D - L - U$, la iteración de Gauss-Seidel es:
$$(D - L) y^{(k+1)} = U y^{(k)} + b$$

Multiplicando por $(D - L)^{-1}$:
$$y^{(k+1)} = \underbrace{(D - L)^{-1} U}_{T_{GS}} y^{(k)} + \underbrace{(D - L)^{-1} b}_{c_{GS}}$$

> [!info]
> **Forma alternativa:** Como $U = D - L - A$, se tiene:
> $$T_{GS} = (D - L)^{-1} (D - L - A) = I - (D - L)^{-1} A$$
> $$c_{GS} = (D - L)^{-1} b$$

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
> $$y_2^{(k+1)} = \frac{2 - (-1) y_1^{(k+1)} - (-1) y_3^{(k)}}{4} = \frac{2 + y_1^{(k+1)} + y_3^{(k)}}{4}$$
> $$y_3^{(k+1)} = \frac{14 - (-1) y_2^{(k+1)}}{4} = \frac{14 + y_2^{(k+1)}}{4}$$
>
> Nótese que $y_2^{(k+1)}$ usa $y_1^{(k+1)}$ (recién calculado) y $y_3^{(k+1)}$ usa $y_2^{(k+1)}$.
>
> **Iteración desde $y^{(0)} = (0, 0, 0)^T$.**
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ | $y_3^{(k)}$ | $\|y^{(k)} - x\|_\infty$ |
> |:---|:---:|:---:|:---:|:---:|
> | 0 | 0.000 | 0.000 | 0.000 | 4.000 |
> | 1 | 1.500 | 1.250 | 3.8125 | 0.750 |
> | 2 | 1.8125 | 1.90625 | 3.9765625 | 0.1875 |
> | 3 | 1.9765625 | 1.98828125 | 3.9970703125 | 0.0234375 |
> | 4 | 1.9970703125 | 1.99853515625 | 3.9996337890625 | 0.0029296875 |
> | 5 | 1.9996337890625 | 1.99981689453125 | 3.9999542236328125 | 0.0003662109375 |
> | 6 | 1.9999542236328125 | 1.9999771118164062 | 3.9999942779541016 | 0.0000457763671875 |
>
> **Comparación con Jacobi.**
>
> | Iteración | Error Jacobi | Error Gauss-Seidel |
> |:---:|:---:|:---:|
> | 1 | 1.500 | 0.750 |
> | 2 | 0.375 | 0.1875 |
> | 3 | 0.1875 | 0.0234375 |
> | 4 | 0.046875 | 0.0029296875 |
> | 5 | 0.0234375 | 0.0003662109375 |
> | 6 | 0.005859375 | 0.0000457763671875 |
>
> Gauss-Seidel converge más rápido que Jacobi al aprovechar los valores recién calculados en cada iteración.
## Matriz de iteración y radio espectral

> [!teorema]
> La matriz de iteración de Gauss-Seidel es:
> $$T_{GS} = (D - L)^{-1} U$$
>
> El método converge para cualquier $y^{(0)}$ si y solo si $\rho(T_{GS}) < 1$.

> [!ejemplo]
> Para la matriz del ejemplo anterior:
>
> $$D - L = \begin{pmatrix} 4 & 0 & 0 \\ -1 & 4 & 0 \\ 0 & -1 & 4 \end{pmatrix}, \quad U = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
>
> Calculando $T_{GS} = (D - L)^{-1} U$:
> $$(D - L)^{-1} = \begin{pmatrix} 1/4 & 0 & 0 \\ 1/16 & 1/4 & 0 \\ 1/64 & 1/16 & 1/4 \end{pmatrix}$$
>
> $$T_{GS} = \begin{pmatrix} 1/4 & 0 & 0 \\ 1/16 & 1/4 & 0 \\ 1/64 & 1/16 & 1/4 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1/4 & 0 \\ 0 & 1/16 & 1/4 \\ 0 & 1/64 & 1/16 \end{pmatrix}$$
>
> Los autovalores de $T_{GS}$ son las raíces de $\det(T_{GS} - \lambda I) = -\lambda^3 = 0$, por lo tanto $\lambda = 0$ (triple). Entonces $\rho(T_{GS}) = 0$, lo que indica convergencia en un número finito de iteraciones para este caso particular (matriz tridiagonal simétrica definida positiva).

El análisis detallado del radio espectral se desarrolla en [[Criterio Radio Espectral Convergencia]].

---

## Relación con Jacobi

> [!teorema] [Stein-Rosenberg]
> Para matrices con $a_{ij} \leq 0$ para $i \neq j$ (matrices de tipo M) y $a_{ii} > 0$, se cumple:
> $$0 \leq \rho(T_{GS}) \leq \rho(T_J) < 1 \quad \text{o} \quad 1 \leq \rho(T_J) \leq \rho(T_{GS})$$
>
> Es decir, si Jacobi converge, Gauss-Seidel converge más rápido (o igual).

La comparación detallada se desarrolla en [[Comparacion Asintotica Convergencia Jacobi]].

---

## Algoritmo

> [!algoritmo]
> **Gauss-Seidel en pseudocódigo.**
> ```
> función gauss_seidel(A, b, y0, tol, max_iter)
>     n = tamaño(A)
>     y = y0
>     para k = 1 hasta max_iter
>         y_nuevo = copia(y)
>         para i = 1 hasta n
>             suma = b[i]
>             para j = 1 hasta i-1
>                 suma = suma - A[i][j] * y_nuevo[j]
>             para j = i+1 hasta n
>                 suma = suma - A[i][j] * y[j]
>             y_nuevo[i] = suma / A[i][i]
>         si ||y_nuevo - y|| < tol * ||y_nuevo||
>             retornar y_nuevo, k
>         y = y_nuevo
>     retornar y, max_iter
> ```

> [!algoritmo]
> **Implementación en Python (sobrescribiendo en el mismo vector).**
> ```python
> import numpy as np
> 
> def gauss_seidel(A, b, y0, tol=1e-10, max_iter=1000):
>     n = len(b)
>     y = y0.copy()
>     
>     for k in range(max_iter):
>         y_old = y.copy()
>         for i in range(n):
>             suma = b[i]
>             for j in range(n):
>                 if j != i:
>                     suma -= A[i, j] * y[j]
>             y[i] = suma / A[i, i]
>         
>         if np.linalg.norm(y - y_old) < tol * np.linalg.norm(y):
>             return y, k + 1
>     
>     return y, max_iter
> 
> A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 4.]])
> b = np.array([6., 2., 14.])
> y0 = np.zeros(3)
> sol, iters = gauss_seidel(A, b, y0)
> print(f"Solución: {sol}")
> print(f"Iteraciones: {iters}")
> ```
>
> **Ventaja de memoria:** A diferencia de Jacobi, no se necesita un vector auxiliar `y_new`; se puede sobrescribir `y` directamente porque los valores actualizados se usan inmediatamente.

---

## Condiciones de convergencia

> [!teorema] [Diagonal dominante estricta]
> Si $A$ es **estrictamente diagonal dominante** por filas:
> $$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i$$
> entonces el método de Gauss-Seidel converge.

> [!teorema] [Matrices simétricas definidas positivas]
> Si $A$ es **simétrica definida positiva**, entonces el método de Gauss-Seidel converge para cualquier $y^{(0)}$.

> [!teorema] [Matrices irreductiblemente diagonal dominantes]
> Si $A$ es **irreductible** y **débilmente diagonal dominante** ($|a_{ii}| \geq \sum_{j \neq i} |a_{ij}|$ con al menos una desigualdad estricta), entonces Gauss-Seidel converge.

La demostración de estos teoremas se encuentra en [[Teorema Diagonal Dominante Estricta]].

---

## Ventajas y desventajas

| Ventajas | Desventajas |
|:---|:---|
| Converge más rápido que Jacobi en general | No es paralelizable (las actualizaciones son secuenciales) |
| Requiere menos memoria (puede sobrescribir el vector de iteración) | El orden de las ecuaciones afecta la convergencia |
| Converge para todas las matrices simétricas definidas positivas | Puede ser inestable para ciertos tipos de matrices |
| La tasa de convergencia es asintóticamente el doble que Jacobi para muchas matrices | Implementación secuencial por naturaleza |

---

## Resumen

| Elemento | Descripción |
|:---|:---|
| Forma algebraica | $y_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} y_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} y_j^{(k)} \right)$ |
| Forma vectorial | $y^{(k+1)} = (D - L)^{-1} U y^{(k)} + (D - L)^{-1} b$ |
| Matriz de iteración | $T_{GS} = (D - L)^{-1} U = I - (D - L)^{-1} A$ |
| Condición de convergencia | $\rho(T_{GS}) < 1$ |
| Condición suficiente | Diagonal dominante estricta, o simétrica definida positiva |
| Paralelismo | Ninguno (actualizaciones secuenciales) |
| Relación con Jacobi | $\rho(T_{GS}) \leq \rho(T_J)$ cuando Jacobi converge (Stein-Rosenberg) |

> [!corolario]
> El método de Gauss-Seidel es una mejora práctica sobre Jacobi que utiliza inmediatamente los valores actualizados. Su convergencia es típicamente más rápida, y para matrices simétricas definidas positivas está siempre garantizada. La comparación cuantitativa con Jacobi, incluyendo el teorema de Stein-Rosenberg y ejemplos donde la diferencia es dramática, se desarrolla en [[Comparacion Asintotica Convergencia Jacobi]]. Las condiciones de convergencia se profundizan en [[Teorema Diagonal Dominante Estricta]].


  
  
$$  
\|(D-L)^{-1}U\|<1  
\Rightarrow  
\rho(T)<1  
$$