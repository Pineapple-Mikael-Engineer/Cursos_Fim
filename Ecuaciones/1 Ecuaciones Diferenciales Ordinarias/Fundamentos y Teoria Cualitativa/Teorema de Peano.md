---
title: Teorema de Peano
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - existencia-unicidad
draft: false
aliases:
  - teorema de Peano
  - existencia de Peano
  - Peano existence theorem
---

# Teorema de Peano

> [!definicion]
> Si $f(x,y)$ es **continua** en un entorno del punto $(x_0,y_0)$, entonces el problema de valor
> inicial
> $$y'=f(x,y),\qquad y(x_0)=y_0$$
> tiene **al menos una** solución local (definida en algún intervalo alrededor de $x_0$). El teorema
> de Peano garantiza **existencia**, pero **no** unicidad: con sola continuidad la solución puede **no
> ser única**.

> [!info]
> Es la versión "mínima" de la teoría de existencia (libro, fundamentos cualitativos): exige solo
> continuidad de $f$, mucho menos que [[Existencia y Unicidad Picard| Picard]]. El precio de pedir
> tan poco es perder la unicidad. Sirve para entender **qué** garantiza cada hipótesis y por qué la
> unicidad —no la mera existencia— es la propiedad físicamente relevante. Complementa al
> [[Campo de Direcciones e Isoclinas| campo de direcciones]] y al [[Concepto General de ODE | concepto
> general de EDO]].

---

## Ejemplo

> [!ejemplo] No unicidad: abanico de soluciones de $y'=xy^{1/2}$
> ![[no_unicidad_peano.svg|460]]
>
> Por el origen pasan infinitas soluciones: la nula $y=0$, la $y=x^4/16$ y todas las que "despegan"
> del eje en un punto $x=a$ arbitrario.

> [!ejemplo]
> **El PVI $y'=x\,y^{1/2}$, $y(0)=0$ admite INFINITAS soluciones.** Como $f(x,y)=x\,y^{1/2}$ es
> **continua** en un entorno del origen, Peano asegura que **existe** solución. Pero veamos cuántas
> hay. Para cada parámetro $a\ge 0$ definamos
> $$y_a(x)=\begin{cases} 0, & x\le a,\\[4pt] \dfrac{(x^{2}-a^{2})^{2}}{16}, & x> a.\end{cases}$$
> Cada una de estas funciones **resuelve** el PVI:
> - Para $x\le a$ es $y_a=0$, luego $y_a'=0$ y $x\,y_a^{1/2}=0$: se cumple la EDO.
> - Para $x>a$, derivando, $y_a'=\dfrac{2(x^{2}-a^{2})\cdot 2x}{16}=\dfrac{x(x^{2}-a^{2})}{4}$, mientras que
>   $x\,y_a^{1/2}=x\cdot\dfrac{x^{2}-a^{2}}{4}=\dfrac{x(x^{2}-a^{2})}{4}$: coinciden.
> - En el empalme $x=a$ ambas ramas valen $0$ y tienen derivada $0$, así que $y_a$ es $C^1$.
>
> Variando $a\in[0,\infty)$ se obtiene un **abanico** (un continuo) de soluciones distintas, todas
> pasando por $(0,0)$: los casos extremos son $a=0$ (la curva $y=x^{4}/16$) y $a\to\infty$ (la solución
> nula $y\equiv 0$). El motivo de fondo es que $\partial f/\partial y=\dfrac{x}{2\sqrt y}$ explota
> cerca de $y=0$, de modo que $f$ **no es Lipschitz** allí y [[Existencia y Unicidad Picard| Picard]]
> no aplica.

---

## En qué consiste

> [!teoria] Esquema de la demostración (poligonales de Euler + Arzelà-Ascoli)
> La idea es **construir** una solución como límite de aproximaciones, sin necesidad de contracción
> (que requeriría Lipschitz). El argumento, en panorama:
> 1. **Poligonales de Euler.** Se parte $[x_0,x_0+h]$ en trozos y se fabrica una aproximación
>    quebrada $y_n(x)$ avanzando con pendiente $f$ evaluada en el nodo anterior (el método de Euler).
>    Cada $y_n$ es continua y resuelve la EDO "a saltos".
> 2. **Acotación y equicontinuidad.** Como $f$ es continua en un compacto, está **acotada**,
>    $|f|\le M$. Entonces todas las poligonales tienen pendiente acotada por $M$: la familia
>    $\{y_n\}$ está **uniformemente acotada** y es **equicontinua** (sus incrementos cumplen
>    $|y_n(x)-y_n(x')|\le M|x-x'|$, la misma cota para todas).
> 3. **Arzelà-Ascoli.** Una familia uniformemente acotada y equicontinua de funciones continuas tiene
>    una **subsucesión que converge uniformemente**. Sea $y$ ese límite.
> 4. **El límite resuelve el PVI.** Pasando al límite en la forma integral
>    $y_n(x)\approx y_0+\int_{x_0}^{x} f(t,y_n)\,dt$ (la continuidad de $f$ permite intercambiar
>    límite e integral), se obtiene $y(x)=y_0+\int_{x_0}^{x} f(t,y(t))\,dt$, es decir, $y$ es solución.
>
> **Por qué esto NO da unicidad:** Arzelà-Ascoli solo garantiza que **alguna** subsucesión converge.
> Distintas subsucesiones pueden converger a **soluciones distintas**. No hay nada que obligue a un
> único límite —eso es justo lo que aportaría la contracción de Picard—, así que el método es
> compatible con el abanico de soluciones del ejemplo.

> [!info] Peano frente a Picard
> | | [[Teorema de Peano\|Peano]] | [[Existencia y Unicidad Picard\|Picard-Lindelöf]] |
> |---|---|---|
> | Hipótesis sobre $f$ | solo **continua** | continua **y Lipschitz en $y$** |
> | Garantiza | **existencia** (al menos una solución) | existencia **y unicidad** |
> | Mecanismo | poligonales de Euler + **Arzelà-Ascoli** | operador de Picard + **punto fijo de Banach** |
> | ¿Constructivo? | da una solución como límite de una subsucesión | sí, [[Iteracion de Picard\|iteración de Picard]] |
> | Ejemplo límite | $y'=xy^{1/2},\ y(0)=0$: **infinitas** soluciones | $y'=x+y$: solución **única** |

> [!warning]
> Que **exista** solución no significa que el problema sea **determinista**. La existencia (Peano) es
> una condición débil; la propiedad físicamente relevante es la **unicidad**, que separa los modelos
> predictivos de los que no lo son. Un PVI con varias soluciones (como el del abanico) describe un
> sistema cuyo mismo presente admite varios futuros: matemáticamente impecable, pero inservible como
> ley causal. Por eso en aplicaciones se busca siempre la hipótesis de Lipschitz de
> [[Existencia y Unicidad Picard| Picard]].

## Resumen

> [!resumen]
> | Aspecto | Peano |
> |---|---|
> | Hipótesis | $f$ **continua** cerca de $(x_0,y_0)$ |
> | Conclusión | existe **al menos una** solución local |
> | Lo que NO da | **unicidad** (puede haber infinitas) |
> | Demostración | poligonales de Euler + Arzelà-Ascoli |
> | Ejemplo estrella | $y'=xy^{1/2},\ y(0)=0$ → abanico de soluciones |

> [!corolario]
> Peano y Picard delimitan dos niveles: la **continuidad** compra existencia; la **Lipschitz** compra,
> además, unicidad. El salto entre ambos es exactamente el contraejemplo $y'=xy^{1/2}$, donde $f$ es
> continua pero no Lipschitz: existe solución (Peano) pero no es única (falla Picard).

> [!referencia]
> - La versión con unicidad: [[Existencia y Unicidad Picard]].
> - El tipo de ecuación del ejemplo, resuelto por separación: [[Variables Separables]].
> - Marco general: [[Concepto General de ODE]] · [[Fundamentos y Teoria Cualitativa/index]].
