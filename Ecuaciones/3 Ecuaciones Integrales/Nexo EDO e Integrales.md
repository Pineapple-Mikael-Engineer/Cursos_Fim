---
title: Nexo EDO e Integrales
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - nexo-edo
draft: false
aliases:
  - nexo EDO e integrales
  - de EDO a ecuación integral
  - reducción de un PVI a Volterra
  - reducción de un PVF a Fredholm
  - link between ODEs and integral equations
---

# Nexo EDO e Integrales

> [!definicion]
> Toda **ecuación diferencial ordinaria con condiciones** se puede reescribir como una **ecuación
> integral equivalente**, sin más que integrar. La regla es nítida:
> - Un **problema de valor inicial** (PVI) se convierte en una ecuación de **Volterra** (límite variable),
>   porque la información se **acumula desde el dato inicial** hacia adelante.
> - Un **problema de valor de frontera** (PVF) se convierte en una ecuación de **Fredholm** (límites
>   fijos), porque el dato se reparte en **ambos extremos** y se acopla vía la
>   [[Funcion de Green para EDO| función de Green]].

> [!info]
> Nota puente del capítulo [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]: justifica por qué la
> familia [[Volterra/index| Volterra]] es la cara integral de los PVI y [[Fredholm/index| Fredholm]] la
> de los PVF. Usa el vocabulario de [[Conceptos Fundamentales]] y la
> [[Funcion de Green para EDO| función de Green]] de las EDO. Es la base de la
> [[Iteracion de Picard| iteración de Picard]].
> Fuente: **Krasnov, Kiseliov, Makarenko**.

---

## Ejemplo

> [!ejemplo] Convertir un PVI de orden 2 en una Volterra y comprobar la solución
> Partimos del PVI
> $$y''+y=0,\qquad y(0)=0,\quad y'(0)=1,$$
> cuya solución conocida es $y=\operatorname{sen}x$. Lo reescribimos como ecuación integral.
>
> **Paso 1 — despejar la derivada más alta.** $y''=-y$.
>
> **Paso 2 — integrar una vez de $0$ a $x$.** Usando $y'(0)=1$,
> $$y'(x)=y'(0)-\int_0^x y(t)\,dt=1-\int_0^x y(t)\,dt.$$
>
> **Paso 3 — integrar otra vez.** Usando $y(0)=0$,
> $$y(x)=y(0)+\int_0^x y'(s)\,ds=x-\int_0^x\!\!\int_0^s y(t)\,dt\,ds.$$
>
> **Paso 4 — colapsar la integral doble.** Por la fórmula de Cauchy (intercambio del orden de
> integración), $\displaystyle\int_0^x\!\!\int_0^s y(t)\,dt\,ds=\int_0^x (x-t)\,y(t)\,dt$. Por tanto
> $$\boxed{\,y(x)=x-\int_0^x (x-t)\,y(t)\,dt\,}$$
> una **Volterra de segunda especie** con término libre $f(x)=x$, parámetro $\lambda=1$ y núcleo
> $K(x,t)=-(x-t)$.
>
> **Paso 5 — comprobar que $y=\operatorname{sen}x$ la satisface.** El lado derecho es
> $$x-\int_0^x (x-t)\operatorname{sen}t\,dt.$$
> Integrando por partes (o usando $\int_0^x(x-t)\operatorname{sen}t\,dt=x-\operatorname{sen}x$), queda
> $x-(x-\operatorname{sen}x)=\operatorname{sen}x$. **Coincide.** $\checkmark$
>
> Lo notable: el dato inicial quedó **incorporado** en el término libre $f(x)=x$ y el núcleo $(x-t)$
> apareció **solo** de integrar dos veces. No hay constantes de integración sueltas.

---

## En qué consiste

> [!teorema] Un PVI de primer orden equivale a una Volterra de 2ª especie
> El problema de valor inicial
> $$y'=f(x,y),\qquad y(x_0)=y_0$$
> es **equivalente** a la ecuación integral de Volterra
> $$y(x)=y_0+\int_{x_0}^x f\big(t,y(t)\big)\,dt.$$

> [!demostracion]
> **Paso 1 — de la EDO a la integral.** Si $y$ resuelve el PVI, integramos $y'=f(x,y)$ de $x_0$ a $x$:
> $$y(x)-y(x_0)=\int_{x_0}^x f\big(t,y(t)\big)\,dt,$$
> y como $y(x_0)=y_0$ se obtiene $y(x)=y_0+\int_{x_0}^x f(t,y(t))\,dt$.
>
> **Paso 2 — de la integral a la EDO.** Recíprocamente, si $y$ es continua y cumple esa ecuación
> integral, el integrando es continuo, así que el **teorema fundamental del cálculo** permite **derivar**:
> $y'(x)=f(x,y(x))$. Y evaluando en $x=x_0$ la integral se anula, luego $y(x_0)=y_0$. Ambas formulaciones
> tienen exactamente las mismas soluciones. $\blacksquare$
>
> La ecuación integral tiene una ventaja: ya **incluye** la condición inicial (no hay constantes que
> fijar) y su lado derecho es un **operador** $\mathcal T y=y_0+\int_{x_0}^x f(t,y)\,dt$ cuyo **punto
> fijo** es la solución. Iterarlo $y_{n+1}=\mathcal T y_n$ es exactamente la
> [[Iteracion de Picard| iteración de Picard]].

> [!proposicion] Orden 2: el núcleo $(x-t)$
> Para una EDO de segundo orden $y''=F(x,y,y')$ con $y(0)=y_0$, $y'(0)=y_1$, integrar **dos veces**
> produce el núcleo $(x-t)$:
> $$y(x)=\underbrace{y_0+y_1 x}_{\text{datos iniciales}}+\int_0^x (x-t)\,F\big(t,y(t),y'(t)\big)\,dt.$$
> Esto se debe a la fórmula de Cauchy para integrales repetidas,
> $\displaystyle\int_0^x\!\!\int_0^s g(t)\,dt\,ds=\int_0^x (x-t)\,g(t)\,dt$. En general, integrar $n$
> veces da el núcleo $\dfrac{(x-t)^{n-1}}{(n-1)!}$.

> [!teorema] Un PVF equivale a una Fredholm (vía función de Green)
> El problema de valor de frontera
> $$-u''=\lambda\,u,\qquad u(0)=u(1)=0$$
> se reescribe como la ecuación integral de **Fredholm homogénea**
> $$u(x)=\lambda\int_0^1 G(x,t)\,u(t)\,dt,$$
> donde $G(x,t)$ es la [[Funcion de Green para EDO| función de Green]] de $-\dfrac{d^2}{dx^2}$ con esas
> condiciones de frontera. Los **autovalores** $\lambda$ de la ecuación integral coinciden con los del
> problema de frontera.

> [!demostracion]
> **Paso 1 — la función de Green.** $G(x,t)$ resuelve $-G_{xx}=\delta(x-t)$ con $G(0,t)=G(1,t)=0$. Para
> este operador es
> $$G(x,t)=\begin{cases} t\,(1-x), & t\le x,\\[2pt] x\,(1-t), & t\ge x,\end{cases}$$
> que es **simétrica**, $G(x,t)=G(t,x)$.
>
> **Paso 2 — invertir el operador diferencial.** La ecuación $-u''=g$ con $u(0)=u(1)=0$ tiene por solución
> $u(x)=\int_0^1 G(x,t)\,g(t)\,dt$. Es decir, $G$ es el **inverso** del operador $-d^2/dx^2$ sujeto a las
> condiciones de frontera.
>
> **Paso 3 — aplicarlo al PVF.** En nuestro problema $g=\lambda u$, así que sustituyendo,
> $$u(x)=\int_0^1 G(x,t)\,\lambda\,u(t)\,dt=\lambda\int_0^1 G(x,t)\,u(t)\,dt,$$
> que es una **Fredholm homogénea de 2ª especie** con núcleo **simétrico** $G$. Sus autovalores son
> $\lambda_n=(n\pi)^2$ y sus funciones propias $u_n(x)=\operatorname{sen}(n\pi x)$ —exactamente las del
> PVF original—. $\blacksquare$
>
> Que el núcleo sea **simétrico** no es casualidad: refleja que el operador $-d^2/dx^2$ con esas
> condiciones es **autoadjunto**, de donde el espectro real y las funciones propias ortogonales.

> [!info] Por qué PVI $\to$ Volterra y PVF $\to$ Fredholm
> La diferencia está en **cómo se reparte la información**. En un PVI todo el dato está en **un punto**
> ($x_0$): al integrar se acumula **hacia adelante**, el límite superior es la variable $x$, y sale
> Volterra. En un PVF el dato está en **dos extremos**: cada punto interior "ve" toda la barra a través de
> la función de Green, los límites son **fijos** $[a,b]$, y sale Fredholm.

## Resumen

> [!resumen]
> | Problema diferencial | Se reescribe como | Núcleo | Naturaleza |
> |---|---|---|---|
> | PVI $y'=f(x,y),\ y(x_0)=y_0$ | Volterra 2ª: $y=y_0+\int_{x_0}^x f$ | $f(t,y)$ | local, siempre soluble |
> | PVI orden 2 $y''=F$ | Volterra 2ª: $y=(\text{datos})+\int_0^x (x-t)F$ | $(x-t)$ | local |
> | PVF $-u''=\lambda u,\ u(0)=u(1)=0$ | Fredholm hom.: $u=\lambda\int_0^1 G\,u$ | $G(x,t)$ simétrico | global, espectral |

> [!corolario]
> El paralelismo es exacto y se repite en las EDP: **PVI $\leftrightarrow$ Volterra** es lo **local**
> (acumular desde un inicio, solución única, base de Picard); **PVF $\leftrightarrow$ Fredholm** es lo
> **global y espectral** (acoplar dos extremos vía función de Green, autovalores y funciones propias).
> Reescribir una EDO como ecuación integral no es un truco: **incorpora las condiciones** en la ecuación y
> convierte la existencia de soluciones en un problema de **punto fijo** (Volterra) o de **espectro**
> (Fredholm).

> [!referencia]
> - El vocabulario de familia y especie: [[Conceptos Fundamentales]].
> - El método de punto fijo asociado: [[Iteracion de Picard| Iteración de Picard]].
> - La función de Green que cierra el caso PVF: [[Funcion de Green para EDO]].
> - Las dos familias: [[Volterra/index]] y [[Fredholm/index]].
> - El mapa del capítulo: [[3 Ecuaciones Integrales/index]].
