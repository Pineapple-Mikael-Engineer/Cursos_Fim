---
title: Potencia en Sistemas Balanceados
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - potencia en sistemas balanceados
  - potencia trifásica equilibrada
  - balanced three-phase power
---

# Potencia en Sistemas Balanceados

> [!definicion]
> En un sistema trifásico **equilibrado**, las potencias activa, reactiva y aparente totales son el
> **triple** de las de una fase y, expresadas en magnitudes de **línea**, valen
> $$P=\sqrt3\,V_L I_L\cos\varphi,\quad Q=\sqrt3\,V_L I_L\operatorname{sen}\varphi,\quad S=\sqrt3\,V_L I_L=\sqrt{P^2+Q^2},$$
> con $\varphi$ el ángulo de la impedancia de carga. La fórmula es **idéntica en estrella y en
> triángulo**.

> [!info]
> El cálculo central de la [[Potencia Trifasica/index| potencia trifásica]] ([[7 Circuitos Trifasicos/index| capítulo 7]]); aplica el triángulo de potencias de la [[Potencia Compleja| potencia compleja]] (cap. 5) a las tres fases. Fraile Mora, cap. 3, §3.7.

---

## Ejemplo

> [!ejemplo]
> **Potencia de una carga trifásica.**
>
> Una carga equilibrada conectada a una línea de $V_L=400\ \text{V}$ toma una corriente de línea
> $I_L=23\ \text{A}$ con un factor de potencia $\cos\varphi=0{,}766$ (inductivo, $\varphi=40^\circ$).
> Hallar $P$, $Q$ y $S$.
>
> **Paso 1 — Potencia aparente.**
> $$S=\sqrt3\,V_L I_L=\sqrt3\cdot400\cdot23\approx15{,}9\ \text{kVA}.$$
>
> **Paso 2 — Activa y reactiva.**
> $$P=S\cos\varphi=15{,}9\cdot0{,}766\approx12{,}2\ \text{kW},\qquad Q=S\operatorname{sen}\varphi=15{,}9\cdot0{,}643\approx10{,}2\ \text{kVAr}.$$
>
> > [!solucion]
> > $S\approx15{,}9\ \text{kVA}$, $P\approx12{,}2\ \text{kW}$, $Q\approx10{,}2\ \text{kVAr}$ (inductiva).
> > El mismo resultado sale por fase: $P=3V_F I_F\cos\varphi$.

---

## En qué consiste

> [!teoria] Por qué $\sqrt3$ y por qué da igual la conexión
> Por fase, la potencia activa es $P_F=V_F I_F\cos\varphi$, así que el total es $P=3V_F I_F\cos\varphi$.
> Al pasar a magnitudes de línea, los factores $\sqrt3$ de las relaciones Y/Δ se combinan de modo que
> **siempre** queda
> $$P=\sqrt3\,V_L I_L\cos\varphi:$$
> - En **estrella**: $V_F=V_L/\sqrt3$, $I_F=I_L$ → $P=3\cdot\tfrac{V_L}{\sqrt3}I_L\cos\varphi=\sqrt3\,V_LI_L\cos\varphi$.
> - En **triángulo**: $V_F=V_L$, $I_F=I_L/\sqrt3$ → mismo resultado.
>
> Por eso la fórmula de línea es universal; el $\cos\varphi$ es **siempre** el de la impedancia de
> fase (no el ángulo entre $V_L$ e $I_L$).

> [!teorema] La potencia instantánea es constante
> A diferencia del monofásico (que pulsa a $2\omega$), la suma de las tres potencias instantáneas de un
> sistema equilibrado es **constante** e igual a la potencia media:
> $$p(t)=p_a+p_b+p_c=3V_F I_F\cos\varphi=P.$$
> Los términos pulsantes de las tres fases están a $120^\circ$ y se cancelan. De ahí el **par mecánico
> uniforme** de los motores trifásicos. → [[Ventajas del Trifasico]].

> [!warning]
> $\varphi$ es el ángulo de la **impedancia de carga** (entre $V_F$ e $I_F$), no el desfase entre
> tensión y corriente de **línea** (que difieren $30^\circ$). Y $V_L,I_L$ son valores **eficaces**. La
> potencia **reactiva no se suma aritméticamente** con la activa: se compone en el triángulo,
> $S=\sqrt{P^2+Q^2}$.

## Resumen

> [!resumen]
> | Potencia | Expresión (línea) | Por fase |
> |:---|:---|:---|
> | Activa $P$ | $\sqrt3\,V_LI_L\cos\varphi$ | $3V_FI_F\cos\varphi$ |
> | Reactiva $Q$ | $\sqrt3\,V_LI_L\operatorname{sen}\varphi$ | $3V_FI_F\operatorname{sen}\varphi$ |
> | Aparente $S$ | $\sqrt3\,V_LI_L$ | $3V_FI_F$ |
> | Instantánea | constante $=P$ | — |

> [!corolario]
> Una sola fórmula —$P=\sqrt3\,V_LI_L\cos\varphi$— resuelve la potencia de cualquier carga equilibrada,
> en Y o en Δ. Y al ser instantáneamente constante, el trifásico entrega un par sin vibración: su mayor
> ventaja sobre el monofásico.

> [!referencia]
> Fraile Mora, cap. 3, §3.7. Base monofásica: [[Potencia Compleja]]. Medición: [[Medicion con Dos Vatimetros]]. Mejora del FP: [[Correccion FP Trifasico]].
