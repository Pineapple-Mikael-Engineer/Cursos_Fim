---
title: Euler Explícito — Orden 1 e Interpretación Geométrica
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - euler-taylor
draft: false
aliases:
  - Método de Euler
  - Euler explícito
  - Forward Euler
  - Euler hacia adelante
---

# Euler Explícito: Orden 1 e Interpretación Geométrica

> [!definicion]
> El **método de Euler explícito** (o hacia adelante) avanza la solución del [[Problema Valor Inicial PVI/index|PVI]] $y'=f(t,y)$ siguiendo la recta tangente durante un paso $h$:
> $$y_{n+1} = y_n + h\,f(t_n, y_n), \qquad t_{n+1} = t_n + h.$$

> [!info]
> Es el método más simple y el ladrillo conceptual de todos los demás. Tiene orden 1 ($O(h)$ global), así que rara vez se usa en producción, pero su análisis introduce todas las ideas clave: [[Error Local Truncamiento vs Error Global Acumulado|truncamiento]], [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]] y convergencia.

---

## Interpretación geométrica

> [!teoria]
> En cada punto $(t_n, y_n)$, la EDO da la **pendiente** $f(t_n, y_n)$ del campo de direcciones. Euler avanza en línea recta con esa pendiente durante $h$:
> $$y_{n+1} = y_n + \underbrace{h}_{\text{avance en }t}\cdot\underbrace{f(t_n,y_n)}_{\text{pendiente}}.$$
> Es seguir la **tangente** a la solución, recalculando la dirección en cada paso. Como la verdadera solución se curva, la tangente se desvía: ahí nace el error.

---

## Deducción y orden

> [!teorema]
> El método de Euler resulta de truncar la serie de Taylor de la solución a primer orden:
> $$y(t_{n+1}) = y(t_n) + h\,y'(t_n) + \frac{h^2}{2}y''(\xi) = y(t_n) + h\,f(t_n,y_n) + \underbrace{\frac{h^2}{2}y''(\xi)}_{\text{error local}}.$$
> El **error local de truncamiento** es $O(h^2)$, lo que da error **global** $O(h)$: el método es de **orden 1**.

> [!demostracion]
> Despreciar el término $\frac{h^2}{2}y''(\xi)$ deja la fórmula de Euler. El error cometido en un paso es $\tau_n = \frac{h^2}{2}y''(\xi)$, de orden $h^2$. Al acumular $N = (t_f-t_0)/h$ pasos, el error global crece a $O(h)$ (un orden menos), como se detalla en [[Error Local Truncamiento vs Error Global Acumulado]].

---

## Ejemplo

> [!ejemplo]
> **Enfriamiento de Newton: $T' = -k(T - T_\infty)$**, con $k=0.5$, $T_\infty=20$, $T(0)=100$, $h=2$:
>
> | $t_n$ | $T_n$ (Euler) | Exacta $20 + 80e^{-0.5t}$ |
> |:---:|:---:|:---:|
> | 0 | 100.0 | 100.0 |
> | 2 | $100 + 2(-0.5)(80) = 20.0$ | 49.4 |
> | 4 | $20 + 2(-0.5)(0) = 20.0$ | 30.8 |
>
> Con $h=2$ demasiado grande, Euler **salta** al equilibrio en un paso (gran error). Con $h=0.1$ seguiría fielmente la curva: el paso debe ser pequeño frente a la escala de tiempo $1/k=2$.

---

## Algoritmo

> [!algoritmo]
> **Euler explícito (escalar y vectorial).**
>
> ```python
> import numpy as np
>
> def euler(f, t0, y0, h, N):
>     t = np.zeros(N + 1)
>     y = np.zeros((N + 1,) + np.shape(y0))
>     t[0], y[0] = t0, y0
>     for n in range(N):
>         y[n+1] = y[n] + h * f(t[n], y[n])      # un solo paso, directo
>         t[n+1] = t[n] + h
>     return t, y
>
> # Oscilador armónico: y = [x, v], y' = [v, -x]
> f = lambda t, y: np.array([y[1], -y[0]])
> t, y = euler(f, 0, np.array([1.0, 0.0]), 0.05, 400)
> ```

---

## Limitaciones

> [!warning]
> 1. **Orden bajo ($O(h)$):** para precisión razonable hace falta $h$ muy pequeño; [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] da $O(h^4)$ con poco más costo.
> 2. **Estabilidad condicional:** para $y'=\lambda y$ requiere $|1 + h\lambda| \leq 1$; pasos grandes **explotan** ([[Regiones Estabilidad Absoluta A Estabilidad|región de estabilidad]]).
> 3. **No conserva energía:** en sistemas oscilatorios (resorte, órbita), Euler explícito **gana energía** sistemáticamente; la órbita se abre en espiral. Lo corrigen los [[Integradores Simplecticos Conservacion|métodos simplécticos]].

> [!ejemplo]
> **Euler en el oscilador armónico** $\ddot x = -x$: la energía $E_n = \frac12(x_n^2+v_n^2)$ crece como $E_{n+1} = (1+h^2)E_n$ — la trayectoria en el plano de fases se abre en **espiral hacia afuera**, un artefacto puramente numérico. Es la motivación física más clara para no usar Euler explícito en mecánica.

---

## Relación con otras notas

> [!info]
> - Cómo el error local $O(h^2)$ se vuelve global $O(h)$: [[Error Local Truncamiento vs Error Global Acumulado]].
> - La variante estable: [[Euler Implicito Estabilidad Incondicional]].
> - El ascenso de orden: [[Metodos Serie Taylor Orden Superior]] y [[Metodos Runge Kutta/index]].
> - Su región de estabilidad: [[Regiones Estabilidad Absoluta A Estabilidad]].
> - La conservación que viola: [[Integradores Simplecticos Conservacion]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $y_{n+1} = y_n + hf(t_n, y_n)$ |
| Geometría | seguir la tangente |
| Error local | $O(h^2)$ |
| Orden global | 1 ($O(h)$) |
| Estabilidad | condicional, $|1+h\lambda|\leq1$ |
| Energía | la gana (espiral hacia afuera) |

> [!corolario]
> El método de Euler explícito avanza siguiendo la tangente, $y_{n+1}=y_n+hf(t_n,y_n)$, truncando Taylor a primer orden: error local $O(h^2)$, global $O(h)$. Simple y didáctico, introduce todas las ideas del campo, pero su orden bajo, su [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad condicional]] y —crucial para la física— su tendencia a **ganar energía** en sistemas oscilatorios lo hacen inadecuado para producción. Sus defectos motivan directamente el [[Euler Implicito Estabilidad Incondicional|Euler implícito]] (estabilidad), [[Metodos Runge Kutta/index|Runge-Kutta]] (orden) y los [[Integradores Simplecticos Conservacion|integradores simplécticos]] (conservación).
