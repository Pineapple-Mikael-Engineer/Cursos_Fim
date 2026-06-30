---
title: Funciones Ortogonales
order: 2
tags:
  - ecuaciones
  - edp
  - teoria
  - fourier
  - ortogonalidad
draft: false
aliases:
  - funciones ortogonales
  - producto interno de funciones
  - base ortogonal
  - orthogonal functions
  - inner product
---

# Funciones Ortogonales

> [!definicion]
> En un espacio de funciones sobre $[a,b]$, el **producto interno** con función **peso** $w(x)>0$ es
> $$\langle f,g\rangle=\int_a^b f(x)\,g(x)\,w(x)\,dx.$$
> Un conjunto $\{\varphi_n\}$ es **ortogonal** (respecto de ese peso) si
> $$\langle \varphi_n,\varphi_m\rangle=0\quad\text{para todo}\ n\neq m,$$
> y es **ortonormal** si además cada función está normalizada, $\langle\varphi_n,\varphi_n\rangle=1$. La cantidad $\|\varphi_n\|^2=\langle\varphi_n,\varphi_n\rangle$ es la **norma al cuadrado** de la función. La idea es **trasladar la geometría de los vectores** (producto punto, ortogonalidad, proyección) al mundo de las funciones.

> [!info]
> Es la base teórica que hace **calculables** los coeficientes de una [[Series de Fourier| serie de Fourier]] y de cualquier [[Desarrollo en Autofunciones| desarrollo en autofunciones]]. Las autofunciones de un problema de [[Sturm-Liouville/index| Sturm-Liouville]] forman precisamente un conjunto ortogonal con un peso $w$, y por eso la separación de variables siempre conduce a este tipo de desarrollo. Nota de [[Separacion de Variables y Fourier/index| esta sección]].

---

## Ejemplo

> [!ejemplo] Verificar la ortogonalidad de los senos y proyectar una función
> Tomemos el conjunto $\varphi_n(x)=\operatorname{sen}\dfrac{n\pi x}{L}$ en $[0,L]$ con peso $w=1$.
>
> **Paso 1 — calcular el producto interno.** Usando la identidad $\operatorname{sen}A\,\operatorname{sen}B=\tfrac12[\cos(A-B)-\cos(A+B)]$,
> $$\langle\varphi_n,\varphi_m\rangle=\int_0^L \operatorname{sen}\frac{n\pi x}{L}\,\operatorname{sen}\frac{m\pi x}{L}\,dx
> =\frac12\int_0^L\!\Big[\cos\frac{(n-m)\pi x}{L}-\cos\frac{(n+m)\pi x}{L}\Big]dx.$$
> Si $n\neq m$, ambos cosenos tienen periodo entero en $[0,L]$ y sus integrales se anulan: el producto es $0$. Si $n=m$, el primer coseno es $\cos 0=1$ y aporta $\tfrac12\cdot L$, mientras el segundo se anula. Por tanto
> $$\langle\varphi_n,\varphi_m\rangle=\frac{L}{2}\,\delta_{nm}.$$
> El conjunto es **ortogonal**, con norma al cuadrado $\|\varphi_n\|^2=L/2$.
>
> **Paso 2 — proyectar una función.** Supongamos que $f(x)=3\operatorname{sen}\frac{\pi x}{L}-5\operatorname{sen}\frac{4\pi x}{L}$ y queremos recuperar sus coeficientes "sin saberlos". Para el modo $n$,
> $$c_n=\frac{\langle f,\varphi_n\rangle}{\langle\varphi_n,\varphi_n\rangle}
> =\frac{2}{L}\int_0^L f(x)\,\operatorname{sen}\frac{n\pi x}{L}\,dx.$$
> Al integrar, la ortogonalidad mata todos los productos cruzados: solo sobrevive el término que tiene el **mismo** $n$. Sale $c_1=3$, $c_4=-5$ y todos los demás $0$, justo como esperábamos. La ortogonalidad es lo que permite "extraer" cada componente por separado.

---

## En qué consiste

> [!teoria] La analogía con los vectores
> En $\mathbb{R}^3$, una base ortonormal $\{\hat e_1,\hat e_2,\hat e_3\}$ permite descomponer cualquier vector como $\vec v=\sum_i (\vec v\cdot\hat e_i)\,\hat e_i$: cada componente se obtiene **proyectando** con el producto punto. Las funciones ortogonales reproducen esa imagen exactamente, cambiando el producto punto $\vec v\cdot\vec w$ por el producto interno $\langle f,g\rangle=\int f g\,w\,dx$. Una función se piensa como un "vector con infinitas componentes" y el conjunto $\{\varphi_n\}$ como una **base** del espacio. El peso $w$ es solo una forma de "ponderar" qué tanto cuenta cada región del intervalo al medir ángulos y longitudes.

> [!teorema] Cálculo de coeficientes por proyección
> Si una función se desarrolla como $f=\sum_n c_n\varphi_n$ sobre un conjunto **ortogonal** $\{\varphi_n\}$, entonces cada coeficiente está dado por la **proyección**
> $$c_n=\frac{\langle f,\varphi_n\rangle}{\langle\varphi_n,\varphi_n\rangle}.$$

> [!demostracion]
> **Paso 1 — tomar producto interno con $\varphi_m$.** Aplicamos $\langle\,\cdot\,,\varphi_m\rangle$ a ambos lados de $f=\sum_n c_n\varphi_n$ y usamos la linealidad del producto interno:
> $$\langle f,\varphi_m\rangle=\Big\langle \sum_n c_n\varphi_n,\ \varphi_m\Big\rangle=\sum_n c_n\,\langle\varphi_n,\varphi_m\rangle.$$
> **Paso 2 — usar la ortogonalidad.** En esa suma, $\langle\varphi_n,\varphi_m\rangle=0$ salvo cuando $n=m$. Sobrevive un único término:
> $$\langle f,\varphi_m\rangle=c_m\,\langle\varphi_m,\varphi_m\rangle.$$
> **Paso 3 — despejar.** Como $\langle\varphi_m,\varphi_m\rangle=\|\varphi_m\|^2\neq0$,
> $$c_m=\frac{\langle f,\varphi_m\rangle}{\langle\varphi_m,\varphi_m\rangle}. \qquad\blacksquare$$

> [!teoria] Por qué la suma parcial es la mejor aproximación
> Fijado $N$, ¿qué combinación $\sum_{n\le N} a_n\varphi_n$ se acerca **más** a $f$? Si medimos el error con la norma cuadrática $\big\|f-\sum_{n\le N} a_n\varphi_n\big\|^2$, la elección óptima es precisamente $a_n=c_n$, los coeficientes de proyección. La razón es geométrica: la suma parcial $\sum_{n\le N} c_n\varphi_n$ es la **proyección ortogonal** de $f$ sobre el subespacio generado por $\{\varphi_1,\dots,\varphi_N\}$, y la proyección es, por definición, el punto del subespacio más cercano a $f$. El error $f-\sum c_n\varphi_n$ queda **perpendicular** a todo el subespacio. Es el mismo hecho que dice que el punto de un plano más próximo a un punto exterior es el pie de la perpendicular.

> [!proposicion] Conjuntos ortogonales que aparecen una y otra vez
> | Conjunto | Intervalo | Peso $w$ | Dónde aparece |
> |---|---|:--:|---|
> | $\{\operatorname{sen}\frac{n\pi x}{L}\}$ | $[0,L]$ | $1$ | calor/onda con extremos fijos (serie de senos) |
> | $\{1,\cos\frac{n\pi x}{L},\operatorname{sen}\frac{n\pi x}{L}\}$ | $[-L,L]$ | $1$ | serie de Fourier completa |
> | Polinomios de **Legendre** $P_n$ | $[-1,1]$ | $1$ | Laplace en la esfera |
> | Polinomios de **Hermite** $H_n$ | $(-\infty,\infty)$ | $e^{-x^2}$ | oscilador cuántico |
> | Autofunciones de [[Sturm-Liouville/index\|Sturm-Liouville]] | $[a,b]$ | $w(x)$ | caso general |

---

## Resumen

> [!resumen]
> | Concepto | Vectores en $\mathbb{R}^n$ | Funciones |
> |---|---|---|
> | producto | $\vec v\cdot\vec w$ | $\langle f,g\rangle=\int_a^b fg\,w\,dx$ |
> | ortogonalidad | $\vec v\cdot\vec w=0$ | $\langle\varphi_n,\varphi_m\rangle=0,\ n\neq m$ |
> | norma | $\lvert\vec v\rvert$ | $\|f\|=\sqrt{\langle f,f\rangle}$ |
> | coeficiente | $v_i=\vec v\cdot\hat e_i$ | $c_n=\langle f,\varphi_n\rangle/\|\varphi_n\|^2$ |

> [!corolario]
> La ortogonalidad es la propiedad que vuelve **triviales** los coeficientes de un desarrollo: en lugar de resolver un sistema acoplado de infinitas incógnitas, cada $c_n$ se obtiene con **una** integral independiente. Sin ortogonalidad, las series de Fourier serían prácticamente incalculables.

> [!referencia]
> - El caso concreto de senos y cosenos: [[Series de Fourier]].
> - La generalización a autofunciones con peso: [[Desarrollo en Autofunciones]] y [[Sturm-Liouville/index]].
> - Cómo se usa al ajustar el dato inicial: [[Separacion de Variables y Fourier/index]].
