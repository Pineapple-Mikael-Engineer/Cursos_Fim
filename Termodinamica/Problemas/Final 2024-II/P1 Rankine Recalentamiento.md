---
title: "P1 — Rankine con recalentamiento (planta de 20 MW)"
order: 2
tags:
  - termodinamica
  - problemas
  - ciclos
  - rankine
draft: false
aliases:
  - Rankine recalentamiento examen final
  - planta térmica 20 MW
---

# P1 — Rankine con recalentamiento (planta de 20 MW)

> [!definicion] Enunciado
> En una planta térmica a vapor, que opera con un ciclo **Rankine con recalentamiento intermedio**, se genera $\dot W_{neta} = 20\ \text{MW}$ de potencia neta. La caldera tiene una eficiencia del $70\%$. La turbina es de **2 etapas** (alta y baja presión) y cada una tiene una eficiencia de expansión adiabática del $90\%$. El vapor ingresa a la turbina de alta presión a $40\ \text{bar}$ y $400\ ^\circ\text{C}$ y sale a $8\ \text{bar}$. El vapor que sale de la turbina de alta presión es recalentado e ingresa a la turbina de baja presión a $8\ \text{bar}$ y $400\ ^\circ\text{C}$, saliendo a $0{,}1\ \text{bar}$.
> Considere: eficiencia mecánica $=100\%$, eficiencia adiabática de la bomba $=100\%$, poder calorífico del combustible $= 40\,000\ \text{kJ/kg}$.
>
> Se pide: **(1)** trabajo de la bomba [kJ/kg]; **(2)** flujo de vapor [kg/s]; **(3)** calor recibido en el recalentador [kW]; **(4)** consumo de combustible [kg/s]; **(5)** eficiencia térmica de la planta [%].

## Estrategia

> [!teoria]
> Cada equipo es un [[Volumenes de Control | volumen de control]] en [[Flujo Estacionario | flujo estacionario]]. La turbina se modela en dos etapas con [[Sistemas/Dispositivos Flujo/Turbinas | eficiencia isentrópica]]; el recalentamiento se hace en la caldera entre etapas. Se recorre el ciclo [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine con Recalentamiento | Rankine con recalentamiento]] fijando los 6 estados con tablas de vapor y aplicando el [[Balance de Energia VC]] a cada componente.

![[rankine_recalentamiento_esquema.svg|460]]
![[rankine_diagrama_Ts.svg|360]]

## Estados del ciclo

> [!info]
> Numeración: **1** entrada turbina AP ($40\ \text{bar}$, $400\,^\circ$C) · **2** salida AP ($8\ \text{bar}$) · **3** entrada turbina BP (recalentado, $8\ \text{bar}$, $400\,^\circ$C) · **4** salida BP ($0{,}1\ \text{bar}$) · **5** líquido saturado a $0{,}1\ \text{bar}$ (salida condensador) · **6** salida bomba ($40\ \text{bar}$). Subíndice $s$ = isentrópico ideal; $r$ = real.
>
> | Estado | $P$ [MPa] | $T$ [°C] | $h$ [kJ/kg] | $s$ [kJ/kg·K] |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 4{,}0 | 400 | 3214 | 6{,}769 |
> | 2s | 0{,}8 | — | 2817 | 6{,}769 |
> | 2r | 0{,}8 | ≈208 | 2856{,}7 | — |
> | 3 | 0{,}8 | 400 | 3267 | 7{,}572 |
> | 4s | 0{,}01 | 45{,}8 | 2400 | 7{,}572 |
> | 4r | 0{,}01 | 45{,}8 | 2486{,}7 | — |
> | 5 | 0{,}01 | 45{,}8 | 191{,}8 | 0{,}6492 |
> | 6 | 4{,}0 | ≈46 | 195{,}8 | 0{,}6492 |

> [!solucion] Estados de turbina con eficiencia isentrópica
> **Etapa AP** ($1\to2$): salida isentrópica a $8\ \text{bar}$ con $s_{2s}=s_1=6{,}769$ da $h_{2s}=2817$. La real:
> $$h_{2r}=h_1-\eta_T(h_1-h_{2s})=3214-0{,}90\,(3214-2817)=2856{,}7\ \text{kJ/kg}.$$
> **Etapa BP** ($3\to4$): a $0{,}1\ \text{bar}$, $s_{4s}=s_3=7{,}572$ cae en la región bifásica ($s_f=0{,}6493$, $s_{fg}=7{,}5009$):
> $$x_{4s}=\frac{7{,}572-0{,}6493}{7{,}5009}=0{,}923,\qquad h_{4s}=191{,}8+0{,}923\,(2392{,}8)=2400\ \text{kJ/kg}.$$
> $$h_{4r}=h_3-\eta_T(h_3-h_{4s})=3267-0{,}90\,(3267-2400)=2486{,}7\ \text{kJ/kg}.$$

## (1) Trabajo de la bomba

> [!solucion]
> Bomba isentrópica de líquido (incompresible) de $0{,}1\ \text{bar}$ a $40\ \text{bar}$, con $v_5=0{,}001010\ \text{m}^3/\text{kg}$:
> $$w_{B}=v_5\,(P_6-P_5)=0{,}001010\,(4000-10)=4{,}03\ \text{kJ/kg}.$$
> $$\boxed{w_B \approx 4\ \text{kJ/kg}}\qquad h_6=h_5+w_B=191{,}8+4=195{,}8\ \text{kJ/kg}.$$

## (2) Flujo de vapor

> [!solucion]
> La potencia **neta** es la de ambas etapas de turbina menos la de la bomba (eficiencia mecánica $100\%$), todo por el mismo $\dot m$:
> $$\dot W_{neta}=\dot m\big[(h_1-h_{2r})+(h_3-h_{4r})-w_B\big].$$
> $$20\,000=\dot m\big[(3214-2856{,}7)+(3267-2486{,}7)-4\big]=\dot m\,(357{,}3+780{,}3-4)=\dot m\,(1133{,}6).$$
> $$\boxed{\dot m=17{,}644\ \text{kg/s}}$$

## (3) Calor en el recalentador

> [!solucion]
> El recalentador lleva el vapor de $2r$ a $3$ a presión constante:
> $$\dot Q_{rec}=\dot m\,(h_3-h_{2r})=17{,}644\,(3267-2856{,}7)=\boxed{7239{,}3\ \text{kW}}.$$

## (4) Consumo de combustible

> [!solucion]
> El calor que el **fluido** recibe en la caldera (tramo $6\to1$) más el del recalentador es el calor útil; el combustible debe cubrirlo a través de la eficiencia de caldera $\eta_{cald}=0{,}70$:
> $$\dot Q_{cald}=\frac{\dot m\,(h_1-h_6)}{\eta_{cald}}=\frac{17{,}644\,(3214-195{,}8)}{0{,}70}=76\,075{,}9\ \text{kW}.$$
> $$\dot Q_{total}=\dot Q_{cald}+\dot Q_{rec}=76\,075{,}9+7239{,}3=83\,315\ \text{kW}.$$
> $$\dot m_{comb}=\frac{\dot Q_{total}}{PC}=\frac{83\,315}{40\,000}=\boxed{2{,}082\ \text{kg/s}}.$$

## (5) Eficiencia térmica de la planta

> [!solucion]
> La eficiencia térmica compara la potencia neta con el calor **absorbido por el fluido** (caldera + recalentador):
> $$\dot Q_A=\dot m\,(h_1-h_6)+\dot Q_{rec}=17{,}644\,(3214-195{,}8)+7239{,}3=53\,253+7239=60\,492{,}5\ \text{kW}.$$
> $$\eta_t=\frac{\dot W_{neta}}{\dot Q_A}=\frac{20\,000}{60\,492{,}5}=\boxed{33{,}06\%}.$$

> [!info] Verificación
> El recalentamiento mantiene la calidad de salida alta ($x_{4s}=0{,}92$), evitando erosión en los álabes de baja presión. La eficiencia de planta ($33\%$) queda por debajo de la térmica del ciclo porque la caldera solo aprovecha el $70\%$ del poder calorífico. Resultados coinciden con la clave: $\dot m=17{,}64$ kg/s, $\dot m_{comb}=2{,}082$ kg/s, $\eta=33{,}06\%$.

## Notas usadas

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine con Recalentamiento | Rankine con Recalentamiento]] · [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]] · [[Balance de Energia VC]] · [[Entalpia]] · [[Calidad]] · [[Vapor Sobrecalentado]]
