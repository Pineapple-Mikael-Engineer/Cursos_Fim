---
title: "P3 — Rankine: eficiencia y temperatura media de adición"
order: 4
tags: [termodinamica, problemas, ciclos, rankine]
draft: false
aliases: [Rankine temperatura media transmisión calor]
---

# P3 — Rankine: eficiencia y temperatura media de adición

> [!definicion] Enunciado
> En un ciclo Rankine el vapor sale de la caldera y entra a la turbina a $30$ bar. La presión en el condensador es de $0{,}1$ bar. **(a)** Determinar la eficiencia y la **temperatura media de transmisión de calor** al ciclo. **(b)** Si existiera un sobrecalentamiento del vapor hasta $600\,^\circ$C, determinar la eficiencia del ciclo Rankine y su temperatura media de transmisión de calor.

![[rankine_diagrama_Ts.svg|340]]

> [!teoria]
> La **temperatura media de adición** de calor es $T_m=\dfrac{q_{ent}}{\Delta s_{ent}}=\dfrac{h_1-h_4}{s_1-s_4}$; el ciclo se comporta como un Carnot entre $T_m$ y $T_{cond}$. Subirla mejora $\eta$.

> [!solucion] (a) Vapor saturado a 30 bar
> Estado 1 (vapor sat. $3$ MPa): $h_1=2804$, $s_1=6{,}187$. Turbina isentrópica a $10$ kPa: $x_2=\dfrac{6{,}187-0{,}6493}{7{,}5009}=0{,}738$, $h_2=1958$. Bomba: $h_4=h_3+v\Delta P=191{,}8+3{,}0=194{,}8$.
> $$\eta=\frac{(h_1-h_2)-w_B}{h_1-h_4}=\frac{846-3}{2609}=\boxed{32{,}3\%}.$$
> $$T_m=\frac{h_1-h_4}{s_1-s_4}=\frac{2609}{6{,}187-0{,}649}=471\ \text{K}=\boxed{198\,^\circ\text{C}}.$$

> [!solucion] (b) Sobrecalentado a 600 °C
> Estado 1 ($3$ MPa, $600\,^\circ$C): $h_1=3682$, $s_1=7{,}510$. Turbina a $10$ kPa: $x_2=\dfrac{7{,}510-0{,}6493}{7{,}5009}=0{,}915$, $h_2=2381$.
> $$\eta=\frac{3682-2381-3}{3682-194{,}8}=\boxed{37{,}2\%},\qquad T_m=\frac{3487}{7{,}510-0{,}649}=508\ \text{K}=\boxed{235\,^\circ\text{C}}.$$

> [!info]
> El sobrecalentamiento sube $T_m$ de $198$ a $235\,^\circ$C y con ello $\eta$ de $32{,}3$ a $37{,}2\%$, además de mejorar la calidad de salida ($0{,}74\to0{,}92$).

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/index | Rankine]] · [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine Simple]]
