---
title: Convergencia Local Cuadrática
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - newton-raphson
  - convergencia
draft: false
aliases:
  - Convergencia cuadrática multivariable
  - Convergencia local de Newton
  - Local quadratic convergence
---

# Convergencia Local Cuadrática de Newton Multivariable

> [!definicion]
> El método de [[Newton Raphson Multivariable/index|Newton multivariable]] converge **cuadráticamente** a una raíz $r$ de $F(x)=0$ si existe $C > 0$ tal que, para $x^{(k)}$ suficientemente cerca de $r$,
> $$\|x^{(k+1)} - r\| \leq C\,\|x^{(k)} - r\|^2.$$
> El orden $p = 2$ se hereda del caso escalar: cerca de $r$, los dígitos correctos se duplican en cada iteración.

> [!info]
> La convergencia es **local**: requiere un punto inicial próximo a $r$. Las hipótesis multivariables sustituyen $f'(r)\neq 0$ por la no singularidad de la [[Matriz Jacobiana y Sistema Lineal Asociado|jacobiana]] $J(r)$, y $f\in C^2$ por la continuidad Lipschitz de $J$.

---

## Teorema de convergencia local

> [!teorema]
> Sea $F:\mathbb{R}^n\to\mathbb{R}^n$ con raíz $r$ ($F(r)=0$). Si en una vecindad de $r$:
> 1. $F$ es diferenciable con jacobiana $J$ **Lipschitz**: $\|J(x) - J(y)\| \leq \gamma\,\|x - y\|$,
> 2. $J(r)$ es **no singular**, con $\|J(r)^{-1}\| \leq \beta$,
>
> entonces existe $\delta > 0$ tal que, para todo $x^{(0)}$ con $\|x^{(0)} - r\| < \delta$, la sucesión de Newton converge a $r$ con
> $$\|x^{(k+1)} - r\| \leq \beta\gamma\,\|x^{(k)} - r\|^2.$$

> [!demostracion]
> **Paso 1: error tras un paso.** De $x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1}F(x^{(k)})$ y $F(r) = 0$, restando $r$:
> $$x^{(k+1)} - r = x^{(k)} - r - J(x^{(k)})^{-1}F(x^{(k)}) = J(x^{(k)})^{-1}\big[F(r) - F(x^{(k)}) - J(x^{(k)})(r - x^{(k)})\big].$$
>
> **Paso 2: cota del término entre corchetes.** Por el teorema fundamental del cálculo a lo largo del segmento $x^{(k)} \to r$,
> $$F(r) - F(x^{(k)}) = \int_0^1 J\big(x^{(k)} + t(r - x^{(k)})\big)\,(r - x^{(k)})\,dt.$$
> Restando $J(x^{(k)})(r - x^{(k)})$ y usando la continuidad Lipschitz de $J$:
> $$\big\|F(r) - F(x^{(k)}) - J(x^{(k)})(r - x^{(k)})\big\| \leq \int_0^1 \gamma\,t\,\|r - x^{(k)}\|\cdot\|r - x^{(k)}\|\,dt = \frac{\gamma}{2}\|x^{(k)} - r\|^2.$$
>
> **Paso 3: acotar $\|J(x^{(k)})^{-1}\|$.** Por continuidad, para $x^{(k)}$ cerca de $r$, $\|J(x^{(k)})^{-1}\| \leq 2\beta$ (lema de Banach sobre perturbación de la inversa).
>
> **Paso 4: combinar.** Multiplicando las cotas:
> $$\|x^{(k+1)} - r\| \leq 2\beta\cdot\frac{\gamma}{2}\,\|x^{(k)} - r\|^2 = \beta\gamma\,\|x^{(k)} - r\|^2.$$
> Si $\delta$ es lo bastante pequeño para que $\beta\gamma\delta < 1$, el error decrece y la convergencia es cuadrática.

---

## Ejemplo: duplicación de dígitos

> [!ejemplo]
> **Sistema $F(x,y) = (x^2 + y^2 - 4,\; xy - 1)^T$** con raíz $r \approx (1.93185, 0.51764)$. Newton desde $(2, 0.5)$:
>
> | $k$ | $\|x^{(k)} - r\|_2$ | $\|e^{(k+1)}\|/\|e^{(k)}\|^2$ | dígitos correctos |
> |:---:|:---:|:---:|:---:|
> | 0 | $6.9\times10^{-2}$ | — | 1 |
> | 1 | $1.2\times10^{-3}$ | 0.25 | 3 |
> | 2 | $3.6\times10^{-7}$ | 0.25 | 6 |
> | 3 | $3.2\times10^{-14}$ | 0.25 | 13 |
>
> El cociente $\|e^{(k+1)}\|/\|e^{(k)}\|^2 \to C \approx 0.25$ confirma orden $2$, y los dígitos correctos se duplican (1 → 3 → 6 → 13), idéntico patrón al [[Orden Convergencia Cuadratica Simple|caso escalar]].

---

## Pérdida de la convergencia cuadrática

> [!warning]
> El orden cae cuando fallan las hipótesis:
>
> | Hipótesis violada | Consecuencia | Remedio |
> |:---|:---|:---|
> | $J(r)$ **singular** (raíz "múltiple") | convergencia solo lineal | Newton modificado, deflación |
> | $x^{(0)}$ **lejos** de $r$ | posible divergencia | globalización: búsqueda de línea, región de confianza |
> | $J$ aproximada (diferencias finitas, cuasi-Newton) | convergencia **superlineal**, no cuadrática | [[Costo Computacional Evaluacion Jacobiano\|Broyden]] |
> | $J$ Lipschitz con $\gamma$ grande | región de convergencia $\delta$ pequeña | mejor estimación inicial |

> [!info]
> **Cuasi-Newton: el precio de no calcular $J$.** Métodos como Broyden, que actualizan una aproximación de $J$ en lugar de recalcularla, pierden la cuadraticidad y convergen **superlinealmente** ($p$ entre $1$ y $2$). Es el mismo compromiso que separa [[Metodo Secante Orden Convergencia Fi|secante]] de [[Orden Convergencia Cuadratica Simple|Newton]] en el caso escalar.

---

## Globalización: de local a robusto

> [!teoria]
> Para garantizar progreso desde puntos iniciales arbitrarios, el paso de Newton $\Delta x^{(k)}$ se amortigua con un factor $t_k \in (0, 1]$:
> $$x^{(k+1)} = x^{(k)} + t_k\,\Delta x^{(k)},$$
> eligiendo $t_k$ para que decrezca la función de mérito $\tfrac12\|F(x)\|_2^2$ (búsqueda de línea). Lejos de $r$ se toman pasos cortos seguros; cerca, $t_k \to 1$ y se **recupera** la convergencia cuadrática. Así se combina robustez global con velocidad local.

---

## Relación con otras notas

> [!info]
> - La linealización que produce el paso de Newton: [[Matriz Jacobiana y Sistema Lineal Asociado]].
> - El caso escalar análogo: [[Orden Convergencia Cuadratica Simple]] y [[Convergencia Lineal Raices Multiples]].
> - El costo de mantener la cuadraticidad y las variantes que la sacrifican: [[Costo Computacional Evaluacion Jacobiano]].
> - La alternativa de punto fijo (lineal, pero global bajo contracción): [[Condicion Contraccion Norma Matricial]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Orden | $p = 2$ (local) |
| Cota | $\|x^{(k+1)} - r\| \leq \beta\gamma\|x^{(k)} - r\|^2$ |
| Hipótesis | $J(r)$ no singular, $J$ Lipschitz, $x^{(0)}$ cercano |
| $J$ singular | cae a lineal |
| $J$ aproximada | cae a superlineal (cuasi-Newton) |
| Globalización | búsqueda de línea recupera $p=2$ cerca de $r$ |

> [!corolario]
> Newton multivariable converge cuadráticamente bajo dos hipótesis que generalizan el caso escalar: jacobiana $J(r)$ no singular (en vez de $f'(r)\neq0$) y $J$ Lipschitz (en vez de $f\in C^2$), con cota $\|x^{(k+1)}-r\| \leq \beta\gamma\|x^{(k)}-r\|^2$. La demostración aísla el error de la linealización mediante el teorema fundamental del cálculo. La cuadraticidad es **local**: jacobiana singular la degrada a lineal, jacobiana aproximada a superlineal (cuasi-Newton), y puntos iniciales lejanos exigen [[Costo Computacional Evaluacion Jacobiano|globalización]]. Es el mismo orden $p=2$ del [[Orden Convergencia Cuadratica Simple|Newton escalar]], razón de su empleo universal pese a su costo.
