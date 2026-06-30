---
title: "P6 — Psicrometría: enfriamiento y deshumidificación"
order: 7
tags:
  - termodinamica
  - problemas
  - psicrometria
draft: false
aliases:
  - deshumidificación examen final
  - serpentín de enfriamiento
---

# P6 — Psicrometría: enfriamiento y deshumidificación

> [!definicion] Enunciado
> En un proceso de deshumidificación, el aire atmosférico entra a $30\,^\circ$C de TBS (bulbo seco) y $26\,^\circ$C de TBH (bulbo húmedo), a razón de $300\ \text{m}^3/\text{min}$. Pasa por un **serpentín de enfriamiento** y posteriormente se le transfiere calor mediante un **serpentín de calentamiento** hasta $21\,^\circ$C y $50\%$ de humedad relativa. Se pide mostrar los procesos en un diagrama psicrométrico y llenar la tabla de datos; luego **(17)** calcular la masa de agua condensada y **(18)** el calor transferido en el calentamiento. $P=101{,}325$ kPa.

## Estrategia

> [!teoria]
> Proceso de [[Procesos Psicrometricos | enfriamiento con deshumidificación]] (1→2) seguido de [[Procesos Psicrometricos | calentamiento sensible]] (2→3). El enfriamiento baja la temperatura hasta saturación y condensa agua; el calentamiento sube la temperatura a $\omega$ constante. Las propiedades se obtienen de la [[Carta Psicrometrica | carta psicrométrica]] o de $\omega=0{,}622\,P_v/(P-P_v)$ y $h=1{,}006\,T+\omega(2501+1{,}805\,T)$.

![[proceso_enfriamiento_deshumidificacion.svg|440]]

## Estados

> [!solucion] Estado 1 (entrada)
> Con TBS$=30$, TBH$=26$: usando $\omega_{s}(26\,^\circ\text{C})=0{,}02133$ y la relación de bulbo húmedo,
> $$\omega_1=\frac{(2501-2{,}326\cdot26)\,\omega_{s,bh}-1{,}006(30-26)}{2501+1{,}805\cdot30-4{,}186\cdot26}=0{,}0196\ \text{kg/kg}.$$
> $P_{v1}=\dfrac{P\,\omega_1}{0{,}622+\omega_1}=3{,}10$ kPa $\Rightarrow \phi_1=\dfrac{3{,}10}{P_{sat}(30)}=\dfrac{3{,}10}{4{,}246}=73\%$. $h_1=1{,}006(30)+0{,}0196(2555)=80{,}3$ kJ/kg. $T_{rocío,1}\approx24{,}6\,^\circ$C.

> [!solucion] Estado 3 (salida)
> TBS$=21$, $\phi=50\%$: $P_{v3}=0{,}5\,P_{sat}(21)=0{,}5(2{,}487)=1{,}244$ kPa.
> $$\omega_3=\frac{0{,}622(1{,}244)}{101{,}325-1{,}244}=0{,}00773\ \text{kg/kg},\qquad h_3=1{,}006(21)+0{,}00773(2539)=40{,}8\ \text{kJ/kg}.$$
> $T_{rocío,3}\approx10{,}1\,^\circ$C.

> [!solucion] Estado 2 (salida del serpentín de enfriamiento)
> El calentamiento $2\to3$ es a $\omega$ constante, luego $\omega_2=\omega_3=0{,}00773$. El aire sale del enfriador **saturado** ($\phi_2=100\%$) a la temperatura de rocío correspondiente:
> $$T_2=T_{rocío}(\omega_2)=10{,}1\,^\circ\text{C},\qquad h_2=1{,}006(10{,}1)+0{,}00773(2519)=29{,}6\ \text{kJ/kg}.$$

> [!info] Tabla de datos
> | Estado | TBS [°C] | TBH [°C] | $\phi$ | $\omega$ [kg/kg] | $h$ [kJ/kg] | $T_R$ [°C] |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | 1 (entrada) | 30 | 26 | 73% | 0{,}0196 | 80{,}3 | 24{,}6 |
> | 2 (post-enfriamiento) | 10{,}1 | 10{,}1 | 100% | 0{,}00773 | 29{,}6 | 10{,}1 |
> | 3 (salida) | 21 | ≈14{,}8 | 50% | 0{,}00773 | 40{,}8 | 10{,}1 |

## (17) Masa de agua condensada

> [!solucion]
> Flujo de aire seco a partir del volumen específico en el estado 1:
> $$v_1=\frac{R_a T_1}{P-P_{v1}}=\frac{0{,}287(303{,}15)}{101{,}325-3{,}10}=0{,}886\ \tfrac{\text{m}^3}{\text{kg aire seco}},\qquad \dot m_a=\frac{300}{0{,}886}=338{,}7\ \tfrac{\text{kg}}{\text{min}}.$$
> El agua condensada es la caída de humedad específica ($1\to2$):
> $$\dot m_w=\dot m_a\,(\omega_1-\omega_2)=338{,}7\,(0{,}0196-0{,}00773)=\boxed{4{,}0\ \text{kg/min}}.$$

## (18) Calor en el calentamiento

> [!solucion]
> El calentamiento $2\to3$ es sensible (a $\omega$ constante):
> $$\dot Q_{cal}=\dot m_a\,(h_3-h_2)=338{,}7\,(40{,}8-29{,}6)=3793\ \text{kJ/min}=\boxed{63{,}2\ \text{kW}}.$$

> [!info] Verificación
> El proceso 1→2 (enfriamiento + deshumidificación) baja $T$ y $\omega$ hasta saturación; el 2→3 (calentamiento) recupera $21\,^\circ$C a $\omega$ fijo, bajando la humedad relativa a $50\%$. La condensación retira $4{,}0$ kg/min de agua.

## Notas usadas

> [!referencia]
> [[Procesos Psicrometricos | Procesos Psicrométricos]] · [[Carta Psicrometrica | Carta Psicrométrica]] · [[Psicrometria/index | Psicrometría]]
