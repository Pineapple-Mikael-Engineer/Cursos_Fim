---
title: Reducción de EDO de Orden n a Sistema de Primer Orden
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - sistemas-edo
draft: false
aliases:
  - Reducción de orden
  - EDO de orden n a primer orden
  - Reduction to first order
  - Variables de estado
---

# Reducción de EDO de Orden $n$ a Sistema de Primer Orden

> [!definicion]
> Toda EDO de orden $n$ resuelta para la derivada más alta,
> $$y^{(n)} = g\big(t, y, y', \dots, y^{(n-1)}\big),$$
> se transforma en un **sistema de $n$ EDOs de primer orden** definiendo las **variables de estado** $u_1=y, u_2=y', \dots, u_n=y^{(n-1)}$.

> [!info]
> Es el truco universal que permite aplicar **cualquier** método de [[Problema Valor Inicial PVI/index|primer orden]] (Euler, RK4) a problemas de orden arbitrario. Como casi toda la física es de segundo orden ($F=ma$), esta reducción es el primer paso de prácticamente toda simulación dinámica.

---

## La transformación

> [!teorema]
> Con $u_i = y^{(i-1)}$ para $i=1,\dots,n$, la EDO de orden $n$ equivale al sistema de primer orden
> $$\mathbf{u}' = \begin{pmatrix} u_1' \\ u_2' \\ \vdots \\ u_{n-1}' \\ u_n' \end{pmatrix} = \begin{pmatrix} u_2 \\ u_3 \\ \vdots \\ u_n \\ g(t, u_1, \dots, u_n) \end{pmatrix}, \qquad \mathbf u(t_0) = \big(y_0, y_0', \dots, y_0^{(n-1)}\big).$$
> Las primeras $n-1$ ecuaciones son triviales ($u_i' = u_{i+1}$); la última contiene la dinámica.

> [!demostracion]
> Por definición $u_i' = y^{(i)} = u_{i+1}$ para $i<n$, y $u_n' = y^{(n)} = g(t, y, \dots, y^{(n-1)}) = g(t, u_1, \dots, u_n)$. Las condiciones iniciales del PVI de orden $n$ ($y, y', \dots, y^{(n-1)}$ en $t_0$) dan exactamente el vector inicial $\mathbf u(t_0)$. La equivalencia es exacta: resolver el sistema da $y = u_1$ y sus derivadas.

---

## Ejemplo físico: oscilador amortiguado forzado

> [!ejemplo]
> **$m\ddot x + c\dot x + kx = F(t)$** (orden 2). Con $u_1 = x$, $u_2 = \dot x = v$:
> $$\begin{pmatrix} \dot u_1 \\ \dot u_2 \end{pmatrix} = \begin{pmatrix} u_2 \\ \frac{1}{m}\big(F(t) - c\,u_2 - k\,u_1\big) \end{pmatrix}.$$
> El estado $(x, v)$ —posición y velocidad— es el **vector de estado**. Toda la mecánica clásica sigue este patrón: el estado es (posición, momento) y la dinámica da su derivada.

> [!ejemplo]
> **Sistema de orden 3: $y''' = -y'' + 2y' - y + \cos t$.** Con $\mathbf u = (y, y', y'')$:
> $$\mathbf u' = \begin{pmatrix} u_2 \\ u_3 \\ -u_3 + 2u_2 - u_1 + \cos t \end{pmatrix}.$$

---

## Sistemas acoplados de orden superior

> [!teoria]
> Varios cuerpos o grados de libertad acoplados se reducen igual, concatenando los estados. Para $N$ partículas en 3D ($\ddot{\mathbf r}_i = \mathbf F_i/m_i$), el estado tiene $6N$ componentes (posiciones + velocidades):
> $$\mathbf y = (\mathbf r_1, \dots, \mathbf r_N, \mathbf v_1, \dots, \mathbf v_N), \qquad \mathbf y' = (\mathbf v_1, \dots, \mathbf v_N, \mathbf F_1/m_1, \dots, \mathbf F_N/m_N).$$
> Así se simulan desde sistemas planetarios hasta dinámica molecular.

---

## Algoritmo

> [!algoritmo]
> **Reducción y simulación de un oscilador.**
>
> ```python
> import numpy as np
> from scipy.integrate import solve_ivp
>
> # m x'' + c x' + k x = F(t)  →  estado [x, v]
> m, c, k = 1.0, 0.3, 4.0
> F = lambda t: np.cos(2*t)
>
> def sistema(t, u):
>     x, v = u
>     return [v, (F(t) - c*v - k*x) / m]      # [x', v']
>
> sol = solve_ivp(sistema, [0, 20], [1.0, 0.0], method='RK45', dense_output=True)
> ```

---

## Relación con otras notas

> [!info]
> - Cómo se aplican los métodos al sistema resultante: [[Acoplamiento Metodos Sistemas Runge Kutta]].
> - La condición de Lipschitz vectorial: [[Teoremas Existencia Unicidad Picard Lindelof]].
> - Para sistemas mecánicos conservativos: [[Integradores Simplecticos Conservacion]].
> - El PVF también reduce orden, pero con condiciones en dos extremos: [[Problema Valor Frontera PVF/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Variables de estado | $u_i = y^{(i-1)}$ |
| Sistema | $u_i'=u_{i+1}$, $u_n'=g$ |
| Estado físico | (posición, velocidad/momento) |
| $N$ cuerpos 3D | $6N$ componentes |
| Propósito | aplicar métodos de primer orden |

> [!corolario]
> Cualquier EDO de orden $n$ se reduce a un sistema de $n$ ecuaciones de primer orden definiendo las variables de estado $u_i = y^{(i-1)}$, donde las primeras $n-1$ ecuaciones son triviales y la última contiene la dinámica. Como la física es mayoritariamente de segundo orden ($F=ma$), el estado natural es (posición, velocidad) y esta reducción es el paso inicial de toda simulación dinámica, escalable a sistemas de $N$ cuerpos con $6N$ componentes. Sobre el sistema resultante, los métodos de un paso actúan [[Acoplamiento Metodos Sistemas Runge Kutta|vectorialmente]], y su estructura permite usar [[Integradores Simplecticos Conservacion|integradores simplécticos]] cuando el sistema es conservativo.
