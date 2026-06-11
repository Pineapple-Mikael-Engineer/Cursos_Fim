---
title: Potencia en Sinuidal y Fasorial
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - potencia en régimen sinusoidal
  - potencia activa reactiva aparente
  - AC power
  - active reactive apparent power
---

# Potencia en Régimen Sinusoidal y Fasorial

> [!definicion]
> En **régimen sinusoidal permanente**, la potencia de una carga se describe con **tres magnitudes**
> derivadas de los valores **eficaces** $V_{ef}$, $I_{ef}$ y del desfase $\varphi$ entre tensión y
> corriente:
> $$P=V_{ef}I_{ef}\cos\varphi\ \ (\text{W}),\qquad Q=V_{ef}I_{ef}\operatorname{sen}\varphi\ \ (\text{VAr}),\qquad S=V_{ef}I_{ef}\ \ (\text{VA}).$$
> $P$ es la **activa** (la que trabaja), $Q$ la **reactiva** (la que oscila en $L$ y $C$) y $S$ la
> **aparente** (el producto de eficaces). Se relacionan por $S^2=P^2+Q^2$ y se reúnen en la
> [[Potencia Compleja| potencia compleja]].

> [!info]
> La definición de las tres potencias en la [[Potencia en AC/index| sección de potencia]]
> ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Nacen de la media temporal de la
> [[Potencia Instantanea| potencia instantánea]] y se empaquetan en la [[Potencia Compleja]]; su
> cociente $P/S$ es el [[Factor de Potencia]]. Fraile Mora, cap. 2, §2.9-2.10.

---

## Ejemplo

> [!ejemplo]
> **Las tres potencias de una carga inductiva.**
>
> Una carga trabaja con $V_{ef}=100\ \text{V}$, $I_{ef}=20\ \text{A}$ y desfase $\varphi=53^\circ$
> (inductiva, la corriente atrasa). Hallar $P$, $Q$ y $S$.
>
> **Paso 1 — Aparente.** Es directamente el producto de eficaces:
> $$S=V_{ef}I_{ef}=100\cdot20=2000\ \text{VA}.$$
>
> **Paso 2 — Activa y reactiva.** Se proyecta $S$ sobre el coseno y el seno del desfase
> ($\cos53^\circ\approx0{,}6$, $\operatorname{sen}53^\circ\approx0{,}8$):
> $$P=S\cos53^\circ=2000\cdot0{,}6=1200\ \text{W},\qquad Q=S\operatorname{sen}53^\circ=2000\cdot0{,}8=1600\ \text{VAr}.$$
>
> > [!solucion]
> > $P=1200\ \text{W}$, $Q=1600\ \text{VAr}$ (positiva, carga inductiva) y $S=2000\ \text{VA}$. Se
> > comprueba la relación pitagórica $S^2=P^2+Q^2$:
> > $$2000^2=1200^2+1600^2\quad\Longrightarrow\quad 4\,000\,000=1\,440\,000+2\,560\,000.\ \checkmark$$

---

## En qué consiste

> [!teoria] Qué significa cada potencia
> Las tres magnitudes salen del mismo producto $V_{ef}I_{ef}$, pero miden cosas físicamente distintas:
> - **Activa $P$ (W).** La que realmente se **convierte en trabajo o calor**; es la que mueve el motor,
>   ilumina la lámpara y la que **se paga** en el contador. Es la media de la
>   [[Potencia Instantanea| potencia instantánea]].
> - **Reactiva $Q$ (VAr).** La que la red **intercambia** con los campos magnético (en $L$) y eléctrico
>   (en $C$). No se "consume": va y vuelve dos veces por ciclo, pero **ocupa** la red. Es **positiva**
>   para cargas inductivas y **negativa** para capacitivas.
> - **Aparente $S$ (VA).** El **producto de eficaces** sin más; **dimensiona los equipos**: cables,
>   alternadores y transformadores se calculan por su VA, no por sus W.
>
> En versión **fasorial**, las tres salen de una sola cantidad, la [[Potencia Compleja| potencia compleja]] $S=\overline{V}\,\overline{I}^{*}=P+jQ$, cuya parte real es $P$, su parte imaginaria $Q$ y
> su módulo $S$.

> [!proposicion] Conservación de la potencia (teorema de Boucherot)
> En un circuito con varias cargas, las potencias **se conservan por separado**:
> $$P_{total}=\sum_k P_k,\qquad Q_{total}=\sum_k Q_k,\qquad S_{total}=\sqrt{P_{total}^2+Q_{total}^2}.$$
> Es decir, las **activas se suman** sin más; las **reactivas se suman con su signo** (inductivas $+$,
> capacitivas $-$, de modo que se compensan); pero las **aparentes NO se suman** directamente
> ($S_{total}\neq\sum_k S_k$), sino que hay que recomponerlas desde $P_{total}$ y $Q_{total}$. Es el
> **teorema de Boucherot**, base del cálculo de instalaciones.

> [!warning]
> $S\neq P+Q$: la aparente es la **hipotenusa**, $S=\sqrt{P^2+Q^2}$, no la suma aritmética. La reactiva
> $Q$ **no** es "potencia perdida" (no se disipa), pero su exceso baja el [[Factor de Potencia]],
> obliga a transportar más corriente y **encarece** la instalación. Y siempre se usan valores
> **eficaces** $V_{ef}$, $I_{ef}$, nunca de pico.

## Resumen

> [!resumen]
> | Potencia | Símbolo | Fórmula | Unidad |
> |:---|:---|:---|:---|
> | Activa | $P$ | $V_{ef}I_{ef}\cos\varphi=\operatorname{Re}\{S\}$ | W (vatio) |
> | Reactiva | $Q$ | $V_{ef}I_{ef}\operatorname{sen}\varphi=\operatorname{Im}\{S\}$ | VAr (voltamperio reactivo) |
> | Aparente | $S$ | $V_{ef}I_{ef}=\sqrt{P^2+Q^2}$ | VA (voltamperio) |
> | Boucherot | — | $P_{total}=\sum P_k$, $\;Q_{total}=\sum Q_k$, $\;S_{total}=\sqrt{P_{total}^2+Q_{total}^2}$ | — |

> [!corolario]
> Una sola pareja $(V_{ef}, I_{ef})$ y un ángulo $\varphi$ bastan para separar lo que la carga
> **consume** ($P$), lo que **intercambia** ($Q$) y lo que **aparenta** ($S$). Sumando activas y
> reactivas con su signo (Boucherot) se analiza cualquier instalación, y de su relación nace el
> [[Factor de Potencia]].

> [!referencia]
> Fraile Mora, cap. 2, §2.9-2.10. Origen temporal: [[Potencia Instantanea]]. Empaquetado fasorial:
> [[Potencia Compleja]]. Eficiencia de la transferencia: [[Factor de Potencia]].
