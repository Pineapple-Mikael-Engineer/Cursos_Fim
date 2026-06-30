---
title: Newton-Raphson Multivariable
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - newton-raphson
  - index
draft: false
aliases:
  - Newton multivariable
  - Newton para sistemas
  - Multivariate Newton
---

# Newton-Raphson Multivariable

> [!definicion]
> El **método de Newton multivariable** resuelve $F(x) = 0$ con $F:\mathbb{R}^n\to\mathbb{R}^n$ iterando
> $$x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1} F(x^{(k)}),$$
> donde $J(x) = \big[\partial f_i/\partial x_j\big]$ es la [[Matriz Jacobiana y Sistema Lineal Asociado|matriz jacobiana]]. En la práctica **no** se invierte $J$: se resuelve el sistema lineal $J(x^{(k)})\,\Delta x^{(k)} = -F(x^{(k)})$ y se actualiza $x^{(k+1)} = x^{(k)} + \Delta x^{(k)}$.

> [!info]
> Es la extensión directa de [[Derivacion Geometrica y Serie Taylor|Newton escalar]]: la derivada $f'(x)$ se vuelve la jacobiana $J(x)$, y la división por $f'$ se vuelve la resolución de un sistema lineal. Conserva la [[Convergencia Local Cuadratica|convergencia cuadrática]] local.

---

## En qué consiste el método

> [!teoria]
> Newton linealiza $F$ alrededor de $x^{(k)}$ con el desarrollo de Taylor de primer orden:
> $$F(x) \approx F(x^{(k)}) + J(x^{(k)})\,(x - x^{(k)}).$$
> Igualar el modelo lineal a cero da el paso de Newton: el cero de la aproximación lineal es la siguiente iterada. Cada paso es, pues, la resolución de un sistema lineal cuya matriz es la jacobiana y cuyo término independiente es $-F(x^{(k)})$. La construcción detallada está en [[Matriz Jacobiana y Sistema Lineal Asociado]].

---

## Ejemplo

> [!ejemplo]
> **Sistema $2\times2$.**
> $$F(x,y) = \begin{pmatrix} x^2 + y^2 - 4 \\ x y - 1 \end{pmatrix}=0, \qquad J = \begin{pmatrix} 2x & 2y \\ y & x \end{pmatrix}.$$
> Desde $(x_0,y_0) = (2, 0.5)$, resolviendo $J\,\Delta = -F$ en cada paso:
>
> | $k$ | $x^{(k)}$ | $y^{(k)}$ | $\|F\|_2$ |
> |:---:|:---:|:---:|:---:|
> | 0 | 2.0000 | 0.5000 | 0.250 |
> | 1 | 1.9319 | 0.5176 | $4.7\text{e-}3$ |
> | 2 | 1.9319 | 0.5176 | $1.8\text{e-}6$ |
> | 3 | 1.9319 | 0.5176 | $<10^{-12}$ |
>
> Converge a $(\sqrt{2+\sqrt3},\,1/\sqrt{2+\sqrt3}) \approx (1.9319, 0.5176)$ en $2$–$3$ pasos: el residuo se eleva al cuadrado en cada iteración.

---

## Componentes del método

> [!info]
> | Componente | Nota |
> |:---|:---|
> | Linealización, jacobiana, sistema lineal por paso | [[Matriz Jacobiana y Sistema Lineal Asociado]] |
> | Orden y condiciones de convergencia | [[Convergencia Local Cuadratica]] |
> | Costo de evaluar $J$ y resolver el sistema; variantes cuasi-Newton | [[Costo Computacional Evaluacion Jacobiano]] |

---

## Algoritmo

> [!algoritmo]
> **Newton multivariable.**
>
> ```python
> import numpy as np
>
> def newton_sistema(F, J, x0, tol=1e-12, max_iter=50):
>     """Resuelve F(x)=0 con F: R^n -> R^n y jacobiana J(x)."""
>     x = x0.astype(float)
>     for k in range(max_iter):
>         Fx = F(x)
>         if np.linalg.norm(Fx, 2) < tol:
>             return x, k
>         dx = np.linalg.solve(J(x), -Fx)   # NO se invierte J: se resuelve el sistema
>         x = x + dx
>         if np.linalg.norm(dx, 2) < tol:
>             return x, k + 1
>     return x, max_iter
> ```

> [!warning]
> **Limitaciones (heredadas del caso escalar, amplificadas).**
> - **Convergencia solo local:** requiere $x^{(0)}$ próximo a la raíz; lejos puede diverger. Se mitiga con *globalización* (búsqueda de línea, región de confianza).
> - **Jacobiana singular o mal condicionada:** el sistema lineal $J\Delta = -F$ no se resuelve de forma fiable (ver [[Condicionamiento Numerico Numero Condicion|condicionamiento]]).
> - **Costo:** evaluar $n^2$ derivadas y resolver un sistema $O(n^3)$ por iteración ([[Costo Computacional Evaluacion Jacobiano]]).

---

## Relación con otras notas

> [!info]
> - Versión escalar de la que procede: [[Newton Raphson/index]] y [[Derivacion Geometrica y Serie Taylor]].
> - Alternativa de punto fijo sin jacobiana: [[Condicion Contraccion Norma Matricial]].
> - Panorama del problema: [[Sistemas Ecuaciones No Lineales/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Iteración | $x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1}F(x^{(k)})$ |
| Paso práctico | resolver $J\,\Delta = -F$, luego $x \mathrel{+}= \Delta$ |
| Orden | cuadrático (local) |
| Costo/iter | $\sim n^2$ derivadas + $\frac{2}{3}n^3$ (resolver) |
| Riesgo | divergencia global, $J$ singular |

> [!corolario]
> Newton multivariable resuelve $F(x)=0$ linealizando con la jacobiana y resolviendo, en cada paso, el sistema lineal $J(x^{(k)})\Delta x = -F(x^{(k)})$ —sin invertir $J$ explícitamente—. Hereda la convergencia cuadrática local de Newton escalar y, con ella, su sensibilidad al punto inicial y al condicionamiento de $J$. Sus tres caras se desarrollan en [[Matriz Jacobiana y Sistema Lineal Asociado|la linealización]], [[Convergencia Local Cuadratica|el orden de convergencia]] y [[Costo Computacional Evaluacion Jacobiano|el costo y las variantes cuasi-Newton]]; la alternativa más barata es la [[Condicion Contraccion Norma Matricial|iteración de punto fijo contractiva]].
