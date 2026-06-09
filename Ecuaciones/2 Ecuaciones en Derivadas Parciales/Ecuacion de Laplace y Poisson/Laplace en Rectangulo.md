---
title: Laplace en Rectángulo
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - separacion
draft: false
aliases:
  - Laplace en un rectángulo
  - problema de Dirichlet en rectángulo
  - separación cartesiana Laplace
  - Laplace on a rectangle
---

# Laplace en Rectángulo

> [!definicion]
> Resolver $\nabla^2u=u_{xx}+u_{yy}=0$ en un **rectángulo** $[0,a]\times[0,b]$ con datos de tipo
> **Dirichlet** sobre sus cuatro lados. Se aplica [[Tecnica de Separacion| separación de variables]]
> $u(x,y)=X(x)\,Y(y)$. Al sustituir, una de las dos direcciones —la que tiene condiciones
> **homogéneas** en sus dos extremos— produce un problema de autovalores con autofunciones
> **trigonométricas** ($\operatorname{sen}$, $\cos$); la otra dirección queda con soluciones
> **hiperbólicas** ($\sinh$, $\cosh$), porque la constante de separación entra con signo opuesto en
> $X''/X$ y en $Y''/Y$.

> [!info]
> Es el caso más sencillo de Laplace en geometría acotada, dentro del
> [[Ecuacion de Laplace y Poisson/index| bloque de Laplace]]. La parte trigonométrica reusa la
> maquinaria de [[Tecnica de Separacion]] y de las series de Fourier; el contraste lo da
> [[Laplace en Disco]], donde la geometría polar cambia las autofunciones. El objeto que se construye
> es una [[Funciones Armonicas| función armónica]] con valores de borde prescritos.

---

## Ejemplo

> [!ejemplo] Dirichlet con dato en un solo lado
> Resolvemos $\nabla^2u=0$ en $[0,a]\times[0,b]$ con
> $$u(0,y)=0,\quad u(a,y)=0,\quad u(x,0)=0,\quad u(x,b)=f(x).$$
> Tres lados a cero y el dato $f(x)$ en el lado superior.
>
> **Paso 1 — Separar.** Con $u=X(x)Y(y)$, la ecuación $X''Y+XY''=0$ se reescribe
> $$\frac{X''}{X}=-\frac{Y''}{Y}=-\lambda\quad(\text{constante}).$$
> Esto da dos EDO: $X''+\lambda X=0$ y $Y''-\lambda Y=0$.
>
> **Paso 2 — Dirección con dos extremos homogéneos ($x$).** Las condiciones $u(0,y)=u(a,y)=0$
> obligan $X(0)=X(a)=0$. Ese problema de autovalores tiene soluciones no triviales solo si
> $\lambda>0$:
> $$X_n(x)=\operatorname{sen}\frac{n\pi x}{a},\qquad \lambda_n=\Big(\frac{n\pi}{a}\Big)^2,\quad n=1,2,\dots$$
>
> **Paso 3 — Dirección hiperbólica ($y$).** Con $\lambda_n>0$, la ecuación $Y''-\lambda_n Y=0$ tiene
> solución general $Y=A\cosh\frac{n\pi y}{a}+B\sinh\frac{n\pi y}{a}$. La condición $u(x,0)=0$ impone
> $Y(0)=0$, luego $A=0$ y
> $$Y_n(y)=\sinh\frac{n\pi y}{a}.$$
>
> **Paso 4 — Superponer y ajustar el dato.** La solución general que cumple las tres condiciones
> homogéneas es
> $$u(x,y)=\sum_{n=1}^{\infty}b_n\,\operatorname{sen}\frac{n\pi x}{a}\,\sinh\frac{n\pi y}{a}.$$
> Imponiendo $u(x,b)=f(x)$:
> $$f(x)=\sum_{n=1}^\infty \Big(b_n\sinh\frac{n\pi b}{a}\Big)\operatorname{sen}\frac{n\pi x}{a}.$$
> El paréntesis es el $n$-ésimo coeficiente de Fourier en senos de $f$ en $[0,a]$, así que
> $$b_n\sinh\frac{n\pi b}{a}=\frac2a\int_0^a f(x)\,\operatorname{sen}\frac{n\pi x}{a}\,dx.$$
>
> **Resultado.** Despejando $b_n$ y reordenando, la solución se escribe limpiamente como
> $$\boxed{\,u(x,y)=\sum_{n=1}^\infty b_n\,\operatorname{sen}\frac{n\pi x}{a}\,
> \frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)},\qquad
> b_n=\frac2a\int_0^a f(x)\,\operatorname{sen}\frac{n\pi x}{a}\,dx\,}$$
> El cociente de senos hiperbólicos vale $1$ en $y=b$ (recuperando $f$) y decae hacia $y=0$.

---

## En qué consiste

> [!teoria] Superposición de las cuatro caras
> El ejemplo trató **un** lado con dato; el problema general tiene un dato distinto en cada uno de
> los **cuatro** lados. La estrategia es la **linealidad**: como $\nabla^2$ es lineal, se parte el
> problema en **cuatro subproblemas**, cada uno con dato en un solo lado y cero en los otros tres:
> $$u=u_{\text{abajo}}+u_{\text{arriba}}+u_{\text{izq}}+u_{\text{der}}.$$
> Cada subproblema se resuelve como el ejemplo (eligiendo en cada caso qué dirección queda
> trigonométrica y cuál hiperbólica), y la **suma** de los cuatro satisface a la vez los cuatro
> datos de frontera. Es el mismo principio de superposición que organiza todas las EDP lineales.

> [!algoritmo] Resolver Laplace en un rectángulo (un lado con dato)
> 1. **Homogeneizar.** Reordena para que tres lados tengan condición **cero**; el cuarto lleva el
>    dato $f$.
> 2. **Separar** $u=X(x)Y(y)$ y escribir $\dfrac{X''}{X}=-\dfrac{Y''}{Y}=-\lambda$.
> 3. **Identificar la dirección trigonométrica**: la que tiene los **dos extremos homogéneos**.
>    Resolver su problema de autovalores $\Rightarrow$ senos o cosenos y los $\lambda_n$.
> 4. **Resolver la dirección hiperbólica** con $\sinh$/$\cosh$ y aplicar la condición homogénea de
>    ese eje para fijar la combinación (típicamente $\sinh$ desde el lado a cero).
> 5. **Superponer** $u=\sum_n b_n X_n(x)Y_n(y)$ e imponer el dato $f$ para obtener los $b_n$ como
>    coeficientes de **Fourier**.
> 6. Si hay datos en **varios lados**, repite por lado y **suma** las soluciones.

> [!warning]
> Hay que cuidar **qué dirección** queda trigonométrica: es siempre la de los dos extremos
> homogéneos. Si el dato está en un lado **vertical** (p. ej. $u(a,y)=g(y)$), entonces es $y$ la
> dirección con senos y $x$ la hiperbólica —exactamente al revés del ejemplo—. Equivocar el eje lleva
> a autofunciones que no satisfacen las condiciones de borde.

## Resumen

> [!resumen]
> | Elemento | En el ejemplo |
> |---|---|
> | Dominio | rectángulo $[0,a]\times[0,b]$ |
> | Dato | $u(x,b)=f(x)$; cero en los otros tres lados |
> | Dirección trigonométrica | $x$: $X_n=\operatorname{sen}\frac{n\pi x}{a}$, $\lambda_n=(n\pi/a)^2$ |
> | Dirección hiperbólica | $y$: $Y_n=\sinh\frac{n\pi y}{a}$ |
> | Solución | $u=\sum_n b_n\operatorname{sen}\frac{n\pi x}{a}\,\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}$ |
> | Coeficientes | $b_n=\frac2a\int_0^a f\operatorname{sen}\frac{n\pi x}{a}\,dx$ |
> | Varios lados | superponer **4 subproblemas** |

> [!corolario]
> En un rectángulo, la geometría cartesiana reparte el trabajo: la dirección "cerrada" entre dos
> bordes a cero impone autofunciones **trigonométricas** (vía Fourier), y la dirección libre las
> conecta con $\sinh$/$\cosh$. Cualquier problema de Dirichlet en el rectángulo se reduce a sumar
> cuatro de estos, uno por lado.

> [!referencia]
> - La geometría polar cambia las autofunciones: [[Laplace en Disco]].
> - El objeto construido: [[Funciones Armonicas]].
> - La maquinaria de separación: [[Tecnica de Separacion]].
> - Marco general: [[Ecuacion de Laplace y Poisson/index]].
