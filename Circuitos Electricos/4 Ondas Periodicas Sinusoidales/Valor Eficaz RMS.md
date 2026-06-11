---
title: Valor Eficaz (RMS)
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
  - valor-eficaz
draft: false
aliases:
  - valor eficaz
  - valor RMS
  - valor eficaz RMS
  - RMS value
---

# Valor Eficaz (RMS) $\;V_{ef}=\dfrac{V_m}{\sqrt2}$

> [!definicion]
> El **valor eficaz** (o **RMS**, *root mean square*) de una onda es la **raíz del valor medio de su
> cuadrado**:
> $$V_{ef}=\sqrt{\frac{1}{T}\int_0^{T} v^2(t)\,dt}.$$
> Es el valor de una **corriente continua que disiparía la misma potencia** en una resistencia. Para
> una senoide vale $V_{ef}=V_m/\sqrt2\approx0{,}707\,V_m$. Es **el** valor que importa en CA: cuando se
> dice "$220\ \text{V}$" de la red, es un valor eficaz.

> [!info]
> El valor más importante de las [[4 Ondas Periodicas Sinusoidales/index| ondas sinusoidales]]: el que
> fija la **potencia**. Se compara con el [[Valor Medio]] (vía el [[Factor de Forma y Cresta| factor de forma]]) y es la magnitud que llevan los [[Fasores| fasores]] del capítulo
> siguiente. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **El valor eficaz de una senoide.**
>
> Hallar el valor eficaz de $v(t)=V_m\operatorname{sen}\omega t$ y la potencia que entrega a una
> resistencia $R$.
>
> ![[valor_eficaz.svg|600]]
>
> *El valor eficaz $V_{ef}$ es la raíz del **valor medio de $v^2$**. Como la media de
> $\operatorname{sen}^2$ es $1/2$, resulta $V_{ef}=V_m/\sqrt2$: la DC que calienta igual.*
>
> **Paso 1 — Media del cuadrado.** Usando $\operatorname{sen}^2\omega t=\dfrac{1-\cos2\omega t}{2}$, su
> promedio en un período es $\dfrac12$ (el término $\cos2\omega t$ promedia cero):
> $$\overline{v^2}=\frac{1}{T}\int_0^T V_m^2\operatorname{sen}^2\omega t\,dt=\frac{V_m^2}{2}.$$
>
> **Paso 2 — Raíz.**
> $$V_{ef}=\sqrt{\overline{v^2}}=\sqrt{\frac{V_m^2}{2}}=\frac{V_m}{\sqrt2}\approx0{,}707\,V_m.$$
>
> > [!solucion]
> > $V_{ef}=V_m/\sqrt2$. La potencia media en $R$ es $P=\dfrac{V_{ef}^2}{R}=\dfrac{V_m^2}{2R}$, **igual**
> > que la de una continua de valor $V_{ef}$. Para la red, $V_{ef}=220\ \text{V}$ ⇒ pico
> > $V_m=220\sqrt2\approx311\ \text{V}$.

---

## En qué consiste

> [!teoria] Por qué "el que calienta igual"
> La potencia instantánea en una resistencia es $p=v^2/R$, **cuadrática** en la tensión. Su promedio en
> un período es $\overline{p}=\overline{v^2}/R$. Si se define $V_{ef}^2=\overline{v^2}$, entonces
> $$\overline{p}=\frac{V_{ef}^2}{R},$$
> idéntica a la potencia de una continua de valor $V_{ef}$. Por eso el valor eficaz es el **equivalente
> energético** de la onda: la DC que produce el mismo calor. El nombre RMS describe el cálculo al revés:
> **R**aíz de la **M**edia del **C**uadrado (*root–mean–square*).

> [!proposicion] Factor $1/\sqrt2$ solo para la senoide
> El cociente $V_{ef}/V_m$ **depende de la forma** de la onda. Para la **senoide** es $1/\sqrt2\approx
> 0{,}707$; para una **onda cuadrada** (de amplitud $V_m$) es $1$ ($V_{ef}=V_m$); para una **triangular**,
> $1/\sqrt3$. No aplicar $V_m/\sqrt2$ a ondas no senoidales.

> [!info] Por qué se usa en CA
> Toda la ingeniería de potencia se expresa en valores eficaces: las tensiones nominales
> ($230\ \text{V}$, $400\ \text{V}$…), las corrientes de los conductores, las potencias. La razón es
> justamente que el valor eficaz es el que determina el **calentamiento** y la **potencia**, no el pico
> ni el medio.

> [!warning]
> El valor eficaz **no** es el valor medio: el medio de una senoide completa es $0$, pero su eficaz es
> $V_m/\sqrt2\neq0$. Y el factor $1/\sqrt2$ es **exclusivo de la senoide**; otras formas tienen el suyo
> ([[Factor de Forma y Cresta]]).

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Definición | $V_{ef}=\sqrt{\overline{v^2}}$ |
> | Senoide | $V_{ef}=V_m/\sqrt2\approx0{,}707\,V_m$ |
> | Potencia media en $R$ | $P=V_{ef}^2/R$ |
> | Onda cuadrada / triangular | $V_m$ / $V_m/\sqrt3$ |
> | Red ($V_{ef}=220$ V) | pico $V_m=220\sqrt2\approx311$ V |

> [!corolario]
> El valor eficaz traduce una onda variable a la continua energéticamente equivalente. Es la magnitud
> que se mide, se factura y se calcula en CA, y la que portarán los fasores: por eso $V_{ef}=V_m/\sqrt2$
> es, quizá, la fórmula más usada del análisis sinusoidal.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Se compara con [[Valor Medio]] vía [[Factor de Forma y Cresta]]. Lo usan
> los [[Fasores| fasores]] y toda la [[Potencia en Regimen Sinusoidal| potencia en CA]].
