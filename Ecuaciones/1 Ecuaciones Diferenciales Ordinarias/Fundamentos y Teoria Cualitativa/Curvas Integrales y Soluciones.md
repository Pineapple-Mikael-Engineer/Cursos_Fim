---
title: Curvas Integrales y Soluciones
order: 3
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - curvas-integrales
draft: false
aliases:
  - curvas integrales
  - solución general
  - solución particular
  - solución singular
  - integral curves
---

# Curvas Integrales y Soluciones

> [!definicion]
> Una **curva integral** es la **gráfica** de una solución $y(x)$ de la EDO $y'=f(x,y)$; en cada punto es **tangente** al [[Campo de Direcciones e Isoclinas| campo de direcciones]]. Según cuántas constantes lleve, distinguimos:
> - **General**: familia con tantas constantes como el **orden** ($n$ constantes para orden $n$).
> - **Particular**: una concreta, fijando las constantes con condiciones.
> - **Singular**: solución que **no** se obtiene de la general para ningún valor de la constante.

> [!info]
> Cierra el bloque cualitativo (libro, cap. 1.2): traduce la noción de [[Concepto General de ODE| solución]] al lenguaje de curvas en el plano. Se apoya en el [[Campo de Direcciones e Isoclinas| campo de direcciones]] (que ellas siguen) y en [[Existencia y Unicidad Picard| unicidad]] (por la que no se cruzan). Las soluciones singulares se estudian aparte en [[Solucion Singular y Envolvente| envolventes]].

---

## Ejemplo

> [!ejemplo] Curvas integrales de $y'=2x$
> ![[curvas_integrales.svg|460]]
>
> La familia $y=x^2+c$: parábolas trasladadas verticalmente que **no se intersecan**. Por cada punto del plano pasa exactamente una.

> [!ejemplo]
> **De dónde sale la familia.** Integrando $y'=2x$ directamente,
> $$y=\int 2x\,dx=x^2+c.$$
> Aparece **una** constante $c$ porque la EDO es de **orden 1**: esa es la **solución general**. Cada valor de $c$ sube o baja la parábola, y al variar $c\in\mathbb{R}$ las curvas **llenan todo el plano sin cruzarse** — por el punto $(1,3)$ pasa solo la de $c=3-1^2=2$, es decir $y=x^2+2$. Fijar el punto fija $c$: eso es pasar de la general a una **particular**.

---

## En qué consiste

> [!teoria]
> La EDO impone una **pendiente** en cada punto; una curva integral es la curva que "obedece" esa pendiente en todo su recorrido (tangente al campo). La constante $c$ de la solución general es la **libertad** que queda antes de imponer condiciones: marca por **qué** punto pasa la curva. Imponer una condición inicial gasta esa libertad y deja una curva única — la solución **particular**.

> [!algoritmo] De general a particular
> 1. Resuelve la EDO de orden $n$ y obtén la **solución general** con $n$ constantes $c_1,\dots,c_n$.
> 2. Reúne $n$ condiciones: **iniciales** (todas en un mismo $x_0$) o **de frontera** (en extremos de un intervalo).
> 3. Sustituye las condiciones para formar un sistema en $c_1,\dots,c_n$ y resuélvelo.
> 4. Comprueba si existe alguna **solución singular** no incluida (suele venir de una envolvente).

> [!teorema] Las curvas integrales no se cruzan
> Si $f(x,y)$ es continua y $\partial f/\partial y$ es continua en una región $R$, entonces por cada punto de $R$ pasa **una sola** curva integral de $y'=f(x,y)$. En consecuencia, **dos curvas integrales distintas no pueden cortarse** dentro de $R$.

> [!demostracion]
> **Paso 1 — supón un cruce.** Sean $y_1$ e $y_2$ dos curvas integrales distintas que se cortan en un punto $(x_0,y_0)$, es decir $y_1(x_0)=y_2(x_0)=y_0$. Ambas resuelven entonces el **mismo PVI**
> $$y'=f(x,y),\qquad y(x_0)=y_0.$$
>
> **Paso 2 — aplica unicidad.** Como $f$ y $\partial f/\partial y$ son continuas cerca de $(x_0,y_0)$, el teorema de [[Existencia y Unicidad Picard| existencia y unicidad]] garantiza una **única** solución del PVI en un entorno de $x_0$. Por tanto $y_1\equiv y_2$ cerca de $x_0$, lo que **contradice** que fueran distintas. Luego no existe tal cruce. $\blacksquare$

> [!proposicion] El no-cruce es el determinismo
> Que por cada punto pase una sola curva integral significa que **las mismas condiciones determinan el mismo futuro y el mismo pasado**: conocido el estado en $(x_0,y_0)$, la trayectoria queda fijada hacia ambos lados. Donde falla la suavidad de $f$ (p. ej. $\partial f/\partial y$ no existe), pueden coexistir varias soluciones por un punto y el determinismo se rompe — ver el caso $y'=xy^{1/2}$ en [[Concepto General de ODE| el PVI sin unicidad]].

> [!info] General, particular, singular
> | Tipo | Constantes | Cómo se obtiene | Ejemplo en $y'=2x$ |
> |---|---|---|---|
> | General | $n$ libres (aquí $1$) | integrar la EDO | $y=x^2+c$ |
> | Particular | $0$ (fijadas) | imponer $n$ condiciones | $y=x^2+2$ por $(1,3)$ |
> | Singular | no sale de la general | envolvente de la familia | $-$ (no hay aquí) |

> [!warning]
> Una EDO de orden $n$ necesita **exactamente $n$ condiciones** para aislar una particular: $n$ condiciones **iniciales** (mismo punto $x_0$) o **de frontera** (puntos distintos). Con menos condiciones queda una subfamilia; con más, el problema suele ser **incompatible** salvo casos especiales.

## Resumen

> [!resumen]
> | Concepto | Definición | Clave |
> |---|---|---|
> | Curva integral | gráfica de una solución | tangente al campo en todo punto |
> | Solución general | familia con $n$ constantes (orden $n$) | $y=x^2+c$ |
> | Solución particular | una, fijando las constantes | $n$ condiciones (iniciales/frontera) |
> | Solución singular | no sale de la general | envolvente de la familia |
> | No cruce | dos integrales no se cortan | consecuencia de la unicidad |

> [!corolario]
> Resolver una EDO es **trazar las curvas que siguen el campo de pendientes**. La solución general describe **todas** a la vez (una constante por orden); las condiciones eligen una. La unicidad las mantiene separadas, y esa separación geométrica **es** el determinismo de las EDO bien planteadas.

> [!referencia]
> - El campo que estas curvas siguen: [[Campo de Direcciones e Isoclinas]].
> - Por qué no se cruzan (teorema): [[Existencia y Unicidad Picard]].
> - Vocabulario y PVI: [[Concepto General de ODE]].
> - Soluciones singulares y envolventes: [[Solucion Singular y Envolvente]].
> - Índice del bloque: [[Fundamentos y Teoria Cualitativa/index]].
