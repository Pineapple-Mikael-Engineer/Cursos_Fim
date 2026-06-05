---
title: Métodos de Taylor y Euler
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - euler-taylor
  - index
draft: false
aliases:
  - Métodos de Taylor y Euler
  - Euler y Taylor
  - Taylor-Euler methods
---

# Métodos de Taylor y Euler

> [!definicion]
> Los **métodos de Taylor** aproximan $y(t_{n+1})$ truncando la serie de Taylor de la solución alrededor de $t_n$. El caso de orden 1 es el **método de Euler**:
> $$y_{n+1} = y_n + h\,f(t_n, y_n).$$
> Los de orden superior añaden términos con derivadas totales de $f$.

> [!info]
> Son los métodos **fundamentales** de los que derivan todos los demás. [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]] es el ladrillo conceptual; su variante [[Euler Implicito Estabilidad Incondicional|implícita]] introduce la estabilidad; las [[Metodos Serie Taylor Orden Superior|series de Taylor]] suben el orden pero exigen derivar $f$ a mano, defecto que [[Metodos Runge Kutta/index|Runge-Kutta]] resuelve.

---

## La familia

> [!info]
> - **[[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]]:** $y_{n+1} = y_n + hf(t_n,y_n)$. Orden 1, interpretación geométrica de "seguir la tangente".
> - **[[Euler Implicito Estabilidad Incondicional|Euler implícito]]:** $y_{n+1} = y_n + hf(t_{n+1},y_{n+1})$. Orden 1, pero **incondicionalmente estable** (clave para sistemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]]).
> - **[[Metodos Serie Taylor Orden Superior|Taylor de orden superior]]:** añaden $\frac{h^2}{2}y'' + \cdots$, con derivadas totales de $f$.
> - **[[Error Local Truncamiento vs Error Global Acumulado|Error local vs global]]:** por qué un error local $O(h^{p+1})$ produce error global $O(h^p)$.

---

## Ejemplo comparativo

> [!ejemplo]
> **$y' = y$, $y(0)=1$** (exacta $y=e^t$), un paso $h=0.1$ hasta $t=0.1$ (exacta $1.10517$):
>
> | Método | $y_1$ | Error |
> |:---|:---:|:---:|
> | Euler explícito | $1 + 0.1(1) = 1.10000$ | $5.2\times10^{-3}$ |
> | Taylor orden 2 | $1 + 0.1 + \frac{0.01}{2} = 1.10500$ | $1.7\times10^{-4}$ |
> | Euler implícito | $\frac{1}{1-0.1} = 1.11111$ | $5.9\times10^{-3}$ |
>
> Taylor orden 2 mejora dos órdenes de magnitud; los dos Euler tienen orden 1 pero el implícito sobrestima (su ventaja es la estabilidad, no la precisión).

---

## Explícito vs implícito

> [!info]
> | | Explícito | Implícito |
> |:---|:---|:---|
> | Fórmula | $y_{n+1} = y_n + hf(t_n, y_n)$ | $y_{n+1} = y_n + hf(t_{n+1}, y_{n+1})$ |
> | Cálculo de $y_{n+1}$ | directo | resolver ecuación (Newton) |
> | Estabilidad | condicional ($h$ limitado) | incondicional |
> | Costo por paso | bajo | alto |
> | Idóneo | problemas no rígidos | problemas [[Rigidez Stiffness Problemas Ingenieria\|rígidos]] |

---

## Resumen

| Tema | Nota |
|:---|:---|
| Euler explícito y geometría | [[Euler Explicito Orden 1 Interpretacion Geometrica]] |
| Error local vs global | [[Error Local Truncamiento vs Error Global Acumulado]] |
| Euler implícito y estabilidad | [[Euler Implicito Estabilidad Incondicional]] |
| Taylor de orden superior | [[Metodos Serie Taylor Orden Superior]] |

> [!corolario]
> Los métodos de Taylor truncan la serie de la solución; su caso de orden 1 es el método de Euler, ladrillo de toda la integración de EDOs. [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]] sigue la tangente con orden 1 y estabilidad condicional; [[Euler Implicito Estabilidad Incondicional|Euler implícito]] gana estabilidad incondicional a cambio de resolver una ecuación por paso; las [[Metodos Serie Taylor Orden Superior|series de Taylor]] suben el orden pero requieren derivadas analíticas de $f$. Este último defecto es lo que motiva los métodos de [[Metodos Runge Kutta/index|Runge-Kutta]], que alcanzan alto orden con solo evaluaciones de $f$.
