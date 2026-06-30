---
title: Ecuación de Urysohn
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - no-lineales
  - urysohn
draft: false
aliases:
  - ecuación de Urysohn
  - ecuación integral de Urysohn
  - Urysohn equation
  - Urysohn integral equation
---

# Ecuación de Urysohn

> [!definicion]
> La **ecuación de Urysohn** es la ecuación integral no lineal **más general**:
> $$\varphi(x)=f(x)+\lambda\int_a^b K\big(x,t,\varphi(t)\big)\,dt,$$
> en la que el **núcleo entero** $K(x,t,u)$ depende de la incógnita de forma no lineal —no hay factorización que separe lo lineal de lo no lineal. Se reduce a la [[Ecuacion de Hammerstein|ecuación de Hammerstein]] en el caso particular $K(x,t,u)=K(x,t)\,g(t,u)$, y a una Fredholm lineal cuando $K(x,t,u)=K(x,t)\,u$. Es, por tanto, el marco que **contiene** a las demás.

> [!info]
> La forma canónica más amplia de la sección [[No Lineales/index|Ecuaciones Integrales No Lineales]] del [[3 Ecuaciones Integrales/index|capítulo de ecuaciones integrales]]. Al no separar la no linealidad, se pierden casi todas las herramientas algebraicas y la existencia se aborda con **teoremas de punto fijo**: **Schauder** (compacidad $\Rightarrow$ existencia, sin unicidad) frente a **Banach** (Lipschitz $\Rightarrow$ existencia y unicidad). En la práctica se resuelve por [[Aproximaciones Sucesivas|aproximaciones sucesivas]] o linealizando con Newton-Kantorovich.

---

## Ejemplo

> [!ejemplo] Una Urysohn sencilla por iteración (paso a paso)
> Resolvamos aproximadamente, en $[0,1]$,
> $$\varphi(x)=\frac{x}{2}+\lambda\int_0^1 \frac{x}{1+\varphi(t)}\,dt,\qquad \lambda=\tfrac{1}{4}.$$
> El núcleo $K(x,t,u)=\dfrac{x}{1+u}$ es **genuinamente de Urysohn**: depende de $\varphi$ de forma no lineal (a través de $1/(1+\varphi)$) y **no** se factoriza como $K(x,t)\,g(t,u)$ separando $t$ y $u$.
>
> **Paso 1 — observa la estructura.** Como $K$ es proporcional a $x$ y nada más depende de $x$, toda iterada tendrá la forma $\varphi(x)=c\,x$. Basta seguir la constante $c$.
>
> **Paso 2 — iteración 0.** Tomamos $\varphi_0(x)=\dfrac{x}{2}$ (el término libre), es decir $c_0=\tfrac12$.
>
> **Paso 3 — iteración 1.** Sustituimos $\varphi_0(t)=t/2$ en el integrando:
> $$\varphi_1(x)=\frac{x}{2}+\frac{1}{4}\int_0^1\frac{x}{1+t/2}\,dt=\frac{x}{2}+\frac{x}{4}\int_0^1\frac{dt}{1+t/2}.$$
> La integral es $\int_0^1\frac{dt}{1+t/2}=2\ln\!\big(1+\tfrac{t}{2}\big)\Big|_0^1=2\ln\tfrac32\approx0{,}8109$, de modo que
> $$\varphi_1(x)=\frac{x}{2}+\frac{x}{4}(0{,}8109)\approx 0{,}7027\,x.$$
>
> **Paso 4 — iteración 2.** Ahora con $\varphi_1(t)=0{,}7027\,t$:
> $$\int_0^1\frac{dt}{1+0{,}7027\,t}=\frac{1}{0{,}7027}\ln(1{,}7027)\approx\frac{0{,}5323}{0{,}7027}\approx0{,}7575,$$
> luego $\varphi_2(x)=\dfrac{x}{2}+\dfrac{x}{4}(0{,}7575)\approx 0{,}6894\,x$.
>
> **Paso 5 — lee la convergencia.** Las constantes $c_n$ van $0{,}5\to0{,}7027\to0{,}6894\to\cdots$ y se estabilizan rápidamente: la sucesión **converge** a la solución $\varphi(x)\approx0{,}69\,x$. La rapidez se debe a que $\lambda$ es pequeño y a que $u\mapsto 1/(1+u)$ es Lipschitz en $u\ge0$, justo las hipótesis del teorema de la contracción.

---

## En qué consiste

> [!teoria] Existencia por punto fijo de Schauder
> Reescribe la ecuación como un **punto fijo** del operador no lineal
> $$T\varphi=f+\lambda\int_a^b K\big(x,t,\varphi(t)\big)\,dt.$$
> El **teorema de Schauder** afirma: si $T$ es **compacto** (continuo y manda conjuntos acotados en conjuntos relativamente compactos) y mapea un conjunto **convexo, cerrado y acotado** $M$ en sí mismo, entonces $T$ tiene **al menos un punto fijo** en $M$ —es decir, la ecuación de Urysohn tiene **solución**. Schauder es la versión infinito-dimensional del teorema de Brouwer y solo da **existencia**: no afirma unicidad, de modo que pueden coexistir varias soluciones.
>
> **Contraste con Banach.** El teorema del punto fijo de Banach exige que $T$ sea una **contracción** (lo que requiere $K$ Lipschitz en $\varphi$ y $\lvert\lambda\rvert$ pequeño) y entonces garantiza solución **única**, obtenida por iteración. Schauder pide **menos** (compacidad en lugar de contracción) y, a cambio, concede **menos** (existencia sin unicidad). Es la disyuntiva típica de lo no lineal: o pides regularidad fuerte y ganas unicidad, o te conformas con compacidad y solo aseguras que **alguna** solución existe.

> [!algoritmo] Resolver una Urysohn en la práctica
> 1. **Aproximaciones sucesivas.** Itera $\varphi_{n+1}=f+\lambda\int_a^b K(x,t,\varphi_n)\,dt$ partiendo de $\varphi_0=f$. Converge si $T$ es contracción (ver [[Aproximaciones Sucesivas|aproximaciones sucesivas]]).
> 2. **Newton-Kantorovich (linealización).** Si la iteración simple converge lento, resuelve en cada paso la ecuación integral **lineal** obtenida al derivar $K$ respecto de $\varphi$:
>    $$\varphi_{n+1}=\varphi_n-\big(I-\lambda K_\varphi[\varphi_n]\big)^{-1}\big(\varphi_n-T\varphi_n\big),$$
>    donde $K_\varphi$ es la derivada (de Fréchet) del operador. Converge **cuadráticamente** cerca de la solución.
> 3. **Discretización.** Sustituye la integral por una cuadratura y resuelve el sistema **algebraico no lineal** resultante con Newton.

> [!proposicion] Urysohn contiene a Hammerstein y a Fredholm lineal
> Eligiendo $K(x,t,u)=K(x,t)\,g(t,u)$ se recupera la [[Ecuacion de Hammerstein|ecuación de Hammerstein]]; tomando además $g(t,u)=u$ se cae en la Fredholm **lineal** de segunda especie. Por eso toda la teoría no lineal (punto fijo, [[Raices Caracteristicas y Funciones Propias|bifurcaciones]]) se enuncia primero para Urysohn y luego se especializa.

> [!warning]
> Que Schauder garantice existencia **no** dice nada sobre cuántas soluciones hay ni cómo hallarlas. Sin hipótesis de contracción, la ecuación de Urysohn puede tener **varias** soluciones, y la iteración simple puede no converger; entonces hay que recurrir a Newton-Kantorovich o a métodos de continuación.

> [!info] Aplicaciones
> La ecuación de Urysohn modela fenómenos donde la respuesta depende no linealmente de la propia incógnita:
> - **Transferencia radiativa** en atmósferas estelares y planetarias (ecuación de Chandrasekhar para la función $H$).
> - **Teoría cinética** de gases (formas no lineales del operador de colisión).
> - **Dinámica de poblaciones** y modelos epidemiológicos con tasas no lineales de interacción.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi=f+\lambda\int_a^b K(x,t,\varphi)\,dt$ |
> | Estructura | **núcleo entero** no lineal en $\varphi$ (la más general) |
> | Reduce a | [[Ecuacion de Hammerstein\|Hammerstein]] si $K=K(x,t)\,g(t,u)$ |
> | Existencia | **Schauder** (compacidad $\Rightarrow$ existencia, sin unicidad) |
> | Unicidad | **Banach** (Lipschitz + $\lvert\lambda\rvert$ pequeño $\Rightarrow$ única) |
> | Métodos | iteración · Newton-Kantorovich · discretización |

> [!corolario]
> Urysohn es el techo de las ecuaciones integrales: lo abarca todo y, por eso mismo, ofrece las garantías más débiles. La existencia se rescata con **compacidad** (Schauder); la unicidad y un método constructivo, solo cuando hay **contracción** (Banach) y se puede iterar con [[Aproximaciones Sucesivas|aproximaciones sucesivas]].

> [!referencia]
> - El caso separable, más manejable: [[Ecuacion de Hammerstein]].
> - El método constructivo: [[Aproximaciones Sucesivas]].
> - El contexto no lineal: [[No Lineales/index]].
