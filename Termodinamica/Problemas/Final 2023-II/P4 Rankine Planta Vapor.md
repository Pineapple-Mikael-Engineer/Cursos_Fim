---
title: "P4 — Planta de vapor (Rankine simple)"
order: 5
tags: [termodinamica, problemas, ciclos, rankine]
draft: false
aliases: [Rankine 14 bar, planta vapor 20 MW]
---

# P4 — Planta de vapor (Rankine simple)

> [!definicion] Enunciado
> En una planta térmica que funciona con vapor, la presión en el caldero es $14$ bar, la temperatura del vapor en el condensador es $60\,^\circ$C y la calidad a la salida de la turbina es $95{,}66\%$. Se desprecia el trabajo de la bomba. Calcular: **(15)** temperatura máxima del ciclo [°C]; **(16)** presión en el condensador [kPa]; **(17)** eficiencia térmica [%]; **(18)** flujo de vapor [kg/s] si la turbina desarrolla $20$ MW; **(19)** flujo de combustible [kg/s] si $PC=40\,000$ kJ/kg; **(20)** temperatura de salida del agua de refrigeración [°C] si su flujo es $1200$ kg/s, $c_p=4{,}18$, y entra a $20\,^\circ$C.

![[rankine_diagrama_Ts.svg|340]]

> [!solucion] (15) y (16) Estados
> Salida de turbina (60 °C, $x=0{,}9566$): $s_4=s_f+x\,s_{fg}=0{,}8313+0{,}9566(7{,}0784)=7{,}602$ kJ/kg·K; $h_4=251{,}1+0{,}9566(2358{,}5)=2507$ kJ/kg.
> Turbina isentrópica $s_1=s_4=7{,}602$ a $P_1=14$ bar $\Rightarrow$ vapor sobrecalentado a $\boxed{T_{max}\approx500\,^\circ\text{C}}$ ($h_1=3474$ kJ/kg).
> Condensador: $\boxed{P_{cond}=P_{sat}(60\,^\circ\text{C})=19{,}94\ \text{kPa}}$.

> [!solucion] (17)–(19) Eficiencia y flujos
> Despreciando la bomba ($h_3\approx h_f(60°\text{C})=251{,}1$):
> $$\eta=\frac{h_1-h_4}{h_1-h_3}=\frac{3474-2507}{3474-251{,}1}=\boxed{30\%}.$$
> $$\dot m_v=\frac{\dot W}{h_1-h_4}=\frac{20\,000}{967}=\boxed{20{,}68\ \text{kg/s}};\quad \dot m_c=\frac{\dot m_v(h_1-h_3)}{PC}=\frac{20{,}68(3222{,}9)}{40\,000}=\boxed{1{,}666\ \text{kg/s}}.$$

> [!solucion] (20) Temperatura del agua de refrigeración
> Balance en el condensador, $\dot m_v(h_4-h_3)=\dot m_w c_p(T-20)$:
> $$20{,}68(2507-251{,}1)=1200(4{,}18)(T-20)\Rightarrow 46\,650=5016\,(T-20)\Rightarrow \boxed{T\approx29{,}3\,^\circ\text{C}}.$$

> [!warning] Discrepancia con la clave
> Los incisos 15–19 coinciden con la clave ($T_{max}=499{,}8$°C, $P=19{,}94$ kPa, $\eta=30\%$, $\dot m_v=20{,}68$, $\dot m_c=1{,}666$). En el (20) la clave da $46{,}27\,^\circ$C, pero con $\dot m_w=1200$ kg/s el aumento de temperatura es $\Delta T=46\,650/(1200\cdot4{,}18)=9{,}3\,^\circ$C, dando $T=29{,}3\,^\circ$C (el valor de la clave requeriría $\dot m_w\approx425$ kg/s).

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine Simple]] · [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]] · [[Calidad]] · [[Intercambiadores]]
