---
title: Metodo Potencia Directo
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - index
draft: false
aliases:
  - Método de la potencia
  - Power method
  - Iteración por potencias
---

# Método de la Potencia Directo

> [!definicion]
> El **método de la potencia** es un algoritmo iterativo para aproximar el autovalor de mayor módulo (autovalor dominante) $\lambda_1$ de una matriz $A \in \mathbb{R}^{n \times n}$, junto con su correspondiente autovector $v_1$.

---

## Ejemplo

> [!ejemplo]
> **Calcular el autovalor dominante de $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.**
>
> Los autovalores exactos son $\lambda_1 = 3$ (dominante) y $\lambda_2 = 1$.
>
> Partiendo de $y^{(0)} = (1, 0)^T$ y normalizando en cada paso:
>
> | $k$ | $y^{(k)}$ (normalizado) | $\lambda^{(k)} = y^{(k)T} A y^{(k)}$ |
> |:---|:---|:---|
> | 0 | (1.000, 0.000) | — |
> | 1 | (0.894, 0.447) | 2.500 |
> | 2 | (0.780, 0.625) | 2.900 |
> | 3 | (0.732, 0.681) | 2.980 |
> | 4 | (0.716, 0.698) | 2.996 |
> | 5 | (0.708, 0.706) | 2.999 |
>
> La sucesión converge a $(1/\sqrt{2}, 1/\sqrt{2}) \approx (0.707, 0.707)$, el autovector unitario, y $\lambda^{(k)} \to 3$.

---

## En qué consiste el método

> [!teoria]
> Dada una matriz $A$ diagonalizable con autovalores $|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|$, el método genera una sucesión de vectores mediante:
> $$y^{(k+1)} = A y^{(k)}$$
>
> Para evitar el crecimiento (o decrecimiento) exponencial de las componentes, en la práctica se normaliza:
> $$y^{(k+1)} = \frac{A y^{(k)}}{\|A y^{(k)}\|}$$
>
> El autovalor dominante se estima mediante el **cociente de Rayleigh**:
> $$\lambda^{(k)} = \frac{y^{(k)T} A y^{(k)}}{y^{(k)T} y^{(k)}}$$
> que, cuando $y^{(k)}$ está normalizado ($\|y^{(k)}\| = 1$), se reduce a $\lambda^{(k)} = y^{(k)T} A y^{(k)}$.

---

## Demostración de convergencia

> [!teorema]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores $\lambda_1, \lambda_2, \dots, \lambda_n$ que satisfacen:
> $$|\lambda_1| > |\lambda_2| \geq |\lambda_3| \geq \cdots \geq |\lambda_n|$$
> Sea $\{v_1, v_2, \dots, v_n\}$ una base de autovectores asociados. Sea $y^{(0)} \in \mathbb{R}^n$ un vector con componente no nula en la dirección de $v_1$, es decir:
> $$y^{(0)} = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n, \quad c_1 \neq 0$$
>
> Entonces la sucesión definida por $z^{(k)} = A^k y^{(0)}$ satisface:
> $$\lim_{k \to \infty} \frac{z^{(k)}}{\|z^{(k)}\|} = \frac{v_1}{\|v_1\|}$$
> y
> $$\lim_{k \to \infty} \frac{z^{(k)T} A z^{(k)}}{z^{(k)T} z^{(k)}} = \lambda_1$$

> [!demostracion]
> **Paso 1: Expresión de $A^k y^{(0)}$ en la base de autovectores.**
>
> Como $A v_i = \lambda_i v_i$, se tiene $A^k v_i = \lambda_i^k v_i$. Aplicando $A^k$ a $y^{(0)}$:
> $$A^k y^{(0)} = A^k (c_1 v_1 + c_2 v_2 + \cdots + c_n v_n) = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \cdots + c_n \lambda_n^k v_n$$
>
> **Paso 2: Factorización del término dominante.**
>
> Factorizando $\lambda_1^k$:
> $$A^k y^{(0)} = \lambda_1^k \left( c_1 v_1 + c_2 \left( \frac{\lambda_2}{\lambda_1} \right)^k v_2 + \cdots + c_n \left( \frac{\lambda_n}{\lambda_1} \right)^k v_n \right)$$
>
> **Paso 3: Comportamiento asintótico del vector.**
>
> Como $|\lambda_2/\lambda_1| < 1$, se tiene $(\lambda_i/\lambda_1)^k \to 0$ para todo $i \geq 2$. Por lo tanto:
> $$\lim_{k \to \infty} \left( c_1 v_1 + c_2 \left( \frac{\lambda_2}{\lambda_1} \right)^k v_2 + \cdots + c_n \left( \frac{\lambda_n}{\lambda_1} \right)^k v_n \right) = c_1 v_1$$
>
> **Paso 4: Convergencia de la dirección.**
>
> Para $k$ suficientemente grande:
> $$A^k y^{(0)} \approx \lambda_1^k c_1 v_1$$
>
> El factor escalar $\lambda_1^k c_1$ no afecta la dirección. Normalizando:
> $$\frac{A^k y^{(0)}}{\|A^k y^{(0)}\|} \approx \frac{\lambda_1^k c_1 v_1}{\|\lambda_1^k c_1 v_1\|} = \frac{v_1}{\|v_1\|}$$
>
> **Paso 5: Convergencia del autovalor.**
>
> Para un vector $w$ cercano a $v_1$, el cociente de Rayleigh satisface:
> $$\frac{w^T A w}{w^T w} \approx \frac{v_1^T A v_1}{v_1^T v_1} = \frac{v_1^T (\lambda_1 v_1)}{v_1^T v_1} = \lambda_1$$
>
> Por lo tanto, $\lambda^{(k)} \to \lambda_1$.

---

## Justificación: ¿Por qué usar este método?

> [!teoria]
> **Ventajas del método de la potencia.**
>
> 1. **Costo por iteración:** $O(n^2)$ para matrices densas, pero solo $O(\text{nnz})$ para matrices dispersas. No modifica la matriz $A$, solo requiere productos matriz-vector.
>
> 2. **Memoria:** Solo necesita almacenar $A$ (en formato disperso si corresponde) y unos pocos vectores $O(n)$.
>
> 3. **Paralelismo:** El producto matriz-vector es fácilmente paralelizable.
>
> 4. **Selectividad:** Calcula solo lo necesario (el autovalor dominante), sin costo adicional.
>
> **Comparación con métodos directos.**
>
> | Método | Costo (matriz densa) | Costo (matriz dispersa) | Memoria |
> |:---|:---|:---|:---|
> | QR (todos los autovalores) | $O(n^3)$ | $O(n^3)$ (con relleno) | $O(n^2)$ |
> | Potencia (solo dominante) | $O(k n^2)$ | $O(k \cdot \text{nnz})$ | $O(n^2)$ o $O(\text{nnz})$ |
>
> Para $k \ll n$ (lo típico si $|\lambda_2/\lambda_1|$ no está cerca de $1$), el método de la potencia es mucho más eficiente.
>
> **Aplicaciones típicas.**
>
> - **PageRank de Google:** El autovector dominante de una matriz estocástica de tamaño miles de millones.
> - **Análisis de estabilidad:** El autovalor dominante de una matriz de transición determina el comportamiento a largo plazo.
> - **Dinámica de poblaciones:** La tasa de crecimiento dominante (modelo de Leslie).
> - **Método de las potencias en PCA:** Para calcular la primera componente principal.

> [!warning]
> **Limitaciones.**
>
> - Requiere $|\lambda_1| > |\lambda_2|$ (autovalor dominante estrictamente mayor en módulo).
> - Requiere $c_1 \neq 0$ (el vector inicial debe tener componente en $v_1$).
> - Convergencia lenta si $|\lambda_2/\lambda_1| \approx 1$.
> - Solo calcula el autovalor dominante (para otros, usar [[Variantes Metodo Potencia/index|potencia inversa o desplazada]]).

---

## Algoritmo

> [!algoritmo]
> **Método de la potencia (con normalización).**
>
> ```
> función potencia(A, y0, tol, max_iter)
>     y = y0 / ||y0||
>     para k = 1 hasta max_iter
>         y_nuevo = A * y
>         λ = y^T * y_nuevo          // cociente de Rayleigh (y normalizado)
>         y_nuevo = y_nuevo / ||y_nuevo||
>         si ||y_nuevo - y|| < tol
>             retornar y_nuevo, λ, k
>         y = y_nuevo
>     retornar y, λ, max_iter
> ```

> [!algoritmo]
> **Implementación en Python.**
>
> ```python
> import numpy as np
> 
> def power_method(A, y0, tol=1e-10, max_iter=1000):
>     """
>     Método de la potencia para autovalor dominante.
>     
>     Parámetros:
>     - A: matriz (n x n)
>     - y0: vector inicial (n,)
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - v: autovector aproximado (normalizado)
>     - λ: autovalor aproximado
>     - iter: número de iteraciones
>     """
>     v = y0 / np.linalg.norm(y0)
>     
>     for k in range(max_iter):
>         v_new = A @ v
>         λ = np.dot(v, v_new)  # cociente de Rayleigh
>         v_new = v_new / np.linalg.norm(v_new)
>         
>         if np.linalg.norm(v_new - v) < tol:
>             return v_new, λ, k + 1
>         
>         v = v_new
>     
>     return v, λ, max_iter
> 
> # Ejemplo
> A = np.array([[2., 1.], [1., 2.]])
> y0 = np.array([1., 0.])
> v, λ, iters = power_method(A, y0)
> print(f"Autovector: {v}")
> print(f"Autovalor: {λ}")
> print(f"Iteraciones: {iters}")
> ```

---

## Velocidad de convergencia

> [!info]
> La convergencia del método de la potencia es lineal, con factor de convergencia dado por la razón:
> $$r = \left| \frac{\lambda_2}{\lambda_1} \right|$$
>
> Cuanto más cerca esté $r$ de $1$, más lenta es la convergencia. Si $r$ es pequeño, convergencia rápida.
>
> El análisis detallado de la velocidad de convergencia, incluyendo la estimación del número de iteraciones necesarias y cómo afectan los autovalores complejos, se desarrolla en [[Velocidad Convergencia Razon Lambda2 Lambda1]].

---

## Cálculo del autovalor: cociente de Rayleigh

> [!info]
> El cociente de Rayleigh proporciona una estimación óptima del autovalor dado un autovector aproximado. Para matrices simétricas, tiene propiedades de convergencia cuadrática.
>
> La definición formal, propiedades y análisis de convergencia se estudian en [[Calculo Constante Normalizacion Rayleigh]].

---

## Resumen

> [!corolario]
> El método de la potencia es el algoritmo fundamental para calcular el autovalor dominante de una matriz:
> - **Iteración:** $y^{(k+1)} = A y^{(k)}$ con normalización
> - **Autovalor:** estimado mediante cociente de Rayleigh
> - **Convergencia:** lineal con factor $r = |\lambda_2/\lambda_1|$
> - **Costo por iteración:** $O(n^2)$ denso, $O(\text{nnz})$ disperso
>
> Para un estudio detallado de la velocidad de convergencia, véase [[Velocidad Convergencia Razon Lambda2 Lambda1]]. Para la estimación óptima del autovalor mediante el cociente de Rayleigh, véase [[Calculo Constante Normalizacion Rayleigh]]. Para calcular otros autovalores (no solo el dominante), consúltense las [[Variantes Metodo Potencia/index|variantes del método de la potencia]].