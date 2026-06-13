---
title: Generación de Tensión Alterna
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
draft: false
aliases:
  - generación de tensión alterna
  - generación de corriente alterna
  - alternador
  - AC voltage generation
  - alternator
---

# Generación de Tensión Alterna $\;e=E_m\operatorname{sen}(\omega t)$

> [!definicion]
> Una **tensión alterna sinusoidal** se genera haciendo **girar uniformemente** una espira (o bobina)
> dentro de un **campo magnético**: ese es el principio del **alternador**. Por la **ley de Faraday**,
> la fem inducida resulta
> $$e(t)=E_m\operatorname{sen}(\omega t),\qquad E_m=N\,B\,A\,\omega,$$
> con $N$ el número de espiras, $B$ el campo magnético, $A$ el área de la espira y $\omega$ su velocidad
> angular de giro. En el fondo, **la senoide es la proyección de un giro uniforme** sobre un eje fijo.

> [!info]
> Es el **origen físico** de la [[Onda Sinusoidal]] dentro de las
> [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas sinusoidales]]: explica de dónde nace la
> forma $\operatorname{sen}(\omega t)$ en los circuitos de CA. La idea del **vector que gira** es,
> además, la semilla de la [[Fasores| representación fasorial]]; el valor de pico
> $E_m$ se relaciona con su [[Valores Caracteristicos]] por $E_m/\sqrt2$. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Alternador elemental.**
>
> Una espira de $N=100$ vueltas y área $A=0{,}02\ \text{m}^2$ gira a $\omega=314\ \text{rad/s}$
> (es decir, $f=50\ \text{Hz}$) dentro de un campo magnético $B=0{,}5\ \text{T}$. Hallar la fem inducida
> $e(t)$.
>
> ![[generacion_alterna.svg|620]]
>
> *La senoide es la proyección de una rotación uniforme: al girar la espira un ángulo $\omega t$, la fem
> inducida traza $e=E_m\operatorname{sen}\omega t$.*
>
> **Paso 1 — Valor de pico de la fem.** Aplicando $E_m=N B A\,\omega$:
> $$E_m=100\cdot 0{,}5\cdot 0{,}02\cdot 314\approx 314\ \text{V}.$$
>
> **Paso 2 — Expresión temporal.** Como el giro es uniforme y arranca con el plano de la espira
> perpendicular a $B$ (flujo máximo, fem nula), la fem queda
> $$e(t)=314\operatorname{sen}(314\,t)\ \text{V}.$$
>
> **Paso 3 — Valor eficaz.** La red trabaja con el [[Valores Caracteristicos]]:
> $E=E_m/\sqrt2\approx 314/\sqrt2\approx 222\ \text{V}$.
>
> > [!solucion]
> > $E_m\approx 314\ \text{V}$ y $e(t)=314\operatorname{sen}(314\,t)\ \text{V}$, con valor eficaz
> > $E_m/\sqrt2\approx 222\ \text{V}$ y frecuencia $f=50\ \text{Hz}$.

---

## En qué consiste

> [!teorema] Fem inducida en una espira giratoria (ley de Faraday)
> Una espira de $N$ vueltas y área $A$ que gira con velocidad angular $\omega$ uniforme en un campo
> magnético uniforme $B$ desarrolla una fem sinusoidal
> $$e(t)=E_m\operatorname{sen}(\omega t),\qquad E_m=N B A\,\omega.$$

> [!demostracion]
> El **flujo magnético** concatenado por la espira depende del ángulo $\omega t$ entre la normal al
> plano de la espira y el campo $B$. Es máximo cuando el plano es perpendicular a $B$ (normal paralela)
> y nulo cuando el plano contiene a $B$:
>
> **Paso 1 — Flujo concatenado.**
> $$\phi(t)=N B A\cos(\omega t).$$
>
> **Paso 2 — Ley de Faraday.** La fem inducida es la variación temporal del flujo (con signo de Lenz):
> $$e=-\frac{d\phi}{dt}=-\frac{d}{dt}\big[N B A\cos(\omega t)\big].$$
>
> **Paso 3 — Derivar.** Como $\dfrac{d}{dt}\cos(\omega t)=-\omega\operatorname{sen}(\omega t)$,
> $$e=N B A\,\omega\operatorname{sen}(\omega t)=E_m\operatorname{sen}(\omega t),\qquad E_m=N B A\,\omega.$$
> $\blacksquare$

> [!teoria] La senoide como proyección de un vector giratorio
> La forma $e=E_m\operatorname{sen}(\omega t)$ no es casual: es la **proyección sobre un eje** de un
> vector de módulo $E_m$ que gira con velocidad angular $\omega$ constante. A cada instante, el ángulo
> recorrido es $\omega t$ y su proyección vertical vale $E_m\operatorname{sen}(\omega t)$. Esta imagen
> conecta de forma directa con los [[Fasores| fasores]]: el fasor es ese mismo vector
> giratorio "congelado" en un instante, conservando módulo $E_m$ y ángulo de fase. La **frecuencia de
> la red** ($50\ \text{Hz}$ en Europa, $60\ \text{Hz}$ en América) la fija la **velocidad de giro** del
> alternador, ya que $\omega=2\pi f$.

> [!warning]
> $E_m=N B A\,\omega$ **crece con la velocidad de giro** $\omega$: a mayor rapidez del alternador, mayor
> tensión de pico (y mayor frecuencia, ligadas por el mismo $\omega$). No confundir la **fem de pico**
> $E_m$ con su **valor eficaz** $E_m/\sqrt2$: la red de $220\ \text{V}$ tiene un pico de
> $220\sqrt2\approx 311\ \text{V}$.

## Resumen

> [!resumen]
> | Magnitud | Expresión | Comentario |
> |:---|:---|:---|
> | Flujo concatenado | $\phi=N B A\cos\omega t$ | máximo con el plano $\perp B$ |
> | Fem inducida | $e=E_m\operatorname{sen}\omega t$ | $e=-\,d\phi/dt$ |
> | Fem de pico | $E_m=N B A\,\omega$ | crece con $\omega$ |
> | Frecuencia | $f=\omega/2\pi$ | la fija el giro del alternador |
> | Valor eficaz | $E=E_m/\sqrt2$ | el que mide la red |

> [!corolario]
> Hacer girar una espira en un campo magnético produce, por Faraday, una fem **exactamente sinusoidal**:
> la senoide de los circuitos de CA es la huella de un giro uniforme. Ese mismo giro, visto como vector,
> es lo que justifica representar las tensiones alternas mediante [[Fasores| fasores]].

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Forma de onda: [[Onda Sinusoidal]]. Valor de pico vs. eficaz:
> [[Valores Caracteristicos]]. Representación compacta: [[Fasores]]. Contexto:
> [[4 Ondas Periodicas Sinusoidales/index]].
