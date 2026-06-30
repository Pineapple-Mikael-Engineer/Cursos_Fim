---
title: "P3 — Motor de explosión (ciclo Otto)"
order: 4
tags:
  - termodinamica
  - problemas
  - ciclos
  - otto
draft: false
aliases:
  - motor Otto examen final
  - ciclo de explosión
---

# P3 — Motor de explosión (ciclo Otto)

> [!definicion] Enunciado
> Un motor teórico de explosión de **4 tiempos** tiene una relación de compresión $r_k=7{,}5$, la temperatura máxima del ciclo es $T_{max}=2524\ \text{K}$, la eficiencia de combustión $90\%$, las condiciones al inicio de la compresión son $P_1=1\ \text{bar}$, $T_1=27\,^\circ\text{C}=300\ \text{K}$, y el poder calorífico del combustible $PC=44\,250\ \text{kJ/kg}$. Aire estándar: $k=1{,}4$, $c_v=0{,}718\ \text{kJ/kg·K}$, $R=0{,}287\ \text{kJ/kg·K}$.
>
> Se pide: **(11)** relación aire-combustible $r_{a/c}$; **(12)** potencia teórica [kW] si gira a $4200\ \text{rpm}$ con $1800\ \text{cm}^3$ de cilindrada; **(13)** eficiencia del ciclo [%]; **(14)** trabajo específico neto [kJ/kg].

## Estrategia

> [!teoria]
> Ciclo [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Otto | Otto]] aire-estándar: compresión isentrópica $1\to2$, adición de calor **isocórica** $2\to3$ (combustión), expansión isentrópica $3\to4$, rechazo isocórico $4\to1$. La combustión fija $r_{a/c}$ por balance de energía; la cilindrada fija la masa por ciclo.

![[otto_diagrama_Pv.svg|360]]

## (11) Relación aire-combustible

> [!solucion]
> Compresión isentrópica:
> $$T_2=T_1\,r_k^{k-1}=300\,(7{,}5)^{0{,}4}=671{,}65\ \text{K}.$$
> Combustión isocórica ($2\to3$, con eficiencia de combustión $\eta_{comb}=0{,}90$):
> $$\eta_{comb}\,\dot m_c\,PC=\dot m_a\,c_v\,(T_3-T_2)\ \Rightarrow\ r_{a/c}=\frac{\eta_{comb}\,PC}{c_v\,(T_3-T_2)}=\frac{0{,}90\cdot44\,250}{0{,}718\,(2524-671{,}65)}=\boxed{30}.$$

## (12) Potencia teórica

> [!solucion]
> Volumen al inicio ($V_1$) desde la cilindrada $V_1-V_2=1800\ \text{cm}^3$ y $V_2=V_1/r_k$:
> $$V_1\Big(1-\tfrac{1}{7{,}5}\Big)=1800\ \Rightarrow\ V_1=2076{,}9\ \text{cm}^3.$$
> Masa de aire por ciclo:
> $$m_a=\frac{P_1 V_1}{R\,T_1}=\frac{100\cdot2076{,}9\times10^{-6}}{0{,}287\cdot300}=2{,}412\times10^{-3}\ \text{kg}.$$
> Masa de combustible y calor por ciclo:
> $$m_c=\frac{m_a}{r_{a/c}}=\frac{2{,}412\times10^{-3}}{30}=8{,}04\times10^{-5}\ \text{kg},\qquad Q_A=m_c\,PC=3{,}558\ \text{kJ}.$$
> Con la eficiencia del ciclo (inciso 13, $\eta=0{,}5533$), el trabajo por ciclo $W=\eta\,Q_A=1{,}9688\ \text{kJ}$. En 4 tiempos hay $\tfrac{\text{rpm}}{120}$ ciclos de potencia por segundo:
> $$\dot W=W\cdot\frac{\text{rpm}}{120}=1{,}9688\cdot\frac{4200}{120}=\boxed{69\ \text{kW}}.$$

## (13) Eficiencia del ciclo

> [!solucion]
> $$\eta=1-\frac{1}{r_k^{\,k-1}}=1-(7{,}5)^{-0{,}4}=\boxed{55{,}33\%}.$$

## (14) Trabajo específico neto

> [!solucion]
> $$w_{neto}=\frac{W}{m_a}=\frac{1{,}9688}{2{,}412\times10^{-3}}=\boxed{816{,}25\ \text{kJ/kg}}.$$

> [!info] Verificación
> Todos los resultados coinciden con la clave ($r_{a/c}=30$, $\dot W=69$ kW, $\eta=55{,}33\%$, $w=816{,}25$ kJ/kg). La eficiencia depende **solo** de $r_k$, no de $T_{max}$.

## Notas usadas

> [!referencia]
> [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Otto | Ciclo Otto]] · [[Gas Ideal]] · [[Proceso Adiabatico]] · [[Combustion/index | Combustión]]
