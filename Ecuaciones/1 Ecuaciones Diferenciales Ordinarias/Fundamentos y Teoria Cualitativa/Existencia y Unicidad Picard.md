---
title: Existencia y Unicidad (Picard-Lindelöf)
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - existencia-unicidad
draft: false
aliases:
  - teorema de Picard
  - Picard-Lindelöf
  - existencia y unicidad
  - existence and uniqueness theorem
  - Picard-Lindelöf theorem
---

# Existencia y Unicidad (Picard-Lindelöf)

> [!definicion]
> El **problema de valor inicial** (PVI)
> $$y'=f(x,y),\qquad y(x_0)=y_0$$
> tiene **una y solo una** solución en algún intervalo alrededor de $x_0$ si $f$ es **continua** y,
> además, **Lipschitz en $y$**: existe una constante $L\ge 0$ tal que
> $$|f(x,y_1)-f(x,y_2)|\ \le\ L\,|y_1-y_2|$$
> para todos los $y_1,y_2$ de un entorno de $y_0$. En la práctica basta verificar algo más simple:
> que $\partial f/\partial y$ sea **continua** (y por tanto acotada) cerca de $(x_0,y_0)$, porque eso
> ya implica la condición de Lipschitz por el teorema del valor medio.

> [!info]
> Es la nota **central** de los [[index | fundamentos cualitativos]]: la pregunta "¿la EDO tiene
> solución y es la única?" se responde aquí (libro, teoría de existencia y unicidad). Geométricamente
> continúa el [[Campo de Direcciones e Isoclinas | campo de direcciones]] (por qué las curvas
> integrales **no se cruzan**); analíticamente apoya todo el [[Concepto General de ODE | concepto de
> EDO]]. Su versión más débil, con sola continuidad, es el [[Teorema de Peano | teorema de Peano]]; su
> versión **constructiva** es la [[Iteracion de Picard | iteración de Picard]].

---

## Ejemplo

> [!ejemplo]
> **Un caso bueno: $y'=x+y$, $y(0)=0$.** Aquí $f(x,y)=x+y$ es continua en todo el plano y
> $$\frac{\partial f}{\partial y}=1$$
> es **constante**, luego continua y acotada: $f$ es Lipschitz en $y$ con $L=1$. El teorema garantiza
> una **única** solución. En efecto, resolviendo (lineal) se obtiene $y=e^{x}-x-1$, definida y única
> en toda la recta. Por cada punto del plano pasa exactamente una curva integral.

> [!ejemplo]
> **Un caso malo: $y'=x\,y^{1/2}$, $y(0)=0$.** Ahora $f(x,y)=x\,y^{1/2}$ **sí** es continua, pero
> $$\frac{\partial f}{\partial y}=\frac{x}{2\sqrt{y}}\ \xrightarrow[\;y\to 0^{+}\;]{}\ \infty,$$
> no está acotada cerca de $y=0$: **falla** la condición de Lipschitz justo en el dato inicial. Sin
> Lipschitz, el teorema **no aplica** y, de hecho, se **pierde la unicidad**: el mismo PVI tiene (al
> menos) dos soluciones,
> $$y\equiv 0 \qquad\text{y}\qquad y=\frac{x^{4}}{16}.$$
> Compruébese la segunda: $y'=\tfrac{4x^{3}}{16}=\tfrac{x^{3}}{4}$ y $x\,y^{1/2}=x\cdot\tfrac{x^{2}}{4}=\tfrac{x^{3}}{4}$.
> Moraleja: la continuidad de $f$ da existencia (Peano), pero la **unicidad** exige el control extra
> que aporta Lipschitz. El abanico completo de soluciones de este PVI se estudia en el
> [[Teorema de Peano | teorema de Peano]].

---

## En qué consiste

> [!teoria] La reformulación integral: el operador de Picard
> El truco que hace demostrable el teorema es convertir la EDO en una **ecuación integral**.
> Integrando $y'=f(x,y)$ desde $x_0$ hasta $x$ y usando $y(x_0)=y_0$:
> $$y(x)\ =\ y_0+\int_{x_0}^{x} f\bigl(t,y(t)\bigr)\,dt.$$
> Una función continua $y(x)$ resuelve el PVI **si y solo si** satisface esta igualdad. El lado
> derecho define el **operador de Picard**
> $$T[y](x)\ :=\ y_0+\int_{x_0}^{x} f\bigl(t,y(t)\bigr)\,dt,$$
> que transforma una función en otra. Entonces:
> $$\text{resolver el PVI}\quad\Longleftrightarrow\quad \text{hallar un \textbf{punto fijo} } y=T[y].$$
> Hemos cambiado "resolver una ecuación diferencial" por "encontrar un punto fijo de un operador",
> y para eso existe una maquinaria muy potente: el **teorema del punto fijo de Banach**.

> [!teorema] Picard-Lindelöf
> Sea $f$ definida en el **rectángulo**
> $$R=\{(x,y):\ |x-x_0|\le a,\ |y-y_0|\le b\}$$
> y supóngase que en $R$:
> 1. $f$ es **continua** y por tanto **acotada**, $|f(x,y)|\le M$;
> 2. $f$ es **Lipschitz en $y$**: $|f(x,y_1)-f(x,y_2)|\le L|y_1-y_2|$.
>
> Entonces el PVI $y'=f(x,y),\ y(x_0)=y_0$ posee una **solución única** $y(x)$, definida al menos en
> el intervalo
> $$|x-x_0|\le h,\qquad h=\min\!\Bigl(a,\ \tfrac{b}{M}\Bigr).$$

> [!demostracion]
> Trabajamos en el espacio $X$ de las funciones **continuas** $y:[x_0-h,\,x_0+h]\to\mathbb{R}$ que no
> se salen de la banda $|y(x)-y_0|\le b$, con la **norma del supremo** $\|y\|=\max|y(x)|$. Este espacio
> es **completo** (límite uniforme de continuas es continua), lo que habilita a Banach.
>
> **Paso 1 — $T$ aplica $X$ en sí mismo.** Hay que ver que si $y\in X$, también $T[y]\in X$, es decir,
> que las iteradas **no escapan** del rectángulo. $T[y]$ es continua (integral de función continua).
> Y para $|x-x_0|\le h$:
> $$\bigl|T[y](x)-y_0\bigr|=\Bigl|\int_{x_0}^{x} f(t,y(t))\,dt\Bigr|\le M\,|x-x_0|\le M\,h\le M\cdot\frac{b}{M}=b.$$
> El recorte $h\le b/M$ es **exactamente** lo que impide que la solución se salga de $R$ en vertical.
>
> **Paso 2 — $T$ es una contracción.** Para $y_1,y_2\in X$ y $|x-x_0|\le h$, usando Lipschitz:
> $$\bigl|T[y_1](x)-T[y_2](x)\bigr|=\Bigl|\int_{x_0}^{x}\!\bigl[f(t,y_1)-f(t,y_2)\bigr]dt\Bigr|
> \le \int_{x_0}^{x} L\,|y_1(t)-y_2(t)|\,dt\le L\,h\,\|y_1-y_2\|.$$
> Tomando el máximo en $x$,
> $$\|T[y_1]-T[y_2]\|\ \le\ L\,h\,\|y_1-y_2\|.$$
> Si elegimos $h$ suficientemente pequeño para que $q:=Lh<1$, el operador $T$ **contrae** distancias:
> es una contracción de constante $q$.
>
> **Paso 3 — punto fijo de Banach.** Un operador que contrae un espacio métrico completo tiene **un
> único punto fijo** $y^\*=T[y^\*]$, alcanzado como límite de las iteradas $y_{n+1}=T[y_n]$ desde
> cualquier $y_0\in X$ (esa sucesión es justo la [[Iteracion de Picard | iteración de Picard]]). Ese
> punto fijo es, por la equivalencia integral, la solución del PVI; y al ser único como punto fijo, la
> solución es **única** en $|x-x_0|\le h$.
>
> **Unicidad global.** La condición $Lh<1$ era solo para que la **contracción** funcionara en un paso;
> la unicidad en todo el intervalo donde la solución viva (no solo en el trozo pequeño) se obtiene sin
> esa restricción mediante la [[Desigualdad de Gronwall | desigualdad de Gronwall]]: si $y,z$ son dos
> soluciones, $u=|y-z|$ satisface $u(x)\le L\int_{x_0}^{x}u$, y Gronwall fuerza $u\equiv 0$.
> $\blacksquare$

> [!info] Por qué la construcción es constructiva
> La demostración **no** es solo existencial: la sucesión $y_{n+1}=T[y_n]$ converge de verdad a la
> solución, con error que decae geométricamente, $\|y_n-y^\*\|\le \dfrac{q^{\,n}}{1-q}\,\|y_1-y_0\|$.
> Ese algoritmo es la [[Iteracion de Picard | iteración de Picard]], el primer "método" para producir
> la solución cuando no hay fórmula cerrada.

> [!proposicion] Lectura geométrica: las curvas integrales no se cruzan
> En la región donde $f$ es continua y Lipschitz, por **cada punto** pasa exactamente una curva
> integral. Por eso, en el [[Campo de Direcciones e Isoclinas | campo de direcciones]], las soluciones
> **nunca se cortan**: dos curvas que se cruzaran en un punto darían allí dos PVI idénticos con dos
> soluciones distintas, contradiciendo la unicidad.

> [!warning]
> La **continuidad sola NO basta** para la unicidad. Garantiza existencia (eso es el
> [[Teorema de Peano | teorema de Peano]]), pero no que la solución sea una. Hace falta el ingrediente
> de **Lipschitz**. El contraejemplo canónico es $y'=x\,y^{1/2}$ desde el origen, donde $f$ es continua
> pero no Lipschitz y aparecen infinitas soluciones. No confundir Lipschitz con derivabilidad: $|y|$ es
> Lipschitz sin ser derivable; lo que importa es la **cota uniforme** del cociente de incrementos.

## Interpretación física

> [!teoria] Unicidad = determinismo causal
> En una ley física escrita como EDO, el estado presente $y(x_0)=y_0$ es la "condición inicial" y la
> ecuación dice cómo evoluciona. La **unicidad** es la traducción matemática del **determinismo**: un
> mismo presente determina un **único** futuro. Cuando la unicidad falla (campo no Lipschitz), el
> mismo estado inicial admite **varias** evoluciones: el modelo deja de ser predictivo. Por eso, en
> física, comprobar que $f$ es Lipschitz no es un tecnicismo, sino la garantía de que el modelo es
> causal.

## Resumen

> [!resumen]
> | Elemento | Enunciado | Papel |
> |---|---|---|
> | Hipótesis | $f$ continua y **Lipschitz en $y$** ($\partial f/\partial y$ continua basta) | da existencia **y** unicidad |
> | Reformulación | $y=y_0+\int_{x_0}^{x} f(t,y)\,dt$, operador $T[y]$ | PVI $\Leftrightarrow$ punto fijo |
> | Intervalo | $\|x-x_0\|\le h=\min(a,\,b/M)$ | recorte para no salir de $R$ |
> | Mecanismo | $T$ es contracción ($Lh<1$) + Banach | punto fijo único |
> | Unicidad global | [[Desigualdad de Gronwall\|Gronwall]] | extiende la unicidad |
> | Construcción | [[Iteracion de Picard\|iteración de Picard]] | produce la solución |

> [!corolario]
> La condición de Lipschitz es la **frontera fina** entre "existe" y "existe y es única". Por debajo
> ([[Teorema de Peano\|solo continuidad]]) puede haber un abanico de soluciones; con ella, el futuro
> queda determinado. Toda la teoría posterior de EDO —y la física que modela— descansa en que esta
> hipótesis se cumple en los casos de interés.

> [!referencia]
> - Existencia con menos hipótesis (y sin unicidad): [[Teorema de Peano]].
> - El algoritmo que construye la solución: [[Iteracion de Picard]].
> - La herramienta de la unicidad global: [[Desigualdad de Gronwall]].
> - Lectura geométrica previa: [[Campo de Direcciones e Isoclinas]].
> - Marco general: [[Concepto General de ODE]] · [[index]].
