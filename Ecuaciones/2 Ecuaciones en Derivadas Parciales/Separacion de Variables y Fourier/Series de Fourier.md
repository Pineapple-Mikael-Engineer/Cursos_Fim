---
title: Series de Fourier
order: 3
tags:
  - ecuaciones
  - edp
  - teoria
  - fourier
  - series
draft: false
aliases:
  - serie de Fourier
  - coeficientes de Fourier
  - serie de senos
  - serie de cosenos
  - Fourier series
---

# Series de Fourier

> [!definicion]
> Una función periódica de periodo $2L$ se desarrolla en **serie de Fourier** como
> $$f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\Big(a_n\cos\frac{n\pi x}{L}+b_n\operatorname{sen}\frac{n\pi x}{L}\Big),$$
> donde los **coeficientes de Fourier** se calculan con las **fórmulas de Euler–Fourier**
> $$a_n=\frac{1}{L}\int_{-L}^{L} f(x)\cos\frac{n\pi x}{L}\,dx\ (n\ge0),\qquad
> b_n=\frac{1}{L}\int_{-L}^{L} f(x)\operatorname{sen}\frac{n\pi x}{L}\,dx\ (n\ge1).$$
> El término $\tfrac{a_0}{2}$ es el **valor medio** de $f$; los demás suman los **armónicos** de frecuencia creciente que reconstruyen la función. (El $\tfrac12$ hace que la fórmula de $a_0$ sea el caso $n=0$ de la de $a_n$.)

> [!info]
> Es el caso "estrella" de los desarrollos en [[Funciones Ortogonales| funciones ortogonales]]: la base son senos y cosenos. Aparece al ajustar el dato inicial en [[Tecnica de Separacion| separación de variables]]. La convergencia y el sobreimpulso cerca de un salto se estudian en [[Convergencia y Gibbs]], y el balance de energía en [[Identidad de Parseval]]. Nota de [[Separacion de Variables y Fourier/index| esta sección]].

---

## Ejemplo

> [!ejemplo] Sumas parciales de la serie de una onda cuadrada
> ![[serie_fourier.svg|470]]
>
> Tomemos la **onda cuadrada** $f(x)=\operatorname{sgn}(x)$ en $[-\pi,\pi]$ (vale $-1$ si $x<0$ y $+1$ si $x>0$), extendida con periodo $2\pi$, de modo que $L=\pi$.
>
> **Paso 1 — usar la paridad.** $f$ es **impar**, así que todos los cosenos se anulan: $a_n=0$ para todo $n$ (y $a_0=0$, el valor medio es cero). Solo sobreviven los senos.
>
> **Paso 2 — calcular $b_n$.** Como el integrando $f(x)\operatorname{sen}(nx)$ es par,
> $$b_n=\frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\operatorname{sen}(nx)\,dx=\frac{2}{\pi}\int_0^{\pi}\operatorname{sen}(nx)\,dx
> =\frac{2}{\pi}\,\frac{1-\cos(n\pi)}{n}.$$
> Ahora bien $\cos(n\pi)=(-1)^n$, así que $1-\cos(n\pi)$ vale $0$ si $n$ es **par** y $2$ si $n$ es **impar**. Solo quedan los armónicos impares:
> $$b_n=\frac{4}{\pi n}\ (n\ \text{impar}),\qquad b_n=0\ (n\ \text{par}).$$
>
> **Paso 3 — escribir la serie.** Reuniendo los términos impares $n=2k+1$,
> $$f(x)=\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\operatorname{sen}\big((2k+1)x\big)}{2k+1}
> =\frac{4}{\pi}\Big(\operatorname{sen}x+\frac{\operatorname{sen}3x}{3}+\frac{\operatorname{sen}5x}{5}+\cdots\Big).$$
> Como muestra la figura, al añadir armónicos las **sumas parciales** se acercan cada vez más a la onda cuadrada; pero cerca del salto persiste un **sobreimpulso** que no desaparece al sumar más términos: es el fenómeno de Gibbs.

---

## En qué consiste

> [!teorema] Las fórmulas de Euler–Fourier salen de la ortogonalidad
> Sobre $[-L,L]$, los senos y cosenos $\{1,\cos\frac{n\pi x}{L},\operatorname{sen}\frac{n\pi x}{L}\}$ son **ortogonales**:
> $$\int_{-L}^{L}\operatorname{sen}\frac{n\pi x}{L}\operatorname{sen}\frac{m\pi x}{L}\,dx=L\,\delta_{nm},\quad
> \int_{-L}^{L}\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx=L\,\delta_{nm},$$
> $$\int_{-L}^{L}\operatorname{sen}\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx=0.$$
> En consecuencia, los coeficientes son los de la definición.

> [!demostracion]
> **Paso 1 — multiplicar por un coseno e integrar.** Partimos de $f=\tfrac{a_0}{2}+\sum_n\big(a_n\cos\frac{n\pi x}{L}+b_n\operatorname{sen}\frac{n\pi x}{L}\big)$, multiplicamos ambos lados por $\cos\frac{m\pi x}{L}$ (con $m\ge1$) e integramos en $[-L,L]$:
> $$\int_{-L}^{L} f\cos\frac{m\pi x}{L}\,dx=\frac{a_0}{2}\!\int_{-L}^{L}\!\cos\frac{m\pi x}{L}\,dx
> +\sum_n a_n\!\int_{-L}^{L}\!\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx
> +\sum_n b_n\!\int_{-L}^{L}\!\operatorname{sen}\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx.$$
> **Paso 2 — anular todo salvo un término.** Por las relaciones de ortogonalidad: la primera integral es $0$ (un coseno completo integra cero), todas las integrales seno–coseno son $0$, y de la suma de cosenos solo sobrevive $n=m$, que vale $L$. Queda
> $$\int_{-L}^{L} f\cos\frac{m\pi x}{L}\,dx=a_m\,L.$$
> **Paso 3 — despejar.** Por tanto $a_m=\dfrac{1}{L}\displaystyle\int_{-L}^{L} f\cos\frac{m\pi x}{L}\,dx$. Repitiendo con $\operatorname{sen}\frac{m\pi x}{L}$ se obtiene la fórmula de $b_m$; con la constante $1$, la de $a_0$. $\blacksquare$

> [!teoria] Series de senos y de cosenos (las de separación de variables)
> Cuando $f$ está definida solo en $[0,L]$ —como en la condición inicial de una barra—, podemos **extenderla** a $[-L,L]$ de dos formas y desarrollar:
> - **Extensión impar** → solo senos: la **serie de senos** $f(x)=\sum_{n\ge1} b_n\operatorname{sen}\frac{n\pi x}{L}$ con $b_n=\frac{2}{L}\int_0^L f\operatorname{sen}\frac{n\pi x}{L}\,dx$. Es la que aparece con extremos a temperatura cero ($u=0$ en los bordes).
> - **Extensión par** → solo cosenos: la **serie de cosenos** $f(x)=\frac{a_0}{2}+\sum_{n\ge1} a_n\cos\frac{n\pi x}{L}$ con $a_n=\frac{2}{L}\int_0^L f\cos\frac{n\pi x}{L}\,dx$. Es la que aparece con extremos aislados (flujo nulo, $u_x=0$ en los bordes).
>
> La elección **la dicta la condición de frontera** del problema separado: cada tipo de borde selecciona qué autofunciones (senos o cosenos) forman la base.

> [!info]
> El factor $\tfrac{2}{L}$ en senos/cosenos sobre $[0,L]$ y el $\tfrac{1}{L}$ sobre $[-L,L]$ no son distintos por capricho: en cada caso es $1/\|\varphi_n\|^2$, la inversa de la norma de la autofunción. Es la misma fórmula de proyección de [[Funciones Ortogonales]] con el peso $w=1$.

---

## Resumen

> [!resumen]
> | Serie | Intervalo | Base | Coeficiente |
> |---|---|---|---|
> | completa | $[-L,L]$ | $1,\cos\frac{n\pi x}{L},\operatorname{sen}\frac{n\pi x}{L}$ | $a_n,b_n=\frac1L\int_{-L}^{L}\!f\,(\cdot)\,dx$ |
> | senos | $[0,L]$ | $\operatorname{sen}\frac{n\pi x}{L}$ | $b_n=\frac2L\int_0^L\!f\operatorname{sen}\frac{n\pi x}{L}dx$ |
> | cosenos | $[0,L]$ | $1,\cos\frac{n\pi x}{L}$ | $a_n=\frac2L\int_0^L\!f\cos\frac{n\pi x}{L}dx$ |

> [!corolario]
> Toda función periódica razonable es una **suma de armónicos**, y la ortogonalidad de senos y cosenos hace que cada armónico se calcule con una integral independiente. Que la base sean senos o cosenos lo decide la simetría del problema (las condiciones de frontera); ese es el puente directo con la [[Tecnica de Separacion| separación de variables]].

> [!referencia]
> - La maquinaria de ortogonalidad subyacente: [[Funciones Ortogonales]].
> - En qué sentido converge la serie y el sobreimpulso: [[Convergencia y Gibbs]].
> - El balance de energía (norma): [[Identidad de Parseval]].
> - Visión global del método: [[Separacion de Variables y Fourier/index]].
