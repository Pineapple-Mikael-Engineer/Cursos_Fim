---
title: Valores Característicos de una Onda
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
draft: false
aliases:
  - valores característicos
  - valor medio
  - componente continua
  - valor eficaz
  - valor RMS
  - factor de forma
  - factor de cresta
  - factor de pico
---

# Valores Característicos de una Onda

> [!definicion]
> Una onda periódica se caracteriza por cuatro magnitudes y dos factores adimensionales:
> - **Valor de pico** $V_m$: la amplitud máxima.
> - **Valor medio** $V_{med}=\dfrac1T\int_0^T v\,dt$: su componente continua (DC); para la senoide
>   completa es **cero**, por lo que se toma sobre la onda **rectificada**.
> - **Valor eficaz** o **RMS** $V=\sqrt{\dfrac1T\int_0^T v^2\,dt}$: la continua que disiparía la misma
>   potencia; para la senoide, $V_m/\sqrt2$.
> - **Factor de forma** $F_f=\dfrac{V}{V_{med}}$ y **factor de cresta** $F_c=\dfrac{V_m}{V}$, que
>   relacionan los anteriores y describen la **forma** de la onda, no su tamaño.

> [!info]
> El núcleo cuantitativo de las [[4 Ondas Periodicas Sinusoidales/index | ondas periódicas]]: con estos
> valores se mide, se factura y se dimensiona en CA. El **eficaz** es el que portan los [[Fasores]] y el
> que fija la [[Potencia en Regimen Sinusoidal | potencia]]. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Los valores característicos de la senoide.**
>
> Para $v(t)=V_m\operatorname{sen}\omega t$, hallar valor medio, eficaz y los dos factores.
>
> ![[valor_eficaz.svg|560]]
>
> *El valor eficaz es la raíz del **valor medio de $v^2$**. Como la media de $\operatorname{sen}^2$ es
> $1/2$, resulta $V=V_m/\sqrt2$: la continua que calienta igual.*
>
> **Valor eficaz.** Con $\operatorname{sen}^2\omega t=\tfrac12(1-\cos2\omega t)$, la media de $v^2$ es
> $V_m^2/2$, luego
> $$V=\sqrt{\overline{v^2}}=\frac{V_m}{\sqrt2}\approx0{,}707\,V_m.$$
>
> **Valor medio** (de la **rectificada** de onda completa; el de la senoide completa es $0$):
> $$V_{med}=\frac1\pi\int_0^\pi V_m\operatorname{sen}\theta\,d\theta=\frac{2V_m}{\pi}\approx0{,}637\,V_m.$$
>
> **Factores.**
> $$F_f=\frac{V}{V_{med}}=\frac{V_m/\sqrt2}{2V_m/\pi}=\frac{\pi}{2\sqrt2}\approx1{,}11,\qquad F_c=\frac{V_m}{V}=\sqrt2\approx1{,}41.$$
>
> > [!solucion]
> > $V_{med}=2V_m/\pi$, $V=V_m/\sqrt2$, $F_f\approx1{,}11$, $F_c\approx1{,}41$. Los factores son
> > **constantes universales** de la forma senoidal: no dependen de amplitud ni frecuencia.

---

## En qué consiste

> [!teoria] Valor medio: la componente DC
> El valor medio es el "nivel" constante alrededor del que oscila la onda —su **componente continua**—.
> Para ondas **simétricas respecto al eje** (la senoide pura) es **cero**: cada valor positivo tiene su
> simétrico negativo y las áreas se cancelan. Por eso, para un valor medio útil en CA, primero se
> **rectifica**:
>
> ![[valor_medio.svg|560]]
>
> *Arriba: la senoide completa promedia cero (áreas $+$ y $-$ se cancelan). Abajo: la rectificada de
> onda completa promedia $2V_m/\pi$.*
>
> - **Rectificada de onda completa** (invierte el semiciclo negativo): $V_{med}=2V_m/\pi\approx0{,}637\,V_m$.
> - **Rectificada de media onda** (anula el semiciclo negativo): $V_{med}=V_m/\pi$, la mitad.
>
> Es lo que mide un instrumento de **bobina móvil**, cuyo par responde al valor medio de la corriente.

> [!teoria] Valor eficaz: "el que calienta igual"
> La potencia en una resistencia es $p=v^2/R$, **cuadrática**; su media es $\overline{v^2}/R$. Si se
> define $V^2=\overline{v^2}$, entonces $\overline{p}=V^2/R$, **idéntica** a la de una continua de valor
> $V$. Por eso el eficaz es el **equivalente energético** de la onda, y el nombre RMS describe el
> cálculo: **R**aíz de la **M**edia del **C**uadrado. Toda la ingeniería de potencia se expresa en
> eficaces: "$230\ \text{V}$" de la red es eficaz (pico $230\sqrt2\approx325\ \text{V}$).

> [!proposicion] El factor $1/\sqrt2$ es solo de la senoide
> El cociente $V/V_m$ **depende de la forma**: senoide $1/\sqrt2\approx0{,}707$; **cuadrada** $1$
> ($V=V_m$); **triangular** $1/\sqrt3$. No aplicar $V_m/\sqrt2$ a ondas no senoidales.

> [!teoria] Los factores: la "huella" de la forma
> Los factores son adimensionales y dependen **solo de la forma**, no de la amplitud:
> - **Factor de forma** $F_f=V/V_{med}$: cuánto se aparta la onda de una continua. La **cuadrada** tiene
>   $F_f=1$ (mínimo); cuanto más **picuda**, mayor.
> - **Factor de cresta** $F_c=V_m/V$: el **pico** frente al eficaz. Es el que fija la tensión que un
>   **aislamiento** debe soportar y advierte de la **saturación** (núcleos, amplificadores).
>
> | Forma | $V_{med}$ (rect.) | $V$ (eficaz) | $F_f=V/V_{med}$ | $F_c=V_m/V$ |
> |:---|:---:|:---:|:---:|:---:|
> | Cuadrada | $V_m$ | $V_m$ | $1$ | $1$ |
> | Senoidal | $2V_m/\pi$ | $V_m/\sqrt2$ | $\pi/(2\sqrt2)\approx1{,}11$ | $\sqrt2\approx1{,}41$ |
> | Triangular | $V_m/2$ | $V_m/\sqrt3$ | $2/\sqrt3\approx1{,}15$ | $\sqrt3\approx1{,}73$ |

> [!warning]
> El **medio** no es el **eficaz**: el medio de una senoide completa es $0$, su eficaz $V_m/\sqrt2\neq0$.
> El factor de forma usa el medio **rectificado** (dividir por el de la onda completa sería dividir por
> cero). Y el $1/\sqrt2$ es **exclusivo de la senoide**: otras formas tienen el suyo.

## Resumen

> [!resumen]
> | Magnitud | Definición | Senoide |
> |:---|:---|:---:|
> | Pico | $V_m$ | $V_m$ |
> | Medio (rect.) | $\dfrac1T\int_0^T v\,dt$ | $2V_m/\pi\approx0{,}637\,V_m$ |
> | Eficaz (RMS) | $\sqrt{\dfrac1T\int_0^T v^2\,dt}$ | $V_m/\sqrt2\approx0{,}707\,V_m$ |
> | Factor de forma | $F_f=V/V_{med}$ | $\approx1{,}11$ |
> | Factor de cresta | $F_c=V_m/V$ | $\approx1{,}41$ |

> [!corolario]
> Cuatro valores (pico, medio, eficaz) y dos factores (forma, cresta) condensan toda la información
> cuantitativa de una onda: conocidos dos, se recuperan los demás salvo la amplitud. De todos, el
> **eficaz** es el rey: es el que calienta, el que se mide, el que portan los fasores y el que fija la
> potencia.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Se define sobre la [[Onda Sinusoidal]]; el eficaz lo usan los [[Fasores]] y
> la [[Potencia en Regimen Sinusoidal | potencia]]. Cierra los descriptores de las [[4 Ondas Periodicas Sinusoidales/index | ondas periódicas]].
