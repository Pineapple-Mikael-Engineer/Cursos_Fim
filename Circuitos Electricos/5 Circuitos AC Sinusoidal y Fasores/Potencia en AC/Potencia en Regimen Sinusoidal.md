---
title: Potencia en Régimen Sinusoidal
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - potencia en régimen sinusoidal
  - potencia instantánea
  - potencia activa reactiva aparente
  - potencia compleja
  - triángulo de potencias
  - potencia en elementos puros
  - potencia en R L C
  - AC power
---

# Potencia en Régimen Sinusoidal

> [!definicion]
> En régimen sinusoidal, la potencia de una carga se describe con **tres magnitudes** construidas a
> partir de los valores **eficaces** $V$, $I$ y del desfase $\varphi$ entre tensión y corriente:
> $$P=VI\cos\varphi\ (\text{W}),\qquad Q=VI\operatorname{sen}\varphi\ (\text{VAr}),\qquad S=VI\ (\text{VA}),$$
> la **activa** $P$ (la que trabaja), la **reactiva** $Q$ (la que oscila en $L$ y $C$) y la **aparente**
> $S$ (la que dimensiona los equipos). Se unifican en la **potencia compleja**
> $$S=\overline{V}\,\overline{I}^{*}=P+jQ,$$
> y se relacionan por el **triángulo de potencias** $S^2=P^2+Q^2$.

> [!info]
> El núcleo de la [[Potencia en AC/index | potencia en CA]] ([[5 Circuitos AC Sinusoidal y Fasores/index | capítulo 5]]). Nace de la media temporal de la potencia instantánea $p=vi$, usa los
> [[Valor Eficaz RMS | valores eficaces]] y el desfase de los [[Fasores]]; su cociente $P/S$ es el
> [[Factor de Potencia]]. Fraile Mora, cap. 2, §2.9-2.10.

---

## Ejemplo

> [!ejemplo]
> **Las tres potencias de una carga inductiva.**
>
> Una carga recibe $\overline{V}=100\angle0^\circ\ \text{V}$ y absorbe
> $\overline{I}=20\angle(-53^\circ)\ \text{A}$ (inductiva, la corriente atrasa). Hallar $S$, $P$ y $Q$.
>
> ![[triangulo_potencias.svg|470]]
>
> *Triángulo de potencias: la activa $P$ en horizontal, la reactiva $Q$ en vertical, la aparente $S$
> como hipotenusa. Su ángulo $\varphi$ es el desfase tensión-corriente.*
>
> **Paso 1 — Potencia compleja** (con el conjugado $\overline{I}^{*}=20\angle53^\circ$):
> $$S=\overline{V}\,\overline{I}^{*}=100\angle0^\circ\cdot20\angle53^\circ=2000\angle53^\circ\ \text{VA}.$$
>
> **Paso 2 — Componentes** ($\cos53^\circ\approx0{,}6$, $\operatorname{sen}53^\circ\approx0{,}8$):
> $$P=2000\cos53^\circ=1200\ \text{W},\qquad Q=2000\operatorname{sen}53^\circ=1600\ \text{VAr}.$$
>
> > [!solucion]
> > $S=1200+j1600=2000\angle53^\circ\ \text{VA}$: aparente $2000\ \text{VA}$, activa $1200\ \text{W}$,
> > reactiva $+1600\ \text{VAr}$ (inductiva, $Q>0$). Se cumple $S^2=P^2+Q^2$
> > ($2000^2=1200^2+1600^2$).

---

## La potencia instantánea: de dónde nace todo

> [!teoria] La media es $P$, la fluctuación es $Q$
> La **potencia instantánea** es el producto en cada instante, $p(t)=v(t)\,i(t)$. Con
> $v=V_m\operatorname{sen}\omega t$ e $i=I_m\operatorname{sen}(\omega t-\varphi)$, la identidad
> producto-suma $\operatorname{sen}A\operatorname{sen}B=\tfrac12[\cos(A-B)-\cos(A+B)]$ da
> $$p(t)=\underbrace{VI\cos\varphi}_{\text{constante }=P}\;-\;\underbrace{VI\cos(2\omega t-\varphi)}_{\text{oscila a }2\omega,\ \text{media }0},$$
> (usando $V_m I_m=2VI$ con valores eficaces). Es decir: $p(t)$ **oscila al doble de la frecuencia**
> en torno a un valor medio que es la **potencia activa** $P=VI\cos\varphi$.
>
> ![[potencia_instantanea.svg|620]]
>
> *La potencia instantánea $p=vi$ oscila a $2\omega$; su valor medio (línea horizontal) es $P$. Los
> tramos negativos son energía que la carga reactiva **devuelve** a la fuente.*

> [!proposicion] La frecuencia doble se nota
> Para carga **resistiva** ($\varphi=0$), $p(t)=P(1-\cos2\omega t)\geq0$: pulsa entre $0$ y $2P$, nunca
> negativa, con media $P$. Su frecuencia es **el doble** de la red ($100\ \text{Hz}$ en $50\ \text{Hz}$):
> por eso las lámparas incandescentes parpadean y los núcleos magnéticos zumban a $100/120\ \text{Hz}$.

## Por elemento: R disipa, L y C intercambian

> [!teoria] El desfase decide el papel energético
> El comportamiento de cada elemento lo fija el desfase $\varphi$ entre $v$ e $i$:
> - **Resistencia ($\varphi=0$):** $v$ e $i$ "tiran a la vez", $p\geq0$ siempre; la energía fluye
>   **siempre hacia** el elemento y se disipa en calor. Es potencia **activa**.
> - **Inductor y condensador ($\varphi=\pm90^\circ$):** medio ciclo la energía entra al campo
>   (magnético en $L$, eléctrico en $C$) y el otro medio sale de vuelta; la media es **cero**. Es
>   potencia **reactiva**: no se consume, solo va y viene.
>
> ![[potencia_elementos.svg|640]]
>
> *Resistencia: $p\geq0$ (área neta positiva, disipa). Inductor y condensador: $p$ oscila simétrica, de
> media nula (almacena y devuelve), y en oposición de fase entre sí.*

> [!proposicion] Potencia en cada elemento ideal
> Con $X_L=\omega L$, $X_C=1/(\omega C)$ las reactancias:
> $$\text{R:}\ \ P=VI=I^2R=\frac{V^2}{R}>0;\qquad \text{L:}\ \ Q_L=I^2X_L>0;\qquad \text{C:}\ \ Q_C=-I^2 X_C<0.$$
> El **signo opuesto** de $Q_L$ y $Q_C$ es la base de la corrección del factor de potencia: un
> condensador aporta $Q_C<0$ que cancela el $Q_L>0$ de las cargas inductivas. →
> [[Correccion del Factor de Potencia]].

## Las tres potencias P, Q, S

> [!teoria] Mismo producto $VI$, tres significados
> Las tres magnitudes salen del producto $VI$, pero miden cosas distintas:
> - **Activa $P$ (W).** La que se **convierte en trabajo o calor** —mueve el motor, ilumina la
>   lámpara— y la que **se factura**. Es la media de $p(t)$.
> - **Reactiva $Q$ (VAr).** La que la red **intercambia** con los campos de $L$ y $C$. No se consume,
>   pero **ocupa** la red. **Positiva** para cargas inductivas, **negativa** para capacitivas.
> - **Aparente $S$ (VA).** El **producto de eficaces**; **dimensiona los equipos** (cables,
>   transformadores y alternadores se calculan por su VA, no por sus W).

## La potencia compleja $S=\overline{V}\,\overline{I}^{*}=P+jQ$

> [!teoria] Por qué el conjugado
> Si $\overline{V}=V\angle\alpha$ e $\overline{I}=I\angle\beta$, el desfase de la carga es
> $\varphi=\alpha-\beta$. Tomando el **conjugado** de la corriente,
> $$S=\overline{V}\,\overline{I}^{*}=VI\angle(\alpha-\beta)=VI\angle\varphi=VI\cos\varphi+jVI\operatorname{sen}\varphi=P+jQ,$$
> el ángulo de $S$ es **justo el desfase** $\varphi$ (sin conjugar saldría $\alpha+\beta$, sin sentido
> físico). Como los módulos son **eficaces**, no aparece el factor $\tfrac12$. El **triángulo de
> potencias** ($P$, $Q$, $S$) es **semejante** al de impedancias ($R$, $X$, $Z$), porque
> $S=I^2 Z$: mismo ángulo $\varphi$.

> [!proposicion] El signo de $Q$ delata la carga
> $Q>0$ **inductiva** ($\overline{I}$ atrasa), $Q<0$ **capacitiva** ($\overline{I}$ adelanta), $Q=0$
> **resistiva**. El módulo de $S$ es siempre la hipotenusa $S=\sqrt{P^2+Q^2}$.

> [!proposicion] Conservación: teorema de Boucherot
> Con varias cargas, las potencias **se conservan por separado**:
> $$P_{tot}=\sum_k P_k,\qquad Q_{tot}=\sum_k Q_k,\qquad S_{tot}=\sqrt{P_{tot}^2+Q_{tot}^2}.$$
> Las **activas se suman**; las **reactivas se suman con su signo** (inductivas $+$, capacitivas $-$,
> de modo que se compensan); las **aparentes NO** se suman directamente, hay que recomponerlas desde
> $P_{tot}$ y $Q_{tot}$. Es la base del cálculo de instalaciones.

> [!warning]
> $S\neq P+Q$: la aparente es la **hipotenusa** $\sqrt{P^2+Q^2}$, no la suma. La reactiva $Q$ **no** se
> disipa, pero su exceso baja el [[Factor de Potencia]], obliga a transportar más corriente y
> **encarece** la instalación. "Media cero" en $L$, $C$ es la potencia **activa**, no la corriente:
> ésta circula y, en cables reales, calienta. Siempre valores **eficaces**.

## Resumen

> [!resumen] Las tres potencias
> | Potencia | Símbolo | Fórmula | Unidad |
> |:---|:---|:---|:---|
> | Activa | $P$ | $VI\cos\varphi=\operatorname{Re}\{S\}$ | W |
> | Reactiva | $Q$ | $VI\operatorname{sen}\varphi=\operatorname{Im}\{S\}$ | VAr |
> | Aparente | $S$ | $VI=\sqrt{P^2+Q^2}$ | VA |
> | Compleja | $S$ | $\overline{V}\,\overline{I}^{*}=P+jQ=I^2 Z$ | VA |

> [!resumen] Origen e interpretación
> | Concepto | Idea |
> |:---|:---|
> | Potencia instantánea | $p=vi=P-VI\cos(2\omega t-\varphi)$; oscila a $2\omega$ |
> | Resistencia | $p\geq0$; solo activa $P=VI$ |
> | Inductor / condensador | media $0$; reactiva $Q_L>0$ / $Q_C<0$ |
> | Boucherot | $P_{tot}=\sum P_k$, $Q_{tot}=\sum Q_k$ (con signo) |

> [!corolario]
> Toda la potencia en CA nace del producto $p=vi$: su **media** es la activa $P$ (lo que se consume),
> su **fluctuación** da la reactiva $Q$ (lo que se intercambia), y juntas forman la compleja
> $S=P+jQ$ y el triángulo de potencias. Gestionar ese triángulo —subir $\cos\varphi$— es el corazón de
> la eficiencia eléctrica.

> [!referencia]
> Fraile Mora, cap. 2, §2.9-2.10. Valores eficaces: [[Valor Eficaz RMS]]. Desfase: [[Fasores]].
> Eficiencia: [[Factor de Potencia]] y [[Correccion del Factor de Potencia]]. Adaptación de carga:
> [[Maxima Transferencia AC]].
