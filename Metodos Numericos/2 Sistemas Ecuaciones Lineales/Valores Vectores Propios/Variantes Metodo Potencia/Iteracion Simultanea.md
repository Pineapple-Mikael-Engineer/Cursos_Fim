---
title: Iteracion Simultanea
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - iteracion-simultanea
  - subespacio
draft: false
aliases:
  - Simultaneous iteration
  - Método de la potencia simultáneo
  - Iteración de subespacio
  - Subspace iteration
---

# Iteración Simultánea (Método de la Potencia para Subespacios)

> [!definicion]
> La **iteración simultánea** es una extensión del [[Metodo Potencia Directo/index|método de la potencia]] que trabaja con un subespacio de dimensión $p > 1$, generando $p$ vectores iterados simultáneamente para aproximar los $p$ autovalores de mayor módulo y sus correspondientes autovectores.

> [!info]
> Mientras que el método de la potencia calcula un solo autovector (el dominante), la iteración simultánea calcula un subespacio invariante asociado a los $p$ autovalores dominantes. Es la base teórica del método QR para el cálculo de todos los autovalores.

---

## Ejemplo

> [!ejemplo]
> **Cálculo de los dos autovalores dominantes de $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$.**
>
> Los autovalores exactos son aproximadamente $\lambda_1 \approx 3.732$, $\lambda_2 \approx 2.000$, $\lambda_3 \approx 1.268$.
>
> Se aplica iteración simultánea con $p = 2$, partiendo de $Y^{(0)} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$ (dos vectores iniciales ortonormales).
>
> **Iteración 1:**
> $$Z^{(1)} = A Y^{(0)} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \\ 0 & 1 \end{pmatrix}$$
>
> Ortonormalización (Gram-Schmidt):
> $$Y^{(1)} \approx \begin{pmatrix} 0.894 & -0.182 \\ 0.447 & 0.548 \\ 0 & 0.816 \end{pmatrix}$$
>
> **Iteración 2:**
> $$Z^{(2)} = A Y^{(1)} \approx \begin{pmatrix} 2.236 & 0.365 \\ 2.236 & 1.461 \\ 0.447 & 1.826 \end{pmatrix}$$
>
> Ortonormalizando:
> $$Y^{(2)} \approx \begin{pmatrix} 0.707 & -0.408 \\ 0.707 & 0.408 \\ 0.141 & 0.816 \end{pmatrix}$$
>
> **Iteración 3:**
> Después de ortonormalizar, las columnas de $Y^{(3)}$ convergen a los autovectores dominantes:
> - Columna 1: autovector de $\lambda_1 \approx (0.5, 0.707, 0.5)^T$
> - Columna 2: autovector de $\lambda_2 \approx (0.707, 0, -0.707)^T$
>
> Los autovalores se estiman mediante la matriz de Rayleigh $Y^{(k)T} A Y^{(k)}$.

---

## En qué consiste el método

> [!teoria]
> **Idea fundamental.**
>
> En lugar de iterar con un solo vector, la iteración simultánea itera con una matriz $Y^{(k)} \in \mathbb{R}^{n \times p}$ cuyas columnas son $p$ vectores linealmente independientes, normalmente ortonormales. El objetivo es que el espacio columna de $Y^{(k)}$ converja al subespacio invariante asociado a los $p$ autovalores de mayor módulo.
>
> **Evolución del subespacio.**
>
> Dada una matriz $Y^{(0)}$ de tamaño $n \times p$ con columnas ortonormales, se define:
> $$Z^{(k)} = A Y^{(k-1)}$$
>
> Luego se ortonormaliza $Z^{(k)}$ para obtener $Y^{(k)}$, por ejemplo mediante la descomposición QR:
> $$Z^{(k)} = Y^{(k)} R^{(k)}$$
> donde $Y^{(k)}$ tiene columnas ortonormales y $R^{(k)}$ es triangular superior.
>
> **Estimación de autovalores.**
>
> La matriz de Rayleigh reducida (o matriz de proyección) de $A$ sobre el subespacio columna de $Y^{(k)}$ es:
> $$B^{(k)} = Y^{(k)T} A Y^{(k)} \in \mathbb{R}^{p \times p}$$
>
> Los autovalores de $B^{(k)}$ (llamados **valores de Ritz**) son aproximaciones de los $p$ autovalores dominantes de $A$. A medida que $k \to \infty$, los autovalores de $B^{(k)}$ convergen a $\lambda_1, \lambda_2, \dots, \lambda_p$.
>
> **Interpretación como potencia simultánea.**
>
> Esto es equivalente a aplicar el método de la potencia a los $p$ vectores simultáneamente:
> $$Y^{(k)} \text{ es la ortonormalización de } \{A^k y_1^{(0)}, A^k y_2^{(0)}, \dots, A^k y_p^{(0)}\}$$
>
> Por lo tanto, cada columna de $Y^{(k)}$ se comporta como si se aplicara el método de la potencia a un vector inicial, pero la ortonormalización evita que todas las columnas converjan al mismo autovector dominante.

---

## Demostración de convergencia

> [!teorema]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n| \geq 0$ (estrictamente separados en módulo). Sea $\mathcal{S}$ el subespacio invariante asociado a $\lambda_1, \dots, \lambda_p$, es decir, $\mathcal{S} = \operatorname{span}\{v_1, v_2, \dots, v_p\}$. Sea $Y^{(0)} \in \mathbb{R}^{n \times p}$ una matriz con columnas ortonormales tal que su espacio columna $\mathcal{S}^{(0)}$ tiene componente no nula en $\mathcal{S}$ (es decir, la proyección de $\mathcal{S}^{(0)}$ sobre $\mathcal{S}$ tiene rango completo). Entonces el espacio columna $\mathcal{S}^{(k)}$ de $Y^{(k)}$ converge a $\mathcal{S}$ en el sentido de que el ángulo entre $\mathcal{S}^{(k)}$ y $\mathcal{S}$ tiende a cero, con tasa de convergencia $|\lambda_{p+1}/\lambda_p|$.

> [!demostracion]
> **Paso 1: Representación de los vectores iniciales en la base de autovectores.**
>
> Sean $v_1, \dots, v_n$ una base ortonormal de autovectores de $A$. Cualquier conjunto de $p$ vectores iniciales puede expresarse como:
> $$Y^{(0)} = V \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix}$$
> donde $V = [v_1 \cdots v_p \cdots v_n]$ y las submatrices $C_{11} \in \mathbb{R}^{p \times p}$, $C_{21} \in \mathbb{R}^{(n-p) \times p}$.
>
> La hipótesis de que $\mathcal{S}^{(0)}$ tiene componente no nula en $\mathcal{S}$ significa que $C_{11}$ es no singular.
>
> **Paso 2: Aplicación de $A^k$ a los vectores iniciales.**
>
> $$A^k Y^{(0)} = V \begin{pmatrix} \Lambda_1^k C_{11} & \Lambda_1^k C_{12} \\ \Lambda_2^k C_{21} & \Lambda_2^k C_{22} \end{pmatrix}$$
> donde $\Lambda_1 = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$ y $\Lambda_2 = \operatorname{diag}(\lambda_{p+1}, \dots, \lambda_n)$.
>
> **Paso 3: Factorización del término dominante.**
>
> Factorizando $\Lambda_1^k$ por la izquierda y $C_{11}$ por la derecha:
> $$A^k Y^{(0)} = V \begin{pmatrix} \Lambda_1^k C_{11} & \Lambda_1^k C_{12} \\ \Lambda_2^k C_{21} & \Lambda_2^k C_{22} \end{pmatrix} = V \begin{pmatrix} \Lambda_1^k & 0 \\ 0 & \Lambda_2^k \end{pmatrix} \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix}$$
>
> Reescribiendo de otra forma para aislar la convergencia:
> $$A^k Y^{(0)} = V \begin{pmatrix} I \\ \Lambda_2^k \Lambda_1^{-k} C_{21} C_{11}^{-1} \end{pmatrix} \Lambda_1^k C_{11} \begin{pmatrix} I & C_{11}^{-1} C_{12} \end{pmatrix}$$
>
> **Paso 4: Comportamiento asintótico.**
>
> Como $|\lambda_{p+1}/\lambda_p| < 1$, se tiene $\Lambda_2^k \Lambda_1^{-k} \to 0$ cuando $k \to \infty$ (en cada entrada). Por lo tanto:
> $$\lim_{k \to \infty} \operatorname{span}(A^k Y^{(0)}) = \operatorname{span}\{v_1, \dots, v_p\} = \mathcal{S}$$
>
> **Paso 5: Efecto de la ortonormalización.**
>
> La ortonormalización (QR) no cambia el espacio columna de $Z^{(k)} = A^k Y^{(0)}$, solo lo ortonormaliza. Por lo tanto:
> $$\operatorname{span}(Y^{(k)}) = \operatorname{span}(A^k Y^{(0)}) \to \mathcal{S}$$
>
> **Paso 6: Velocidad de convergencia.**
>
> La convergencia está dominada por el término $\|\Lambda_2^k \Lambda_1^{-k}\| = O(|\lambda_{p+1}/\lambda_p|^k)$, donde $\lambda_{p+1}$ es el autovalor dominante del complemento. El ángulo entre $\mathcal{S}^{(k)}$ y $\mathcal{S}$ satisface:
> $$\angle(\mathcal{S}^{(k)}, \mathcal{S}) = O\left( \left| \frac{\lambda_{p+1}}{\lambda_p} \right|^k \right)$$
>
> **Paso 7: Convergencia de los valores de Ritz.**
>
> La matriz de Rayleigh $B^{(k)} = Y^{(k)T} A Y^{(k)}$ tiene autovalores que convergen a $\lambda_1, \dots, \lambda_p$ con tasa de convergencia al menos $|\lambda_{p+1}/\lambda_p|^k$ y, para matrices simétricas, incluso cuadrática debido a las propiedades del cociente de Rayleigh.

> [!info]
> **Interpretación geométrica.** La iteración simultánea "rota" el subespacio inicial hacia el subespacio invariante dominante, con una velocidad determinada por la separación espectral entre $\lambda_p$ y $\lambda_{p+1}$.

---

## Algoritmo

> [!algoritmo]
> **Iteración simultánea (versión con QR).**
>
> ```
> función iteracion_simultanea(A, p, y0, tol, max_iter)
>     // y0 es matriz n x p con columnas ortonormales
>     Y = y0
>     para k = 1 hasta max_iter
>         Z = A * Y
>         // Descomposición QR: Z = Y * R
>         [Y, R] = qr(Z)
>         
>         // Matriz de Rayleigh reducida
>         B = Y^T * A * Y
>         
>         // Calcular autovalores de B (valores de Ritz)
>         λ_ritz = eigvals(B)
>         
>         // Criterio de parada (por ejemplo, cambio en Y)
>         si cambio_en_Y < tol
>             retornar Y, λ_ritz, k
>     retornar Y, λ_ritz, max_iter
> ```

> [!algoritmo]
> **Implementación en Python.**
>
> ```python
> import numpy as np
> from scipy.linalg import qr, eig
> 
> def simultaneous_iteration(A, p, Y0, tol=1e-10, max_iter=1000):
>     """
>     Iteración simultánea para calcular los p autovalores de mayor módulo.
>     
>     Parámetros:
>     - A: matriz (n x n)
>     - p: número de autovalores deseados (p ≤ n)
>     - Y0: matriz inicial (n x p) con columnas ortonormales
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - Y: matriz (n x p) con base ortonormal del subespacio convergido
>     - λ: lista de p autovalores aproximados
>     - iter: número de iteraciones
>     """
>     Y = Y0.copy()
>     
>     for k in range(max_iter):
>         Z = A @ Y
>         Y_new, R = qr(Z, mode='economic')
>         
>         # Matriz de Rayleigh reducida
>         B = Y_new.T @ A @ Y_new
>         
>         # Autovalores de B (valores de Ritz)
>         λ_ritz = eig(B, left=False, right=False)
>         
>         # Criterio de parada: cambio en el subespacio
>         # Se mide el ángulo entre columnas (norma de la diferencia)
>         # Como Y y Y_new son ortonormales, se usa la norma de Y_new - Y
>         diff = np.linalg.norm(Y_new @ Y_new.T - Y @ Y.T, ord='fro')
>         
>         if diff < tol:
>             return Y_new, λ_ritz, k + 1
>         
>         Y = Y_new
>     
>     return Y, λ_ritz, max_iter
> 
> # Ejemplo
> A = np.array([[2., 1., 0.], [1., 3., 1.], [0., 1., 2.]])
> n = 3
> p = 2
> # Inicializar con vectores ortonormales aleatorios
> Y0 = np.random.randn(n, p)
> Y0, _ = qr(Y0, mode='economic')
> 
> Y, λ, iters = simultaneous_iteration(A, p, Y0)
> print(f"Autovalores aproximados: {λ}")
> print(f"Autovectores: \n{Y}")
> print(f"Iteraciones: {iters}")
> ```

---

## Relación con el método QR

> [!teoria]
> La iteración simultánea es la base teórica del **método QR** para el cálculo de todos los autovalores.
>
> | Método | Descripción |
> |:---|:---|
> | Iteración simultánea | Aplica $A$ a un bloque de $p$ vectores y ortonormaliza |
> | Método QR | Aplica transformaciones ortogonales a toda la matriz $A$ para triangularizarla |
>
> **Conexión:** Si se toma $p = n$ (toda la matriz) y $Y^{(0)} = I$, entonces la iteración simultánea genera la misma secuencia de matrices que el método QR sin desplazamientos. Específicamente:
> $$A_k = Q_k^T A Q_k$$
> donde $Q_k$ es la matriz de ortonormalización acumulada. Este es precisamente el paso iterativo del método QR básico.
>
> Por lo tanto, la iteración simultánea se puede ver como una generalización del método QR para subespacios de dimensión $p$, y el método QR es el caso particular $p = n$.

---

## Limitaciones y advertencias

> [!warning]
> **Limitaciones de la iteración simultánea.**
>
> 1. **Separación espectral:** La convergencia depende de $|\lambda_{p+1}/\lambda_p|$. Si esta razón es cercana a $1$, la convergencia es lenta.
>
> 2. **Costo computacional:** Cada iteración requiere un producto matriz-matriz $A Y$ (costo $O(p \cdot \text{nnz})$) y una descomposición QR (costo $O(np^2)$). Para $p$ grande, esto puede ser costoso.
>
> 3. **Bloqueo de convergencia:** Las columnas de $Y^{(k)}$ convergen a los autovectores dominantes, pero la convergencia puede ser no uniforme (primeras columnas convergen más rápido).
>
> 4. **Matrices no diagonalizables:** La teoría se complica, pero el método sigue funcionando (convergencia al subespacio invariante asociado a los autovalores dominantes, incluyendo bloques de Jordan).
>
> **Mejoras prácticas:**
> - Para acelerar convergencia, se introducen desplazamientos (shift) como en el método QR.
> - Para matrices simétricas, se utiliza la iteración de Lanczos (más eficiente que iteración simultánea con $p$ pequeño).

---

## Relación con otras notas

> [!info]
> - Este método generaliza el [[Metodo Potencia Directo/index]] al caso de subespacios.
> - La velocidad de convergencia está determinada por la razón $|\lambda_{p+1}/\lambda_p|$, análoga a la razón $|\lambda_2/\lambda_1|$ en el método de la potencia (véase [[Velocidad Convergencia Razon Lambda2 Lambda1]]).
> - Los valores de Ritz se calculan mediante el cociente de Rayleigh (véase [[Calculo Constante Normalizacion Rayleigh]]).
> - El método QR (para todos los autovalores) se basa en este principio con $p = n$.
> - Para casos particulares (matrices simétricas), existen variantes más eficientes como el método de Lanczos.

---

## Resumen

> [!corolario]
> La iteración simultánea es una extensión natural del método de la potencia para el cálculo de los $p$ autovalores de mayor módulo:
>
> | Aspecto | Descripción |
> |:---|:---|
> | Objetivo | Aproximar los $p$ autovalores dominantes y sus autovectores |
> | Iteración | $Z = A Y$, luego $Z = QR$ (ortonormalización) |
> | Estimación | Autovalores de $B = Y^T A Y$ (valores de Ritz) |
> | Convergencia | El subespacio converge con razón $|\lambda_{p+1}/\lambda_p|$ |
> | Relación con QR | El método QR es iteración simultánea con $p = n$ |
>
> **Conclusión práctica:** La iteración simultánea es la base conceptual del método QR, uno de los algoritmos más importantes del álgebra lineal numérica. Para $p$ pequeño (por ejemplo, $p = 2$ o $3$), es una herramienta práctica para calcular los primeros autovalores de matrices grandes. Para $p$ grande, el costo puede ser prohibitivo, por lo que se recomienda el método QR o métodos de Krylov (Arnoldi/Lanczos).