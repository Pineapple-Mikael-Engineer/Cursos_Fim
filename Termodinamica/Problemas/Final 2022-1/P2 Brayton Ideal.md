---
title: "P2 — Ciclo Brayton (Joule) ideal"
order: 3
tags: [termodinamica, problemas, ciclos, brayton]
draft: false
aliases: [Brayton Joule ideal 2022]
---

# P2 — Ciclo Brayton (Joule) ideal

> [!definicion] Enunciado
> Una planta de potencia con turbina a gas trabaja con un ciclo **Joule-Brayton estándar**: el aire ingresa al compresor a $312$ K y $107$ kPa, la relación de presiones es $11$ y la temperatura máxima es $1420$ K. Determinar **(a)** $P$ y $T$ en cada estado; **(b)** trabajo del compresor, de la turbina y eficiencia térmica. ($k=1{,}4$, $c_p=1{,}005$.)

![[brayton_diagrama_Ts.svg|330]]

> [!solucion] (a) Estados
> $T_2=312\,(11)^{0{,}2857}=619{,}3$ K, $P_2=11(107)=1177$ kPa. $T_3=1420$ K, $P_3=1177$ kPa. $T_4=1420/(11)^{0{,}2857}=715{,}4$ K, $P_4=107$ kPa.

> [!solucion] (b) Trabajos y eficiencia
> $$w_C=c_p(T_2-T_1)=308{,}8,\quad w_T=c_p(T_3-T_4)=708{,}1\ \text{kJ/kg},$$
> $$\eta=1-\frac{1}{11^{0{,}2857}}=\boxed{49{,}6\%},\qquad w_{neto}=399{,}3\ \text{kJ/kg}.$$

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton Simple | Brayton Simple]]
