---
title: Criterio Radio Espectral Convergencia
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - convergencia
  - radio-espectral
draft: false
aliases:
  - Criterio del radio espectral
  - Teorema espectral de convergencia
  - ρ(T) < 1
---

# Criterio del Radio Espectral para Convergencia

> [!definicion]
> El **radio espectral** de una matriz $T \in \mathbb{R}^{n \times n}$ se define como:
> $$\rho(T) = \max\{|\lambda| : \lambda \text{ es autovalor de } T\}$$
> donde $\lambda$ son los autovalores (reales o complejos) de $T$.

---

## Ejemplo

> [!ejemplo]
> **Comparación de convergencia según $\rho(T)$.**
>
> Considérense tres matrices $T_1, T_2, T_3 \in \mathbb{R}^{2 \times 2}$ y la iteración $y^{(k+1)} = T y^{(k)}$ partiendo de $y^{(0)} = (1, 1)^T$.
>
> **Caso 1: $\rho(T_1) = 0.5 < 1$ (convergencia rápida).**
> $$T_1 = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.3 \end{pmatrix}, \quad \rho(T_1) = 0.5$$
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ | $\|y^{(k)}\|_\infty$ |
> |:---|:---:|:---:|:---:|
> | 0 | 1.000 | 1.000 | 1.000 |
> | 1 | 0.500 | 0.300 | 0.500 |
> | 2 | 0.250 | 0.090 | 0.250 |
> | 3 | 0.125 | 0.027 | 0.125 |
> | 4 | 0.063 | 0.008 | 0.063 |
> | 5 | 0.031 | 0.002 | 0.031 |
>
> **Caso 2: $\rho(T_2) = 0.95 < 1$ (convergencia lenta).**
> $$T_2 = \begin{pmatrix} 0.95 & 0 \\ 0 & 0.3 \end{pmatrix}, \quad \rho(T_2) = 0.95$$
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ | $\|y^{(k)}\|_\infty$ |
> |:---|:---:|:---:|:---:|
> | 0 | 1.000 | 1.000 | 1.000 |
> | 1 | 0.950 | 0.300 | 0.950 |
> | 2 | 0.903 | 0.090 | 0.903 |
> | 3 | 0.857 | 0.027 | 0.857 |
> | 4 | 0.814 | 0.008 | 0.814 |
> | 5 | 0.774 | 0.002 | 0.774 |
>
> **Caso 3: $\rho(T_3) = 1$ (sin convergencia).**
> $$T_3 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad \rho(T_3) = 1$$
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ |
> |:---|:---:|:---:|
> | 0 | 1.000 | 1.000 |
> | 1 | 2.000 | 1.000 |
> | 2 | 3.000 | 1.000 |
> | 3 | 4.000 | 1.000 |
> | 4 | 5.000 | 1.000 |
>
> **Caso 4: $\rho(T_4) = 1.2 > 1$ (divergencia).**
> $$T_4 = \begin{pmatrix} 1.2 & 0 \\ 0 & 0.3 \end{pmatrix}, \quad \rho(T_4) = 1.2$$
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ |
> |:---|:---:|:---:|
> | 0 | 1.000 | 1.000 |
> | 1 | 1.200 | 0.300 |
> | 2 | 1.440 | 0.090 |
> | 3 | 1.728 | 0.027 |
> | 4 | 2.074 | 0.008 |
> | 5 | 2.488 | 0.002 |

---

## Relación con la iteración de punto fijo

> [!teoria]
> Sea la iteración de punto fijo $y^{(k+1)} = T y^{(k)} + c$ con punto fijo $x = Tx + c$. Defínase el error $e^{(k)} = y^{(k)} - x$. Entonces:
> $$e^{(k+1)} = T e^{(k)}$$
>
> y por inducción:
> $$e^{(k)} = T^k e^{(0)}$$
>
> La iteración converge a $x$ para cualquier $y^{(0)}$ si y solo si $T^k \to 0$ (matriz nula).

---

## Teorema principal

> [!teorema]
> Para cualquier matriz $T \in \mathbb{R}^{n \times n}$, se cumple:
> $$\lim_{k \to \infty} T^k = 0 \quad \text{si y solo si} \quad \rho(T) < 1$$

---

## Demostración

### Parte 1: $T^k \to 0 \implies \rho(T) < 1$

> [!demostracion]
> Sea $\lambda$ un autovalor de $T$ con autovector $v \neq 0$:
> $$T v = \lambda v$$
>
> Entonces:
> $$T^k v = \lambda^k v$$
>
> Si $T^k \to 0$, entonces $T^k v \to 0$, es decir $\lambda^k v \to 0$. Como $v \neq 0$, necesariamente $\lambda^k \to 0$, lo cual implica $|\lambda| < 1$.
>
> Esto vale para todo autovalor $\lambda$ de $T$, por lo tanto:
> $$\rho(T) = \max |\lambda| < 1$$

### Parte 2: $\rho(T) < 1 \implies T^k \to 0$

> [!lema]
> Para toda matriz $T$ y todo $\varepsilon > 0$, existe una norma matricial subordinada $\|\cdot\|$ (dependiente de $T$ y $\varepsilon$) tal que:
> $$\|T\| \leq \rho(T) + \varepsilon$$

> [!demostracion]
> (Lema no demostrado aquí, es un resultado estándar del análisis matricial que sigue de la forma de Jordan de $T$).

> [!demostracion]
> Supóngase $\rho(T) < 1$. Elíjase $\varepsilon = \frac{1 - \rho(T)}{2} > 0$. Por el lema, existe una norma matricial $\|\cdot\|$ tal que:
> $$\|T\| \leq \rho(T) + \varepsilon = \frac{1 + \rho(T)}{2} =: q < 1$$
>
> Por la propiedad submultiplicativa de la norma:
> $$\|T^k\| \leq \|T\|^k \leq q^k$$
>
> Como $q < 1$, se tiene $q^k \to 0$, por lo tanto $\|T^k\| \to 0$.
>
> En un espacio de dimensión finita, la convergencia a cero en una norma implica convergencia a cero en cualquier norma (todas las normas son equivalentes). Por lo tanto $T^k \to 0$.

---

## Resumen de la demostración

| Dirección                        | Argumento clave                                                  |
| :------------------------------- | :--------------------------------------------------------------- |
| $T^k \to 0 \implies \rho(T) < 1$ | Autovalores: $T^k v = \lambda^k v \to 0 \implies \|\lambda \| < 1$ |
| $\rho(T) < 1 \implies T^k \to 0$ | Existe norma con $\|T\| < 1 \implies \|T^k\| \leq \|T\|^k \to 0$ |

> [!info]
> **Observación importante.**
>
> La implicación $\rho(T) < 1 \implies T^k \to 0$ **no** significa que $\|T\| < 1$ para toda norma. De hecho, puede ocurrir que $\rho(T) < 1$ pero $\|T\|_\infty > 1$ o $\|T\|_1 > 1$. Lo que garantiza el teorema es la **existencia** de alguna norma (dependiente de $T$) en la que $\|T\| < 1$.
>
> Por ejemplo, la matriz del caso 3 ($\rho(T)=1$) no converge. La matriz $T = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$ tiene $\rho(T)=0$ y $T^2=0$ (converge), pero $\|T\|_\infty = 2 > 1$.

---

## Implicaciones prácticas

> [!info]
> **Interpretación del radio espectral.**
>
> - $\rho(T)$ es el factor de contracción asintótico del error.
> - Si $\rho(T) = 0.1$, el error se multiplica por $0.1$ en cada iteración (aproximadamente un dígito decimal por iteración).
> - Si $\rho(T) = 0.9$, el error se multiplica por $0.9$ (se requieren muchas más iteraciones).
> - La tasa de convergencia lineal es $R = -\ln \rho(T)$.
> - Los dígitos ganados por iteración son $R_{10} = -\log_{10} \rho(T)$.

> [!warning]
> **Limitaciones del criterio.**
>
> - Calcular $\rho(T)$ explícitamente puede ser tan costoso como resolver el sistema original.
> - El criterio es **necesario y suficiente**, pero en la práctica se utilizan condiciones suficientes más fáciles de verificar, como la [[Convergencia Iterativos/Teorema Diagonal Dominante Estricta|diagonal dominante estricta]].
> - El caso $\rho(T) = 1$ es indeterminado: $T^k$ puede converger (si $T = I$? no, $I^k = I \not\to 0$), diverger u oscilar.

---

## Relación con Jacobi y Gauss-Seidel

> [!info]
> Para el método de [[Jacobi]], la matriz de iteración es $T_J = D^{-1}(E+F)$. El método converge si y solo si $\rho(T_J) < 1$.
>
> Para el método de [[Gauss Seidel]], la matriz de iteración es $T_{GS} = (D-E)^{-1}F$. El método converge si y solo si $\rho(T_{GS}) < 1$.
>
> El teorema de Stein-Rosenberg (véase [[Gauss Seidel]]) establece que para matrices con $a_{ij} \leq 0$ para $i \neq j$ y $a_{ii} > 0$, si $\rho(T_J) < 1$, entonces $\rho(T_{GS}) \leq \rho(T_J) < 1$.

---

## Resumen

> [!corolario]
> El criterio del radio espectral es el resultado fundamental del análisis de convergencia de métodos iterativos lineales:
> - $T^k \to 0$ si y solo si $\rho(T) < 1$.
> - Por lo tanto, la iteración $y^{(k+1)} = T y^{(k)} + c$ converge para cualquier $y^{(0)}$ si y solo si $\rho(T) < 1$.
>
> La demostración requiere dos direcciones:
> 1. $T^k \to 0 \implies \rho(T) < 1$ (argumento con autovalores).
> 2. $\rho(T) < 1 \implies T^k \to 0$ (existencia de una norma con $\|T\| < 1$, usando el lema de la forma de Jordan).
>
> Este criterio se aplica directamente a [[Jacobi]] y [[Gauss Seidel]]. Las condiciones suficientes prácticas, como la diagonal dominante estricta, se demuestran mostrando que $\rho(T_J) < 1$ o $\rho(T_{GS}) < 1$ bajo dichas hipótesis, tema desarrollado en [[Convergencia Iterativos/Teorema Diagonal Dominante Estricta|Teorema Diagonal Dominante Estricta]].