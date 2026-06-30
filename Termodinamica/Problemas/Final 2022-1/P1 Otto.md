---
title: "P1 — Ciclo Otto (presión media indicada)"
order: 2
tags: [termodinamica, problemas, ciclos, otto]
draft: false
aliases: [Otto presión media indicada 2022]
---

# P1 — Ciclo Otto (presión media indicada)

> [!definicion] Enunciado
> En un ciclo Otto, el inicio de la compresión adiabática es a $108$ kPa y $303$ K, la relación de compresión es $8$ y el calor agregado al ciclo es $2250$ kJ/kg. **(a)** Diagrama $P$–$v$ con presiones y temperaturas; **(b)** presión media indicada; **(c)** eficiencia térmica. ($k=1{,}4$, $c_v=0{,}718$, $R=0{,}287$.)

![[otto_diagrama_Pv.svg|340]]

> [!solucion] (a) Estados
> $T_2=303\,(8)^{0{,}4}=696{,}1$ K, $P_2=108\,(8)^{1{,}4}=1985$ kPa.
> $T_3=T_2+\dfrac{q_{in}}{c_v}=696{,}1+\dfrac{2250}{0{,}718}=3829{,}8$ K, $P_3=P_2\dfrac{T_3}{T_2}=10\,921$ kPa.
> $T_4=T_3/8^{0{,}4}=1667$ K, $P_4=594$ kPa.

> [!solucion] (b) y (c)
> $$\eta=1-8^{-0{,}4}=\boxed{56{,}5\%},\qquad w_{neto}=\eta\,q_{in}=1271\ \text{kJ/kg}.$$
> $v_1=RT_1/P_1=0{,}805$, $v_2=v_1/8=0{,}1007\ \text{m}^3/\text{kg}$:
> $$\text{PMI}=\frac{w_{neto}}{v_1-v_2}=\frac{1271}{0{,}705}=\boxed{1803\ \text{kPa}}.$$

> [!referencia]
> [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Otto | Ciclo Otto]]
