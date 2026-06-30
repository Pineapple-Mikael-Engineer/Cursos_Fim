---
title: "P2 — Ciclo combinado gas-vapor (45 MW)"
order: 3
tags: [termodinamica, problemas, ciclos, brayton, rankine]
draft: false
aliases: [ciclo combinado Brayton Rankine, planta combinada 45 MW]
---

# P2 — Ciclo combinado gas-vapor (45 MW)

> [!definicion] Enunciado
> Para el ciclo combinado de turbina de gas (TG) y turbina de vapor (TV), potencia neta total $=45$ MW. **TG:** $T_1=300$ K, $P_1=100$ kPa; $T_3=1400$ K; $P_2=P_3=1200$ kPa; $\eta_T=0{,}88$, $\eta_C=0{,}84$; $T_5=400$ K (escape), $P_5=P_4=100$ kPa. **TV:** $T_7=400\,^\circ$C, $P_7=8$ MPa, $P_8=8$ kPa; $\eta_B=0{,}8$, $\eta_T=0{,}9$. Calcular **(a)** eficiencia de la planta; **(b)** flujos de masa; **(c)** trabajo neto en cada etapa.

## Estrategia

> [!teoria]
> Un [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton Simple | Brayton]] superior acoplado a un [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine]] inferior por un intercambiador (HRSG): el calor del escape del gas ($4\to5$) genera el vapor ($6\to7$). $\dot m_g c_p(T_4-T_5)=\dot m_v(h_7-h_6)$.

![[brayton_diagrama_Ts.svg|300]]

> [!solucion] Estados del gas ($c_p=1{,}005$, $k=1{,}4$)
> Compresor: $T_{2s}=300\,(12)^{0{,}2857}=610{,}2$ K; real $T_2=300+\dfrac{310{,}2}{0{,}84}=669{,}3$ K.
> Turbina: $T_{4s}=1400\,(1/12)^{0{,}2857}=688{,}2$ K; real $T_4=1400-0{,}88(711{,}8)=773{,}6$ K.

> [!solucion] Estados del vapor
> $7$ ($8$ MPa, $400\,^\circ$C): $h_7=3139{,}4$, $s_7=6{,}366$. Turbina a $8$ kPa: $x_{8s}=0{,}756$, $h_{8s}=1991$, real $h_8=3139{,}4-0{,}9(1148{,}8)=2105{,}5$. Bomba: $h_6=173{,}9+\dfrac{v\Delta P}{\eta_B}=173{,}9+10{,}1=184{,}0$.

> [!solucion] Acoplamiento y flujos
> HRSG: $\dfrac{\dot m_v}{\dot m_g}=\dfrac{c_p(T_4-T_5)}{h_7-h_6}=\dfrac{1{,}005(373{,}6)}{2955{,}4}=0{,}127$.
> Trabajos específicos: $w_g=c_p[(T_3-T_4)-(T_2-T_1)]=258{,}3$ kJ/kg-gas; $w_v=(h_7-h_8)-w_B=1023{,}8$ kJ/kg-vapor.
> $$\dot m_g=\frac{45\,000}{w_g+0{,}127\,w_v}=\frac{45\,000}{388{,}4}=\boxed{115{,}9\ \text{kg/s}},\quad \dot m_v=0{,}127(115{,}9)=\boxed{14{,}7\ \text{kg/s}}.$$

> [!solucion] (a) Eficiencia y (c) trabajos
> $\dot Q_{in}=\dot m_g c_p(T_3-T_2)=115{,}9(1{,}005)(730{,}7)=85\,100$ kW:
> $$\eta=\frac{45\,000}{85\,100}=\boxed{52{,}9\%}.$$
> $$\dot W_{TG}=\dot m_g\,w_g=\boxed{29{,}9\ \text{MW}},\qquad \dot W_{TV}=\dot m_v\,w_v=\boxed{15{,}1\ \text{MW}}.$$

> [!info]
> El ciclo combinado alcanza $\sim53\%$ —muy superior al Brayton o al Rankine solos— porque el Rankine recupera el calor del escape del gas que de otro modo se perdería.

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton Simple | Brayton]] · [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine]] · [[Sistemas/Dispositivos Flujo/Intercambiadores | Intercambiadores]]
