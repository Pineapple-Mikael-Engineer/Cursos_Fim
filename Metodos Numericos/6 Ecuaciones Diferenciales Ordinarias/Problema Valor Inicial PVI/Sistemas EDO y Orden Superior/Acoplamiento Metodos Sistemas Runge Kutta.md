---
title: Acoplamiento de Métodos a Sistemas (Runge-Kutta Vectorial)
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - sistemas-edo
  - runge-kutta
draft: false
aliases:
  - Runge-Kutta para sistemas
  - Métodos vectoriales
  - RK vectorial
  - Sistemas acoplados
---

# Acoplamiento de Métodos a Sistemas (Runge-Kutta Vectorial)

> [!definicion]
> Todo método de un paso ([[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]], [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]], etc.) se aplica a un **sistema** $\mathbf{y}' = \mathbf{f}(t, \mathbf{y})$, $\mathbf y\in\mathbb{R}^m$, **sin ningún cambio de fórmula**: las operaciones escalares se vuelven vectoriales. Las etapas $\mathbf k_i$ y el estado $\mathbf y_n$ son ahora **vectores**.

> [!info]
> Esta es la razón de que reducir a [[Reduccion EDO Orden n a Sistema Primer Orden|primer orden]] sea tan poderoso: una vez en forma $\mathbf y'=\mathbf f$, el mismo código escalar funciona vectorialmente. RK4 para un planeta y RK4 para mil partículas son **el mismo algoritmo**, solo cambia la dimensión de $\mathbf y$.

---

## RK4 vectorial

> [!teorema]
> Para $\mathbf y' = \mathbf f(t, \mathbf y)$, RK4 es idéntico al caso escalar con vectores:
> $$\mathbf k_1 = \mathbf f(t_n, \mathbf y_n),\quad \mathbf k_2 = \mathbf f\big(t_n+\tfrac h2, \mathbf y_n+\tfrac h2\mathbf k_1\big),\quad \mathbf k_3 = \mathbf f\big(t_n+\tfrac h2, \mathbf y_n+\tfrac h2\mathbf k_2\big),\quad \mathbf k_4 = \mathbf f(t_n+h, \mathbf y_n+h\mathbf k_3),$$
> $$\mathbf y_{n+1} = \mathbf y_n + \tfrac h6(\mathbf k_1 + 2\mathbf k_2 + 2\mathbf k_3 + \mathbf k_4).$$
> Las componentes se actualizan **simultáneamente** (no una por una): cada $\mathbf k_i$ depende de **todas** las componentes del estado, lo que respeta el **acoplamiento** entre ecuaciones.

> [!warning]
> **Error común: actualizar componentes por separado.** Hay que calcular **todas** las etapas $\mathbf k_i$ del vector completo antes de avanzar. Avanzar una componente antes de evaluar las otras rompe el acoplamiento y arruina el orden. La actualización es atómica sobre el vector entero.

---

## Ejemplo: presa-depredador (Lotka-Volterra)

> [!ejemplo]
> **$\dot x = \alpha x - \beta xy$, $\dot y = \delta xy - \gamma y$** (presas $x$, depredadores $y$). Estado $\mathbf y = (x, y)$:
> $$\mathbf f(\mathbf y) = \big(\alpha x - \beta xy,\ \delta xy - \gamma y\big).$$
> Las ecuaciones están **acopladas** (cada derivada depende de ambas variables). RK4 vectorial las integra conjuntamente, produciendo las oscilaciones cíclicas características en el plano de fases $(x,y)$. Aplicar un método "componente a componente" daría resultados erróneos.

---

## Algoritmo

> [!algoritmo]
> **RK4 vectorial genérico (cualquier sistema).**
>
> ```python
> import numpy as np
>
> def rk4_sistema(f, t0, y0, h, N):
>     y = np.array(y0, dtype=float)          # estado vectorial
>     t = t0
>     traj = [y.copy()]
>     for _ in range(N):
>         k1 = f(t,       y)
>         k2 = f(t + h/2, y + h/2 * k1)
>         k3 = f(t + h/2, y + h/2 * k2)
>         k4 = f(t + h,   y + h   * k3)
>         y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)   # vector completo
>         t += h
>         traj.append(y.copy())
>     return np.array(traj)
>
> # Lotka-Volterra
> a, b, d, g = 1.0, 0.1, 0.075, 1.5
> f = lambda t, y: np.array([a*y[0] - b*y[0]*y[1],
>                            d*y[0]*y[1] - g*y[1]])
> traj = rk4_sistema(f, 0, [10, 5], 0.01, 5000)
> ```

---

## El papel de la jacobiana

> [!teoria]
> Para sistemas, la **matriz jacobiana** $J = \partial\mathbf f/\partial\mathbf y$ gobierna el comportamiento local:
> - Sus **autovalores** $\lambda_i$ generalizan el $\lambda$ de la [[Regiones Estabilidad Absoluta A Estabilidad|ecuación de prueba escalar]]: el método es estable si **todos** los $h\lambda_i$ están en la región de estabilidad.
> - Si los $|\lambda_i|$ difieren en muchos órdenes de magnitud, el sistema es [[Rigidez Stiffness Problemas Ingenieria|rígido]].
> - En métodos implícitos, $J$ se necesita para el [[Newton Raphson Multivariable/index|Newton interno]].

---

## Relación con otras notas

> [!info]
> - La reducción que produce el sistema: [[Reduccion EDO Orden n a Sistema Primer Orden]].
> - El método escalar que se vectoriza: [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - Cómo los autovalores de $J$ determinan la estabilidad: [[Regiones Estabilidad Absoluta A Estabilidad]] y [[Rigidez Stiffness Problemas Ingenieria]].
> - La jacobiana en métodos implícitos: [[Newton Raphson Multivariable/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Estado | vector $\mathbf y\in\mathbb{R}^m$ |
| Etapas | vectores $\mathbf k_i$ |
| Fórmula | idéntica al escalar, vectorial |
| Acoplamiento | cada $\mathbf k_i$ usa todas las componentes |
| Estabilidad | autovalores de $J=\partial\mathbf f/\partial\mathbf y$ |

> [!corolario]
> Los métodos de un paso se aplican a sistemas $\mathbf y'=\mathbf f(t,\mathbf y)$ sin cambiar la fórmula: estado y etapas se vuelven vectores y las componentes se actualizan simultáneamente, respetando el acoplamiento entre ecuaciones. Por eso, tras [[Reduccion EDO Orden n a Sistema Primer Orden|reducir a primer orden]], el mismo código de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] simula desde un péndulo hasta dinámica molecular. La estabilidad pasa a depender de los autovalores de la [[Newton Raphson Multivariable/index|jacobiana]] $\partial\mathbf f/\partial\mathbf y$, cuya dispersión define la [[Rigidez Stiffness Problemas Ingenieria|rigidez]] del sistema.
