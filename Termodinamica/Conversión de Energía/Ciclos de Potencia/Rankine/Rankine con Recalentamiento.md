---
title: "Rankine con Recalentamiento"
order: 2
tags:
  - termodinamica
  - ciclos
  - rankine
  - recalentamiento
  - reheat
draft: false
aliases:
  - Rankine con Recalentamiento
  - Reheat Rankine
  - ciclo Rankine reheat
---

# Rankine con Recalentamiento

> [!definicion]
> En el **ciclo Rankine con recalentamiento** la expansión en la turbina se divide en **dos etapas** con un **calentamiento intermedio** (recalentamiento) del vapor entre ellas. El vapor sale de la primera turbina de alta presión (TAP), retorna a la caldera para ser calentado nuevamente a la misma presión pero mayor temperatura, y luego se expande en la segunda turbina de baja presión (TBP).
>
> *¿Por qué se usa?* En el ciclo Rankine simple, aumentar la presión de la caldera eleva la eficiencia pero reduce la calidad del vapor a la salida ($x_4$), lo que daña los álabes de la turbina. El recalentamiento resuelve ambos problemas simultáneamente: permite operar a alta presión en la TAP sin generar vapor húmedo en la TBP.

![[rankine_recalentamiento_esquema.svg|500]]
*Ciclo Rankine con recalentamiento. El vapor expande en la TAP de $P_3$ a $P_r$ (presión de recalentamiento), retorna a la caldera (proceso 4→5), y expande en la TBP de $P_r$ hasta $P_L$ (proceso 5→6). El condensador, bomba y caldera son los mismos del ciclo simple.*

---

## Estados del ciclo y nomenclatura

| Estado | Descripción |
|:---:|:---|
| 1 | Líquido saturado a $P_L$ (salida condensador) |
| 2 | Líquido comprimido a $P_H$ (salida bomba) |
| 3 | Vapor sobrecalentado a $P_H$, $T_3$ (entrada TAP) |
| 4 | Salida de TAP a $P_r$ (presión de recalentamiento) |
| 5 | Vapor recalentado a $P_r$, $T_5$ (entrada TBP, normalmente $T_5 \approx T_3$) |
| 6 | Salida TBP a $P_L$ (entrada condensador) |

---

## Balances de energía

> [!proposicion]
> Aplicando primera ley a cada dispositivo:
>
> **Trabajo total de turbina:**
> $$
> w_T = (h_3 - h_4) + (h_5 - h_6).
> $$
>
> **Calor total de entrada** (caldera + recalentador, ambos isobáricos):
> $$
> q_H = (h_3 - h_2) + (h_5 - h_4).
> $$
>
> **Calor rechazado** (condensador):
> $$
> q_L = h_6 - h_1.
> $$
>
> **Eficiencia térmica:**
> $$
> \eta_{\rm th} = \frac{w_T - w_P}{q_H} = \frac{(h_3-h_4)+(h_5-h_6)-(h_2-h_1)}{(h_3-h_2)+(h_5-h_4)}.
> $$

---

## Elección óptima de la presión de recalentamiento

> [!teoria]
> La presión de recalentamiento $P_r$ es un parámetro de diseño. Existen dos efectos opuestos:
>
> - Si $P_r \to P_H$ (recalentamiento temprano): se añade mucho calor a temperatura alta → $\eta_{\rm th}\uparrow$, pero la TBP maneja casi todo el rango de expansión y la calidad $x_6$ mejora poco.
> - Si $P_r \to P_L$ (recalentamiento tardío): el recalentador añade calor a temperatura baja → $\eta_{\rm th}\downarrow$.
>
> En la práctica, la presión óptima de recalentamiento está en el rango $P_r \approx P_H/4$ a $P_H/5$, y se elige de modo que la temperatura de salida de ambas turbinas sea similar, maximizando la calidad $x_6 \geq 0.88$.

---

## Ejemplo: Rankine con recalentamiento a 500°C/3 MPa

> [!ejemplo]
> Ciclo Rankine ideal con recalentamiento:
> - Caldera: $P_H = 15\,\mathrm{MPa}$, $T_3 = 500°\mathrm{C}$.
> - Presión de recalentamiento: $P_r = 3\,\mathrm{MPa}$, $T_5 = 500°\mathrm{C}$.
> - Condensador: $P_L = 10\,\mathrm{kPa}$.
>
> Determinar: (a) entalpías y calidades en todos los estados; (b) $\eta_{\rm th}$; (c) comparar $x_6$ con el ciclo sin recalentamiento.

> [!solucion]
> **Estado 1** ($P_L = 10\,\mathrm{kPa}$, líquido saturado):
> $h_1 = 191.8\,\mathrm{kJ/kg}$, $v_1 = 0.001010\,\mathrm{m^3/kg}$.
>
> **Estado 2** ($P_H = 15000\,\mathrm{kPa}$):
> $h_2 = 191.8 + 0.001010\times(15000-10) = 191.8 + 15.14 = 206.9\,\mathrm{kJ/kg}$.
>
> **Estado 3** ($15\,\mathrm{MPa}$, $500°\mathrm{C}$):
> $h_3 = 3310.8\,\mathrm{kJ/kg}$, $s_3 = 6.3480\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 4** (expansión isentrópica a $P_r = 3\,\mathrm{MPa}$, $s_4 = s_3 = 6.3480$):
> A $3\,\mathrm{MPa}$: $T_{\rm sat} = 234.0°\mathrm{C}$, $s_g = 6.1869$. Como $s_4 = 6.3480 > s_g$: vapor sobrecalentado.
> Interpolando en tablas de vapor sobrecalentado a $3\,\mathrm{MPa}$:
> A $250°\mathrm{C}$: $s = 6.2872$, $h = 2803.3$; a $300°\mathrm{C}$: $s = 6.5390$, $h = 2924.5$.
> Interpolando: $T_4 = 250 + (6.3480-6.2872)/(6.5390-6.2872)\times50 = 250 + 0.0608/0.2518\times50 = 250+12.1 = 262.1°\mathrm{C}$.
> $h_4 = 2803.3 + 0.242\times(2924.5-2803.3) = 2803.3 + 29.3 = 2832.6\,\mathrm{kJ/kg}$.
>
> **Estado 5** ($3\,\mathrm{MPa}$, $500°\mathrm{C}$, recalentado):
> $h_5 = 3456.5\,\mathrm{kJ/kg}$, $s_5 = 7.2338\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 6** (expansión isentrópica a $10\,\mathrm{kPa}$, $s_6 = s_5 = 7.2338$):
> A $10\,\mathrm{kPa}$: $s_f = 0.6493$, $s_g = 8.1502$. Mezcla:
> $x_6 = (7.2338 - 0.6493)/7.5009 = 6.5845/7.5009 = 0.878$.
> $h_6 = 191.8 + 0.878\times2392.8 = 191.8 + 2100.9 = 2292.7\,\mathrm{kJ/kg}$.
>
> **(b) Eficiencia:**
> $w_T = (3310.8-2832.6)+(3456.5-2292.7) = 478.2+1163.8 = 1642.0\,\mathrm{kJ/kg}$.
> $w_P = 15.14\,\mathrm{kJ/kg}$.
> $q_H = (3310.8-206.9)+(3456.5-2832.6) = 3103.9+623.9 = 3727.8\,\mathrm{kJ/kg}$.
> $$\eta_{\rm th} = \frac{1642.0-15.14}{3727.8} = \frac{1626.9}{3727.8} = 0.436 = 43.6\%.$$
>
> **(c) Comparación:** Sin recalentamiento (a $15\,\mathrm{MPa}$, $500°\mathrm{C}$, condenser a $10\,\mathrm{kPa}$):
> $s_3 = 6.3480$, $x_{4,\rm sin} = (6.3480-0.6493)/7.5009 = 5.6987/7.5009 = 0.760$.
>
> | Parámetro | Sin recalentamiento | Con recalentamiento |
> |:---:|:---:|:---:|
> | $\eta_{\rm th}$ | $\approx 38\%$ | $43.6\%$ |
> | $x_4$ o $x_6$ | $0.760$ ❌ (muy húmedo) | $0.878$ ✓ |
>
> $\boxed{\eta_{\rm th} = 43.6\%,\quad x_6 = 0.878.}$ $\blacksquare$

> [!referencia]
> Borgnakke & Sonntag, §11.3; Çengel & Boles, §10-5; Moran & Shapiro, §8.4.
