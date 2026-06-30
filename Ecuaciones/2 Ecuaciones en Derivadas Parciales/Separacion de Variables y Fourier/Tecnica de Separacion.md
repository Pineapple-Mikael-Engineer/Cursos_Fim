---
title: Técnica de Separación de Variables
order: 1
tags:
  - ecuaciones
  - edp
  - teoria
  - separacion-variables
  - fourier
draft: false
aliases:
  - separación de variables
  - método producto
  - separation of variables
  - product method
---

# Técnica de Separación de Variables

> [!definicion]
> La **separación de variables** busca soluciones de una EDP lineal con la forma de un **producto**
> $$u(x,t)=X(x)\,T(t),$$
> donde $X$ depende **solo** del espacio y $T$ **solo** del tiempo. Al sustituir en la EDP y dividir entre $XT$, los términos en $x$ y los términos en $t$ quedan en lados opuestos de una igualdad; como cada lado depende de una variable distinta, ambos deben igualar una misma **constante de separación** $-\lambda$. Eso parte la EDP en **dos EDO**. Las **condiciones de frontera homogéneas** solo admiten soluciones no triviales para ciertos valores $\lambda=\lambda_n$ (los **autovalores**), con **autofunciones** $X_n(x)$. La solución general es la **superposición**
> $$u(x,t)=\sum_{n} c_n\,X_n(x)\,T_n(t),$$
> y los coeficientes $c_n$ se fijan imponiendo la **condición inicial** mediante una serie de Fourier.

> [!info]
> Es el procedimiento central de [[Separacion de Variables y Fourier/index| esta sección]] y la herramienta maestra del capítulo de [[2 Ecuaciones en Derivadas Parciales/index| EDP]]. Su base teórica son las [[Funciones Ortogonales]] (para extraer los $c_n$) y las [[Series de Fourier]] (para el desarrollo del dato inicial). El problema de autovalores que aparece en el paso espacial es un caso de [[Sturm-Liouville/index| Sturm-Liouville]].

---

## Ejemplo

> [!ejemplo] La ecuación del calor en una barra con extremos fríos
> Resolvemos la difusión de calor en una barra de longitud $L$ con los extremos mantenidos a temperatura cero y un perfil inicial $f(x)$:
> $$u_t=\alpha^2 u_{xx},\qquad 0<x<L,\ t>0,$$
> $$u(0,t)=u(L,t)=0\ \ (\text{frontera}),\qquad u(x,0)=f(x)\ \ (\text{inicial}).$$
>
> **Paso 1 — proponer el producto y separar.** Sustituimos $u=X(x)T(t)$. Como $u_t=X T'$ y $u_{xx}=X'' T$, la EDP queda $X T'=\alpha^2 X'' T$. Dividimos entre $\alpha^2 X T$:
> $$\frac{T'}{\alpha^2 T}=\frac{X''}{X}=-\lambda.$$
> El lado izquierdo depende solo de $t$ y el derecho solo de $x$: para que coincidan **en todo** $(x,t)$, ambos deben ser una constante, que llamamos $-\lambda$ (el signo se elige por conveniencia).
>
> **Paso 2 — el problema espacial (autovalores).** De $\dfrac{X''}{X}=-\lambda$ obtenemos
> $$X''+\lambda X=0,\qquad X(0)=0,\ X(L)=0,$$
> donde las condiciones de frontera vienen de $u(0,t)=X(0)T(t)=0$ y $u(L,t)=X(L)T(t)=0$ (con $T\neq0$). Probemos los signos de $\lambda$:
> - Si $\lambda\le 0$, la solución general es combinación de exponenciales (o lineal si $\lambda=0$) y las dos condiciones $X(0)=X(L)=0$ fuerzan $X\equiv0$: **solución trivial**, inútil.
> - Si $\lambda>0$, escribimos $\lambda=\mu^2$ y $X=A\cos\mu x+B\operatorname{sen}\mu x$. La condición $X(0)=0$ da $A=0$; la condición $X(L)=B\operatorname{sen}\mu L=0$ exige (con $B\neq0$) $\operatorname{sen}\mu L=0$, es decir $\mu L=n\pi$.
>
> Esto **cuantiza** la constante: los autovalores y autofunciones son
> $$\boxed{\ \lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\qquad X_n(x)=\operatorname{sen}\frac{n\pi x}{L},\qquad n=1,2,3,\dots\ }$$
>
> **Paso 3 — el problema temporal.** Con $\lambda=\lambda_n$, la ecuación en $t$ es de primer orden:
> $$T'=-\alpha^2\lambda_n\,T\ \Longrightarrow\ T_n(t)=e^{-\alpha^2(n\pi/L)^2\,t}.$$
> Cada modo decae exponencialmente, y **más rápido** cuanto mayor es $n$ (los detalles finos del perfil se borran primero).
>
> **Paso 4 — superponer y ajustar la condición inicial.** Como la EDP es lineal y homogénea, cualquier combinación de soluciones producto es solución. Superponemos:
> $$u(x,t)=\sum_{n=1}^{\infty} b_n\,\operatorname{sen}\frac{n\pi x}{L}\;e^{-\alpha^2(n\pi/L)^2\,t}.$$
> Falta solo imponer $u(x,0)=f(x)$. En $t=0$ las exponenciales valen $1$, así que
> $$f(x)=\sum_{n=1}^{\infty} b_n\,\operatorname{sen}\frac{n\pi x}{L}.$$
> Esto es la **serie de senos** de $f$ en $[0,L]$. Por la ortogonalidad de los senos (ver [[Funciones Ortogonales]]) los coeficientes son
> $$\boxed{\ b_n=\frac{2}{L}\int_0^{L} f(x)\,\operatorname{sen}\frac{n\pi x}{L}\,dx.\ }$$
> Con eso la solución queda completamente determinada. Por ejemplo, si $f(x)=\operatorname{sen}\frac{\pi x}{L}$ ya es un solo modo: $b_1=1$, el resto $0$, y $u(x,t)=\operatorname{sen}\frac{\pi x}{L}\,e^{-\alpha^2(\pi/L)^2 t}$ simplemente decae sin cambiar de forma.

---

## En qué consiste

> [!teoria] La apuesta geométrica detrás del método
> Una EDP **acopla** espacio y tiempo: la evolución en $t$ depende de la forma en $x$ y viceversa. Separar variables **apuesta** a que existen soluciones especiales donde ese acoplamiento se **factoriza**, $u=X(x)T(t)$ —el perfil espacial conserva su forma y solo se reescala con un factor temporal—. Esas soluciones producto son los **modos normales** del sistema (como los modos de vibración de una cuerda). Aunque un dato inicial cualquiera **no** sea un solo modo, sí puede escribirse como **superposición** de modos; ahí entra Fourier. La linealidad es lo que permite sumar modos y seguir teniendo una solución.

> [!teorema] Por qué la separación obliga a una constante
> Si una identidad de la forma $G(t)=H(x)$ se cumple para **todo** $x$ del dominio y **todo** $t$, con $G$ función solo de $t$ y $H$ función solo de $x$, entonces ambas son **constantes**: existe $k$ tal que $G(t)=H(x)=k$ para todos los valores.

> [!demostracion]
> **Paso 1 — fijar una variable.** Tomemos un punto $x_0$ del dominio y dejémoslo fijo. Entonces, para todo $t$, $G(t)=H(x_0)$. Pero $H(x_0)$ es un **número** (no depende de $t$): luego $G(t)$ es ese mismo número para todo $t$, es decir $G$ es constante, $G\equiv k$. **Paso 2 — repetir con la otra.** Como $H(x)=G(t)=k$ para cualquier $t$, también $H(x)=k$ para todo $x$. Por tanto $G(t)=H(x)=k$, una constante común. $\blacksquare$

> [!algoritmo] Resolver una EDP lineal por separación de variables
> 1. **Proponer** $u(x,t)=X(x)T(t)$ y sustituir en la EDP.
> 2. **Separar**: reagrupa para dejar todo lo que depende de $x$ a un lado y todo lo de $t$ al otro; iguala cada lado a la constante $-\lambda$. Obtienes dos EDO.
> 3. **Resolver el problema de autovalores** (el lado con las condiciones de frontera homogéneas): halla los $\lambda_n$ que dan soluciones no triviales y sus autofunciones $X_n(x)$.
> 4. **Resolver la EDO temporal** para cada $\lambda_n$, obteniendo $T_n(t)$.
> 5. **Superponer**: $u=\sum_n c_n X_n(x)T_n(t)$.
> 6. **Ajustar la condición inicial** desarrollándola en serie de las $X_n$; los $c_n$ salen por ortogonalidad (Fourier).

> [!warning] Cuándo se puede separar
> El método **no** es universal. Requiere que se cumplan tres condiciones:
> - La EDP debe ser **lineal y homogénea** (para poder superponer modos y dividir por $XT$).
> - El **dominio** debe ser "separable": un rectángulo, una caja, un disco o una esfera, con bordes alineados a las coordenadas. En una región de forma arbitraria no funciona directamente.
> - Las **condiciones de frontera** que cuantizan deben ser **homogéneas** (iguales a cero). Si el dato de frontera no es nulo, primero se **homogeneiza** (restando una solución estacionaria) y luego se separa.

---

## Resumen

> [!resumen]
> | Paso | Acción | Resultado |
> |---|---|---|
> | Proponer | $u=X(x)T(t)$ | factoriza espacio y tiempo |
> | Separar | dividir entre $XT$ | dos EDO con constante $-\lambda$ |
> | Espacial | $X''+\lambda X=0$ + frontera | autovalores $\lambda_n$, autofunciones $X_n$ |
> | Temporal | EDO en $T$ con $\lambda_n$ | factores $T_n(t)$ |
> | Superponer | $u=\sum_n c_n X_n T_n$ | solución general |
> | Inicial | serie de Fourier de $f$ | coeficientes $c_n$ |

> [!corolario]
> Separar variables transforma **una** EDP en una **infinidad de EDO desacopladas**, una por modo $X_n$. Cada modo evoluciona en el tiempo de forma independiente; Fourier es lo que recombina esos modos para reproducir el dato inicial. Toda la dificultad se traslada al problema de autovalores y a la ortogonalidad de sus soluciones.

> [!referencia]
> - La extracción de coeficientes por ortogonalidad: [[Funciones Ortogonales]].
> - El desarrollo del dato inicial: [[Series de Fourier]].
> - El problema de autovalores que aparece en el paso 3: [[Sturm-Liouville/index]].
> - Visión global del método: [[Separacion de Variables y Fourier/index]].
