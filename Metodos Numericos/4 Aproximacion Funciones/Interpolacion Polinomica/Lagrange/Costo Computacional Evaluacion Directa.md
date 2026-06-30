---
title: Costo Computacional y Evaluación Directa
order: 2
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - lagrange
draft: false
aliases:
  - Costo de Lagrange
  - Forma baricéntrica
  - Barycentric Lagrange
---

# Costo Computacional y Evaluación Directa (Lagrange)

> [!definicion]
> La **evaluación directa** de la [[Formulacion Polinomios Cardinales L i x|forma de Lagrange]] calcula, para cada punto $x$, los $n+1$ polinomios cardinales $L_i(x)$ y suma $p_n(x) = \sum_i y_i L_i(x)$. Cada $L_i(x)$ es un producto de $n$ factores, de modo que el costo por punto es $O(n^2)$.

> [!info]
> Ese costo cuadrático por punto, y la pésima propiedad de **no ser incremental**, son los defectos de la forma directa. Ambos se corrigen con la **forma baricéntrica**, que reescribe Lagrange para evaluar en $O(n)$ por punto tras un precálculo de $O(n^2)$.

---

## Costo de la forma directa

> [!proposicion]
> Evaluar $p_n(x) = \sum_{i=0}^n y_i \prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ en un punto cuesta:
> - $n+1$ cardinales, cada uno con $\sim 2n$ operaciones → $O(n^2)$ por punto.
> - Evaluar en $m$ puntos: $O(m\,n^2)$.
> - **No incremental:** añadir un nodo recalcula todos los $L_i$ (cambian de grado).

> [!warning]
> Además del costo, la forma directa es numéricamente frágil: los denominadores $\prod_{j\neq i}(x_i - x_j)$ pueden ser muy pequeños o grandes, y la suma de cardinales con signos opuestos sufre [[Perdida Significancia y Cancelacion Catastrofica|cancelación]] para $n$ alto.

---

## Forma baricéntrica

> [!teorema]
> Definiendo los **pesos baricéntricos** (independientes de $x$ y de los $y_i$)
> $$w_i = \frac{1}{\prod_{j\neq i}(x_i - x_j)},$$
> el interpolador admite la **segunda forma baricéntrica**
> $$p_n(x) = \frac{\displaystyle\sum_{i=0}^n \dfrac{w_i}{x - x_i}\,y_i}{\displaystyle\sum_{i=0}^n \dfrac{w_i}{x - x_i}}, \qquad x \neq x_i.$$

> [!demostracion]
> Escríbase $\ell(x) = \prod_{j=0}^n (x - x_j)$. Entonces $L_i(x) = \ell(x)\,\dfrac{w_i}{x - x_i}$, de modo que $p_n(x) = \ell(x)\sum_i \dfrac{w_i}{x-x_i}y_i$. Aplicando lo mismo a la función constante $1 = \sum_i L_i(x) = \ell(x)\sum_i\frac{w_i}{x-x_i}$, se despeja $\ell(x) = 1/\sum_i\frac{w_i}{x-x_i}$. Sustituyendo, $\ell(x)$ se cancela y queda la fórmula baricéntrica.

> [!info]
> **Costos de la forma baricéntrica:**
> - **Precálculo de los $w_i$:** $O(n^2)$, una sola vez.
> - **Evaluación por punto:** $O(n)$ (dos sumas).
> - **Incremental:** añadir un nodo cuesta $O(n)$ (actualizar todos los $w_i$ y calcular el nuevo).
> - **Estable:** la versión baricéntrica es numéricamente estable para nodos bien distribuidos (Chebyshev).

---

## Ejemplo: comparación de costos

> [!ejemplo]
> **Evaluar $p_n$ en $m = 1000$ puntos**, distintos $n$:
>
> | $n$ | Directa $O(mn^2)$ | Baricéntrica: precálculo $O(n^2)$ + $O(mn)$ |
> |:---:|:---:|:---:|
> | 10 | $10^5$ | $10^2 + 10^4$ |
> | 50 | $2.5\times10^6$ | $2.5\times10^3 + 5\times10^4$ |
> | 100 | $10^7$ | $10^4 + 10^5$ |
>
> La forma baricéntrica es $\sim n$ veces más rápida al evaluar en muchos puntos, porque amortiza el $O(n^2)$ de los pesos una sola vez.

---

## Pesos baricéntricos para nodos especiales

> [!info]
> Para nodos estructurados los $w_i$ tienen fórmula cerrada (precálculo $O(n)$):
>
> | Nodos | Peso $w_i$ |
> |:---|:---|
> | Equiespaciados | $w_i = (-1)^i \binom{n}{i}$ |
> | Chebyshev (2.ª especie) | $w_i = (-1)^i \delta_i$, con $\delta_i = \tfrac12$ en los extremos, $1$ en el interior |
>
> Con nodos de Chebyshev, la forma baricéntrica es **el** método de referencia para interpolación de alto grado, estable y de costo $O(n)$ por evaluación.

---

## Algoritmo

> [!algoritmo]
> **Interpolación baricéntrica en Python.**
>
> ```python
> import numpy as np
>
> def pesos_baricentricos(x):
>     n = len(x)
>     w = np.ones(n)
>     for i in range(n):
>         for j in range(n):
>             if j != i:
>                 w[i] /= (x[i] - x[j])
>     return w                                  # O(n²), una sola vez
>
> def interp_baricentrica(x, y, w, xx):
>     num = np.zeros_like(xx, dtype=float)
>     den = np.zeros_like(xx, dtype=float)
>     for i in range(len(x)):
>         d = xx - x[i]
>         num += w[i] * y[i] / d
>         den += w[i] / d
>     return num / den                          # O(n) por punto de xx
> ```

---

## Relación con otras notas

> [!info]
> - La base que se evalúa: [[Formulacion Polinomios Cardinales L i x]] y [[Lagrange/index]].
> - La alternativa incremental con coeficientes: [[Forma Anidada y Eficiencia Algoritmo Horner]] (Newton + Horner).
> - La cancelación que la forma directa sufre: [[Perdida Significancia y Cancelacion Catastrofica]].
> - Dónde brilla la baricéntrica: [[Fenomeno Runge y Nodos Chebyshev]].

---

## Resumen

| Forma | Precálculo | Por punto | Incremental |
|:---|:---:|:---:|:---:|
| Directa | — | $O(n^2)$ | no |
| Baricéntrica | $O(n^2)$ | $O(n)$ | sí ($O(n)$) |
| [[Forma Anidada y Eficiencia Algoritmo Horner\|Newton + Horner]] | $O(n^2)$ | $O(n)$ | sí ($O(n)$) |

> [!corolario]
> La forma directa de Lagrange evalúa el interpolador en $O(n^2)$ por punto y no es incremental, defectos que la **forma baricéntrica** corrige: con pesos $w_i = 1/\prod_{j\neq i}(x_i-x_j)$ precalculados en $O(n^2)$, cada evaluación cuesta $O(n)$ y añadir un nodo es $O(n)$. Para nodos de Chebyshev los pesos tienen fórmula cerrada y la interpolación baricéntrica es estable hasta grados muy altos, convirtiéndola en el método práctico de referencia. La alternativa con coeficientes explícitos es [[Newton Diferencias Divididas/index|Newton]] evaluado por [[Forma Anidada y Eficiencia Algoritmo Horner|Horner]].
