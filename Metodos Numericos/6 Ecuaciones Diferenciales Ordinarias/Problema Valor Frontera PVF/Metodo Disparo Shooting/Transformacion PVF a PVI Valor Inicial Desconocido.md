---
title: Transformación de PVF a PVI con Valor Inicial Desconocido
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - disparo
draft: false
aliases:
  - Transformación PVF a PVI
  - Parámetro de disparo
  - Función objetivo del disparo
  - Shooting parameter
---

# Transformación de PVF a PVI con Valor Inicial Desconocido

> [!definicion]
> El método de [[Metodo Disparo Shooting/index|disparo]] parametriza el PVF $y''=f(x,y,y')$, $y(a)=\alpha$, $y(b)=\beta$ tratando la pendiente inicial desconocida $y'(a)=s$ como un **parámetro**. Cada $s$ define un [[Problema Valor Inicial PVI/index|PVI]] con solución $y(x; s)$, y se busca el $s$ que reproduce la condición de frontera del extremo derecho.

> [!info]
> La idea convierte "encontrar una función que satisface dos extremos" en "encontrar un número $s$": el PVF de dimensión infinita se reduce a una ecuación escalar $\phi(s)=0$. Es la reducción que hace al disparo tan atractivo: reutiliza PVI + raíces sin maquinaria nueva.

---

## El PVI parametrizado

> [!teorema]
> Para cada valor del parámetro $s$, el problema de valor inicial
> $$y'' = f(x, y, y'), \qquad y(a) = \alpha, \qquad y'(a) = s,$$
> tiene solución única $y(x; s)$ (por [[Teoremas Existencia Unicidad Picard Lindelof|Picard-Lindelöf]]). El PVF se satisface cuando $y(b; s) = \beta$.

> [!definicion]
> La **función objetivo** (o residuo de frontera) mide cuánto falla el extremo derecho:
> $$\phi(s) = y(b; s) - \beta.$$
> Resolver el PVF equivale a hallar la raíz $s^*$ de $\phi(s)=0$. Cada **evaluación** de $\phi$ requiere integrar el PVI completo de $a$ a $b$.

---

## Caso lineal: un solo ajuste

> [!teorema]
> Si el PVF es **lineal** ($y'' = p(x)y' + q(x)y + r(x)$), entonces $\phi(s)$ es una función **afín** de $s$:
> $$\phi(s) = y(b; s) - \beta = As + B.$$
> Basta con **dos** disparos ($s_0, s_1$) para determinar la recta y obtener exactamente $s^* = s_0 - \phi(s_0)\frac{s_1-s_0}{\phi(s_1)-\phi(s_0)}$. No hay iteración.

> [!demostracion]
> Por linealidad, $y(x;s) = y_p(x) + s\,y_h(x)$, donde $y_p$ resuelve el PVI con $y'(a)=0$ y $y_h$ el problema homogéneo con $y'(a)=1$, $y(a)=0$. Entonces $\phi(s) = y_p(b) + s\,y_h(b) - \beta$, afín en $s$. Dos evaluaciones fijan la recta y dan la raíz exacta.

> [!ejemplo]
> **$y'' = y$, $y(0)=0$, $y(1)=1$** (lineal). Dos disparos:
>
> | $s$ | $y(1;s)$ (RK4) | $\phi(s) = y(1;s) - 1$ |
> |:---:|:---:|:---:|
> | $0.5$ | $0.5876$ | $-0.4124$ |
> | $1.0$ | $1.1752$ | $+0.1752$ |
>
> Interpolación lineal: $s^* = 0.5 + 0.412\cdot\frac{0.5}{0.588} = 0.8504$. La solución exacta tiene $y'(0) = 1/\sinh 1 \approx 0.8509$. ✓

---

## Caso no lineal: iteración

> [!warning]
> Si $f$ es **no lineal**, $\phi(s)$ es no lineal y se necesita **iterar** ([[Metodo Newton para Condicion Frontera Residual|Newton]] o secante) hasta converger. Cada iteración integra un PVI completo, así que el costo es (nº de iteraciones) × (costo de una integración). Suele converger en pocas iteraciones si la estimación inicial es razonable.

---

## Algoritmo (caso lineal)

> [!algoritmo]
> **Disparo lineal con dos integraciones.**
>
> ```python
> import numpy as np
> from scipy.integrate import solve_ivp
>
> def disparo_lineal(f, a, b, alpha, beta, s0, s1):
>     def integra(s):
>         sol = solve_ivp(f, [a, b], [alpha, s], dense_output=True, rtol=1e-9)
>         return sol.y[0, -1]                 # y(b; s)
>     phi0 = integra(s0) - beta
>     phi1 = integra(s1) - beta
>     s = s0 - phi0 * (s1 - s0) / (phi1 - phi0)   # raíz exacta (afín)
>     sol = solve_ivp(f, [a, b], [alpha, s], dense_output=True, rtol=1e-9)
>     return s, sol
>
> # y'' = y  →  [y, y']' = [y', y]
> f = lambda x, u: [u[1], u[0]]
> s, sol = disparo_lineal(f, 0, 1, 0.0, 1.0, 0.5, 1.0)
> ```

---

## Relación con otras notas

> [!info]
> - El PVI que se integra repetidamente: [[Problema Valor Inicial PVI/index]] y [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - La iteración para el caso no lineal: [[Metodo Newton para Condicion Frontera Residual]].
> - La existencia del PVI parametrizado: [[Teoremas Existencia Unicidad Picard Lindelof]].
> - La alternativa que no parametriza: [[Comparacion Disparo vs Diferencias Finitas]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Parámetro | pendiente inicial $s = y'(a)$ |
| PVI | $y(a)=\alpha$, $y'(a)=s$ → $y(x;s)$ |
| Objetivo | $\phi(s) = y(b;s) - \beta = 0$ |
| Lineal | $\phi$ afín → 2 disparos, exacto |
| No lineal | iterar (Newton/secante) |
| Costo de $\phi(s)$ | una integración PVI completa |

> [!corolario]
> El disparo transforma el PVF en la búsqueda de un único número $s = y'(a)$: cada valor define un [[Problema Valor Inicial PVI/index|PVI]] con solución $y(x;s)$, y el PVF se cumple cuando el residuo de frontera $\phi(s)=y(b;s)-\beta$ se anula. Para problemas **lineales**, $\phi$ es afín y dos disparos bastan para la raíz exacta; para **no lineales** se itera con [[Metodo Newton para Condicion Frontera Residual|Newton]]. Así, un problema funcional se reduce a una ecuación escalar resuelta reutilizando integradores de PVI y métodos de raíces, sin maquinaria nueva.
