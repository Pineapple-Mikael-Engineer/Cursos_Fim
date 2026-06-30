---
title: "P2 — Turborreactor (avión turbo jet)"
order: 3
tags: [termodinamica, problemas, ciclos, brayton, propulsion]
draft: false
aliases: [turbojet, turborreactor, propulsión a chorro]
---

# P2 — Turborreactor (avión turbo jet)

> [!definicion] Enunciado
> Un avión turbo jet vuela a $280\ \text{m/s}$. El aire entra al **difusor** a $-10\,^\circ$C y $80$ kPa, la relación de presiones en el **compresor** es $10$, la temperatura máxima del ciclo es $1100\,^\circ$C, el trabajo de la **turbina** es el justo para mover el compresor, los gases se expanden en la **tobera** bajo un proceso adiabático reversible y salen a $80$ kPa, el flujo de gases es $60$ kg/s. Se pide: **(5)** $T$ y $P$ en el punto 4; **(6)** $P$ y $T$ en el punto 2; **(7)** velocidad de salida (punto 5); **(8)** potencia de propulsión; **(9)** eficiencia de propulsión.

## Estrategia

> [!teoria]
> Ciclo de propulsión: difusor $a\to1$ (frena el aire, sube $h$), compresor $1\to2$, cámara $2\to3$, turbina $3\to4$ ($w_T=w_C$), tobera $4\to5$ (acelera el chorro). Se usan **tablas de aire real** (CATT3): la entalpía de estancamiento $h_0=h+\tfrac{C^2}{2}$ se conserva en difusor y tobera; los procesos isentrópicos usan $s_2=s_1+R\ln(P_2/P_1)$.

> [!info] Estados (aire, CATT3)
> | | $a$ | 1 | 2 | 3 | 4 | 5 |
> |:---|:---:|:---:|:---:|:---:|:---:|:---:|
> | $h$ [kJ/kg] | 263{,}5 | 302{,}7 | 584{,}7 | 1483 | 1201 | 690{,}1 |
> | $P$ [kPa] | 80 | 129{,}84 | 1298{,}5 | 1298{,}5 | 590{,}8 | 80 |
> | $T$ | −10°C | — | 305{,}2°C | 1100°C | 861{,}2°C | — |

> [!solucion] (6) Estado 2 (salida del compresor)
> Difusor $a\to1$: $h_1=h_a+\tfrac{C_a^2}{2}=263{,}5+\tfrac{280^2}{2}\times10^{-3}=302{,}7$ kJ/kg, de donde $s_1=6{,}877$. La presión de estancamiento: $s_1=s_a+R\ln(P_1/P_a)\Rightarrow P_1=129{,}84$ kPa. Compresor ($r_p=10$): $P_2=10\,P_1=\boxed{1298{,}5\ \text{kPa}}$; isentrópico $s_2=s_1\Rightarrow h_2=584{,}7$, $\boxed{T_2=305{,}2\,^\circ\text{C}}$.

> [!solucion] (5) Estado 4 (salida de turbina)
> El trabajo de turbina iguala el del compresor: $h_3-h_4=h_2-h_1$:
> $$h_4=1483-(584{,}7-302{,}7)=1201\ \text{kJ/kg}\ \Rightarrow\ \boxed{T_4=861{,}2\,^\circ\text{C}},\quad \boxed{P_4=590{,}8\ \text{kPa}}.$$

> [!solucion] (7) Velocidad de salida (tobera $4\to5$, isentrópica a 80 kPa)
> Con $s_5=s_4$ y $P_5=80$ kPa: $h_5=690{,}1$ kJ/kg. Conservación de $h_0$:
> $$h_4=h_5+\tfrac{C_5^2}{2}\Rightarrow C_5=\sqrt{2(h_4-h_5)\times10^3}=\sqrt{2(1201-690{,}1)\times10^3}=\boxed{1010\ \text{m/s}}.$$

> [!solucion] (8) y (9) Potencia y eficiencia de propulsión
> Empuje $F=\dot m(C_5-C_a)$; potencia de propulsión $\dot W_p=F\,C_a$:
> $$\dot W_p=\dot m(C_5-C_a)\,C_a=60(1010-280)(280)\times10^{-3}=\boxed{12\,279\ \text{kW}}.$$
> Calor aportado $\dot Q_A=\dot m(h_3-h_2)=60(1483-584{,}7)=53\,898$ kW:
> $$\eta_p=\frac{\dot W_p}{\dot Q_A}=\frac{12\,279}{53\,898}=\boxed{22{,}78\%}.$$

> [!info] Verificación
> Todos los valores coinciden con la clave manuscrita ($P_4=590{,}8$ kPa, $C_5=1010$ m/s, $\dot W_p=12\,279$ kW, $\eta_p=22{,}78\%$).

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Brayton/index | Brayton]] · [[Toberas]] · [[Difusores]] · [[Gas Ideal]]
