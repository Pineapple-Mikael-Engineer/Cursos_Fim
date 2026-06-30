---
title: Puntos Ordinarios
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - puntos-ordinarios
draft: false
aliases:
  - puntos ordinarios
  - serie de potencias
  - relación de recurrencia
  - ordinary point
  - power series method
---

# Puntos Ordinarios

> [!definicion]
> Para $y''+p(x)\,y'+q(x)\,y=0$, el punto $x_0$ es **ordinario** si $p$ y $q$ son **analíticas** en $x_0$ (tienen serie de Taylor convergente ahí). Entonces existen **dos** soluciones independientes en serie de potencias
> $$y(x)=\sum_{n=0}^{\infty}a_n\,(x-x_0)^{n},$$
> cuyos coeficientes se obtienen de una **relación de recurrencia** al sustituir en la EDO.

> [!info]
> El caso **fácil y garantizado** del bloque [[Soluciones por Series/index| soluciones por series]]. Si el punto **no** es ordinario (singular), se usa el [[Frobenius/index| método de Frobenius]]. Las constantes $a_0,a_1$ son los datos $y(x_0),y'(x_0)$.

---

## Ejemplo

> [!ejemplo] Recuperar $\cos x$ y $\operatorname{sen}x$ de la serie
> **Resolver $y''+y=0$ en el punto ordinario $x_0=0$** ($p=0,q=1$, analíticas). **Paso 1 — proponer la serie y derivar:** $y=\sum_{n\ge0}a_nx^n$, $y''=\sum_{n\ge0}(n+2)(n+1)a_{n+2}x^n$ (reindexado). **Paso 2 — sustituir:** $\sum_{n\ge0}\big[(n+2)(n+1)a_{n+2}+a_n\big]x^n=0$. **Paso 3 — recurrencia** (coeficiente de cada $x^n$ nulo):
> $$a_{n+2}=-\frac{a_n}{(n+2)(n+1)}.$$
> **Paso 4 — generar:** los pares salen de $a_0$ y los impares de $a_1$:
> $$a_2=-\tfrac{a_0}{2!},\ a_4=\tfrac{a_0}{4!},\dots;\qquad a_3=-\tfrac{a_1}{3!},\ a_5=\tfrac{a_1}{5!},\dots$$
> **Paso 5 — sumar:**
> $$y=a_0\underbrace{\Big(1-\tfrac{x^2}{2!}+\tfrac{x^4}{4!}-\dots\Big)}_{\cos x}+a_1\underbrace{\Big(x-\tfrac{x^3}{3!}+\tfrac{x^5}{5!}-\dots\Big)}_{\operatorname{sen}x}.$$
> Las dos series son $\cos x$ y $\operatorname{sen}x$: el método las **reconstruye** desde cero, con $a_0=y(0)$ y $a_1=y'(0)$.

> [!ejemplo] Convergencia de las sumas parciales
> ![[convergencia_serie.svg|470]]
>
> Sumas parciales de la serie de $\cos x$ (solución de $y''+y=0$): al añadir términos, los polinomios de Taylor se ciñen a $\cos x$ en un intervalo cada vez mayor.

> [!ejemplo] Una serie que NO es elemental: la ecuación de Airy
> **$y''-xy=0$ en $x_0=0$.** Sustituyendo $y=\sum a_nx^n$ se llega a la recurrencia $a_{n+2}=\dfrac{a_{n-1}}{(n+2)(n+1)}$ (con $a_2=0$). La solución **no** se expresa con funciones elementales: define las **funciones de Airy** $\mathrm{Ai},\mathrm{Bi}$. El método funciona igual, aunque la "respuesta" sea una función nueva.

---

## En qué consiste

> [!teorema] Existencia de soluciones en serie (punto ordinario)
> Si $x_0$ es un punto **ordinario** de $y''+p y'+q y=0$, entonces toda solución es **analítica** en $x_0$: se desarrolla en serie de potencias convergente al menos en el mayor intervalo $|x-x_0|<R$ libre de singularidades de $p,q$. Hay exactamente **dos** soluciones independientes, fijadas por $a_0=y(x_0)$ y $a_1=y'(x_0)$.

> [!demostracion] De la EDO a la recurrencia (esquema)
> **Paso 1 — derivar término a término.** En el radio de convergencia, $y'=\sum n a_nx^{n-1}$, $y''=\sum n(n-1)a_nx^{n-2}$; reindexando, $y''=\sum_{n\ge0}(n+2)(n+1)a_{n+2}x^n$. **Paso 2 — multiplicar por las series de $p,q$.** Como $p,q$ son analíticas, sus productos por series son de nuevo series de potencias (producto de Cauchy). **Paso 3 — igualar coeficientes.** La EDO dice que la serie resultante es **idénticamente cero**; por unicidad de los coeficientes de una serie de potencias, **cada** coeficiente de $x^k$ se anula. Esa familia de ecuaciones es la **recurrencia**, que despeja $a_{n+2}$ en función de los anteriores. **Paso 4 — dos grados de libertad.** $a_0$ y $a_1$ quedan **libres**; cada elección genera una solución, y las dos básicas ($a_0{=}1,a_1{=}0$) y ($a_0{=}0,a_1{=}1$) son independientes. $\blacksquare$

> [!algoritmo] Resolver en un punto ordinario
> 1. Verifica que $x_0$ es ordinario ($p,q$ analíticas).
> 2. Propón $y=\sum a_n(x-x_0)^n$ y calcula $y',y''$ reindexando a la misma potencia.
> 3. Sustituye e **iguala a cero** el coeficiente de cada potencia → recurrencia.
> 4. Genera los $a_n$ a partir de $a_0,a_1$; identifica el patrón (par/impar).
> 5. Si reconoces la serie, escribe la función cerrada; si no, deja la serie (define una función).

> [!warning]
> El **radio de convergencia** llega hasta la singularidad más cercana de $p,q$ (en el plano complejo). Para $(1-x^2)y''-\dots$ (Legendre) las singularidades están en $x=\pm1$, así que la serie en $x_0=0$ converge en $|x|<1$.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Punto ordinario | $p,q$ analíticas en $x_0$ |
> | Proponer | $y=\sum a_n(x-x_0)^n$ |
> | Recurrencia | igualar a 0 el coeficiente de cada $x^k$ |
> | Libres | $a_0=y(x_0),\ a_1=y'(x_0)$ |
> | Convergencia | hasta la singularidad más cercana |

> [!corolario]
> En un punto ordinario el método **nunca falla**: la EDO se vuelve una recurrencia y entrega las dos soluciones como series de Taylor. Reconstruye funciones conocidas ($\cos,\operatorname{sen}$) y, en cuanto los coeficientes son variables "de verdad", **fabrica** funciones nuevas (Airy, Hermite).

> [!referencia]
> - El caso singular (serie con $x^r$): [[Frobenius/index]].
> - Las funciones que aparecen: [[Funciones Especiales/index]].
> - Marco del bloque: [[Soluciones por Series/index]].
