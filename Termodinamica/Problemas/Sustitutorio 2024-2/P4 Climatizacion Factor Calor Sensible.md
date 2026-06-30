---
title: "P4 — Climatización con factor de calor sensible"
order: 5
tags: [termodinamica, problemas, psicrometria]
draft: false
aliases: [factor de calor sensible, unidad climatización]
---

# P4 — Climatización con factor de calor sensible

> [!definicion] Enunciado
> Se enfría $200\ \text{m}^3/\text{min}$ de aire en una unidad de climatización desde $25\,^\circ$C de TBS y $60\%$ de humedad relativa, con un **factor de calor sensible (FCS) de $0{,}6$**, hasta la saturación, para luego calentarse con una resistencia hasta $20\,^\circ$C tras evacuar el condensado. Se pide **(a)** graficar; **(b)** condiciones del aire antes del calentamiento (TBS, $\phi$); **(c)** flujo de condensado [L/hr]; **(d)** capacidad frigorífica [kcal/hr]; **(e)** caudal de aire en el estado final.

![[proceso_enfriamiento_deshumidificacion.svg|420]]

> [!teoria]
> El **factor de calor sensible** $\text{FCS}=\dfrac{q_{sensible}}{q_{total}}=\dfrac{1{,}006(T_1-T_2)}{h_1-h_2}$ fija la dirección de la línea de proceso $1\to2$ en la carta. El estado 2 es la intersección de esa línea con la curva de saturación.

> [!solucion] Estado 1 y estado 2 (b)
> **1** ($25\,^\circ$C, $60\%$): $\omega_1=0{,}0119$ kg/kg, $h_1=55{,}5$ kJ/kg. Con $\text{FCS}=0{,}6$ y estado 2 saturado, iterando sobre la curva $\phi=100\%$ se obtiene
> $$\boxed{T_2\approx11{,}5\,^\circ\text{C},\quad \phi_2=100\%},\qquad \omega_2=0{,}00843,\ h_2=32{,}8\ \text{kJ/kg}.$$
> (Comprobación: $\text{FCS}=1{,}006(25-11{,}5)/(55{,}5-32{,}8)=13{,}6/22{,}7=0{,}60$ ✓.) Tras calentar a $20\,^\circ$C a $\omega$ constante: estado 3 con $\phi_3=58\%$.

> [!solucion] (c) Condensado
> $v_1=\dfrac{R_a T_1}{P-P_{v1}}=\dfrac{0{,}287(298{,}15)}{99{,}42}=0{,}861\ \text{m}^3/\text{kg}$, $\dot m_a=\dfrac{200}{0{,}861}=232{,}4$ kg/min.
> $$\dot m_w=\dot m_a(\omega_1-\omega_2)=232{,}4(0{,}0119-0{,}00843)=0{,}806\ \text{kg/min}=\boxed{48{,}4\ \text{L/hr}}.$$

> [!solucion] (d) Capacidad frigorífica
> $$\dot Q_L=\dot m_a(h_1-h_2)=232{,}4(22{,}7)=5275\ \text{kJ/min}=87{,}9\ \text{kW}=\boxed{75\,600\ \text{kcal/hr}}.$$

> [!solucion] (e) Caudal final
> $v_3=\dfrac{R_a T_3}{P-P_{v3}}=\dfrac{0{,}287(293{,}15)}{99{,}97}=0{,}842\ \text{m}^3/\text{kg}$:
> $$\dot V_3=\dot m_a\,v_3=232{,}4(0{,}842)=\boxed{195{,}6\ \text{m}^3/\text{min}}\;(\approx11\,740\ \text{m}^3/\text{hr}).$$

> [!referencia]
> [[Procesos Psicrometricos | Procesos Psicrométricos]] · [[Carta Psicrometrica | Carta Psicrométrica]] · [[Psicrometria/index | Psicrometría]]
