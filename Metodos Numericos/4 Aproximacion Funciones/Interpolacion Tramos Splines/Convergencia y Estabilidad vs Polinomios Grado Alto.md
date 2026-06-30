---
title: Convergencia y Estabilidad frente a Polinomios de Grado Alto
order: 5
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
  - convergencia
draft: false
aliases:
  - Splines vs polinomios
  - Convergencia de splines
  - Estabilidad de splines
---

# Convergencia y Estabilidad frente a Polinomios de Grado Alto

> [!definicion]
> La ventaja decisiva de los [[Interpolacion Tramos Splines/index|splines]] sobre la [[Interpolacion Polinomica/index|interpolación polinómica global]] es su **convergencia estable**: al refinar la malla ($h \to 0$ con grado fijo), el error decrece de forma garantizada, sin la divergencia del [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]].

> [!info]
> La diferencia estructural: el polinomio global aumenta el **grado** con el número de nodos; el spline mantiene el grado bajo y aumenta el **número de tramos**. Lo primero amplifica el factor $f^{(n+1)}/(n+1)!$ del error; lo segundo lo mantiene acotado.

---

## Convergencia comparada

> [!teorema]
> Para $f \in C^4[a,b]$ y malla de paso $h$:
> $$\text{Spline cúbico:}\quad \|f - S\|_\infty = O(h^4) \xrightarrow{h\to0} 0 \ \text{(siempre)}.$$
> En cambio, la interpolación polinómica global con nodos **equiespaciados** puede cumplir
> $$\|f - p_n\|_\infty \xrightarrow{n\to\infty} \infty \quad \text{(p. ej. función de Runge)}.$$

> [!info]
> | Estrategia de refinamiento | Convergencia |
> |:---|:---|
> | Spline lineal ($h\to0$) | $O(h^2)$, garantizada |
> | Spline cúbico ($h\to0$) | $O(h^4)$, garantizada |
> | Polinomio global equiespaciado ($n\to\infty$) | puede **diverger** (Runge) |
> | Polinomio global en Chebyshev ($n\to\infty$) | converge (si $f$ analítica) |

---

## Por qué los splines son estables

> [!teoria]
> El [[Error Interpolacion Formula Cauchy|error de interpolación]] en cada tramo de un spline depende solo de $f^{(m+1)}$ **local** y de $h$ pequeño, no de derivadas de orden creciente. Como el grado $m$ es fijo ($1$ o $3$), el factor $f^{(m+1)}/(m+1)!$ está acotado y $h^{m+1} \to 0$ controla el error. El polinomio global, en cambio, involucra $f^{(n+1)}$ con $n\to\infty$, que puede crecer más rápido que $(n+1)!$.

> [!info]
> **Constante de Lebesgue.** La sensibilidad de la interpolación a perturbaciones la mide $\Lambda$:
>
> | Método | Constante de Lebesgue |
> |:---|:---|
> | Polinomio equiespaciado | $\sim 2^n$ (explota) |
> | Polinomio Chebyshev | $\sim \log n$ |
> | Spline cúbico | acotada, $\leq 3$ (independiente de $n$) |
>
> La constante acotada del spline implica estabilidad numérica uniforme: el error de los datos no se amplifica al refinar.

---

## Ejemplo: función de Runge revisitada

> [!ejemplo]
> **$f(x) = 1/(1+25x^2)$ en $[-1,1]$**, error máximo:
>
> | Nodos | Polinomio global | Spline cúbico |
> |:---:|:---:|:---:|
> | 11 | 1.92 | 0.022 |
> | 21 | 58.6 | $1.4\times10^{-3}$ |
> | 41 | $> 10^3$ | $9\times10^{-5}$ |
>
> El spline converge monótonamente como $O(h^4)$ mientras el polinomio global diverge. Con la misma malla equiespaciada, el spline es la única opción viable.

---

## Cuándo usar cada uno

> [!info]
> | Situación | Método |
> |:---|:---|
> | Pocos nodos, $f$ muy suave | polinomio global |
> | Nodos libres, alta precisión | polinomio en Chebyshev (baricéntrico) |
> | Muchos nodos equiespaciados | **spline cúbico** |
> | Datos con esquinas o cambios bruscos | spline (lineal o con nodos adaptados) |
> | Se necesita derivada/curvatura continua | spline cúbico |

> [!warning]
> Los splines no son perfectos: su convergencia $O(h^4)$ es menor que la **espectral** ($O(\rho^{-n})$) de la interpolación de Chebyshev para funciones analíticas. Para $f$ analítica y nodos libres, Chebyshev gana; para datos dados o $f$ poco suave, el spline es superior.

---

## Relación con otras notas

> [!info]
> - El fenómeno que los splines evitan: [[Fenomeno Runge y Nodos Chebyshev]].
> - La propiedad variacional que da la estabilidad: [[Propiedad Minima Curvatura]].
> - Las cotas de error por tramo: [[Splines Lineales Continuidad C0]] y [[Splines Cubicos Naturales Sujetos]].
> - El error global del polinomio: [[Error Interpolacion Formula Cauchy]].

---

## Resumen

| Aspecto | Spline | Polinomio global (equi.) |
|:---|:---|:---|
| Refinamiento | $h\to0$, grado fijo | $n\to\infty$, grado crece |
| Convergencia | $O(h^4)$ garantizada | puede diverger |
| Constante de Lebesgue | acotada | $\sim 2^n$ |
| Oscilación | ninguna | Runge |
| Suavidad | $C^2$ | $C^\infty$ |

> [!corolario]
> Los splines convergen de forma estable porque refinan aumentando tramos a grado fijo, manteniendo acotado el factor $f^{(m+1)}/(m+1)!$ del error y la constante de Lebesgue; el polinomio global equiespaciado, al subir el grado, puede diverger por el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]. Por eso, para muchos nodos —especialmente equiespaciados o datos con poca suavidad— el [[Splines Cubicos Naturales Sujetos|spline cúbico]] $O(h^4)$ es la elección robusta, reservando la interpolación polinómica global de alto orden para funciones analíticas con nodos de Chebyshev. Esta estabilidad cierra el estudio de la [[Interpolacion Tramos Splines/index|interpolación por tramos]].
