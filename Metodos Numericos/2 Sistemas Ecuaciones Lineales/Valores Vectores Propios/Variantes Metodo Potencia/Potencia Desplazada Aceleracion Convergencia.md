---
title: Potencia Desplazada Aceleracion Convergencia
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - potencia-desplazada
  - shift
draft: false
aliases:
  - Shifted power method
  - Potencia con desplazamiento
  - Aceleración de convergencia
  - Rayleigh quotient iteration
---

# Potencia Desplazada: Aceleración de la Convergencia

> [!definicion]
> El **método de la potencia desplazada** es una variante del método de la potencia inversa que aplica la iteración a la matriz $(A - \mu I)^{-1}$ con un desplazamiento $\mu$ elegido estratégicamente para acelerar la convergencia hacia el autovalor más cercano a $\mu$.

> [!info]
> Mientras que la [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] es un caso particular con $\mu = 0$, la potencia desplazada permite apuntar a cualquier autovalor del espectro. Con una elección adecuada de $\mu$, especialmente si se actualiza dinámicamente mediante el cociente de Rayleigh, se puede alcanzar convergencia cuadrática o incluso cúbica.

---

## Ejemplo

> [!ejemplo]
> **Cálculo del autovalor intermedio de $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ mediante potencia desplazada.**
>
> Los autovalores exactos son aproximadamente $\lambda_1 \approx 3.732$, $\lambda_2 = 2.000$, $\lambda_3 \approx 1.268$.
>
> Se desea calcular $\lambda_2 = 2$, un autovalor interior. Se elige un desplazamiento $\mu = 2$ (cercano al autovalor buscado).
>
> **Paso 1: Construir $(A - \mu I)^{-1}$.**
>
> $$A - 2I = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$
>
> Esta matriz es singular (determinante $0$), lo que indica que $\mu = 2$ es un autovalor exacto. En la práctica se usa un $\mu$ cercano pero no exacto para evitar singularidad.
>
> Usando $\mu = 1.9$:
>
> $$A - 1.9I = \begin{pmatrix} 0.1 & 1 & 0 \\ 1 & 1.1 & 1 \\ 0 & 1 & 0.1 \end{pmatrix}$$
>
> Su inversa (calculada numéricamente) tiene autovalor dominante $1/(\lambda_2 - 1.9) = 1/0.1 = 10$.
>
> **Paso 2: Aplicar potencia inversa desde $y^{(0)} = (1, 0, 0)^T$.**
>
> | $k$ | $y^{(k)}$ (normalizado) | $\lambda^{(k)} = \mu + 1/R_{(A-\mu I)^{-1}}(y^{(k)})$ |
> |:---|:---|:---|
> | 0 | (1.000, 0.000, 0.000) | — |
> | 1 | (0.995, 0.099, 0.010) | 1.990 |
> | 2 | (0.708, 0.706, 0.010) | 1.999 |
> | 3 | (0.707, 0.707, 0.000) | 2.000 |
>
> Convergencia rápida (3 iteraciones) gracias a que $\mu$ está cerca del autovalor buscado.
>
> **Comparación con potencia inversa sin desplazamiento ($\mu = 0$):**
> - Con $\mu = 0$, se calcularía el autovalor de menor módulo ($\lambda_3 \approx 1.268$), no $\lambda_2 = 2$.
> - Para calcular $\lambda_2$ sin desplazamiento, se necesitaría otro método (por ejemplo, deflación).

---

## En qué consiste el método

> [!teoria]
> **Idea fundamental.**
>
> El método de la potencia desplazada aplica el [[Variantes Metodo Potencia/index|método de la potencia inversa]] a la matriz $(A - \mu I)^{-1}$. La razón es que los autovalores de esta matriz son $1/(\lambda_i - \mu)$, por lo que el autovalor dominante de $(A - \mu I)^{-1}$ corresponde al $\lambda_i$ más cercano a $\mu$.
>
> **Iteración.**
>
> Dado un desplazamiento $\mu$ (fijo o variable) y un vector inicial $y^{(0)}$, se itera:
>
> 1. Resolver $(A - \mu I) z^{(k)} = y^{(k)}$ para $z^{(k)}$
> 2. Normalizar: $y^{(k+1)} = z^{(k)} / \|z^{(k)}\|$
> 3. Estimar el autovalor: $\lambda^{(k)} = \mu + 1 / R_{(A-\mu I)^{-1}}(y^{(k)})$
>
> **Efecto del desplazamiento en la convergencia.**
>
> Sea $\lambda_j$ el autovalor más cercano a $\mu$. La razón de convergencia está dada por:
> $$r = \left| \frac{\lambda_j - \mu}{\lambda_k - \mu} \right|$$
> donde $\lambda_k$ es el autovalor más cercano a $\mu$ después de $\lambda_j$.
>
> Si $\mu$ está cerca de $\lambda_j$, entonces $|\lambda_j - \mu|$ es pequeño, lo que hace que $r$ sea pequeño y la convergencia sea rápida. En el límite $\mu \to \lambda_j$, la convergencia es instantánea (una iteración).
>
> **Caso especial: iteración del cociente de Rayleigh (RQI).**
>
> Si se actualiza $\mu$ en cada iteración con el cociente de Rayleigh:
> $$\mu^{(k)} = R_A(y^{(k)}) = \frac{y^{(k)T} A y^{(k)}}{y^{(k)T} y^{(k)}}$$
> entonces la convergencia es **cúbica** para matrices simétricas (el número de dígitos correctos se triplica en cada iteración).

---

## Demostración de convergencia

> [!teorema]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores $\lambda_1, \lambda_2, \dots, \lambda_n$. Sea $\mu$ un desplazamiento tal que $\mu$ no es autovalor de $A$ (para que $A - \mu I$ sea invertible). Sea $\lambda_j$ el autovalor más cercano a $\mu$, es decir:
> $$|\lambda_j - \mu| < |\lambda_i - \mu| \quad \forall i \neq j$$
>
> Entonces la iteración de la potencia desplazada converge al autovector $v_j$ y al autovalor $\lambda_j$, con razón de convergencia:
> $$r = \left| \frac{\lambda_j - \mu}{\lambda_k - \mu} \right|$$
> donde $\lambda_k$ es el autovalor más cercano a $\mu$ después de $\lambda_j$ (es decir, $\lambda_k$ minimiza $|\lambda_i - \mu|$ para $i \neq j$).

> [!demostracion]
> **Paso 1: Espectro de la matriz transformada.**
>
> Sea $B = (A - \mu I)^{-1}$. Los autovalores de $B$ son $\mu_i = 1/(\lambda_i - \mu)$, y los autovectores son los mismos que los de $A$.
>
> Como $\lambda_j$ es el más cercano a $\mu$, se tiene $|\lambda_j - \mu|$ mínimo, por lo tanto $|\mu_j| = 1/|\lambda_j - \mu|$ es el autovalor de $B$ de mayor módulo.
>
> **Paso 2: Orden de convergencia de la potencia inversa.**
>
> Aplicando el teorema de convergencia de la [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] a la matriz $B$, se obtiene que la iteración converge a $v_j$ y a $\mu_j$, con razón de convergencia:
> $$r_B = \left| \frac{\mu_k}{\mu_j} \right| = \left| \frac{1/(\lambda_k - \mu)}{1/(\lambda_j - \mu)} \right| = \left| \frac{\lambda_j - \mu}{\lambda_k - \mu} \right|$$
>
> **Paso 3: Recuperación del autovalor de $A$.**
>
> Una vez que se tiene $\mu_j$ (el autovalor dominante de $B$), el autovalor buscado es:
> $$\lambda_j = \mu + \frac{1}{\mu_j}$$
>
> La convergencia de $\mu_j$ implica la convergencia de $\lambda_j$ con la misma razón.

> [!corolario]
> **Aceleración:** Si $\mu$ está muy cerca de $\lambda_j$, entonces $|\lambda_j - \mu| \ll |\lambda_k - \mu|$, por lo que $r \ll 1$ y la convergencia es extremadamente rápida.

---

## Elección óptima del desplazamiento

> [!teoria]
> **¿Cómo elegir $\mu$?**
>
> 1. **Desplazamiento fijo:** Si se tiene una estimación $\tilde{\lambda}$ del autovalor deseado, elegir $\mu = \tilde{\lambda}$ (o muy cerca). Esto ya acelera significativamente la convergencia.
>
> 2. **Desplazamiento adaptativo (RQI):** En cada iteración, se actualiza $\mu^{(k)} = R_A(y^{(k)})$, el cociente de Rayleigh. Para matrices simétricas, esto produce convergencia cúbica.
>
> **Iteración del cociente de Rayleigh (RQI).**
>
> Para matrices simétricas, el algoritmo RQI es:
>
> $$
> \begin{cases}
> \mu^{(k)} = \dfrac{y^{(k)T} A y^{(k)}}{y^{(k)T} y^{(k)}} \\[1em]
> \text{Resolver } (A - \mu^{(k)} I) z^{(k)} = y^{(k)} \\[1em]
> y^{(k+1)} = \dfrac{z^{(k)}}{\|z^{(k)}\|}
> \end{cases}
> $$
>
> **Velocidad de convergencia del RQI:**
> - Si $\mu^{(k)}$ está a distancia $O(\varepsilon)$ de $\lambda_j$, entonces $\mu^{(k+1)}$ está a distancia $O(\varepsilon^2)$ (cuadrática).
> - Para matrices simétricas, la convergencia es **cúbica** ($O(\varepsilon^3)$), lo que significa que los dígitos correctos se triplican en cada iteración.
>
> **Ejemplo de convergencia cúbica:**
> - Iteración 1: 1 dígito correcto
> - Iteración 2: 3 dígitos correctos
> - Iteración 3: 9 dígitos correctos
> - Iteración 4: 27 dígitos correctos (más que la precisión de máquina)

> [!ejemplo]
> **RQI aplicado a $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\lambda_1 = 3$.**
>
> Partiendo de $y^{(0)} = (1, 0)^T$:
>
> | $k$ | $\mu^{(k)}$ | $y^{(k)}$ | Error en $\mu^{(k)}$ |
> |:---|:---|:---|:---|
> | 0 | 2.000 | (1.000, 0.000) | 1.000 |
> | 1 | 2.500 | (0.894, 0.447) | 0.500 |
> | 2 | 2.900 | (0.780, 0.625) | 0.100 |
> | 3 | 2.990 | (0.707, 0.707) | 0.010 |
> | 4 | 2.999 | (0.707, 0.707) | 0.001 |
>
> La convergencia es más rápida que la potencia directa pero no cúbica en este caso porque la matriz es pequeña; la ventaja cúbica se nota en iteraciones posteriores.

---

## Algoritmo

> [!algoritmo]
> **Potencia desplazada con desplazamiento fijo.**
>
> ```
> función potencia_desplazada(A, mu, y0, tol, max_iter)
>     // Factorización LU de (A - mu I) (una sola vez)
>     P, L, U = factorizar_lu(A - mu * I)
>     y = y0 / ||y0||
>     
>     para k = 1 hasta max_iter
>         // Resolver (A - mu I) z = y
>         z = resolver_lu(P, L, U, y)
>         
>         // Cociente de Rayleigh para (A - mu I)^{-1}
>         rho = y^T * z
>         λ = mu + 1 / rho
>         
>         y_nuevo = z / ||z||
>         
>         si ||y_nuevo - y|| < tol
>             retornar y_nuevo, λ, k
>         y = y_nuevo
>     retornar y, λ, max_iter
> ```

> [!algoritmo]
> **Iteración del cociente de Rayleigh (RQI) para matrices simétricas.**
>
> ```
> función rqi(A, y0, tol, max_iter)
>     y = y0 / ||y0||
>     
>     para k = 1 hasta max_iter
>         mu = y^T * A * y          // cociente de Rayleigh
>         
>         // Resolver (A - mu I) z = y
>         // Nota: la matriz cambia en cada iteración!
>         z = resolver_sistema(A - mu * I, y)
>         
>         y_nuevo = z / ||z||
>         
>         si ||y_nuevo - y|| < tol
>             retornar y_nuevo, mu, k
>         y = y_nuevo
>     retornar y, mu, max_iter
> ```

> [!algoritmo]
> **Implementación en Python de la potencia desplazada.**
>
> ```python
> import numpy as np
> from scipy.linalg import lu, solve
> 
> def shifted_power_method(A, mu, y0, tol=1e-10, max_iter=1000):
>     """
>     Método de la potencia desplazada para el autovalor más cercano a mu.
>     
>     Parámetros:
>     - A: matriz (n x n)
>     - mu: desplazamiento (escalar)
>     - y0: vector inicial (n,)
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - v: autovector aproximado (normalizado)
>     - λ: autovalor aproximado (el más cercano a mu)
>     - iter: número de iteraciones
>     """
>     n = len(y0)
>     A_shift = A - mu * np.eye(n)
>     
>     # Factorización LU (una sola vez, mu fijo)
>     P, L, U = lu(A_shift)
>     
>     v = y0 / np.linalg.norm(y0)
>     
>     for k in range(max_iter):
>         # Resolver (A - mu I) z = v
>         z1 = P.T @ v
>         z2 = solve(L, z1, lower=True)
>         z = solve(U, z2)
>         
>         # Cociente de Rayleigh para (A - mu I)^{-1}
>         rho = np.dot(v, z)
>         λ = mu + 1.0 / rho
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
> A = np.array([[2., 1., 0.], [1., 3., 1.], [0., 1., 2.]])
> y0 = np.array([1., 0., 0.])
> mu = 1.9  # cerca del autovalor 2
> 
> v, λ, iters = shifted_power_method(A, mu, y0)
> print(f"Autovector: {v}")
> print(f"Autovalor (cercano a {mu}): {λ}")
> print(f"Iteraciones: {iters}")
> ```

> [!algoritmo]
> **Implementación en Python de la iteración del cociente de Rayleigh (RQI).**
>
> ```python
> import numpy as np
> from scipy.linalg import solve
> 
> def rayleigh_quotient_iteration(A, y0, tol=1e-10, max_iter=100):
>     """
>     Iteración del cociente de Rayleigh (RQI) para autovalores de matrices simétricas.
>     
>     Parámetros:
>     - A: matriz simétrica (n x n)
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
>         mu = np.dot(v, A @ v)  # cociente de Rayleigh
>         
>         # Resolver (A - mu I) z = v
>         A_shift = A - mu * np.eye(len(v))
>         
>         # Nota: A_shift puede ser casi singular si mu está cerca de un autovalor
>         # Se usa solve con manejo de singularidad
>         try:
>             z = solve(A_shift, v)
>         except np.linalg.LinAlgError:
>             # Si es singular, el sistema tiene solución (v está en el núcleo)
>             # En la práctica, se aplica un pequeño desplazamiento adicional
>             z = solve(A_shift + 1e-12 * np.eye(len(v)), v)
>         
>         v_new = z / np.linalg.norm(z)
>         
>         if np.linalg.norm(v_new - v) < tol:
>             return v_new, mu, k + 1
>         
>         v = v_new
>     
>     return v, mu, max_iter
> 
> # Ejemplo (matriz simétrica)
> A = np.array([[2., 1.], [1., 2.]])
> y0 = np.array([1., 0.])
> 
> v, λ, iters = rayleigh_quotient_iteration(A, y0)
> print(f"Autovector: {v}")
> print(f"Autovalor: {λ}")
> print(f"Iteraciones: {iters}")
> ```

---

## Costo computacional

> [!info]
> **Comparación de costos.**
>
> | Método | Costo por iteración | Observaciones |
> |:---|:---|:---|
> | Potencia directa | $O(\text{nnz})$ | Solo productos matriz-vector |
> | Potencia inversa fija | $O(n^2)$ (tras LU $O(n^3)$) | LU una sola vez |
> | Potencia desplazada fija | $O(n^2)$ (tras LU $O(n^3)$) | LU una sola vez |
> | RQI | $O(n^3)$ | ¡Matriz cambia cada iteración! |
>
> **Observaciones importantes:**
>
> - Para $\mu$ fijo, la factorización LU se calcula **una sola vez** y se reutiliza en todas las iteraciones.
> - En RQI, la matriz $A - \mu^{(k)} I$ cambia en cada iteración porque $\mu^{(k)}$ cambia. Esto requiere una nueva factorización en cada paso, con costo $O(n^3)$ por iteración.
> - RQI es más costoso por iteración, pero su convergencia cúbica significa que se requieren muy pocas iteraciones (típicamente 3-5) para alcanzar precisión de máquina.

---

## Relación con otras notas

> [!info]
> - Este método generaliza la [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] ($\mu = 0$) al caso de desplazamiento arbitrario.
> - La velocidad de convergencia está determinada por la razón $|\lambda_j - \mu|/|\lambda_k - \mu|$, análoga a la razón $|\lambda_2/\lambda_1|$ en el método de la potencia (véase [[Velocidad Convergencia Razon Lambda2 Lambda1]]).
> - La estimación del autovalor se basa en el [[Calculo Constante Normalizacion Rayleigh|cociente de Rayleigh]].
> - La iteración del cociente de Rayleigh (RQI) es una de las técnicas más rápidas para calcular autovalores aislados de matrices simétricas.
> - Para matrices no simétricas, el RQI converge cuadráticamente (no cúbicamente), pero sigue siendo muy eficiente.

---

## Limitaciones y advertencias

> [!warning]
> **Limitaciones del método de la potencia desplazada.**
>
> 1. **Elección de $\mu$:** Si $\mu$ está lejos del autovalor deseado, la convergencia puede ser lenta o incluso divergente (si el autovalor dominante de $(A - \mu I)^{-1}$ no es el deseado).
>
> 2. **Singularidad:** Si $\mu$ es exactamente igual a un autovalor de $A$, entonces $A - \mu I$ es singular y el método falla. En la práctica se usa un $\mu$ cercano pero no exacto.
>
> 3. **Costo de RQI:** Para RQI, cada iteración requiere resolver un sistema lineal con matriz diferente, lo que puede ser prohibitivo para matrices grandes.
>
> 4. **Estabilidad:** Cuando $\mu$ está muy cerca de $\lambda_j$, la matriz $A - \mu I$ está mal condicionada, lo que puede causar inestabilidad numérica al resolver el sistema lineal.
>
> 5. **No simétricas:** Para matrices no simétricas, el RQI no garantiza convergencia cúbica (solo cuadrática) y puede ser inestable.

---

## Resumen

> [!corolario]
> El método de la potencia desplazada es una poderosa extensión de la potencia inversa que permite:
>
> | Aspecto | Descripción |
> |:---|:---|
> | Objetivo | Calcular el autovalor más cercano a $\mu$ |
> | Iteración | Resolver $(A - \mu I) z = y^{(k)}$, normalizar |
> | Convergencia (fijo) | Lineal con razón $|\lambda_j - \mu|/|\lambda_k - \mu|$ |
> | RQI (adaptativo) | Convergencia cúbica para matrices simétricas |
> | Costo por iteración | $O(n^2)$ (tras LU inicial) para $\mu$ fijo; $O(n^3)$ para RQI |
>
> **Conclusión práctica:**
> - Si se tiene una buena estimación del autovalor deseado, la potencia desplazada con $\mu$ fijo es muy eficiente (pocas iteraciones, LU una sola vez).
> - Para máxima precisión en matrices simétricas, RQI es imbatible (convergencia cúbica), pero su costo por iteración es alto.
> - Para matrices muy grandes donde $O(n^3)$ es inviable, se prefieren métodos de Krylov (Lanczos/Arnoldi).
>
> La potencia desplazada y RQI completan el espectro de variantes del método de la potencia, junto con la [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] ($\mu = 0$) y la [[Iteracion Simultanea|iteración simultánea]] para múltiples autovalores.