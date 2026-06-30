---
title: Orden Convergencia Lineal Constante Asintotica
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - punto-fijo
  - convergencia
draft: false
aliases:
  - Orden de convergencia lineal
  - Constante asintótica
  - Factor de convergencia lineal
---

# Orden de Convergencia Lineal y Constante Asintótica

> [!definicion]
> Sea $\{x^{(k)}\}$ una sucesión que converge a $r$. Se dice que la convergencia es **lineal** si existe una constante $c \in (0, 1)$ tal que:
> $$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = c$$
>
> La constante $c$ se llama **constante asintótica** o **factor de convergencia lineal**.

> [!info]
> Para el método de punto fijo $x^{(k+1)} = g(x^{(k)})$ con $g$ diferenciable y $|g'(r)| < 1$, la constante asintótica es precisamente $c = |g'(r)|$.

---

## Ejemplo

> [!ejemplo]
> **Comparación de convergencia lineal con diferentes constantes asintóticas.**
>
> | $c = \|g'(r)\|$ | Iteraciones para 1 dígito | Iteraciones para 3 dígitos | Iteraciones para 6 dígitos |
> |:---|:---:|:---:|:---:|
> | 0.1 | 1 | 2 | 3 |
> | 0.5 | 4 | 10 | 20 |
> | 0.8 | 11 | 31 | 62 |
> | 0.9 | 22 | 66 | 132 |
> | 0.99 | 230 | 690 | 1380 |
>
> **Cálculo:** Para reducir el error en un factor $\varepsilon = 10^{-d}$, se necesita:
> $$c^k \approx \varepsilon \quad \Rightarrow \quad k \approx \frac{\ln \varepsilon}{\ln c} = \frac{-d \ln 10}{\ln c}$$
>
> **Observación:** Cuando $c$ se acerca a $1$, el número de iteraciones crece drásticamente. Para $c=0.99$, se necesitan $230$ iteraciones para un dígito y $1380$ para seis dígitos.

---

## Relación entre la constante asintótica y la derivada

> [!teorema]
> Sea $g$ una función continuamente diferenciable en una vecindad del punto fijo $r$, con $r = g(r)$. Si $|g'(r)| < 1$, entonces la iteración $x^{(k+1)} = g(x^{(k)})$ converge localmente a $r$ con convergencia lineal y constante asintótica $c = |g'(r)|$.

> [!demostracion]
> Por el teorema del valor medio:
> $$x^{(k+1)} - r = g(x^{(k)}) - g(r) = g'(\xi_k)(x^{(k)} - r)$$
> donde $\xi_k$ está entre $x^{(k)}$ y $r$.
>
> Tomando valor absoluto:
> $$\frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = |g'(\xi_k)|$$
>
> Como $x^{(k)} \to r$, se tiene $\xi_k \to r$. Por continuidad de $g'$:
> $$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = |g'(r)| = c$$

> [!corolario]
> **Interpretación práctica:**
> - Si $c = 0.1$, cada iteración agrega aproximadamente 1 dígito decimal.
> - Si $c = 0.5$, cada iteración agrega aproximadamente 0.3 dígitos.
> - Si $c = 0.9$, cada iteración agrega aproximadamente 0.045 dígitos.

---

## Estimación de la constante asintótica en la práctica

> [!info]
> **¿Cómo estimar $c$ sin conocer $g'(r)$?**
>
> Durante la iteración, se puede aproximar $c$ mediante:
> $$c_k = \frac{|x^{(k+1)} - x^{(k)}|}{|x^{(k)} - x^{(k-1)}|}$$
>
> Para $k$ suficientemente grande, $c_k \to c$.
>
> **Ejemplo:** Para $g(x) = \sqrt{x+1}$ con $r = \phi \approx 1.618$:
>
> | $k$ | $x^{(k)}$ | $\|x^{(k)} - x^{(k-1)}\|$ | $c_k$ |
> |:---|:---|:---|:---|
> | 0 | 1.0000 | — | — |
> | 1 | 1.4142 | 0.4142 | — |
> | 2 | 1.5538 | 0.1396 | 0.337 |
> | 3 | 1.5981 | 0.0443 | 0.317 |
> | 4 | 1.6118 | 0.0137 | 0.309 |
> | 5 | 1.6161 | 0.0043 | 0.314 |
>
> El valor teórico es $c = |g'(r)| = 1/(2\sqrt{r+1}) \approx 0.309$, consistente con la estimación.

---

## Caso especial: convergencia sublineal

> [!definicion]
> La convergencia es **sublineal** si:
> $$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = 1$$
> pero la sucesión sigue convergiendo (más lentamente que cualquier convergencia lineal con $c < 1$).

> [!ejemplo]
> **La bisección tiene convergencia sublineal?**
>
> Para bisección, se cumple $|x^{(k)} - r| \leq (b-a)/2^{k+1}$. El cociente entre errores consecutivos tiende a $1/2$, por lo que **es lineal** con $c = 1/2$. No es sublineal.
>
> **Ejemplo verdadero de convergencia sublineal:**
> $$x^{(k)} = \frac{1}{k} \to 0, \quad \lim_{k \to \infty} \frac{1/(k+1)}{1/k} = 1$$
>
> Este tipo de convergencia es más lento que cualquier progresión geométrica. En métodos numéricos, la convergencia sublineal es indeseable.

---

## Relación con el teorema de Banach

> [!info]
> El [[Teorema Punto Fijo Banach Contraccion]] garantiza convergencia lineal con constante $L$, que es una cota superior de $|g'(x)|$ en todo el intervalo. La constante asintótica $c = |g'(r)|$ puede ser menor que $L$, por lo que la convergencia real es más rápida que la cota garantizada por el teorema.
>
> **Ejemplo:** Para $g(x) = \cos(x)$ en $[0, 1]$, $L = \sin(1) \approx 0.8415$, pero $c = |g'(r)| = \sin(r) \approx \sin(0.7391) \approx 0.673$. La convergencia real es más rápida que la cota pesimista.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Orden de convergencia** | Lineal ($p = 1$) |
| **Definición** | $\lim_{k \to \infty} \frac{\|e_{k+1}\|}{\|e_k\|} = c$ con $0 < c < 1$ |
| **Constante asintótica** | $c = \|g'(r)\|$ para punto fijo |
| **Interpretación** | $c \approx 0.1$: 1 dígito por iteración; $c \approx 0.9$: muy lento |
| **Caso límite** | $c \to 1$: convergencia sublineal (indeseable) |
| **Caso óptimo** | $c = 0$: convergencia superlineal o cuadrática |

> [!corolario]
> La convergencia del método de punto fijo es lineal con constante asintótica $c = |g'(r)|$, siempre que $0 < |g'(r)| < 1$. Cuanto menor sea $c$, más rápida es la convergencia. El [[Teorema Punto Fijo Banach Contraccion]] proporciona una cota $L$ que puede ser más pesimista que $c$. Para acelerar la convergencia, se busca construir $g$ con $|g'(r)|$ pequeño, idealmente $0$, como en el [[Newton Raphson/index]].