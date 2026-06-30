---
title: "P01 — Rankine con análisis de factibilidad económica"
order: 2
tags: [termodinamica, problemas, ciclos, rankine, economia]
draft: false
aliases: [Rankine factibilidad económica, planta 10 MW costo vapor]
---

# P01 — Rankine con análisis de factibilidad económica

> [!definicion] Enunciado
> Una planta de vapor que sigue un ciclo Rankine opera entre $20$ MPa y $1$ atm para generar $10$ MW para una pequeña aglomeración urbana. La municipalidad invertirá $30$ millones de dólares por año en operarla. Detalles: la caldera entrega vapor sobrecalentado a $35\,^\circ$C sobre la temperatura de saturación; la turbina tiene rendimiento $80\%$ y la bomba es isentrópica; el costo de cada kilogramo de vapor producido es $0{,}05$ USD; la planta funciona $24$ h/día, $365$ días/año. Determinar **(6)** el costo anual de funcionamiento; **(7)** el rendimiento de la planta; **(8)** si el proyecto es factible.

## Estrategia

> [!teoria]
> Ciclo [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine]] con [[Sistemas/Dispositivos Flujo/Turbinas | turbina]] de eficiencia $80\%$. El flujo de vapor $\dot m$ se obtiene de la potencia; el costo anual es $\dot m\times(\text{kg/año})\times0{,}05$.

![[rankine_diagrama_Ts.svg|330]]

> [!solucion] Estados
> $T_{sat}(20\,\text{MPa})=365{,}8\,^\circ$C $\Rightarrow T_3=365{,}8+35=400{,}8\,^\circ$C. Condensador a $1$ atm ($0{,}1$ MPa, $99{,}6\,^\circ$C).
> - **1** (líq. sat. $0{,}1$ MPa): $h_1=417{,}5$, $v_1=0{,}001043$.
> - **2** (bomba a $20$ MPa): $w_B=v_1\Delta P=20{,}76$ kJ/kg, $h_2=438{,}2$.
> - **3** ($20$ MPa, $400{,}8\,^\circ$C): $h_3=2813{,}1$, $s_3=5{,}553$.
> - **4** (turbina a $0{,}1$ MPa): $x_{4s}=\dfrac{5{,}553-1{,}303}{6{,}057}=0{,}702$, $h_{4s}=2002{,}3$; real $h_{4r}=2813{,}1-0{,}8(810{,}8)=2165{,}5$.

> [!solucion] (6) Costo anual y flujo de vapor
> $\dot m=\dfrac{\dot W}{(h_3-h_{4r})-w_B}=\dfrac{10\,000}{647{,}6-20{,}76}=15{,}32$ kg/s. Segundos por año $=365\cdot24\cdot3600=3{,}154\times10^7$:
> $$\text{Costo}=\dot m\cdot(\text{s/año})\cdot0{,}05=15{,}32\cdot3{,}154\times10^7\cdot0{,}05=\boxed{24{,}16\ \text{millones USD/año}}.$$

> [!solucion] (7) Rendimiento de la planta
> $$\eta=\frac{\dot W_{neto}}{\dot m\,(h_3-h_2)}=\frac{10\,000}{15{,}32\,(2813{,}1-438{,}2)}=\boxed{27{,}42\%}.$$

> [!solucion] (8) Factibilidad
> La inversión disponible ($30$ M USD) supera el costo anual ($24{,}16$ M USD):
> $$\boxed{\text{El proyecto es factible}}\quad(\text{superávit }\approx5{,}84\ \text{M USD/año}).$$

> [!info]
> Coincide con la clave ($\eta=27{,}42\%$, costo $24{,}16$ M USD, factible). Tipo aplicado: combina el ciclo termodinámico con un análisis económico.

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Simple | Rankine Simple]] · [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]]
