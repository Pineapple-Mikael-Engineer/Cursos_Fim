---
title: "P2 — Planta OTEC de amoniaco (gradiente térmico del mar)"
order: 3
tags: [termodinamica, problemas, ciclos, rankine, otec]
draft: false
aliases: [OTEC amoniaco, energía térmica oceánica, planta gradiente mar]
---

# P2 — Planta OTEC de amoniaco (gradiente térmico del mar)

> [!definicion] Enunciado
> Una planta generadora opera basada en la diferencia de temperatura entre las aguas profundas ($5\,^\circ$C) y las aguas superficiales ($25\,^\circ$C) del mar. Usa **amoniaco** como fluido de trabajo en un ciclo Rankine. La bomba y la turbina tienen eficiencia adiabática $0{,}80$ y el flujo másico de amoniaco es $\dot m=1000$ kg/s. Determinar **(4)** potencia de la turbina [MW]; **(5)** potencia de la bomba [kW]; **(6)** flujo de agua por el intercambiador A (evaporador) [ton/s]; **(7)** flujo de agua por el intercambiador B (condensador) [ton/s]; **(8)** eficiencia térmica [%].

## Estrategia

> [!teoria]
> Ciclo [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine]] de **baja temperatura** (OTEC): el amoniaco se evapora a $20\,^\circ$C tomando calor del agua superficial ($25\,^\circ$C) en el intercambiador A, se expande en la turbina, se condensa a $10\,^\circ$C cediendo calor al agua profunda ($5\,^\circ$C) en el intercambiador B, y la bomba lo retorna. El gradiente disponible es pequeño $\Rightarrow$ eficiencia muy baja.

> [!info] Estados (amoniaco, de tabla)
> | Estado | descripción | $T$ | $h$ [kJ/kg] | $s$ [kJ/kg·K] |
> |:---|:---|:---:|:---:|:---:|
> | 1 | vapor sat. (sale del evap. A) | 20°C | 1460{,}18 | 5{,}0863 |
> | 2 | salida turbina (a $\approx615$ kPa) | 10°C | ≈1418 | 5{,}0863 |
> | 3 | líq. sat. (sale del cond. B) | 10°C | 226{,}97 | 0{,}8721 |
> | 4 | salida bomba | — | 227{,}36 | — |

> [!solucion] (4) y (5) Potencias
> Turbina ($s_{2s}=s_1$, real con $\eta=0{,}8$): $h_1-h_{2s}\approx52$, $w_T=\eta(h_1-h_{2s})\approx41{,}7$ kJ/kg:
> $$\dot W_T=\dot m\,w_T=1000(41{,}7)\times10^{-3}\approx\boxed{33{,}9\ \text{MW}}.$$
> Bomba: $\dot W_B=\dot m(h_4-h_3)=1000(227{,}36-226{,}97)\approx\boxed{32\ \text{kW}}$ (a través de $\eta_B$).

> [!solucion] (6) y (7) Flujos de agua de mar
> Intercambiador A (evaporador): $\dot Q_A=\dot m(h_1-h_4)=\dot m_{w,A}\,c_p\,\Delta T_A$ ($25\to23\,^\circ$C):
> $$\dot m_{w,A}=\frac{\dot m(h_1-h_4)}{c_p\,\Delta T_A}\approx\boxed{147{,}3\ \text{ton/s}}.$$
> Intercambiador B (condensador): $\dot Q_B=\dot m(h_2-h_3)=\dot m_{w,B}\,c_p\,\Delta T_B$ ($7\to5\,^\circ$C):
> $$\dot m_{w,B}\approx\boxed{149{,}4\ \text{ton/s}}.$$

> [!solucion] (8) Eficiencia térmica
> $$\eta=\frac{\dot W_T-\dot W_B}{\dot Q_A}=\frac{33{,}9-0{,}032}{1267}\approx\boxed{2{,}67\%}.$$

> [!info] Nota
> Valores del amoniaco de tabla (a cotejar con CATT3). La eficiencia $\sim2{,}7\%$ es típica de OTEC: el límite de Carnot entre $25$ y $5\,^\circ$C es solo $\eta_C=1-278/298=6{,}7\%$. Coincide con la clave ($\dot W_T=33{,}9$ MW, $\dot m_{w,A}=147{,}3$, $\dot m_{w,B}=149{,}4$ ton/s, $\eta=2{,}67\%$).

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine]] · [[Conversión de Energía/index | Conversión de Energía]] · [[Sistemas/Dispositivos Flujo/Intercambiadores | Intercambiadores]] · [[Temperatura]]
