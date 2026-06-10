---
title: Factor de Forma y Factor de Cresta
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
  - factor-de-forma
  - factor-de-cresta
draft: false
aliases:
  - factor de forma
  - factor de cresta
  - factor de pico
  - form factor
  - crest factor
  - peak factor
---

# Factor de Forma y Cresta $\;F_f=\dfrac{V_{ef}}{V_{med}}\,,\;\;F_c=\dfrac{V_m}{V_{ef}}$

> [!definicion]
> Dos números **adimensionales** que describen la **forma** de una onda periódica, no su amplitud:
> - **Factor de forma** $F_f=\dfrac{V_{ef}}{V_{med}}$: cociente entre el [[Valor Eficaz RMS| valor eficaz]] y el [[Valor Medio| valor medio]] de la onda **rectificada**.
> - **Factor de cresta** (o de **pico**) $F_c=\dfrac{V_m}{V_{ef}}$: cociente entre el **valor de pico**
>   $V_m$ y el valor eficaz.
>
> Para una **senoide**: $F_f=\dfrac{\pi}{2\sqrt2}\approx1{,}11$ y $F_c=\sqrt2\approx1{,}414$.

> [!info]
> Cierran la caracterización de las [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas]]
> relacionando entre sí sus tres descriptores: el [[Valor Medio]], el [[Valor Eficaz RMS| valor eficaz]]
> y el valor de pico de la [[Onda Sinusoidal]]. Conocidos dos factores se reconstruyen los demás valores
> salvo la amplitud. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Los dos factores de una senoide.**
>
> Calcular el factor de forma y el factor de cresta de $v(t)=V_m\operatorname{sen}\omega t$, partiendo de
> sus valores característicos $V_{ef}=V_m/\sqrt2$ y $V_{med}=2V_m/\pi$ (este último, el de la onda
> **rectificada**, pues el de la senoide completa es cero).
>
> **Paso 1 — Factor de forma.** Cociente eficaz / medio rectificado:
> $$F_f=\frac{V_{ef}}{V_{med}}=\frac{V_m/\sqrt2}{2V_m/\pi}=\frac{\pi}{2\sqrt2}\approx1{,}111.$$
> La amplitud $V_m$ se **cancela**: el factor no depende de cuán grande sea la onda.
>
> **Paso 2 — Factor de cresta.** Cociente pico / eficaz:
> $$F_c=\frac{V_m}{V_{ef}}=\frac{V_m}{V_m/\sqrt2}=\sqrt2\approx1{,}414.$$
>
> > [!solucion]
> > Para la senoide, $F_f\approx1{,}11$ y $F_c\approx1{,}41$. Son **constantes universales** de la forma
> > senoidal: cualquier senoide, sea cual sea su amplitud o frecuencia, tiene exactamente estos dos
> > factores.

---

## En qué consiste

> [!teoria] Qué mide cada factor
> El **factor de forma** indica cuánto se **aparta** la onda de una continua. Una onda **cuadrada** es,
> en valor absoluto, constante: su eficaz iguala a su medio rectificado y $F_f=1$ (el mínimo posible).
> Cuanto más **picuda** es la onda —más concentra su energía en picos breves frente a un valor medio
> bajo— mayor es $F_f$. Así, $F_f$ crece de la cuadrada ($1$) a la senoide ($1{,}11$) y a la triangular
> ($1{,}15$).
>
> El **factor de cresta** compara el **pico** con el eficaz, y es el que importa en la práctica: fija la
> tensión máxima que un aislamiento debe **soportar** y advierte de la **saturación** (de núcleos
> magnéticos, de amplificadores). Un $F_c$ alto significa picos pronunciados respecto a un eficaz
> modesto: la red de $220\ \text{V}$ eficaces alcanza picos de $220\sqrt2\approx311\ \text{V}$, y es ese
> pico el que debe aislar el dieléctrico.

> [!proposicion] Valores por forma de onda
> Los factores dependen solo de la forma; para las tres ondas canónicas (de amplitud de pico $V_m$):
>
> | Forma | $V_{med}$ (rect.) | $V_{ef}$ | $F_f=V_{ef}/V_{med}$ | $F_c=V_m/V_{ef}$ |
> |:---|:---:|:---:|:---:|:---:|
> | Cuadrada | $V_m$ | $V_m$ | $1$ | $1$ |
> | Senoidal | $2V_m/\pi$ | $V_m/\sqrt2$ | $\pi/(2\sqrt2)\approx1{,}11$ | $\sqrt2\approx1{,}41$ |
> | Triangular | $V_m/2$ | $V_m/\sqrt3$ | $2/\sqrt3\approx1{,}15$ | $\sqrt3\approx1{,}73$ |
>
> La cuadrada es el caso límite "más plano" ($F_f=F_c=1$); la triangular, la más "picuda" de las tres.

> [!warning]
> El factor de forma usa el valor medio de la onda **rectificada**, no el de la onda completa: el medio
> de una senoide simétrica sobre un período es **cero**, y dividir por cero no tiene sentido. Además,
> ambos factores dependen **solo de la forma**, no de la amplitud: multiplicar la onda por una constante
> no los altera.

## Resumen

> [!resumen]
> | Magnitud | Definición | Senoide |
> |:---|:---|:---:|
> | Factor de forma | $F_f=V_{ef}/V_{med}$ (rect.) | $\pi/(2\sqrt2)\approx1{,}11$ |
> | Factor de cresta | $F_c=V_m/V_{ef}$ | $\sqrt2\approx1{,}41$ |
> | Mide $F_f$ | apartamiento de una continua | — |
> | Mide $F_c$ | pico frente al eficaz (aislamiento) | — |
> | Cuadrada / Triangular | — | $F_f{:}\,1\,/\,1{,}15\;\;F_c{:}\,1\,/\,1{,}73$ |

> [!corolario]
> Los factores de forma y de cresta condensan la "huella" de una onda en dos números puros: con el
> [[Valor Medio]], el [[Valor Eficaz RMS| valor eficaz]] y el pico ligados por $F_f$ y $F_c$, basta
> conocer una de las magnitudes para recuperar las otras. Son, además, la base de cómo miden los
> instrumentos analógicos, calibrados para senoide con $F_f=1{,}11$.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Relaciona el [[Valor Eficaz RMS]] con el [[Valor Medio]] y el pico de la
> [[Onda Sinusoidal]]; cierra el capítulo de [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas sinusoidales]].
