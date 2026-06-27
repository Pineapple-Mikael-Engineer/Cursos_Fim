---
title: "Ciclo Rankine Simple"
order: 1
tags:
  - termodinamica
  - ciclos
  - rankine
  - vapor
draft: false
aliases:
  - Rankine Simple
  - ciclo Rankine básico
  - ideal Rankine cycle
---

# Ciclo Rankine Simple $\eta_{\rm th} = \dfrac{(h_3-h_4)-(h_2-h_1)}{h_3-h_2}$

> [!definicion]
> El **ciclo Rankine simple** (o ideal) es la versión de cuatro estados del ciclo de vapor, con los cuatro procesos idealizados como isentrópicos (turbina y bomba) e isobáricos (caldera y condensador). No tiene pérdidas internas: las irreversibilidades de los dispositivos reales se modelan con eficiencias isentrópicas $\eta_T$ y $\eta_P$ cuando se pasa al ciclo Rankine real.

---

## Identificación de estados (convención del curso)

| Estado | Descripción | Región |
|:---:|:---|:---|
| 1 | Salida del condensador = entrada de bomba | Líquido saturado ($x=0$, $P_{\rm baja}$) |
| 2 | Salida de bomba = entrada de caldera | Líquido comprimido ($P_{\rm alta}$) |
| 3 | Salida de caldera = entrada de turbina | Vapor sobrecalentado ($P_{\rm alta}$, $T_3$) |
| 4 | Salida de turbina = entrada de condensador | Mezcla o vapor ($P_{\rm baja}$) |

---

## Algoritmo de cálculo

> [!proposicion]
> **Paso 1 — Estado 1** (líquido saturado a $P_L$):
> De tablas de saturación: $h_1 = h_f(P_L)$, $v_1 = v_f(P_L)$, $s_1 = s_f(P_L)$.
>
> **Paso 2 — Estado 2** (salida de bomba isentrópica):
> $$
> h_2 = h_1 + v_1(P_H - P_L).
> $$
>
> **Paso 3 — Estado 3** (vapor sobrecalentado a $P_H$, $T_3$):
> De tablas de vapor sobrecalentado: $h_3$, $s_3$.
>
> **Paso 4 — Estado 4** (expansión isentrópica, $s_4 = s_3$ a $P_L$):
> Comparar $s_3$ con $s_f(P_L)$ y $s_g(P_L)$:
> - Si $s_f < s_3 < s_g$: mezcla húmeda. $x_4 = (s_3 - s_f)/s_{fg}$; $h_4 = h_f + x_4 h_{fg}$.
> - Si $s_3 > s_g$: vapor sobrecalentado. Interpolar en tablas.
>
> **Paso 5 — Eficiencia**:
> $$
> \eta_{\rm th} = \frac{(h_3 - h_4) - (h_2 - h_1)}{h_3 - h_2}.
> $$

---

## Ciclo Rankine real con eficiencias isentrópicas

> [!proposicion]
> Los dispositivos reales son irreversibles. Las eficiencias isentrópicas corrigen los estados 2 y 4:
>
> **Turbina real** (la irreversibilidad hace que $h_4 > h_{4s}$, o sea, genera más entropía):
> $$
> \eta_T = \frac{h_3 - h_{4,\rm real}}{h_3 - h_{4s}} \implies h_{4,\rm real} = h_3 - \eta_T(h_3 - h_{4s}).
> $$
>
> **Bomba real** (necesita más trabajo):
> $$
> \eta_P = \frac{h_{2s} - h_1}{h_{2,\rm real} - h_1} \implies h_{2,\rm real} = h_1 + \frac{v_1(P_H-P_L)}{\eta_P}.
> $$

---

## Ejemplo: planta de vapor de 50 MW

> [!ejemplo]
> Una planta de vapor opera con el ciclo Rankine ideal. Condiciones:
> - Turbina: entrada a $P_3 = 5\,\mathrm{MPa}$, $T_3 = 400°\mathrm{C}$.
> - Condensador: $P_L = 10\,\mathrm{kPa}$.
> - Eficiencia turbina: $\eta_T = 0.88$; eficiencia bomba: $\eta_P = 0.80$.
>
> Determinar: (a) calidades y entalpías en los 4 estados; (b) $\eta_{\rm th}$ del ciclo real; (c) flujo másico $\dot{m}$ para $\dot{W}_{\rm neto} = 50\,\mathrm{MW}$.

> [!solucion]
> **Tablas de vapor (Borgnakke & Sonntag, Apéndices):**
>
> **Estado 1** — Líquido saturado a $P_L = 10\,\mathrm{kPa}$:
> $T_{\rm sat} = 45.8°\mathrm{C}$, $h_1 = h_f = 191.8\,\mathrm{kJ/kg}$, $v_1 = v_f = 0.001010\,\mathrm{m^3/kg}$, $s_1 = s_f = 0.6493\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 2** — Salida de bomba (isentrópica, $P_H = 5000\,\mathrm{kPa}$):
> $h_{2s} = h_1 + v_1(P_H - P_L) = 191.8 + 0.001010\times(5000-10) = 191.8 + 5.04 = 196.8\,\mathrm{kJ/kg}$.
> Real: $h_{2,\rm real} = 191.8 + 5.04/0.80 = 191.8 + 6.30 = 198.1\,\mathrm{kJ/kg}$.
>
> **Estado 3** — Vapor sobrecalentado a $5\,\mathrm{MPa}$, $400°\mathrm{C}$:
> $h_3 = 3196.7\,\mathrm{kJ/kg}$, $s_3 = 6.6459\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 4s** — Expansión isentrópica a $P_L = 10\,\mathrm{kPa}$ ($s_{4s} = s_3 = 6.6459$):
> A $10\,\mathrm{kPa}$: $s_f = 0.6493$, $s_g = 8.1502$, $s_{fg} = 7.5009\,\mathrm{kJ/(kg\cdot K)}$.
> $s_{4s} = 6.6459 > s_f$ y $< s_g$ → mezcla:
> $x_{4s} = (6.6459 - 0.6493)/7.5009 = 5.9966/7.5009 = 0.799$.
> $h_{4s} = h_f + x_{4s}\,h_{fg} = 191.8 + 0.799\times2392.8 = 191.8 + 1911.8 = 2103.6\,\mathrm{kJ/kg}$.
>
> **Estado 4 real** (con $\eta_T = 0.88$):
> $h_{4,\rm real} = h_3 - \eta_T(h_3 - h_{4s}) = 3196.7 - 0.88\times(3196.7-2103.6) = 3196.7 - 0.88\times1093.1 = 3196.7 - 961.9 = 2234.8\,\mathrm{kJ/kg}$.
> $x_{4,\rm real} = (2234.8 - 191.8)/2392.8 = 2043.0/2392.8 = 0.854 > 0.88$? No: $0.854 < 0.88$. La calidad $x_{4} = 0.854$ está por debajo de 0.88 — en diseño real se requeriría recalentamiento.
>
> **(b) Eficiencia térmica real:**
> $w_T = h_3 - h_{4,\rm real} = 3196.7 - 2234.8 = 961.9\,\mathrm{kJ/kg}$.
> $w_P = h_{2,\rm real} - h_1 = 198.1 - 191.8 = 6.3\,\mathrm{kJ/kg}$.
> $w_{\rm neto} = w_T - w_P = 961.9 - 6.3 = 955.6\,\mathrm{kJ/kg}$.
> $q_H = h_3 - h_{2,\rm real} = 3196.7 - 198.1 = 2998.6\,\mathrm{kJ/kg}$.
> $$\eta_{\rm th} = \frac{955.6}{2998.6} = 0.319 = 31.9\%.$$
>
> **(c) Flujo másico para $\dot{W}_{\rm neto} = 50\,\mathrm{MW}$:**
> $$\dot{m} = \frac{\dot{W}_{\rm neto}}{w_{\rm neto}} = \frac{50\times10^3\,\mathrm{kW}}{955.6\,\mathrm{kJ/kg}} = 52.3\,\mathrm{kg/s}.$$
>
> **Verificación:**
> $q_L = h_{4,\rm real} - h_1 = 2234.8 - 191.8 = 2043.0\,\mathrm{kJ/kg}$.
> $\eta_{\rm th} = 1 - q_L/q_H = 1 - 2043.0/2998.6 = 1 - 0.681 = 0.319$ ✓.
>
> $\boxed{\eta_{\rm th} = 31.9\%, \quad \dot{m} = 52.3\,\mathrm{kg/s}.}$ $\blacksquare$

> [!warning]
> La calidad $x_4 = 0.854 < 0.88$ (ASME recomienda $x_{\rm min}=0.88$): hay riesgo de erosión en los últimos álabes de la turbina por impacto de gotitas. La solución es **recalentamiento** — ver [[Rankine con Recalentamiento]].

> [!referencia]
> Borgnakke & Sonntag, §11.1–11.2; Çengel & Boles, §10-2 a 10-3; tablas de vapor: Apéndice B (Borgnakke) o Apéndice A-4 a A-6 (Çengel).
