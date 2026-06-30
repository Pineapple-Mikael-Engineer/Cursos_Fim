---
title: Potencia Inversa Valor Propio Menor Modulo
order: 1
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - potencia-inversa
draft: false
aliases:
  - Inverse power method
  - Método de la potencia inversa
  - Cálculo del autovalor más pequeño
---

# Potencia Inversa: Cálculo del Autovalor de Menor Módulo

> [!definicion]
> El **método de la potencia inversa** es una variante del método de la potencia que se aplica a la matriz $A^{-1}$ para calcular el autovalor de menor módulo $|\lambda_n|$ y su correspondiente autovector.

> [!info]
> Se basa en que los autovalores de $A^{-1}$ son $1/\lambda_i$, por lo que el autovalor dominante de $A^{-1}$ (el de mayor módulo) corresponde al autovalor de menor módulo de $A$. Aplicando el [[Metodo Potencia Directo/index|método de la potencia]] a $A^{-1}$ se obtiene convergencia a $v_n$ y a $1/\lambda_n$.

---

## Ejemplo

> [!ejemplo]
> **Cálculo del autovalor de menor módulo de $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.**
>
> Los autovalores exactos son $\lambda_1 = 3$ y $\lambda_2 = 1$. El de menor módulo es $\lambda_2 = 1$.
>
> **Paso 1: Calcular $A^{-1}$.**
> $$A^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \approx \begin{pmatrix} 0.6667 & -0.3333 \\ -0.3333 & 0.6667 \end{pmatrix}$$
>
> **Paso 2: Aplicar el método de la potencia a $A^{-1}$ desde $y^{(0)} = (1, 0)^T$.**
>
> | $k$ | $y^{(k)}$ (normalizado) | $\mu^{(k)} = R_{A^{-1}}(y^{(k)})$ | $\lambda^{(k)} = 1 / \mu^{(k)}$ |
> |:---|:---|:---|:---|
> | 0 | (1.000, 0.000) | 0.6667 | 1.500 |
> | 1 | (0.894, -0.447) | 0.8333 | 1.200 |
> | 2 | (0.780, -0.625) | 0.9375 | 1.067 |
> | 3 | (0.732, -0.681) | 0.9792 | 1.021 |
> | 4 | (0.716, -0.698) | 0.9948 | 1.005 |
> | 5 | (0.708, -0.706) | 0.9987 | 1.001 |
>
> El autovector converge a $(0.707, -0.707)$, que es $v_2$ (normalizado). El autovalor $\lambda^{(k)}$ converge a $1$.
>
> **Observación:** En la práctica no se calcula $A^{-1}$ explícitamente; en cada iteración se resuelve $A z = y^{(k)}$.

---

## En qué consiste el método

> [!teoria]
> El método de la potencia inversa calcula el autovalor de menor módulo $\lambda_n$ y su autovector $v_n$ aplicando el método de la potencia a la matriz inversa $A^{-1}$.
>
> **Fundamento matemático.**
>
> Supóngase que $A$ es diagonalizable con autovalores $\lambda_1, \lambda_2, \dots, \lambda_n$ ordenados como:
> $$|\lambda_1| \geq |\lambda_2| \geq \cdots \geq |\lambda_{n-1}| > |\lambda_n| > 0$$
>
> Entonces $A^{-1}$ tiene autovalores $1/\lambda_i$, con orden:
> $$\left| \frac{1}{\lambda_n} \right| > \left| \frac{1}{\lambda_{n-1}} \right| \geq \cdots \geq \left| \frac{1}{\lambda_1} \right|$$
>
> El autovalor dominante de $A^{-1}$ es $1/\lambda_n$, y su autovector asociado es $v_n$ (el mismo de $A$). Por lo tanto, al aplicar el método de la potencia a $A^{-1}$ se obtiene:
> - Convergencia a $v_n$ (el autovector de $\lambda_n$)
> - El cociente de Rayleigh sobre $A^{-1}$ converge a $1/\lambda_n$
>
> **Implementación práctica sin calcular $A^{-1}$.**
>
> En lugar de calcular explícitamente $A^{-1}$ (costoso $O(n^3)$ y numéricamente inestable), se observa que aplicar $A^{-1}$ a un vector $y$ equivale a resolver el sistema lineal:
> $$A z = y \quad \Longrightarrow \quad z = A^{-1} y$$
>
> Por lo tanto, cada iteración del método de la potencia inversa consiste en:
>
> 1. **Resolver el sistema lineal:** Encontrar $z$ tal que $A z = y^{(k)}$
> 2. **Normalizar:** $y^{(k+1)} = z / \|z\|$
> 3. **Estimar el autovalor:** $\lambda^{(k)} = 1 / R_{A^{-1}}(y^{(k)})$
>
> **Ventaja:** No se necesita calcular $A^{-1}$; basta con resolver sistemas lineales. Si se factoriza $A = LU$ al inicio, cada iteración solo requiere sustituciones progresiva y regresiva ($O(n^2)$).
>
> **Relación con el método de la potencia directo.**
>
> | Método | Potencia directa | Potencia inversa |
> |:---|:---|:---|
> | Objetivo | $\lambda_1$ (mayor módulo) | $\lambda_n$ (menor módulo) |
> | Matriz aplicada | $A$ | $A^{-1}$ (implícitamente) |
> | Operación principal | $z = A y$ | Resolver $A z = y$ |
> | Factor de convergencia | $\|\lambda_2/\lambda_1\|$ | $\|\lambda_n/\lambda_{n-1}\|$ |

---

## Demostración de convergencia

> [!teorema]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores $|\lambda_1| \geq |\lambda_2| \geq \cdots \geq |\lambda_{n-1}| > |\lambda_n| > 0$ (el autovalor de menor módulo es estrictamente menor que los demás y no nulo). Sea $y^{(0)}$ un vector con componente no nula en la dirección de $v_n$ (es decir, $c_n \neq 0$ en su descomposición espectral). Entonces la sucesión definida por:
>
> $$
> \begin{cases}
> \text{Resolver } A z^{(k)} = y^{(k)} \\
> y^{(k+1)} = \dfrac{z^{(k)}}{\|z^{(k)}\|}
> \end{cases}
> $$
>
> satisface:
> $$
> \lim_{k \to \infty} y^{(k)} = \frac{v_n}{\|v_n\|}
> $$
> y
> $$
> \lim_{k \to \infty} \frac{1}{R_{A^{-1}}(y^{(k)})} = \lambda_n
> $$
>
> donde $R_{A^{-1}}(y) = \dfrac{y^T A^{-1} y}{y^T y}$ es el cociente de Rayleigh de $A^{-1}$.

> [!demostracion]
> **Paso 1: Relación con el método de la potencia en $A^{-1}$.**
>
> La iteración $z^{(k)} = A^{-1} y^{(k)}$ es exactamente la iteración del método de la potencia aplicado a la matriz $B = A^{-1}$. Por el teorema del [[Metodo Potencia Directo/index|método de la potencia]], sabemos que si $B$ es diagonalizable y tiene un autovalor dominante estricto, la sucesión normalizada converge al autovector correspondiente.
>
> **Paso 2: Autovalores y autovectores de $B = A^{-1}$.**
>
> Como $A$ es diagonalizable, existe una base de autovectores $\{v_1, v_2, \dots, v_n\}$ con $A v_i = \lambda_i v_i$. Entonces:
> $$A^{-1} v_i = \frac{1}{\lambda_i} v_i$$
>
> Por lo tanto, los autovalores de $B$ son $\mu_i = 1/\lambda_i$, y los autovectores son los mismos $\{v_i\}$.
>
> **Paso 3: Orden de los autovalores de $B$.**
>
> Como $|\lambda_1| \geq |\lambda_2| \geq \cdots \geq |\lambda_{n-1}| > |\lambda_n| > 0$, se tiene:
> $$\left| \frac{1}{\lambda_n} \right| > \left| \frac{1}{\lambda_{n-1}} \right| \geq \cdots \geq \left| \frac{1}{\lambda_1} \right|$$
>
> El autovalor dominante de $B$ es $\mu_n = 1/\lambda_n$ (el de mayor módulo), y su autovector asociado es $v_n$.
>
> **Paso 4: Aplicación del teorema del método de la potencia a $B$.**
>
> Sea $y^{(0)}$ cualquier vector con componente no nula en la dirección de $v_n$. Escribiendo $y^{(0)}$ en la base de autovectores de $B$:
> $$y^{(0)} = \sum_{i=1}^n c_i v_i, \quad c_n \neq 0$$
>
> Aplicando $B$ repetidamente:
> $$B^k y^{(0)} = \sum_{i=1}^n c_i \mu_i^k v_i = \mu_n^k \left( c_n v_n + \sum_{i=1}^{n-1} c_i \left( \frac{\mu_i}{\mu_n} \right)^k v_i \right)$$
>
> Como $|\mu_i/\mu_n| = |\lambda_n/\lambda_i| < 1$ para $i = 1, \dots, n-1$, se tiene:
> $$\lim_{k \to \infty} \frac{B^k y^{(0)}}{\|B^k y^{(0)}\|} = \frac{v_n}{\|v_n\|}$$
>
> **Paso 5: Convergencia del autovalor.**
>
> Por el teorema del método de la potencia, el cociente de Rayleigh aplicado a $B$ converge al autovalor dominante:
> $$\lim_{k \to \infty} R_B(y^{(k)}) = \mu_n = \frac{1}{\lambda_n}$$
>
> Por lo tanto:
> $$\lim_{k \to \infty} \frac{1}{R_B(y^{(k)})} = \lambda_n$$
>
> **Paso 6: Razón de convergencia.**
>
> La razón de convergencia del método de la potencia aplicado a $B = A^{-1}$ está dada por la relación entre el segundo autovalor en módulo y el dominante:
> $$r = \left| \frac{\mu_{n-1}}{\mu_n} \right| = \left| \frac{1/\lambda_{n-1}}{1/\lambda_n} \right| = \left| \frac{\lambda_n}{\lambda_{n-1}} \right|$$
>
> Por lo tanto, el error en el autovector se reduce como $O(|\lambda_n/\lambda_{n-1}|^k)$, y el error en el autovalor (estimado mediante el cociente de Rayleigh) tiene la misma tasa de convergencia lineal (o cuadrática si $A$ es simétrica, por las propiedades del [[Calculo Constante Normalizacion Rayleigh|cociente de Rayleigh]]).

> [!warning]
> **Caso particular importante.**
>
> Si $\lambda_n = 0$ (matriz singular), el método de la potencia inversa no está definido pues $A^{-1}$ no existe. En este caso, el autovalor de menor módulo es $0$, y se requieren otros métodos (por ejemplo, calcular el autovector asociado al núcleo de $A$ resolviendo $A v = 0$).

---

## Algoritmo

> [!algoritmo]
> **Método de la potencia inversa.**
>
> ```
> función potencia_inversa(A, y0, tol, max_iter)
>     // Factorización LU de A (una sola vez)
>     P, L, U = factorizar_lu(A)
>     y = y0 / ||y0||
>     
>     para k = 1 hasta max_iter
>         // Resolver A z = y usando la factorización LU
>         // 1. Resolver P w = y  → w = P^T y
>         // 2. Resolver L z1 = w
>         // 3. Resolver U z = z1
>         z = resolver_lu(P, L, U, y)
>         
>         // Cociente de Rayleigh para A^{-1}
>         μ = y^T * z
>         λ = 1 / μ
>         
>         y_nuevo = z / ||z||
>         
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
> from scipy.linalg import lu, solve
> 
> def inverse_power_method(A, y0, tol=1e-10, max_iter=1000):
>     """
>     Método de la potencia inversa para el autovalor de menor módulo.
>     
>     Parámetros:
>     - A: matriz (n x n) no singular
>     - y0: vector inicial (n,)
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - v: autovector aproximado (normalizado)
>     - λ: autovalor aproximado (menor módulo)
>     - iter: número de iteraciones
>     """
>     # Factorización LU (una sola vez)
>     P, L, U = lu(A)
>     
>     v = y0 / np.linalg.norm(y0)
>     
>     for k in range(max_iter):
>         # Resolver A z = v usando la factorización LU
>         # Primero resuelve P z1 = v → z1 = P^T v
>         z1 = P.T @ v
>         # Luego resuelve L z2 = z1
>         z2 = solve(L, z1, lower=True)
>         # Finalmente resuelve U z = z2
>         z = solve(U, z2)
>         
>         # Cociente de Rayleigh para A^{-1}
>         μ = np.dot(v, z)
>         λ = 1.0 / μ
>         
>         v_new = z / np.linalg.norm(z)
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
> v, λ, iters = inverse_power_method(A, y0)
> print(f"Autovector: {v}")
> print(f"Autovalor (menor módulo): {λ}")
> print(f"Iteraciones: {iters}")
> ```

---

## Costo computacional

> [!info]
> **Comparación con el método de la potencia directo.**
>
> | Método | Operación principal | Costo por iteración |
> |:---|:---|:---|
> | Potencia directa | Producto matriz-vector $A y$ | $O(n^2)$ (denso) / $O(\text{nnz})$ (disperso) |
> | Potencia inversa | Resolver $A z = y$ | $O(n^3)$ para factorización inicial + $O(n^2)$ por iteración (denso) |
>
> **Observaciones:**
>
> - La factorización LU de $A$ se calcula **una sola vez** al inicio, con costo $O(n^3)$.
> - Cada iteración requiere resolver dos sistemas triangulares (sustitución progresiva y regresiva), con costo $O(n^2)$.
> - Para matrices dispersas, se utilizan solvers directos dispersos o métodos iterativos (como gradiente conjugado) para resolver $A z = y$ en cada iteración, con costo variable.
> - El costo inicial $O(n^3)$ puede ser prohibitivo para matrices muy grandes. En esos casos, se prefiere la [[Variantes Metodo Potencia/Potencia Desplazada Aceleracion Convergencia|potencia desplazada]] con desplazamiento dinámico o métodos de subespacio de Krylov.

---

## Relación con la factorización LU

> [!info]
> Para evitar calcular $A^{-1}$ explícitamente, se factoriza $A = P L U$ (con pivoteo) al inicio. Luego, cada iteración resuelve:
>
> 1. $P L U z = y$ → resolver $L (U z) = P^T y$ en dos pasos:
>    - Sustitución progresiva: $L w = P^T y$
>    - Sustitución regresiva: $U z = w$
>
> Esto es mucho más eficiente que calcular $A^{-1}$ y multiplicar.

---

## Limitaciones y advertencias

> [!warning]
> **Limitaciones del método de la potencia inversa.**
>
> 1. **Matriz singular:** Si $\lambda_n = 0$, $A$ no es invertible y el método falla.
>
> 2. **Autovalores múltiples:** Si $|\lambda_n| = |\lambda_{n-1}|$ (mismo módulo), la convergencia no está garantizada (puede oscilar).
>
> 3. **Costo inicial:** La factorización LU cuesta $O(n^3)$, lo que puede ser prohibitivo para matrices muy grandes (para esos casos, se recomienda potencia desplazada o métodos de Krylov).
>
> 4. **Condicionamiento:** Si $A$ está mal condicionada ($\lambda_n \approx 0$), resolver $A z = y$ puede ser numéricamente inestable.

---

## Relación con otras notas

> [!info]
> - Este método es una variante del [[Metodo Potencia Directo/index]] aplicado a $A^{-1}$.
> - La convergencia está determinada por la razón $|\lambda_n / \lambda_{n-1}|$, similar a cómo $|\lambda_2/\lambda_1|$ afecta a la potencia directa (véase [[Velocidad Convergencia Razon Lambda2 Lambda1]]).
> - El autovalor se estima mediante el cociente de Rayleigh (véase [[Calculo Constante Normalizacion Rayleigh]]).
> - La generalización con desplazamiento $\mu$ (potencia desplazada) permite acelerar convergencia y apuntar a autovalores interiores (véase [[Potencia Desplazada Aceleracion Convergencia]]).

---

## Resumen

> [!corolario]
> El método de la potencia inversa calcula el autovalor de menor módulo y su autovector:
>
> | Aspecto | Descripción |
> |:---|:---|
> | Idea central | Aplicar potencia a $A^{-1}$ |
> | Iteración | Resolver $A z = y^{(k)}$, normalizar |
> | Costo por iteración | $O(n^2)$ (tras factorización LU inicial $O(n^3)$) |
> | Factor de convergencia | $r = \|\lambda_n / \lambda_{n-1}\|$ |
> | Velocidad | Rápido si $\|\lambda_n\| \ll \|\lambda_{n-1}\|$ |
> | Principal desventaja | Costo de factorización inicial |
>
> **Conclusión práctica:** La potencia inversa es ideal cuando se necesita el autovalor de menor módulo y se puede permitir una factorización inicial (o ya se tiene factorizada). Para matrices muy grandes o cuando se requiere gran precisión, la [[Potencia Desplazada Aceleracion Convergencia|potencia desplazada]] con desplazamiento adaptativo puede ser más eficiente.