---
title: Potencia Compleja
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - potencia compleja
  - triángulo de potencias
  - potencia aparente
  - complex power
---

# Potencia Compleja $\;S=\overline{V}\,\overline{I}^{*}=P+jQ$

> [!definicion]
> La **potencia compleja** reúne las tres potencias de la CA en un solo número:
> $$S=\overline{V}\,\overline{I}^{*}=P+jQ,$$
> donde $\overline{I}^{*}$ es el **conjugado** de la corriente. Su parte real es la potencia **activa**
> $P=VI\cos\varphi$ (W), su parte imaginaria la **reactiva** $Q=VI\operatorname{sen}\varphi$ (VAr) y su
> módulo la **aparente** $\lvert S\rvert=VI$ (VA). Las tres forman el **triángulo de potencias**.

> [!info]
> El número que unifica la [[Potencia en AC/index| potencia en CA]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Su ángulo es el del [[Factor de Potencia]] y el de la
> [[Impedancia Compleja| impedancia]]. Fraile Mora, cap. 2, §2.10.

---

## Ejemplo

> [!ejemplo]
> **Las tres potencias de una carga.**
>
> Una carga recibe $\overline{V}=100\angle0^\circ\ \text{V}$ y absorbe $\overline{I}=20\angle(-53^\circ)
> \ \text{A}$ (inductiva). Hallar $S$, $P$ y $Q$.
>
> ![[triangulo_potencias.svg|470]]
>
> *Triángulo de potencias: la activa $P$ en horizontal, la reactiva $Q$ en vertical, la aparente $S$
> como hipotenusa. Su ángulo $\varphi$ es el desfase tensión-corriente.*
>
> **Paso 1 — Potencia compleja.** Con $\overline{I}^{*}=20\angle53^\circ$,
> $$S=\overline{V}\,\overline{I}^{*}=100\angle0^\circ\cdot20\angle53^\circ=2000\angle53^\circ\ \text{VA}.$$
>
> **Paso 2 — Componentes.**
> $$P=2000\cos53^\circ=1200\ \text{W},\qquad Q=2000\operatorname{sen}53^\circ=1600\ \text{VAr}.$$
>
> > [!solucion]
> > $S=1200+j1600=2000\angle53^\circ\ \text{VA}$: aparente $2000\ \text{VA}$, activa $1200\ \text{W}$,
> > reactiva $+1600\ \text{VAr}$ (inductiva, $Q>0$). Se cumple $\lvert S\rvert^2=P^2+Q^2$
> > ($2000^2=1200^2+1600^2$).

---

## En qué consiste

> [!teoria] Por qué el conjugado
> Si $\overline{V}=V\angle\alpha$ e $\overline{I}=I\angle\beta$, el desfase de la carga es
> $\varphi=\alpha-\beta$. Tomando $S=\overline{V}\,\overline{I}^{*}=VI\angle(\alpha-\beta)=VI\angle
> \varphi$, el **ángulo de $S$ es justo el desfase** $\varphi$ (no $\alpha+\beta$, que saldría sin
> conjugar). Así $S=VI\cos\varphi+jVI\operatorname{sen}\varphi=P+jQ$ separa limpiamente activa y
> reactiva. (Los módulos son **eficaces**, por eso no aparece el factor $\tfrac12$.)

> [!info] Las tres potencias y sus unidades
> | Potencia | Símbolo | Fórmula | Unidad |
> |:---|:---|:---|:---|
> | Aparente | $\lvert S\rvert$ | $VI$ | VA (voltamperio) |
> | Activa | $P$ | $VI\cos\varphi=\operatorname{Re}\{S\}$ | W (vatio) |
> | Reactiva | $Q$ | $VI\operatorname{sen}\varphi=\operatorname{Im}\{S\}$ | VAr (voltamperio reactivo) |
>
> Distintas unidades para distinto significado físico: $P$ trabaja, $Q$ oscila, $S$ dimensiona el
> equipo (cables, transformadores se calculan por su VA).

> [!proposicion] Signo de Q y el triángulo
> El signo de $Q$ revela la naturaleza de la carga: $Q>0$ **inductiva** ($\overline{I}$ atrasa), $Q<0$
> **capacitiva** ($\overline{I}$ adelanta), $Q=0$ **resistiva**. El **triángulo de potencias**
> ($P$, $Q$, $\lvert S\rvert$) es **semejante** al de impedancias ($R$, $X$, $\lvert Z\rvert$): mismo
> ángulo $\varphi$, porque $S=\lvert I\rvert^2 Z$.

> [!warning]
> La potencia aparente **no** es la suma aritmética de activa y reactiva: $\lvert S\rvert=\sqrt{P^2+Q^2}$,
> no $P+Q$. Y las potencias **activas se suman** entre cargas, las **reactivas se suman con su signo**
> (las inductivas y capacitivas se restan), pero las **aparentes no se suman** directamente.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Potencia compleja | $S=\overline{V}\,\overline{I}^{*}=P+jQ$ |
> | Aparente | $\lvert S\rvert=VI=\sqrt{P^2+Q^2}$ |
> | Activa | $P=VI\cos\varphi$ (W) |
> | Reactiva | $Q=VI\operatorname{sen}\varphi$ (VAr) |
> | Relación con $Z$ | $S=\lvert I\rvert^2 Z$ |

> [!corolario]
> La potencia compleja $S=P+jQ$ empaqueta en un número lo que la carga **consume** ($P$), lo que
> **intercambia** ($Q$) y lo que **aparenta** ($\lvert S\rvert$). Su ángulo es el factor de potencia, y
> su gestión, el corazón de la eficiencia eléctrica.

> [!referencia]
> Fraile Mora, cap. 2, §2.10. Detalle de cada potencia: [[Potencia en Sinuidal y Fasorial]]. Su
> cociente: [[Factor de Potencia]].
