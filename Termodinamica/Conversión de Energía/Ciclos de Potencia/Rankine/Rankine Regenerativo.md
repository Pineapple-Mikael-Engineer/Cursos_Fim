---
title: "Rankine Regenerativo"
order: 3
tags:
  - termodinamica
  - ciclos
  - rankine
  - regeneracion
  - feedwater-heater
draft: false
aliases:
  - Rankine Regenerativo
  - Regenerative Rankine
  - ciclo con extracción
  - calentador abierto de alimentación
---

# Rankine Regenerativo $\eta_{\rm th} > \eta_{\rm Rankine simple}$

> [!definicion]
> El **ciclo Rankine regenerativo** extrae una fracción del vapor de la turbina —antes de que se expanda completamente— y lo usa para **precalentar el condensado** antes de entrar a la caldera. Esto eleva la temperatura media a la que se añade calor ($T_{m,\rm entrada}$), acercando el ciclo al límite de Carnot. El dispositivo donde se mezclan el vapor extraído y el condensado se llama **calentador abierto de alimentación** (CAA) o *open feedwater heater*.
>
> *Intuición física:* en el ciclo simple, el agua fría del condensador (~45°C) entra directamente a la caldera y debe calentarse desde baja temperatura — ese proceso es ineficiente porque absorbe calor a temperatura baja. Si el vapor extraído cede su calor al condensado, se recupera energía que de otro modo se perdería en el condensador.

![[rankine_regenerativo_esquema.svg|500]]
*Ciclo Rankine regenerativo con un calentador abierto. Una fracción $y$ del vapor se extrae de la turbina al nivel de presión intermedia $P_e$; el resto $(1-y)$ se expande hasta $P_L$. Las dos corrientes se mezclan en el CAA, cuya salida (estado 3) es líquido saturado a $P_e$.*

---

## Nomenclatura de estados

| Estado | Descripción |
|:---:|:---|
| 1 | Líquido saturado a $P_L$ (salida condensador) |
| 2 | Líquido comprimido a $P_e$ (salida bomba 1) |
| 3 | Líquido saturado a $P_e$ (salida CAA) |
| 4 | Líquido comprimido a $P_H$ (salida bomba 2) |
| 5 | Vapor sobrecalentado a $P_H$, $T_5$ (entrada turbina) |
| $e$ | Vapor extraído a $P_e$ (fracción $y$) |
| 6 | Vapor expandido a $P_L$ (fracción $1-y$, entrada condensador) |

---

## Balance del calentador abierto (determina $y$)

> [!proposicion]
> El CAA opera en régimen estacionario, sin calor ni trabajo al exterior, mezclando el vapor extraído ($\dot{m}_e = y\dot{m}$) con el condensado ($\dot{m}_1 = (1-y)\dot{m}$) para producir líquido saturado ($\dot{m}_3 = \dot{m}$):
>
> **Balance de masa:** $y + (1-y) = 1$ ✓.
>
> **Balance de energía** (primera ley, adiabático, sin trabajo):
> $$
> y\,h_e + (1-y)\,h_2 = 1\cdot h_3 \implies \boxed{y = \frac{h_3 - h_2}{h_e - h_2}}.
> $$

> [!demostracion]
> **Hipótesis:** VC estacionario, adiabático ($\dot{Q}=0$), sin trabajo de eje ($\dot{W}=0$), despreciable EC y EP. Base: $\dot{m} = 1\,\mathrm{kg/s}$ de vapor a la entrada de la turbina.
>
> **Paso 1.** Flujos másicos: el vapor entra a la turbina a razón $1\,\mathrm{kg/s}$; al estado $e$, una fracción $y$ se desvía al CAA, dejando $(1-y)$ para seguir expandiéndose hasta $P_L$.
>
> **Paso 2.** Balance de energía sobre el CAA:
> $$
> \text{Entalpía entrante} = \text{Entalpía saliente}
> $$
> $$
> y\,h_e + (1-y)\,h_2 = h_3.
> $$
>
> **Paso 3.** Despejar $y$:
> $$
> y\,h_e - y\,h_2 = h_3 - h_2 \implies y(h_e - h_2) = h_3 - h_2 \implies y = \frac{h_3 - h_2}{h_e - h_2}. \qquad \blacksquare
> $$
>
> *Interpretación:* $y$ es la fracción de calor "recobrado" del vapor de extracción respecto al salto total $h_e - h_2$. Si el vapor extraído tiene la misma entalpía que el condensado ($h_e = h_2$), no hay extracción ($y=0$); si el vapor cede todo su calor hasta $h_3$, se obtiene la fracción máxima.

---

## Eficiencia y calores del ciclo regenerativo

> [!proposicion]
> Con base en 1 kg de vapor en la turbina:
>
> **Trabajo de turbina** (en dos etapas):
> $$
> w_T = (h_5 - h_e) + (1-y)(h_e - h_6).
> $$
>
> **Trabajo de bombas:** $w_{P1} = (1-y)(h_2 - h_1) = (1-y)v_1(P_e - P_L)$ (bomba 1: eleva de $P_L$ a $P_e$). $w_{P2} = h_4 - h_3 = v_3(P_H - P_e)$ (bomba 2: eleva de $P_e$ a $P_H$).
>
> **Calor de entrada** (solo a la caldera; el CAA no intercambia con el exterior):
> $$
> q_H = h_5 - h_4.
> $$
>
> **Eficiencia:**
> $$
> \eta_{\rm th} = \frac{w_T - w_{P1} - w_{P2}}{q_H}.
> $$
>
> El calor rechazado al condensador es solo por la fracción $(1-y)$: $q_L = (1-y)(h_6 - h_1)$.

---

## Ejemplo: Rankine regenerativo con un CAA

> [!ejemplo]
> Ciclo Rankine regenerativo ideal:
> - Turbina: entrada a $P_H = 10\,\mathrm{MPa}$, $T_5 = 500°\mathrm{C}$.
> - Extracción a $P_e = 1\,\mathrm{MPa}$ para el CAA.
> - Condensador: $P_L = 10\,\mathrm{kPa}$.
>
> Determinar: (a) fracción extraída $y$; (b) $\eta_{\rm th}$; (c) comparar con ciclo simple a las mismas condiciones.

> [!solucion]
> **Estado 1** ($10\,\mathrm{kPa}$, líquido saturado): $h_1 = 191.8\,\mathrm{kJ/kg}$, $v_1 = 0.001010\,\mathrm{m^3/kg}$.
>
> **Estado 2** ($P_e = 1000\,\mathrm{kPa}$, bomba 1 isentrópica): $h_2 = 191.8 + 0.001010\times(1000-10) = 191.8 + 1.00 = 192.8\,\mathrm{kJ/kg}$.
>
> **Estado 3** ($1\,\mathrm{MPa}$, líquido saturado — salida CAA): $h_3 = h_f(1\,\mathrm{MPa}) = 762.8\,\mathrm{kJ/kg}$, $v_3 = 0.001127\,\mathrm{m^3/kg}$.
>
> **Estado 4** ($10\,\mathrm{MPa}$, bomba 2 isentrópica): $h_4 = 762.8 + 0.001127\times(10000-1000) = 762.8 + 10.14 = 772.9\,\mathrm{kJ/kg}$.
>
> **Estado 5** ($10\,\mathrm{MPa}$, $500°\mathrm{C}$): $h_5 = 3373.7\,\mathrm{kJ/kg}$, $s_5 = 6.5966\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado $e$** (extracción isentrópica a $P_e = 1\,\mathrm{MPa}$, $s_e = s_5 = 6.5966$): A $1\,\mathrm{MPa}$: $s_g = 6.5865$. $s_e = 6.5966 > s_g$ → vapor levemente sobrecalentado. A $1\,\mathrm{MPa}$, $180°\mathrm{C}$: $s = 6.3794$, $h = 2778.1$; a $200°\mathrm{C}$: $s = 6.6940$, $h = 2827.9$. Interpolando: $h_e = 2778.1 + (6.5966-6.3794)/(6.6940-6.3794)\times(2827.9-2778.1) = 2778.1 + 0.6902\times49.8 = 2778.1 + 34.4 = 2812.5\,\mathrm{kJ/kg}$.
>
> **Estado 6** (expansión isentrópica a $P_L = 10\,\mathrm{kPa}$, $s_6 = s_5 = 6.5966$): $x_6 = (6.5966-0.6493)/7.5009 = 5.9473/7.5009 = 0.793$. $h_6 = 191.8 + 0.793\times2392.8 = 191.8 + 1897.5 = 2089.3\,\mathrm{kJ/kg}$.
>
> **(a) Fracción extraída $y$:**
> $$y = \frac{h_3 - h_2}{h_e - h_2} = \frac{762.8 - 192.8}{2812.5 - 192.8} = \frac{570.0}{2619.7} = 0.2176.$$
>
> **(b) Eficiencia:** $w_T = (3373.7-2812.5) + (1-0.2176)(2812.5-2089.3) = 561.2 + 0.7824\times723.2 = 561.2 + 565.8 = 1127.0\,\mathrm{kJ/kg}$. $w_{P1} = (1-0.2176)\times1.00 = 0.782\,\mathrm{kJ/kg}$. $w_{P2} = 10.14\,\mathrm{kJ/kg}$. $w_{\rm neto} = 1127.0 - 0.782 - 10.14 = 1116.1\,\mathrm{kJ/kg}$. $q_H = h_5 - h_4 = 3373.7 - 772.9 = 2600.8\,\mathrm{kJ/kg}$.
> $$\eta_{\rm th} = \frac{1116.1}{2600.8} = 0.429 = 42.9\%.$$
>
> **(c) Ciclo simple a las mismas condiciones** ($10\,\mathrm{MPa}$, $500°\mathrm{C}$, $10\,\mathrm{kPa}$): $w_T = h_5 - h_6 = 3373.7 - 2089.3 = 1284.4\,\mathrm{kJ/kg}$ (más trabajo, pero...). $q_H = h_5 - h_2' = 3373.7 - 201.9 = 3171.8\,\mathrm{kJ/kg}$ (también más calor). $\eta_{\rm th,simple} = (1284.4-10.14)/3171.8 = 1274.3/3171.8 = 0.402 = 40.2\%$.
>
> | Parámetro | Simple | Regenerativo |
> |:---:|:---:|:---:|
> | $\eta_{\rm th}$ | $40.2\%$ | $42.9\%$ |
> | $q_H$ [kJ/kg] | $3171.8$ | $2600.8$ |
> | $w_{\rm neto}$ [kJ/kg] | $1274.3$ | $1116.1$ |
>
> La regeneración aumenta $\eta_{\rm th}$ en $+2.7\%$ reduciendo el calor de entrada (mejor aprovechamiento). El costo: menor trabajo neto por kg → se necesita mayor $\dot{m}$ para la misma potencia.
>
> $\boxed{\eta_{\rm th} = 42.9\%,\quad y = 0.218.}$ $\blacksquare$

> [!info]
> Las plantas modernas tienen **hasta 8 calentadores** de alimentación (abiertos y cerrados) que juntos elevan $\eta_{\rm th}$ en 10–15% sobre el Rankine simple. El análisis de múltiples extracciones sigue el mismo principio: balance de masa y energía en cada CAA.

> [!referencia]
> Borgnakke & Sonntag, §11.4; Çengel & Boles, §10-6; Moran & Shapiro, §8.5.
