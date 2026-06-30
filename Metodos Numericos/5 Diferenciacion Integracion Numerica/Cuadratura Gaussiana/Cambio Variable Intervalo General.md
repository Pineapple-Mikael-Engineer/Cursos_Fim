---
title: Cambio de Variable a Intervalo General
order: 5
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
draft: false
aliases:
  - Cambio de variable de cuadratura
  - Intervalo general
  - Transformación afín de Gauss
---

# Cambio de Variable a Intervalo General

> [!definicion]
> Los nodos y pesos de [[Cuadratura Gaussiana/index|Gauss-Legendre]] se tabulan en el intervalo de referencia $[-1,1]$. Para integrar en un intervalo general $[a,b]$ se aplica el **cambio de variable afín**
> $$x = \frac{b-a}{2}\,t + \frac{a+b}{2}, \qquad dx = \frac{b-a}{2}\,dt, \qquad t\in[-1,1].$$

> [!info]
> La transformación lineal mapea $[-1,1]$ en $[a,b]$ conservando el grado de exactitud. Es un paso mecánico imprescindible para usar las tablas estándar en cualquier integral.

---

## Fórmula transformada

> [!teorema]
> Con el cambio afín, la cuadratura de Gauss-Legendre en $[a,b]$ es
> $$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^1 f\!\left(\frac{b-a}{2}t + \frac{a+b}{2}\right)dt \approx \frac{b-a}{2}\sum_{i=1}^n w_i\, f\!\left(\frac{b-a}{2}t_i + \frac{a+b}{2}\right),$$
> donde $t_i, w_i$ son los nodos y pesos tabulados en $[-1,1]$.

> [!demostracion]
> Sustituyendo $x = \frac{b-a}{2}t + \frac{a+b}{2}$ en la integral, $dx = \frac{b-a}{2}dt$, y los límites $x=a,b$ corresponden a $t=-1,1$. Aplicando la regla de Gauss en $t$ a la integral transformada se obtiene la fórmula. El factor $\frac{b-a}{2}$ (jacobiano del cambio) multiplica tanto los pesos como el diferencial.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^2 e^x\,dx = e^2 - 1 \approx 6.389056$** con Gauss de 2 nodos. Cambio $[0,2]\to[-1,1]$: $x = t + 1$, factor $\frac{b-a}{2} = 1$. Nodos $t_i = \pm1/\sqrt3 \Rightarrow x_i = 1\pm1/\sqrt3 \approx 0.4226,\ 1.5774$:
> $$\int_0^2 e^x\,dx \approx 1\cdot\big[1\cdot e^{0.4226} + 1\cdot e^{1.5774}\big] = 1.5259 + 4.8424 = 6.3683.$$
> Error $2.1\times10^{-2}$ con 2 evaluaciones; con 3 nodos baja a $\sim10^{-3}$.

---

## Composición: Gauss compuesto

> [!teoria]
> Para integrandos sobre intervalos grandes o poco suaves, se **subdivide** $[a,b]$ en paneles y se aplica Gauss en cada uno (Gauss compuesto), igual que con [[Metodos Compuestos/index|Newton-Cotes]]:
> $$\int_a^b f\,dx = \sum_{k} \int_{c_k}^{c_{k+1}} f\,dx \approx \sum_k \frac{c_{k+1}-c_k}{2}\sum_i w_i f(\cdots).$$
> Combina la eficiencia de Gauss por panel con la robustez de la subdivisión, y permite **adaptividad** (más paneles donde $f$ varía rápido).

---

## Intervalos infinitos

> [!info]
> Para dominios no acotados, en vez de truncar se usan **otras familias ortogonales** o cambios de variable:
>
> | Integral | Método |
> |:---|:---|
> | $\int_0^\infty e^{-x}f(x)\,dx$ | Gauss-Laguerre (peso $e^{-x}$) |
> | $\int_{-\infty}^\infty e^{-x^2}f(x)\,dx$ | Gauss-Hermite (peso $e^{-x^2}$) |
> | $\int_0^\infty f(x)\,dx$ general | cambio $x = \frac{t}{1-t}$ a $[0,1)$ |
>
> Cada familia ([[Fundamentos Gauss Legendre Polinomios Ortogonales|polinomios ortogonales]]) integra exactamente su peso por un polinomio.

---

## Algoritmo

> [!algoritmo]
> **Gauss-Legendre en $[a,b]$ con NumPy.**
>
> ```python
> import numpy as np
>
> def gauss_legendre(f, a, b, n):
>     t, w = np.polynomial.legendre.leggauss(n)   # nodos y pesos en [-1,1]
>     x = 0.5*(b - a)*t + 0.5*(a + b)              # cambio de variable
>     return 0.5*(b - a) * np.sum(w * f(x))
> ```

---

## Relación con otras notas

> [!info]
> - Los nodos/pesos de referencia que se transforman: [[Determinacion Nodos y Pesos Optimos]].
> - La eficiencia que se conserva tras el cambio: [[Comparacion Eficiencia vs Newton Cotes]].
> - La subdivisión análoga: [[Metodos Compuestos/index]].
> - Otras familias para dominios especiales: [[Fundamentos Gauss Legendre Polinomios Ortogonales]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Cambio | $x = \frac{b-a}{2}t + \frac{a+b}{2}$ |
| Jacobiano | $\frac{b-a}{2}$ |
| Fórmula | $\frac{b-a}{2}\sum_i w_i f(x_i)$ |
| Gauss compuesto | subdividir + Gauss por panel |
| Infinitos | Laguerre, Hermite |

> [!corolario]
> El cambio de variable afín $x = \frac{b-a}{2}t + \frac{a+b}{2}$ traslada los nodos y pesos tabulados de Gauss-Legendre de $[-1,1]$ a cualquier $[a,b]$, multiplicando por el jacobiano $\frac{b-a}{2}$ y conservando el grado de exactitud. Para intervalos grandes o integrandos poco suaves se usa Gauss compuesto (subdivisión por paneles, con posible adaptividad), y para dominios infinitos las familias de [[Fundamentos Gauss Legendre Polinomios Ortogonales|Laguerre y Hermite]]. Con este paso mecánico, la [[Cuadratura Gaussiana/index|cuadratura gaussiana]] queda lista para integrar cualquier función sobre cualquier intervalo, cerrando el capítulo de integración numérica.
