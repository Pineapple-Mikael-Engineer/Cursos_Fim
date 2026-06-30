---
title: Convergencia Lineal Raices Multiples
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - newton-raphson
  - convergencia
  - raices-multiples
draft: false
aliases:
  - Raíces múltiples
  - Newton en raíces múltiples
  - Convergencia lineal Newton
---

# Convergencia Lineal en Raíces Múltiples

> [!definicion]
> Sea $f$ una función suficientemente diferenciable. Se dice que $r$ es una **raíz de multiplicidad $m$** ($m \geq 1$) si:
> $$f(r) = f'(r) = \cdots = f^{(m-1)}(r) = 0, \quad f^{(m)}(r) \neq 0$$
>
> - Si $m = 1$: raíz **simple**.
> - Si $m \geq 2$: raíz **múltiple** (doble, triple, etc.)

> [!info]
> En raíces simples, el método de Newton tiene convergencia cuadrática. En raíces múltiples ($m \geq 2$), la convergencia se reduce a **lineal**, perdiendo su principal ventaja.

---

## Ejemplo

> [!ejemplo]
> **Newton aplicado a $f(x) = (x-1)^2$ (raíz doble en $r=1$).**
>
> La iteración es:
> $$x^{(k+1)} = x^{(k)} - \frac{(x^{(k)}-1)^2}{2(x^{(k)}-1)} = x^{(k)} - \frac{x^{(k)}-1}{2} = \frac{x^{(k)} + 1}{2}$$
>
> Partiendo de $x^{(0)} = 2$:
>
> | $k$ | $x^{(k)}$ | Error $e^{(k)}$ | $e^{(k+1)}/e^{(k)}$ |
> |:---|:---|:---|:---|
> | 0 | 2.0 | 1.0 | — |
> | 1 | 1.5 | 0.5 | 0.5 |
> | 2 | 1.25 | 0.25 | 0.5 |
> | 3 | 1.125 | 0.125 | 0.5 |
> | 4 | 1.0625 | 0.0625 | 0.5 |
>
> **Observación:** El error se reduce a la mitad en cada iteración (convergencia lineal con $c = 0.5$), no cuadrática.

---

## ¿Por qué falla la convergencia cuadrática?

> [!teoria]
> Recordemos la función de iteración de Newton:
> $$g(x) = x - \frac{f(x)}{f'(x)}$$
>
> Su derivada es:
> $$g'(x) = \frac{f(x)f''(x)}{(f'(x))^2}$$
>
> **En una raíz simple ($f'(r) \neq 0$):** $f(r)=0 \Rightarrow g'(r)=0$, lo que garantiza convergencia cuadrática.
>
> **En una raíz múltiple de multiplicidad $m$:** Se puede demostrar que:
> $$g'(r) = 1 - \frac{1}{m} \neq 0$$
>
> Por lo tanto, la convergencia es **lineal** con constante asintótica $c = 1 - 1/m$.

> [!demostracion]
> **Esquema de la demostración.**
>
> Para una raíz de multiplicidad $m$, podemos escribir $f(x) = (x-r)^m h(x)$ con $h(r) \neq 0$.
>
> Calculando $f'(x) = m(x-r)^{m-1}h(x) + (x-r)^m h'(x)$.
>
> Entonces:
> $$\frac{f(x)}{f'(x)} = \frac{(x-r)^m h(x)}{m(x-r)^{m-1}h(x) + (x-r)^m h'(x)} = \frac{(x-r) h(x)}{m h(x) + (x-r) h'(x)}$$
>
> La iteración de Newton es:
> $$g(x) = x - \frac{f(x)}{f'(x)} = x - \frac{(x-r) h(x)}{m h(x) + (x-r) h'(x)}$$
>
> Derivando y evaluando en $x=r$ se obtiene $g'(r) = 1 - 1/m$.
>
> (La demostración completa requiere álgebra adicional, pero el resultado es estándar en análisis numérico.)

---

## Modificación para recuperar convergencia cuadrática

> [!info]
> **Modificación de Newton para raíces múltiples.**
>
> Si se conoce la multiplicidad $m$, se puede modificar la iteración:
> $$x^{(k+1)} = x^{(k)} - m \cdot \frac{f(x^{(k)})}{f'(x^{(k)})}$$
>
> En este caso, la nueva función de iteración satisface $g'(r)=0$, recuperando la convergencia cuadrática.

> [!ejemplo]
> **Misma función $f(x) = (x-1)^2$ con $m=2$.**
>
> Iteración modificada:
> $$x^{(k+1)} = x^{(k)} - 2 \cdot \frac{(x^{(k)}-1)^2}{2(x^{(k)}-1)} = x^{(k)} - (x^{(k)}-1) = 1$$
>
> ¡Converge en una sola iteración!

> [!warning]
> En la práctica, la multiplicidad $m$ no se conoce de antemano. Existen estrategias para estimarla o utilizar métodos alternativos como el método de Schröder (que no requiere conocer $m$).

---

## Comparativa: raíz simple vs múltiple

> [!info]
> | Aspecto | Raíz simple ($m=1$) | Raíz múltiple ($m \geq 2$) |
> |:---|:---|:---|
> | $f'(r)$ | $\neq 0$ | $= 0$ |
> | $g'(r)$ | $0$ | $1 - 1/m \neq 0$ |
> | Orden de convergencia | Cuadrático ($p=2$) | Lineal ($p=1$) |
> | Constante asintótica | $C = \|f''(r)\|/(2\|f'(r)\|)$ | $c = 1 - 1/m$ |
> | Velocidad | Muy rápida | Lenta (especialmente si $m$ es grande) |
> | Modificación | No necesaria | Multiplicar por $m$ |

> [!ejemplo]
> **Para $m=2$:** $c = 0.5$ (el error se reduce a la mitad por iteración, como en la bisección).
>
> **Para $m=3$:** $c = 2/3 \approx 0.6667$ (más lento aún).
>
> **Para $m=10$:** $c = 0.9$ (muy lento, comparable a punto fijo con mala elección de $g$).

---

## Algoritmo modificado

> [!algoritmo]
> **Newton modificado para raíces múltiples (con $m$ conocido).**
>
> ```
> función newton_multiple(f, df, m, x0, tol, max_iter)
>     x = x0
>     para k = 1 hasta max_iter
>         x_nuevo = x - m * f(x) / df(x)
>         si |x_nuevo - x| < tol
>             retornar x_nuevo, k
>         x = x_nuevo
>     retornar x, max_iter
> ```

> [!algoritmo]
> **Método de Schröder (no requiere conocer $m$).**
>
> Otra alternativa que recupera convergencia cuadrática sin conocer $m$ es:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)}) f'(x^{(k)})}{(f'(x^{(k)}))^2 - f(x^{(k)}) f''(x^{(k)})}$$
>
> Este método es más costoso (requiere $f''$) pero robusto para raíces múltiples.

---

## Relación con otras notas

> [!info]
> - La derivación de la fórmula de Newton y su convergencia cuadrática en raíces simples se estudia en [[Derivacion Geometrica y Serie Taylor]] y [[Orden Convergencia Cuadratica Simple]].
> - Los criterios de fallo por divergencia, oscilación o mala condición inicial (no relacionados con raíces múltiples) se desarrollan en [[Criterios Fallo Divergencia Oscilacion]].
> - El [[Metodo Secante Orden Convergencia Fi]] también sufre degradación en raíces múltiples, aunque su análisis es más complejo.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Raíz múltiple** | $f(r)=f'(r)=\cdots=f^{(m-1)}(r)=0$, $f^{(m)}(r)\neq0$ |
| **Newton estándar** | Convergencia **lineal** con $c = 1 - 1/m$ |
| **Causa** | $g'(r) = 1 - 1/m \neq 0$ |
| **Modificación** | $x^{(k+1)} = x^{(k)} - m \cdot f(x^{(k)})/f'(x^{(k)})$ |
| **Método de Schröder** | No requiere conocer $m$, pero usa $f''$ |

> [!corolario]
> El método de Newton pierde su convergencia cuadrática cuando la raíz es múltiple, reduciéndose a convergencia lineal con constante $c = 1 - 1/m$. Si se conoce la multiplicidad $m$, se puede modificar la iteración multiplicando el paso por $m$ para recuperar la convergencia cuadrática. En la práctica, cuando no se conoce $m$, se puede usar el método de Schröder (requiere $f''$) o aplicar técnicas de aceleración. Para otros tipos de fallo de Newton (divergencia, oscilación, mala condición inicial), véase [[Criterios Fallo Divergencia Oscilacion]].