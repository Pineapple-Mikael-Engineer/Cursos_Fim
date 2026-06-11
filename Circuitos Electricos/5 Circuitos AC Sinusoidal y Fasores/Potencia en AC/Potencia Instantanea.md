---
title: Potencia Instantánea
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - potencia instantánea
  - potencia momentánea
  - instantaneous power
---

# Potencia Instantánea $\;p(t)=v(t)\,i(t)$

> [!definicion]
> La **potencia instantánea** es el producto, en cada instante, de la tensión y la corriente:
> $$p(t)=v(t)\,i(t).$$
> En régimen sinusoidal, con $v$ e $i$ desfasados un ángulo $\varphi$, $p(t)$ **oscila al doble de la
> frecuencia** ($2\omega$) en torno a un valor medio. Ese valor medio es la **potencia activa**
> $$P=V_{ef}\,I_{ef}\cos\varphi.$$
> A diferencia de la tensión o la corriente, $p(t)$ puede ser **negativa** durante parte del ciclo: son
> los instantes en que la carga **devuelve energía** a la fuente.

> [!info]
> Es el punto de partida de toda la [[Potencia en AC/index| potencia en CA]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]):
> de su **valor medio** sale la potencia activa y de su **parte fluctuante** la reactiva, como se detalla
> en [[Potencia en Sinuidal y Fasorial]]. El valor medio usa los [[Valor Eficaz RMS| valores eficaces]].
> Fraile Mora, cap. 2, §2.9.

---

## Ejemplo

> [!ejemplo]
> **Descomposición de la potencia instantánea.**
>
> Sean $v=V_m\operatorname{sen}\omega t$ e $i=I_m\operatorname{sen}(\omega t-\varphi)$ con
> $\varphi=53^\circ$ (carga inductiva, la corriente atrasa). Mostrar que $p(t)$ oscila a $2\omega$ y que
> su valor medio es la potencia activa $P$.
>
> ![[potencia_instantanea.svg|620]]
>
> *La potencia instantánea $p=vi$ oscila al doble de la frecuencia ($2\omega$); su valor medio (la línea
> horizontal) es la potencia activa $P=V_{ef}I_{ef}\cos\varphi$. Los tramos negativos son energía
> devuelta.*
>
> **Paso 1 — Producto de las dos senoides.**
> $$p(t)=V_m I_m\operatorname{sen}\omega t\,\operatorname{sen}(\omega t-\varphi).$$
>
> **Paso 2 — Identidad producto-suma.** Con $\operatorname{sen}A\operatorname{sen}B=\tfrac12[\cos(A-B)-\cos(A+B)]$,
> $$p(t)=\frac{V_m I_m}{2}\big[\cos\varphi-\cos(2\omega t-\varphi)\big].$$
>
> **Paso 3 — Valores eficaces.** Como $V_m I_m=2\,V_{ef}I_{ef}$,
> $$p(t)=V_{ef}I_{ef}\cos\varphi\;-\;V_{ef}I_{ef}\cos(2\omega t-\varphi).$$
> El primer término es **constante** ($=P$); el segundo **oscila a $2\omega$** y promedia cero.
>
> **Paso 4 — Números.** Con $\cos53^\circ=0{,}6$:
> $$P=V_{ef}I_{ef}\cdot0{,}6,\qquad \text{amplitud de la oscilación}=V_{ef}I_{ef}.$$
>
> > [!solucion]
> > El **valor medio** de $p$ es $P=V_{ef}I_{ef}\cos\varphi$. La parte que oscila a $2\omega$ no aporta
> > potencia neta (su media en un periodo es cero), pero hace que $p(t)$ se vuelva negativa en parte del
> > ciclo: esa es la energía que la carga reactiva devuelve a la fuente.

---

## En qué consiste

> [!teoria] Las dos piezas de $p(t)$
> La potencia instantánea sinusoidal se descompone siempre en **un término constante más uno oscilante**:
> $$\underbrace{V_{ef}I_{ef}\cos\varphi}_{\text{activa }P}\;-\;\underbrace{V_{ef}I_{ef}\cos(2\omega t-\varphi)}_{\text{oscila a }2\omega,\ \text{media }0}.$$
> La frecuencia es $2\omega$ porque $p$ es **producto de dos senoides de frecuencia $\omega$**, y el
> producto de dos ondas de igual frecuencia genera una componente de frecuencia doble más una continua.
> Los tramos $p<0$ son **energía que regresa** a la fuente, y son tanto mayores cuanto mayor sea el
> desfase $\varphi$:
> - En una **resistencia** ($\varphi=0$): $p(t)=V_{ef}I_{ef}(1-\cos2\omega t)\geq0$ siempre; nunca
>   devuelve energía.
> - En **$L$ o $C$ puros** ($\varphi=\pm90^\circ$): $\cos\varphi=0$, la media es **cero** y $p(t)$ es una
>   senoide pura a $2\omega$ que oscila simétricamente entre positivo y negativo (solo intercambio).

> [!proposicion] El caso resistivo y la frecuencia doble
> Para carga **resistiva** ($\varphi=0$) la potencia instantánea se escribe como
> $$p(t)=P\,(1-\cos2\omega t)=P\,(1+\cos2\omega t'),$$
> es decir, una pulsación siempre positiva entre $0$ y $2P$ con media $P$. Su **frecuencia es el doble**
> de la de la red: $100\ \text{Hz}$ en una red de $50\ \text{Hz}$, o $120\ \text{Hz}$ en una de
> $60\ \text{Hz}$. Por eso las **lámparas incandescentes parpadean** a esa frecuencia doble y los
> **núcleos magnéticos vibran** (zumbido de $100/120\ \text{Hz}$).

> [!warning]
> La potencia instantánea **no es una senoide pura**: tiene una **media no nula** ($=P$), mientras que
> $v$ e $i$ tienen media cero. Su **frecuencia es $2\omega$**, no $\omega$. Y no hay que confundir su
> **valor medio** ($P$, la línea horizontal) con su **amplitud** de oscilación ($V_{ef}I_{ef}$): solo
> coinciden en el caso resistivo.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Potencia instantánea | $p(t)=v(t)\,i(t)$ |
> | Forma sinusoidal | $p(t)=V_{ef}I_{ef}\cos\varphi-V_{ef}I_{ef}\cos(2\omega t-\varphi)$ |
> | Valor medio (activa) | $P=V_{ef}I_{ef}\cos\varphi$ |
> | Frecuencia de $p$ | $2\omega$ (doble de la red) |
> | Resistencia ($\varphi=0$) | $p=P(1-\cos2\omega t)\geq0$ |
> | $L$ o $C$ puros ($\varphi=\pm90^\circ$) | media $=0$, solo intercambio |

> [!corolario]
> Toda la potencia en CA nace aquí: el **valor medio** de $p(t)$ es la potencia **activa** $P$ (lo que de
> verdad se consume) y la **parte oscilante a $2\omega$** —en particular los tramos negativos— es lo que
> da lugar a la potencia **reactiva**. Separar media y fluctuación de $p(t)$ es el origen físico del
> triángulo de potencias.

> [!referencia]
> Fraile Mora, cap. 2, §2.9. De su media y su fluctuación salen las potencias activa y reactiva en
> [[Potencia en Sinuidal y Fasorial]]. Casos extremos por elemento: [[Potencia en Elementos Puros]].
> Valores eficaces: [[Valor Eficaz RMS]].
