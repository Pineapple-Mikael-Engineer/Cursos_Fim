---
title: "P4 — Motor Diesel (8 cilindros)"
order: 5
tags:
  - termodinamica
  - problemas
  - ciclos
  - diesel
draft: false
aliases:
  - motor Diesel examen final
  - ciclo Diesel 8 cilindros
---

# P4 — Motor Diesel (8 cilindros)

> [!definicion] Enunciado
> Un motor Diesel de **8 cilindros** y $1000\ \text{rpm}$ tiene $r_k=20$, $r_{a/c}=25$, $PC=40\,000\ \text{kJ/kg}$, $m=0{,}04\ \text{kg/cilindro}$ (aire por ciclo), factor de diagrama $f_d=0{,}78$, eficiencia mecánica $\eta_m=0{,}85$, $P_1=1\ \text{bar}$, $T_1=27\,^\circ\text{C}=300\ \text{K}$. Aire estándar: $k=1{,}4$, $c_p=1{,}0035\ \text{kJ/kg·K}$.
>
> Se pide: **(15)** temperatura al final de la compresión [K]; **(16)** eficiencia del ciclo [%]; **(17)** trabajo indicado; **(18)** potencia al eje [kW].

## Estrategia

> [!teoria]
> Ciclo [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Diesel | Diesel]] aire-estándar: compresión isentrópica $1\to2$, adición **isobárica** $2\to3$, expansión isentrópica $3\to4$, rechazo isocórico $4\to1$. La combustión a presión constante fija la relación de corte $r_c=V_3/V_2$.

![[diesel_diagrama_Pv.svg|360]]

## (15) Temperatura al final de la compresión

> [!solucion]
> $$T_2=T_1\,r_k^{k-1}=300\,(20)^{0{,}4}=\boxed{994{,}3\ \text{K}}.$$
> Combustión isobárica ($2\to3$): $\ \dot m_c\,PC=\dot m_a\,c_p\,(T_3-T_2)$, con $PC=r_{a/c}\,c_p\,(T_3-T_2)$:
> $$40\,000=25\cdot1{,}0035\,(T_3-994{,}3)\ \Rightarrow\ T_3=2588{,}8\ \text{K},\qquad r_c=\frac{T_3}{T_2}=2{,}6.$$

## (16) Eficiencia del ciclo

> [!solucion]
> $$\eta_D=1-\frac{1}{r_k^{\,k-1}}\,\frac{r_c^{\,k}-1}{k\,(r_c-1)}=1-(20)^{-0{,}4}\,\frac{2{,}6^{1{,}4}-1}{1{,}4\,(2{,}6-1)}=1-0{,}3017\cdot1{,}254=\boxed{62{,}1\%}.$$

## (17) Trabajo indicado

> [!solucion]
> Calor y trabajo ideal por cilindro y ciclo. Masa de combustible $m_c=m_a/r_{a/c}=0{,}04/25=1{,}6\times10^{-3}$ kg:
> $$Q_A=m_c\,PC=1{,}6\times10^{-3}\cdot40\,000=64\ \text{kJ},\qquad W=\eta_D\,Q_A=0{,}6216\cdot64=39{,}8\ \text{kJ}.$$
> El trabajo **indicado** aplica el factor de diagrama:
> $$\boxed{W_{ind}=f_d\,W=0{,}78\cdot39{,}8=31{,}0\ \text{kJ}}\quad(\text{por cilindro y ciclo}).$$

## (18) Potencia al eje

> [!solucion]
> Potencia indicada (8 cilindros, $\tfrac{\text{rpm}}{120}$ ciclos/s por cilindro en 4 tiempos) corregida por la eficiencia mecánica:
> $$\dot W_{eje}=W_{ind}\cdot\frac{\text{rpm}}{120}\cdot N\cdot\eta_m=31{,}0\cdot\frac{1000}{120}\cdot8\cdot0{,}85=\boxed{1757\ \text{kW}}.$$

> [!warning] Discrepancia con la clave
> La clave reporta $1550\ \text{kW}$, pero $31\cdot\tfrac{1000}{120}\cdot8\cdot0{,}85=31\cdot8{,}333\cdot8\cdot0{,}85=1756{,}7\ \text{kW}$ (desliz aritmético en la clave). Los incisos 15–17 coinciden con la clave ($T_2=994{,}3$ K, $\eta=62{,}1\%$, $W_{ind}=31$ kJ).

## Notas usadas

> [!referencia]
> [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Diesel | Ciclo Diesel]] · [[Gas Ideal]] · [[Proceso Adiabatico]] · [[Proceso Isobarico]]
