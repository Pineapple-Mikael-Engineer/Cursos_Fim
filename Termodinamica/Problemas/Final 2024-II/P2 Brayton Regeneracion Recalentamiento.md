---
title: "P2 — Brayton con recalentamiento y regenerador (12 MW)"
order: 3
tags:
  - termodinamica
  - problemas
  - ciclos
  - brayton
draft: false
aliases:
  - turbina de gas examen final
  - Brayton regenerador recalentamiento
---

# P2 — Brayton con recalentamiento y regenerador (12 MW)

> [!definicion] Enunciado
> Una **turbina a gas** produce una potencia al eje de $\dot W_{eje}=12\,000\ \text{kW}$ y está constituida por **2 etapas de expansión** montadas en el mismo eje, con **recalentamiento intermedio a la presión teórica óptima** y hasta la temperatura máxima del ciclo. Posee un **regenerador de $75\%$ de eficiencia** a la salida del compresor y antes de la primera cámara de combustión. Se cumplen:
> - $P$ entrada compresor $=100\ \text{kPa}$, $T$ entrada compresor $=290\ \text{K}$.
> - $P$ máx del ciclo $=9\ \text{bar}$, $T$ máx del ciclo $=1200\ \text{K}$.
> - Eficiencia adiabática de compresión $=$ eficiencia adiabática de expansión $=90\%$.
> - $PC=44\,000\ \text{kJ/kg}$. Aire estándar: $c_p=1{,}0035\ \text{kJ/kg·K}$, $k=1{,}4$.
>
> Se pide: **(6)** $T$ del aire a la entrada de la 1ª cámara de combustión [K]; **(7)** relación aire-combustible $r_{a/c}$ en la 1ª cámara; **(8)** trabajo neto [kJ/kg]; **(9)** flujo de aire al compresor [kg/min]; **(10)** eficiencia térmica [%].

## Estrategia

> [!teoria]
> Ciclo [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton con Regeneración | Brayton con regeneración]] y recalentamiento. Cada compresión/expansión usa la relación isentrópica del [[Gas Ideal | gas ideal]] $T_2/T_1=(P_2/P_1)^{(k-1)/k}$ corregida por la [[Sistemas/Dispositivos Flujo/Compresores | eficiencia adiabática]]. El recalentamiento a presión **óptima** parte en dos iguales la relación de expansión; el regenerador precalienta el aire con el escape.

![[brayton_regeneracion_esquema.svg|480]]

## Presión óptima y estados isentrópicos

> [!solucion] Presión intermedia óptima
> Para dos etapas de expansión con recalentamiento, el reparto óptimo iguala las relaciones de presión:
> $$P_i=\sqrt{P_{max}\,P_{min}}=\sqrt{900\cdot100}=300\ \text{kPa}.$$
> Cada etapa expande con relación $r_p=3$ (de $900$ a $300$ y de $300$ a $100$). El exponente es $(k-1)/k=0{,}2857$.

> [!info] Estados (K)
> | | 1 | 2 | 3 | 4 | 5 | 6 | X (regen.) |
> |:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | $P$ [kPa] | 100 | 900 | 900 | 300 | 300 | 100 | 900 |
> | $T$ isentrópico | 290 | 543{,}3 | 1200 | 876{,}7 | 1200 | 876{,}7 | — |
> | $T$ real | 290 | **571{,}4** | 1200 | **909{,}0** | 1200 | **909{,}0** | **824{,}6** |
>
> **Compresor** $1\to2$: $T_{2s}=290\,(9)^{0{,}2857}=543{,}3$ K; real $T_{2r}=290+\dfrac{543{,}3-290}{0{,}9}=571{,}4$ K.
> **Turbina AP** $3\to4$: $T_{4s}=1200\,(1/3)^{0{,}2857}=876{,}7$ K; real $T_{4r}=1200-0{,}9(1200-876{,}7)=909{,}0$ K.
> **Turbina BP** $5\to6$: por simetría ($r_p=3$, $T_5=1200$): $T_{6r}=909{,}0$ K.

## (6) Temperatura a la entrada de la 1ª cámara

> [!solucion]
> El regenerador precalienta el aire del compresor ($T_{2r}=571{,}4$) usando el escape ($T_{6r}=909{,}0$), con efectividad $\varepsilon=0{,}75$:
> $$T_X=T_{2r}+\varepsilon\,(T_{6r}-T_{2r})=571{,}4+0{,}75\,(909{,}0-571{,}4)=\boxed{824{,}6\ \text{K}}.$$
> Esta es la temperatura del aire que **entra a la 1ª cámara de combustión**.

## (7) Relación aire-combustible

> [!solucion]
> Balance de energía en la 1ª cámara ($X\to3$): el combustible aporta $\dot m_c\,PC$ y calienta el aire de $T_X$ a $T_3$:
> $$\dot m_c\,PC=\dot m_a\,c_p\,(T_3-T_X)\ \Rightarrow\ r_{a/c}=\frac{PC}{c_p\,(T_3-T_X)}=\frac{44\,000}{1{,}0035\,(1200-824{,}6)}=\boxed{116{,}8\ \tfrac{\text{kg aire}}{\text{kg comb.}}}.$$

## (8) Trabajo neto

> [!solucion]
> Trabajo de las dos turbinas menos el del compresor:
> $$w_T=c_p\big[(T_3-T_{4r})+(T_5-T_{6r})\big]=1{,}0035\,(291+291)=584{,}0\ \text{kJ/kg},$$
> $$w_C=c_p\,(T_{2r}-T_1)=1{,}0035\,(571{,}4-290)=282{,}4\ \text{kJ/kg},$$
> $$\boxed{w_{neto}=w_T-w_C=584{,}0-282{,}4=301{,}6\ \text{kJ/kg}}.$$

## (9) Flujo de aire

> [!solucion]
> $$\dot m_a=\frac{\dot W_{eje}}{w_{neto}}=\frac{12\,000}{301{,}6}=39{,}79\ \text{kg/s}=\boxed{2387\ \text{kg/min}}.$$

## (10) Eficiencia térmica

> [!solucion]
> El calor aportado por el combustible es el de **ambas cámaras**. Gracias al regenerador, la 1ª cámara solo calienta desde $T_X$ (no desde $T_{2r}$):
> $$q_A=c_p\,(T_3-T_X)+c_p\,(T_5-T_{4r})=1{,}0035\,(1200-824{,}6)+1{,}0035\,(1200-909)=376{,}7+292{,}0=668{,}7\ \text{kJ/kg}.$$
> $$\eta=\frac{w_{neto}}{q_A}=\frac{301{,}6}{668{,}7}=\boxed{45{,}1\%}.$$

> [!warning] Discrepancia con la clave
> La clave manuscrita reporta $\eta=32{,}68\%$ porque en el denominador usó $q_A=c_p(T_3-T_{2r})+\dots$ con $T_{2r}=571{,}4$ K, es decir, **ignoró el regenerador en el calor aportado** — pese a haberlo usado correctamente ($T_X=824{,}6$) en la razón aire-combustible. Eso es inconsistente: si el aire entra a la cámara a $824{,}6$ K, el combustible solo debe cubrir $T_3-T_X$. La eficiencia físicamente correcta es **$45{,}1\%$** (el regenerador *sube* la eficiencia, no la baja). Los demás resultados (6–9) coinciden con la clave.

## Notas usadas

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton con Regeneración | Brayton con Regeneración]] · [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton Simple | Brayton Simple]] · [[Gas Ideal]] · [[Combustion/index | Combustión]]
