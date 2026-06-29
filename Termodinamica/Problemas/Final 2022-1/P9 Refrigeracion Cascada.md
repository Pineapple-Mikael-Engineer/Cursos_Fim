---
title: "P9 — Refrigeración en cascada (Freón-12)"
order: 10
tags: [termodinamica, problemas, refrigeracion]
draft: false
aliases: [cascada Freón-12, refrigeración dos etapas]
---

# P9 — Refrigeración en cascada (Freón-12)

> [!definicion] Enunciado
> El sistema de refrigeración en cascada trabaja con **Freón-12**. El evaporador del ciclo inferior está a $-30\,^\circ$C con capacidad $25$ TON; el intercambiador de cascada acopla el condensador del ciclo inferior ($\approx-10\,^\circ$C) con el evaporador del ciclo superior ($\approx-15\,^\circ$C); el condensador superior está a $40\,^\circ$C. Determinar **(a)** flujos másicos del ciclo inferior y superior; **(b)** potencia de entrada; **(c)** COP de la cascada.

## Estrategia

> [!teoria]
> Dos ciclos de [[Conversión de Energía/Refrigeración/Compresión de Vapor | compresión de vapor]] acoplados por un intercambiador: el calor que **cede** el condensador del ciclo inferior es el que **absorbe** el evaporador del ciclo superior,
> $$\dot Q_{cond,B}=\dot Q_{evap,A}\quad\Rightarrow\quad \dot m_B(h_{2B}-h_{3B})=\dot m_A(h_{1A}-h_{4A}).$$
> Cada ciclo tiene sus 4 estados: compresor isentrópico ($1\to2$), condensador ($2\to3$, sale líquido sat.), válvula ($3\to4$, $h_4=h_3$), evaporador ($4\to1$, sale vapor sat.).

![[refrigeracion_diagrama_flujos.svg|360]]

## Procedimiento

> [!solucion] (a) Flujos másicos
> **Ciclo inferior B** (evap $-30\,^\circ$C, cond $-10\,^\circ$C). De la capacidad $\dot Q_L=25\ \text{TON}=25(3{,}517)=87{,}9$ kW y el efecto refrigerante $q_{L,B}=h_{1B}-h_{4B}$:
> $$\dot m_B=\frac{\dot Q_L}{h_{1B}-h_{4B}}.$$
> **Ciclo superior A** (evap $-15\,^\circ$C, cond $40\,^\circ$C). Del acoplamiento $\dot Q_{cond,B}=\dot m_B(h_{2B}-h_{3B})=\dot Q_{evap,A}$:
> $$\dot m_A=\frac{\dot m_B(h_{2B}-h_{3B})}{h_{1A}-h_{4A}}.$$

> [!solucion] (b) y (c) Potencia y COP
> $$\dot W=\dot m_B(h_{2B}-h_{1B})+\dot m_A(h_{2A}-h_{1A}),\qquad \mathrm{COP}_{cascada}=\frac{\dot Q_L}{\dot W}.$$
> El COP de la cascada es mayor que el de un solo ciclo entre $-30$ y $40\,^\circ$C, porque cada etapa opera con una relación de presiones menor.

> [!warning] Datos pendientes
> El cálculo numérico requiere las **tablas de saturación y vapor sobrecalentado del R-12** para leer $h$ en los $8$ estados (a $-30$, $-15$, $-10$ y $40\,^\circ$C, más las salidas isentrópicas de cada compresor). El enunciado escaneado es ambiguo en las temperaturas/capacidades intermedias (aparecen "$-10\,^\circ$C, $15$ TON" y "$-15\,^\circ$C"); conviene confirmarlo con el original y completar con las tablas del curso. La **estructura y las ecuaciones** de arriba resuelven el problema una vez fijados esos $h$.

> [!referencia]
> [[Conversión de Energía/Refrigeración/Compresión de Vapor | Compresión de Vapor]] · [[Conversión de Energía/Refrigeración/index | Refrigeración]] · [[Conversión de Energía/Refrigeración/Bomba de Calor | Bomba de Calor]]
