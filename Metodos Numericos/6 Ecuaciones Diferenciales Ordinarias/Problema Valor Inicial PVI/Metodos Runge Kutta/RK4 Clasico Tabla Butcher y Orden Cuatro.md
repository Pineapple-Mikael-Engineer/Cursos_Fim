---
title: RK4 Clásico — Tabla de Butcher y Orden Cuatro
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
draft: false
aliases:
  - RK4
  - Runge-Kutta clásico
  - Método RK4
  - Classical Runge-Kutta
---

# RK4 Clásico: Tabla de Butcher y Orden Cuatro

> [!definicion]
> El **Runge-Kutta clásico de orden 4** (RK4) usa **cuatro** evaluaciones de $f$ por paso, combinándolas con pesos $\frac16, \frac13, \frac13, \frac16$:
> $$y_{n+1} = y_n + \frac{h}{6}\big(k_1 + 2k_2 + 2k_3 + k_4\big),$$
> $$k_1 = f(t_n, y_n),\quad k_2 = f\big(t_n+\tfrac h2, y_n+\tfrac h2 k_1\big),\quad k_3 = f\big(t_n+\tfrac h2, y_n+\tfrac h2 k_2\big),\quad k_4 = f\big(t_n+h, y_n+hk_3\big).$$

> [!info]
> Es el **método de referencia** de la simulación física: orden 4 (error global $O(h^4)$) con solo 4 evaluaciones, en el punto óptimo de las [[Construccion General Etapas s y Orden p|barreras de Butcher]] ($p=s=4$). Excelente equilibrio precisión/costo, robusto y fácil de implementar.

---

## Tabla de Butcher

> [!teorema]
> RK4 se codifica en
> $$\begin{array}{c|cccc} 0 & & & & \\ \tfrac12 & \tfrac12 & & & \\ \tfrac12 & 0 & \tfrac12 & & \\ 1 & 0 & 0 & 1 & \\ \hline & \tfrac16 & \tfrac13 & \tfrac13 & \tfrac16 \end{array}$$
> Es **explícito** ($A$ estrictamente triangular inferior): las etapas se calculan secuencialmente.

> [!teoria]
> **Interpretación.** RK4 muestrea la pendiente en cuatro puntos: el inicio ($k_1$), dos veces el punto medio ($k_2, k_3$, cada una refinando la anterior) y el final ($k_4$). El promedio ponderado $\frac16(k_1+2k_2+2k_3+k_4)$ —que da peso doble a las pendientes medias— equivale a la [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|regla de Simpson]] aplicada a la integral $\int_{t_n}^{t_{n+1}}f\,dt$. RK4 es "Simpson para EDOs".

---

## Ejemplo: órbita de un planeta

> [!ejemplo]
> **Problema de Kepler (órbita 2D), $\ddot{\mathbf r} = -\mathbf r/|\mathbf r|^3$**, reducido a sistema de 4 variables $(x, y, v_x, v_y)$. Condición inicial de órbita elíptica, $h=0.01$, una revolución:
>
> | Método | Error en posición tras 1 órbita | Deriva de energía |
> |:---|:---:|:---:|
> | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler]] | $\sim10^{0}$ (órbita se abre) | crece sin control |
> | [[RK2 Heun Euler Modificado Punto Medio\|RK2]] | $\sim10^{-2}$ | crece lento |
> | **RK4** | $\sim10^{-6}$ | crece muy lento |
>
> RK4 sigue la órbita con altísima fidelidad en una revolución. **Advertencia:** en integraciones de **millones** de órbitas, incluso RK4 acumula deriva de energía; ahí se prefieren [[Integradores Simplecticos Conservacion|integradores simplécticos]].

---

## Algoritmo

> [!algoritmo]
> **RK4 vectorial (sirve para cualquier sistema físico).**
>
> ```python
> import numpy as np
>
> def rk4(f, t0, y0, h, N):
>     t, y = t0, np.array(y0, float)
>     traj = [y.copy()]
>     for _ in range(N):
>         k1 = f(t,         y)
>         k2 = f(t + h/2,   y + h/2 * k1)
>         k3 = f(t + h/2,   y + h/2 * k2)
>         k4 = f(t + h,     y + h   * k3)
>         y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
>         t += h
>         traj.append(y.copy())
>     return np.array(traj)
>
> # Péndulo no lineal: y = [θ, ω], y' = [ω, -(g/L) sinθ]
> g_L = 9.81
> f = lambda t, y: np.array([y[1], -g_L*np.sin(y[0])])
> traj = rk4(f, 0, [np.pi/3, 0.0], 0.01, 2000)
> ```

---

## Por qué RK4 es el estándar

> [!info]
> | Ventaja | Detalle |
> |:---|:---|
> | Orden 4 | error global $O(h^4)$; halvar $h$ divide el error por 16 |
> | Eficiencia óptima | $p=s=4$, sin etapas desperdiciadas |
> | Sin derivadas | solo evalúa $f$, a diferencia de [[Metodos Serie Taylor Orden Superior\|Taylor]] |
> | Autoarranque | método de un paso, no necesita valores previos |
> | Robusto | buena región de estabilidad para problemas no rígidos |

> [!warning]
> **Limitaciones.**
> - **Paso fijo:** sin control de error; para eso se usa el par [[Control Paso Adaptativo RK45 Dormand Prince|RK45 adaptativo]].
> - **No conserva invariantes:** acumula deriva de energía en integraciones muy largas ([[Integradores Simplecticos Conservacion|simplécticos]]).
> - **Inadecuado para rigidez:** su región de estabilidad acotada exige $h$ minúsculo en problemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]].

---

## Relación con otras notas

> [!info]
> - La familia de la que es el caso óptimo: [[Construccion General Etapas s y Orden p]] y [[RK2 Heun Euler Modificado Punto Medio]].
> - La versión con control de error: [[Control Paso Adaptativo RK45 Dormand Prince]].
> - Su región de estabilidad: [[Regiones Estabilidad Absoluta A Estabilidad]].
> - La analogía con Simpson: [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]].
> - La alternativa conservativa: [[Integradores Simplecticos Conservacion]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Etapas | 4 |
| Fórmula | $y_n + \tfrac h6(k_1+2k_2+2k_3+k_4)$ |
| Orden | 4 ($O(h^4)$) |
| Analogía | Simpson para EDOs |
| Eficiencia | $p=s=4$ (óptimo) |
| Limitaciones | paso fijo, no conserva, no rígido |

> [!corolario]
> RK4 combina cuatro evaluaciones de $f$ —inicio, dos puntos medios y final— con pesos $\frac16,\frac13,\frac13,\frac16$ para lograr orden 4 con error global $O(h^4)$, en el punto óptimo de las barreras de Butcher ($p=s=4$). Equivale a aplicar [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|Simpson]] a la integral de la pendiente, y es el método estándar de simulación física por su equilibrio precisión/costo, robustez y autoarranque. Sus límites —paso fijo, no conservación, inadecuación a la rigidez— se cubren con [[Control Paso Adaptativo RK45 Dormand Prince|RK45 adaptativo]], [[Integradores Simplecticos Conservacion|integradores simplécticos]] y métodos implícitos respectivamente.
