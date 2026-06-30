---
title: Ecuación de Hammerstein
order: 1
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - no-lineales
  - hammerstein
draft: false
aliases:
  - ecuación de Hammerstein
  - ecuación integral de Hammerstein
  - Hammerstein equation
  - Hammerstein integral equation
---

# Ecuación de Hammerstein

> [!definicion]
> La **ecuación de Hammerstein** es la ecuación integral no lineal
> $$\varphi(x)=f(x)+\lambda\int_a^b K(x,t)\,g\big(t,\varphi(t)\big)\,dt,$$
> en la que el núcleo lineal $K(x,t)$ (a menudo **simétrico**, $K(x,t)=K(t,x)$) aparece **separado** de la no linealidad: toda la dependencia no lineal en la incógnita está encerrada en la función $g\big(t,\varphi(t)\big)$. Es el caso particular de la [[Ecuacion de Urysohn|ecuación de Urysohn]] en que el núcleo entero se factoriza como $K(x,t,u)=K(x,t)\,g(t,u)$. Por carecer de superposición, puede tener **una, ninguna o varias** soluciones.

> [!info]
> La forma no lineal **más estudiada** de la sección [[No Lineales/index|Ecuaciones Integrales No Lineales]], dentro del [[3 Ecuaciones Integrales/index|capítulo de ecuaciones integrales]]. Su estructura "núcleo lineal $\times$ no linealidad" la hace ideal para tres herramientas: el **punto fijo** vía [[Aproximaciones Sucesivas|aproximaciones sucesivas]], el **método variacional** (es la condición de Euler-Lagrange de un funcional cuando $g=\partial_u G$) y la reducción a un **sistema algebraico no lineal** cuando $K$ es degenerado. Es también el escenario natural de las **bifurcaciones**: al aumentar $\lambda$ y cruzar la primera [[Raices Caracteristicas y Funciones Propias|raíz característica]] del núcleo linealizado, nacen soluciones no triviales.

---

## Ejemplo

> [!ejemplo] Bifurcación: nacen soluciones nuevas
> ![[bifurcacion_hammerstein.svg|470]]
>
> Diagrama de bifurcación de un Hammerstein tipo $\varphi=\lambda\int K(x,t)\,(\varphi-\varphi^3)\,dt$: la solución trivial $\varphi\equiv0$ existe siempre, pero en $\lambda=\lambda_1$ aparece una rama no trivial (bifurcación de horquilla) cuya amplitud crece como $\sqrt{\lambda-\lambda_1}$.

El diagrama anticipa la idea central de toda la nota: en lo lineal, el problema homogéneo solo tiene la solución trivial salvo en valores aislados de $\lambda$; en lo no lineal, esos valores se convierten en **puntos de nacimiento** de ramas enteras de soluciones. Resolvamos primero un caso concreto donde todo esto se ve con números, eligiendo un núcleo **degenerado** que reduce la ecuación a una sola ecuación algebraica.

> [!ejemplo] Núcleo degenerado con no linealidad cúbica (resuelto paso a paso)
> Buscamos las soluciones del Hammerstein **homogéneo**
> $$\varphi(x)=\lambda\int_0^1 x\,t\,\varphi(t)^3\,dt,$$
> con núcleo $K(x,t)=xt$ (degenerado de rango $1$) y no linealidad $g(t,u)=u^3$.
>
> **Paso 1 — saca de la integral lo que depende de $x$.** Como $x$ no es variable de integración,
> $$\varphi(x)=\lambda\,x\underbrace{\int_0^1 t\,\varphi(t)^3\,dt}_{C},\qquad\text{luego}\qquad \varphi(x)=\lambda\,C\,x.$$
> Toda solución tiene **forma lineal** $\varphi(x)=\lambda C x$; el problema continuo se reduce a hallar la constante $C$.
>
> **Paso 2 — cierra la ecuación para $C$.** Sustituimos $\varphi(t)=\lambda C t$ dentro de la definición de $C$:
> $$C=\int_0^1 t\,(\lambda C t)^3\,dt=\lambda^3 C^3\int_0^1 t^4\,dt=\frac{\lambda^3 C^3}{5}.$$
> Queda la **ecuación algebraica no lineal**
> $$C=\frac{\lambda^3}{5}\,C^3.$$
>
> **Paso 3 — resuelve y distingue las ramas.** Factorizando $C\Big(1-\tfrac{\lambda^3}{5}C^2\Big)=0$:
> - **Solución trivial:** $C=0\Rightarrow\varphi\equiv0$. Existe para **todo** $\lambda$.
> - **Soluciones no triviales:** $C^2=\dfrac{5}{\lambda^3}$, es decir $C=\pm\sqrt{5/\lambda^3}$, que solo son reales si $\lambda>0$. Entonces
>   $$\varphi(x)=\pm\,\lambda\sqrt{\frac{5}{\lambda^3}}\;x=\pm\sqrt{\frac{5}{\lambda}}\;x.$$
>
> **Paso 4 — lee el resultado.** Para cada $\lambda>0$ coexisten **tres** soluciones: la trivial y dos no triviales simétricas $\pm\sqrt{5/\lambda}\,x$. Su amplitud **decrece** al crecer $\lambda$, pero lo esencial es cualitativo: la no linealidad cúbica genera **multiplicidad** de soluciones, algo imposible en una ecuación lineal homogénea. La elección concreta de $g$ y de $K$ decide si la rama nace al aumentar o al disminuir $\lambda$; el rasgo universal es la **separación** de ramas a partir de la trivial.

---

## En qué consiste

> [!teoria] Tres caminos para una Hammerstein
> La factorización "núcleo lineal $\times$ no linealidad" abre tres estrategias complementarias:
> 1. **Punto fijo (aproximaciones sucesivas).** Se itera el operador
>    $$\varphi_{n+1}(x)=f(x)+\lambda\int_a^b K(x,t)\,g\big(t,\varphi_n(t)\big)\,dt,\qquad \varphi_0=f.$$
>    Si $g$ es **Lipschitz** en su segundo argumento, $\lvert g(t,u)-g(t,v)\rvert\le L\lvert u-v\rvert$, y $\lvert\lambda\rvert$ es **suficientemente pequeño**, el operador es una contracción y la iteración converge a la **única** solución (ver [[Aproximaciones Sucesivas|aproximaciones sucesivas]]).
> 2. **Método variacional.** Si la no linealidad es un gradiente, $g(t,u)=\partial_u G(t,u)$ para cierta $G$, y $K$ es simétrico, la ecuación de Hammerstein es exactamente la **condición de Euler-Lagrange** del funcional
>    $$J[\varphi]=\frac{1}{2}\int_a^b\int_a^b K(x,t)\,\varphi(x)\varphi(t)\,dx\,dt-\frac{1}{\lambda}\int_a^b G\big(t,\varphi(t)\big)\,dt.$$
>    Buscar soluciones equivale entonces a buscar **puntos críticos** de $J$, y se usan métodos de minimización.
> 3. **Núcleo degenerado.** Si $K(x,t)=\sum_{i=1}^m a_i(x)\,b_i(t)$ (ver [[Nucleo Degenerado|núcleo degenerado]]), la solución es $\varphi(x)=f(x)+\lambda\sum_i C_i\,a_i(x)$ con $C_i=\int b_i\,g(t,\varphi)\,dt$, y la ecuación se convierte en un **sistema algebraico no lineal finito** para $(C_1,\dots,C_m)$.

> [!algoritmo] Resolver una Hammerstein de núcleo degenerado
> 1. Escribe el núcleo como $K(x,t)=\sum_{i=1}^m a_i(x)\,b_i(t)$.
> 2. Propón la forma $\varphi(x)=f(x)+\lambda\sum_{i=1}^m C_i\,a_i(x)$, con incógnitas $C_i$.
> 3. Sustituye en $C_i=\int_a^b b_i(t)\,g\big(t,\varphi(t)\big)\,dt$ para obtener un **sistema no lineal** en $(C_1,\dots,C_m)$.
> 4. Resuélvelo (factorización, Newton, etc.); cada raíz real da una solución $\varphi$.
> 5. Identifica la rama trivial y las ramas que nacen al variar $\lambda$.

### Bifurcación: el fenómeno central

> [!teoria] Cómo nacen las soluciones no triviales
> Considera el problema **homogéneo** $\varphi=\lambda\int_a^b K(x,t)\,g(t,\varphi)\,dt$ con $g(t,0)=0$, de modo que $\varphi\equiv0$ es siempre solución. **Linealiza** alrededor de la trivial escribiendo $g(t,\varphi)\approx g_u(t,0)\,\varphi$ para $\varphi$ pequeña: cerca de cero la ecuación se comporta como la **homogénea lineal**
> $$\varphi(x)\approx\lambda\int_a^b K(x,t)\,g_u(t,0)\,\varphi(t)\,dt,$$
> cuyo espectro son las [[Raices Caracteristicas y Funciones Propias|raíces características]] $\lambda_1,\lambda_2,\dots$ del núcleo efectivo $K(x,t)\,g_u(t,0)$. Mientras $\lambda$ no alcance la primera raíz $\lambda_1$, la única solución cercana es la trivial. **Al cruzar $\lambda_1$**, la trivial pierde estabilidad y de ella **se desprende** una rama de soluciones no triviales: es la **bifurcación**. Para una no linealidad cúbica simétrica $g(t,u)=u-u^3$ se obtiene la típica **horquilla** (*pitchfork*), con amplitud que crece como $\sqrt{\lambda-\lambda_1}$, tal como ilustra el diagrama del ejemplo.

> [!proposicion] Las raíces características marcan los puntos de bifurcación
> Los valores de $\lambda$ donde pueden aparecer ramas no triviales son, precisamente, las **raíces características** del núcleo linealizado $K(x,t)\,g_u(t,0)$. Por eso el análisis no lineal de Hammerstein **hereda** el espectro de la teoría lineal de [[Fredholm/index|Fredholm]]: la pregunta cambia de "¿cuál es la solución?" a "¿en qué $\lambda$ y con qué amplitud nacen soluciones nuevas?".

> [!warning]
> Sin linealidad **no** hay unicidad garantizada. El teorema de la contracción solo asegura una solución cuando $g$ es Lipschitz y $\lvert\lambda\rvert$ es pequeño; fuera de ese régimen pueden coexistir **varias** soluciones (como en el ejemplo, donde había tres) o **ninguna**. No se cumple el principio de superposición: sumar dos soluciones no produce otra.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi=f+\lambda\int_a^b K(x,t)\,g(t,\varphi)\,dt$ |
> | Estructura | núcleo lineal $K$ **separado** de la no linealidad $g$ |
> | Caso de | [[Ecuacion de Urysohn\|Urysohn]] con $K(x,t,u)=K(x,t)\,g(t,u)$ |
> | Existencia/unicidad | Banach (única) si $g$ Lipschitz y $\lvert\lambda\rvert$ pequeño |
> | Métodos | punto fijo · variacional ($g=\partial_u G$) · núcleo degenerado |
> | Fenómeno nuevo | **bifurcación** al cruzar la raíz característica $\lambda_1$ |

> [!corolario]
> Hammerstein es el puente entre lo lineal y lo no lineal: conserva el **núcleo** y su espectro, pero deja que la no linealidad $g$ multiplique las soluciones. Las raíces características de Fredholm reaparecen como **puntos de bifurcación**, y la iteración de [[Aproximaciones Sucesivas|aproximaciones sucesivas]] sigue sirviendo —pero solo localmente y para $\lambda$ pequeño.

> [!referencia]
> - El caso general que la contiene: [[Ecuacion de Urysohn]].
> - La iteración que la resuelve: [[Aproximaciones Sucesivas]].
> - El espectro que marca las bifurcaciones: [[Raices Caracteristicas y Funciones Propias]].
> - El contexto no lineal: [[No Lineales/index]].
