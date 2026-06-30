---
title: Operador Differintegral
order: 1
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - differintegral
draft: false
aliases:
  - differintegral
  - operador de orden arbitrario
  - media derivada
  - differintegral operator
---

# Operador Differintegral $D^{q}$

> [!definicion]
> El **differintegral** $D^{q}$ es un único operador de **orden arbitrario** $q\in\mathbb{R}$ que unifica derivar e integrar: $D^{1}$ deriva, $D^{2}$ deriva dos veces, $D^{-1}$ integra, $D^{-2}$ integra dos veces. Para órdenes **no enteros** interpola con continuidad entre ellos. Sobre potencias obedece una regla limpia (Gamma en lugar de factorial):
> $$D^{q}\,x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1-q)}\,x^{\mu-q}.$$

> [!info]
> La idea fundacional del [[Calculo Fraccionario/index| cálculo fraccionario]]. Lo concreto (cómo se define $D^q$ por una integral) está en la [[Integral de Riemann-Liouville| integral de Riemann-Liouville]] y sus derivadas ([[Derivada de Caputo| Caputo]] y compañía). Aquí se fija la **intuición**: el orden de derivación es una **perilla continua**.

---

## Ejemplo

> [!ejemplo] La perilla del orden, aplicada a $f(x)=x$
> ![[differintegral.svg|480]]
>
> Con la regla de las potencias sobre $f(x)=x$ (es decir $\mu=1$), $D^{q}x=\dfrac{\Gamma(2)}{\Gamma(2-q)}x^{1-q}=\dfrac{x^{1-q}}{\Gamma(2-q)}$:
> | $q$ | $D^{q}x$ | interpretación |
> |:--:|:--|:--|
> | $-1$ | $\dfrac{x^{2}}{2}$ | **integral** de $x$ |
> | $0$ | $x$ | la **función** |
> | $\tfrac12$ | $\dfrac{2}{\sqrt{\pi}}\,x^{1/2}$ | **media derivada** |
> | $1$ | $1$ | **derivada** |
> | $\tfrac32$ | $\dfrac{1}{\sqrt{\pi}}\,x^{-1/2}$ | derivada y media |
> | $2$ | $0$ | **segunda derivada** ($\Gamma(0)=\infty$) |
>
> Al deslizar $q$ de $-1$ a $2$, la curva se transforma **suavemente** de la parábola (integral) a la recta, de ahí a la constante y, finalmente, a cero. Derivar e integrar son los extremos de un mismo camino.

---

## En qué consiste

> [!teorema] Propiedad de semigrupo (la media derivada)
> El differintegral compone los órdenes: $D^{q}\,D^{p}=D^{q+p}$ (en condiciones de regularidad adecuadas). En particular, **dos medias derivadas hacen una derivada entera**:
> $$D^{1/2}\,D^{1/2}=D^{1}=\frac{d}{dx}.$$

> [!demostracion] Sobre potencias
> **Paso 1 — aplicar dos veces la regla.** $D^{p}x^{\mu}=\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1-p)}x^{\mu-p}$; aplicando ahora $D^{q}$ a $x^{\mu-p}$:
> $$D^{q}D^{p}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1-p)}\cdot\frac{\Gamma(\mu-p+1)}{\Gamma(\mu-p+1-q)}\,x^{\mu-p-q}.$$
> **Paso 2 — telescopio de Gammas.** El factor $\Gamma(\mu+1-p)=\Gamma(\mu-p+1)$ se cancela, dejando $\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1-(p+q))}x^{\mu-(p+q)}=D^{p+q}x^{\mu}$. $\blacksquare$ Es la misma estructura por la que, en el [[Problema de Abel| problema de Abel]], convolucionar el núcleo $1/\sqrt{x}$ consigo mismo da una constante: **media integración** repetida = una integración.

> [!info] De dónde sale (la fórmula de Cauchy)
> La integral iterada $n$ veces es $I^{n}f(x)=\dfrac{1}{(n-1)!}\displaystyle\int_0^x(x-t)^{n-1}f(t)\,dt$. Sustituir $(n-1)!\to\Gamma(\alpha)$ y permitir $\alpha$ real define $I^{\alpha}$ (ver [[Integral de Riemann-Liouville| Riemann-Liouville]]); el differintegral $D^{q}$ es $I^{-q}$ para $q<0$, y para $q>0$ es una integral fraccionaria seguida de derivadas enteras.

> [!warning] No es local
> A diferencia de la derivada clásica (que solo "mira" un entorno del punto), el differintegral de orden no entero es **no local**: $D^{q}f(x)$ depende de **todos** los valores de $f$ en $[0,x]$ —es, en el fondo, una **integral con memoria**—. Por eso modela sistemas con historia.

## Resumen

> [!resumen]
> | $q$ | Operación |
> |:--:|:--|
> | $q=n>0$ entero | $n$-ésima derivada |
> | $q=-n<0$ entero | $n$ integraciones |
> | $q$ no entero | derivada/integral **fraccionaria** (no local) |
> | regla potencias | $D^{q}x^\mu=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1-q)}x^{\mu-q}$ |
> | semigrupo | $D^{q}D^{p}=D^{q+p}$ |

> [!corolario]
> El differintegral convierte el "orden de derivación" en un **parámetro continuo**. Esa simple idea —cambiar el factorial por la Gamma— abre un cálculo entero donde derivar e integrar son el mismo gesto a distintas alturas de una perilla, y donde la **no localidad** codifica memoria.

> [!referencia]
> - La definición concreta: [[Integral de Riemann-Liouville]].
> - Las variantes derivada: [[Derivada de Riemann-Liouville]], [[Derivada de Caputo]].
> - El medio-cálculo histórico: [[Problema de Abel]].
