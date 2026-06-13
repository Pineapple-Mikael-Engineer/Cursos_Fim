---
title: "Problema 01 — Turbina de vapor adiabática"
tags:
  - termodinamica
  - problemas
  - volumen_de_control
  - segunda_ley
draft: false
aliases:
  - turbina de vapor
  - eficiencia isentrópica turbina
---

# Problema 01 — Turbina de vapor adiabática

> [!definicion] Enunciado
> Vapor de agua entra a una [[Turbinas | turbina]] adiabática a $P_1 = 4\ \text{MPa}$ y $T_1 = 400\ ^\circ\text{C}$, con un flujo másico $\dot m = 15\ \text{kg/s}$, y se expande hasta $P_2 = 10\ \text{kPa}$. Se desprecian los cambios de energía cinética y potencial.
>
> Se pide:
> 1. La potencia que entregaría la turbina si fuese **isentrópica**.
> 2. La potencia real, dada una eficiencia isentrópica $\eta_T = 0.85$, y el estado de salida.
> 3. La tasa de generación de entropía y comprobar la segunda ley.

## Estrategia

> [!teoria]
> El equipo es un [[Volumen Especifico | volumen de control]] en **flujo estacionario**, una entrada y una salida, adiabático ($\dot Q = 0$) y sin trabajo de frontera. Aplican:
> - [[Balance de Masa VC]]: $\dot m_1 = \dot m_2 = \dot m$.
> - [[Balance de Energia VC]], despreciando $\Delta\text{EC}$ y $\Delta\text{EP}$: $\dot W = \dot m\,(h_1 - h_2)$.
> - [[Balance de Entropia VC]]: $\dot S_{gen} = \dot m\,(s_2 - s_1) \ge 0$ (adiabático).
>
> La idealización isentrópica fija $s_{2s} = s_1$; la eficiencia corrige hacia el proceso real.

## Estado de entrada

> [!info]
> A $P_1 = 4\ \text{MPa}$, $T_1 = 400\ ^\circ\text{C}$ el vapor está **sobrecalentado**. De tablas:
> $$
> h_1 \approx 3214\ \text{kJ/kg}, \qquad s_1 \approx 6.769\ \text{kJ/kg·K}
> $$
> La [[Presion]] y la [[Temperatura]] son independientes en esta región, así que $(P_1,T_1)$ fijan el estado.

## Inciso 1 — Potencia isentrópica

> [!proposicion]
> La salida isentrópica tiene $s_{2s} = s_1 = 6.769\ \text{kJ/kg·K}$ a $P_2 = 10\ \text{kPa}$. Comparando con los valores de saturación a $10\ \text{kPa}$ ($s_f = 0.6493$, $s_g = 8.1502\ \text{kJ/kg·K}$), como $s_f < s_{2s} < s_g$ el estado cae en la **región bifásica**. La [[Calidad]] es:
> $$
> x_{2s} = \frac{s_{2s} - s_f}{s_{fg}} = \frac{6.769 - 0.6493}{7.5009} = 0.816
> $$

> [!solucion]
> Con $h_f = 191.83$, $h_{fg} = 2392.8\ \text{kJ/kg}$, la entalpía de salida isentrópica:
> $$
> h_{2s} = h_f + x_{2s}\,h_{fg} = 191.83 + 0.816\,(2392.8) = 2144\ \text{kJ/kg}
> $$
> El trabajo específico y la potencia isentrópicos:
> $$
> w_s = h_1 - h_{2s} = 3214 - 2144 = 1070\ \text{kJ/kg}
> $$
> $$
> \dot W_s = \dot m\,w_s = 15 \times 1070 = 1.605\times 10^4\ \text{kW} \approx 16.0\ \text{MW}
> $$

## Inciso 2 — Potencia real y estado de salida

> [!definicion]
> La eficiencia isentrópica de una turbina compara el trabajo real con el ideal a la misma presión de salida:
> $$
> \eta_T = \frac{w_{real}}{w_s} = \frac{h_1 - h_2}{h_1 - h_{2s}}
> $$

> [!solucion]
> Trabajo real y potencia:
> $$
> w_{real} = \eta_T\,w_s = 0.85 \times 1070 = 909.5\ \text{kJ/kg}
> $$
> $$
> \dot W_{real} = 15 \times 909.5 = 1.364\times 10^4\ \text{kW} \approx 13.6\ \text{MW}
> $$
> Entalpía real de salida y su [[Calidad]]:
> $$
> h_2 = h_1 - w_{real} = 3214 - 909.5 = 2304.5\ \text{kJ/kg}
> $$
> $$
> x_2 = \frac{h_2 - h_f}{h_{fg}} = \frac{2304.5 - 191.83}{2392.8} = 0.883
> $$
> La irreversibilidad desplaza la salida a mayor calidad (más vapor) que el caso isentrópico.

## Inciso 3 — Generación de entropía

> [!solucion]
> Entropía específica real de salida:
> $$
> s_2 = s_f + x_2\,s_{fg} = 0.6493 + 0.883\,(7.5009) = 7.272\ \text{kJ/kg·K}
> $$
> Del [[Balance de Entropia VC]] adiabático:
> $$
> \dot S_{gen} = \dot m\,(s_2 - s_1) = 15\,(7.272 - 6.769) = 7.55\ \text{kW/K}
> $$

> [!info] Verificación física
> $\dot S_{gen} > 0$: el proceso real es **irreversible**, consistente con la segunda ley. El caso isentrópico daría $\dot S_{gen} = 0$. La caída de potencia $16.0 \to 13.6\ \text{MW}$ es la manifestación energética de esa generación de entropía.

## Notas usadas

> [!referencia]
> [[Turbinas]] · [[Balance de Masa VC]] · [[Balance de Energia VC]] · [[Balance de Entropia VC]] · [[Entalpia]] · [[Entropia]] · [[Calidad]] · [[Presion]] · [[Temperatura]]

> [!info]
> **Convención de notación**:
> - subíndice $s$: estado o proceso isentrópico; sin subíndice: real.
> - $\dot W > 0$: potencia entregada por la turbina; $\dot S_{gen}$ [kW/K].
> - valores de tablas de vapor citados como aproximados.
