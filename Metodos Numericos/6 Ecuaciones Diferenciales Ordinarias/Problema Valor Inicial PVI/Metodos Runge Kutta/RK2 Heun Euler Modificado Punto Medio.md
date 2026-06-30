---
title: RK2 — Heun, Euler Modificado y Punto Medio
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
draft: false
aliases:
  - RK2
  - Método de Heun
  - Punto medio
  - Euler modificado
---

# RK2: Heun, Euler Modificado y Punto Medio

> [!definicion]
> Los **métodos de Runge-Kutta de orden 2** (RK2) usan **dos** evaluaciones de $f$ por paso para alcanzar orden global 2. Sus variantes —Heun, punto medio, Euler modificado— difieren solo en dónde se toma la segunda evaluación.

> [!info]
> Mejoran a [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]] corrigiendo la pendiente: en vez de usar solo la pendiente inicial, **promedian** o **recentran** la pendiente sobre el paso. Son el ejemplo más simple del principio de [[Construccion General Etapas s y Orden p|Runge-Kutta]] y la base intuitiva de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]].

---

## Método de Heun (trapecio)

> [!teorema]
> **Heun** predice con Euler y corrige promediando las pendientes en los extremos:
> $$k_1 = f(t_n, y_n), \quad k_2 = f(t_n + h,\ y_n + h k_1), \quad y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2).$$
> Tabla de Butcher: $\begin{array}{c|cc} 0 & & \\ 1 & 1 & \\ \hline & \tfrac12 & \tfrac12 \end{array}$. Es la versión "EDO" de la [[Trapecio Error Truncamiento Segunda Derivada|regla del trapecio]].

## Método del punto medio

> [!teorema]
> **Punto medio** evalúa la pendiente en el centro del paso:
> $$k_1 = f(t_n, y_n), \quad k_2 = f\big(t_n + \tfrac{h}{2},\ y_n + \tfrac{h}{2}k_1\big), \quad y_{n+1} = y_n + h\,k_2.$$
> Tabla: $\begin{array}{c|cc} 0 & & \\ \tfrac12 & \tfrac12 & \\ \hline & 0 & 1 \end{array}$. Usa la pendiente del punto medio para todo el paso.

> [!info]
> Ambos son orden 2 (error local $O(h^3)$, global $O(h^2)$); pertenecen a la [[Construccion General Etapas s y Orden p|familia de un parámetro]] $b_2c_2=\tfrac12$. "Euler modificado" es otro nombre del punto medio. Difieren solo en la constante de error.

---

## Por qué orden 2: predictor-corrector

> [!teoria]
> Heun ilustra la lógica **predictor-corrector**:
> 1. **Predictor:** un paso de Euler estima $y_{n+1}^* = y_n + hk_1$.
> 2. **Corrector:** se recalcula la pendiente allí ($k_2$) y se promedia con la inicial.
>
> El promedio captura la **curvatura** del paso que Euler ignora, ganando un orden. Geométricamente, en lugar de seguir la tangente inicial, sigue una pendiente media más representativa del arco.

---

## Ejemplo

> [!ejemplo]
> **$y' = -2ty^2$, $y(0)=1$** (exacta $y=1/(1+t^2)$), Heun con $h=0.2$, primer paso:
> $$k_1 = -2(0)(1)^2 = 0, \quad y^* = 1 + 0.2(0) = 1,$$
> $$k_2 = -2(0.2)(1)^2 = -0.4, \quad y_1 = 1 + \tfrac{0.2}{2}(0 - 0.4) = 0.96.$$
> Exacta $y(0.2) = 1/1.04 = 0.96154$. Error $1.5\times10^{-3}$, frente al $0$ de Euler en este primer paso (engañoso: $k_1=0$) y mucho mejor en los siguientes.

---

## Algoritmo

> [!algoritmo]
> **Heun (RK2) vectorial.**
>
> ```python
> import numpy as np
>
> def heun(f, t0, y0, h, N):
>     t, y = t0, np.array(y0, float)
>     traj = [y.copy()]
>     for _ in range(N):
>         k1 = f(t, y)
>         k2 = f(t + h, y + h*k1)
>         y = y + 0.5*h*(k1 + k2)
>         t += h
>         traj.append(y.copy())
>     return np.array(traj)
> ```

---

## Comparación

> [!info]
> | Método | $k_2$ evaluado en | $y_{n+1}$ | Orden |
> |:---|:---|:---|:---:|
> | Heun | $(t_n+h,\ y_n+hk_1)$ | $y_n + \tfrac{h}{2}(k_1+k_2)$ | 2 |
> | Punto medio | $(t_n+\tfrac h2,\ y_n+\tfrac h2 k_1)$ | $y_n + hk_2$ | 2 |
> | Ralston | $(t_n+\tfrac{2h}{3},\ \cdot)$ | $y_n + h(\tfrac14 k_1 + \tfrac34 k_2)$ | 2 (error mínimo) |

> [!warning]
> RK2 cuesta el **doble** que Euler (2 evaluaciones) pero da orden 2 en vez de 1: casi siempre vale la pena. Aun así, para precisión seria, [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] (4 evaluaciones, orden 4) tiene mejor relación costo/precisión.

---

## Relación con otras notas

> [!info]
> - El método de orden 1 que mejora: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - La familia general y sus condiciones: [[Construccion General Etapas s y Orden p]].
> - El siguiente nivel de orden: [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - El análogo en integración: [[Trapecio Error Truncamiento Segunda Derivada]] (Heun) y [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]] (RK4).

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Etapas | 2 |
| Heun | $y_n + \tfrac h2(k_1+k_2)$ |
| Punto medio | $y_n + hk_2$, $k_2$ en el centro |
| Orden | 2 ($O(h^2)$) |
| Lógica | predictor-corrector |

> [!corolario]
> Los métodos RK2 —Heun, punto medio, Euler modificado— usan dos evaluaciones de $f$ por paso para lograr orden 2, corrigiendo la pendiente única de [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]] mediante un promedio (Heun) o un recentrado (punto medio) que captura la curvatura del arco. Son el caso más simple de la [[Construccion General Etapas s y Orden p|familia de Runge-Kutta]] e ilustran la lógica predictor-corrector. Para mayor precisión a costo razonable, el estándar es [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]].
