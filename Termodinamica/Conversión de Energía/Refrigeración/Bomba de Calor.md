---
title: "Bomba de Calor"
order: 2
tags:
  - termodinamica
  - ciclos
  - bomba_de_calor
  - refrigeracion
draft: false
aliases:
  - Bomba de Calor
  - heat pump
  - calefacción por bomba de calor
---

# Bomba de Calor $\text{COP}_{HP} = \text{COP}_R + 1$

> [!definicion]
> Una **bomba de calor** usa el mismo ciclo de compresión de vapor que un refrigerador, pero el objetivo es diferente: en lugar de extraer calor del espacio frío para enfriar, el objetivo es **ceder calor al espacio caliente** para calentarlo. El "espacio frío" puede ser el exterior ($-5°\mathrm{C}$ en invierno), el suelo, o un cuerpo de agua.
>
> *Relación con el refrigerador:* son el mismo ciclo visto desde distintos propósitos. Un **aire acondicionado reversible** (o *heat pump* doméstico) alterna entre los dos modos invirtiendo el flujo del refrigerante:
> - Modo refrigeración: el evaporador está dentro de la habitación (enfría el interior).
> - Modo calefacción: el condensador está dentro de la habitación (calienta el interior).
>
> *Efecto útil:* $q_H$ (calor cedido al espacio caliente).
> $$
> \text{COP}_{HP} = \frac{q_H}{w_C} = \frac{h_2 - h_3}{h_2 - h_1}.
> $$

---

## Relación entre $\text{COP}_R$ y $\text{COP}_{HP}$

> [!teorema]
> Para cualquier ciclo de compresión de vapor:
> $$
> \boxed{\text{COP}_{HP} = \text{COP}_R + 1}.
> $$

> [!demostracion]
> **Hipótesis:** sistema estacionario, primera ley del ciclo.
>
> **Paso 1 — Primera ley del ciclo completo:**
> $$
> q_H = q_L + w_C.
> $$
>
> **Paso 2 — Dividir entre $w_C$:**
> $$
> \frac{q_H}{w_C} = \frac{q_L}{w_C} + 1.
> $$
>
> **Paso 3 — Identificar COPs:**
> $$
> \text{COP}_{HP} = \text{COP}_R + 1. \qquad \blacksquare
> $$
>
> *Interpretación:* el $+1$ proviene del trabajo de entrada que también se convierte en calor cedido. La bomba de calor entrega al espacio caliente tanto el calor tomado del exterior ($q_L$) como la energía del compresor ($w_C$) — ambos terminan en el condensador.

---

## Comparación con calefacción eléctrica por resistencia

> [!teoria]
> Una **resistencia eléctrica** convierte 1 kW eléctrico en exactamente 1 kW de calor ($\text{COP}_{resistencia} = 1$). Una bomba de calor con $\text{COP}_{HP} = 3$ entrega 3 kW de calor por cada 1 kW eléctrico.
>
> La bomba de calor es siempre más eficiente que la resistencia siempre que $\text{COP}_{HP} > 1$, lo cual es cierto para cualquier ciclo real con condición $T_H > T_L$.
>
> **Condición de ventaja sobre la resistencia:**
> $$
> \text{COP}_{HP} > 1 \iff q_H > w_C \iff q_L > 0.
> $$
>
> Esto siempre se cumple mientras la fuente fría esté a temperatura mayor que el cero absoluto. En la práctica, el $\text{COP}_{HP}$ cae cuando la diferencia $T_H - T_L$ es grande (interior muy caliente o exterior muy frío). Cuando $T_{\rm exterior} < -15°\mathrm{C}$, muchas bombas de calor tienen un COP cercano a 1–1.5 y se combinan con resistencia de apoyo.

---

## Límite de Carnot para la bomba de calor

> [!proposicion]
> El **COP máximo** de Carnot para una bomba de calor entre temperaturas absolutas $T_L$ y $T_H$:
> $$
> \text{COP}_{HP,\rm Carnot} = \frac{T_H}{T_H - T_L}.
> $$
>
> Para $T_H = 295\,\mathrm{K}$ (22°C, interior) y $T_L = 273\,\mathrm{K}$ (0°C, exterior):
> $$
> \text{COP}_{HP,\rm Carnot} = \frac{295}{295-273} = \frac{295}{22} = 13.4.
> $$
>
> Los equipos reales alcanzan $\text{COP}_{HP} \approx 3{-}5$ en condiciones nominales (diferencia moderada de temperatura), muy por encima de la resistencia ($\text{COP}=1$) pero lejos del límite de Carnot.

---

## Ejemplo: bomba de calor residencial

> [!ejemplo]
> Una bomba de calor usa R-134a para calentar una habitación a $T_H = 24°\mathrm{C}$ tomando calor del exterior a $T_L = 2°\mathrm{C}$.
>
> - Estado 1 (entrada compresor): vapor saturado a $T_L' = -5°\mathrm{C}$ (evaporador a temperatura menor que la del exterior para que haya transferencia de calor).
> - Estado 3 (entrada válvula): líquido saturado a $T_H' = 32°\mathrm{C}$ (condensador a temperatura mayor que la del interior).
> - Compresor ideal: $s_2 = s_1$.
> - Potencia del compresor: $\dot{W}_C = 2.5\,\mathrm{kW}$.
>
> Determinar: (a) COP de la bomba de calor; (b) calor cedido a la habitación $\dot{Q}_H$; (c) comparar con resistencia eléctrica de igual potencia; (d) comparar con el límite de Carnot.

> [!solucion]
> **Propiedades del R-134a:**
>
> **Estado 1** — vapor saturado a $-5°\mathrm{C}$: $h_1 = h_g(-5°\mathrm{C}) = 396.43\,\mathrm{kJ/kg}$, $s_1 = s_g(-5°\mathrm{C}) = 1.7281\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 3** — líquido saturado a $32°\mathrm{C}$: $h_3 = h_f(32°\mathrm{C}) = 237.23\,\mathrm{kJ/kg}$. $P_H = P_{\rm sat}(32°\mathrm{C}) = 770\,\mathrm{kPa}$ (aprox).
>
> **Estado 2** — compresor isentrópico ($s_2 = s_1 = 1.7281$, $P_2 = 770\,\mathrm{kPa}$):
>
> A $770\,\mathrm{kPa}$, interpolando en vapor sobrecalentado de R-134a: A $40°\mathrm{C}$: $s \approx 1.7148$, $h \approx 420.25\,\mathrm{kJ/kg}$. A $50°\mathrm{C}$: $s \approx 1.7461$, $h \approx 431.10\,\mathrm{kJ/kg}$.
>
> Interpolando para $s_2 = 1.7281$: $T_2 \approx 40 + (1.7281-1.7148)/(1.7461-1.7148)\times10 = 40 + 0.425\times10 = 44.25°\mathrm{C}$. $h_2 \approx 420.25 + 0.425\times(431.10-420.25) = 420.25 + 4.61 = 424.86\,\mathrm{kJ/kg}$.
>
> **Trabajo del compresor:** $w_C = h_2 - h_1 = 424.86 - 396.43 = 28.43\,\mathrm{kJ/kg}$.
>
> **Calor cedido en condensador:** $q_H = h_2 - h_3 = 424.86 - 237.23 = 187.63\,\mathrm{kJ/kg}$.
>
> **Calor absorbido del exterior:** $q_L = h_1 - h_4 = h_1 - h_3 = 396.43 - 237.23 = 159.20\,\mathrm{kJ/kg}$.
>
> **(a) COP de la bomba de calor:**
> $$\text{COP}_{HP} = \frac{q_H}{w_C} = \frac{187.63}{28.43} = 6.60.$$
>
> Verificación: $\text{COP}_R = q_L/w_C = 159.20/28.43 = 5.60 = \text{COP}_{HP} - 1 = 6.60-1 = 5.60$ ✓.
>
> **(b) Calor cedido a la habitación:**
> $$\dot{Q}_H = \dot{W}_C \cdot \text{COP}_{HP} = 2.5 \times 6.60 = 16.5\,\mathrm{kW}.$$
>
> Calor tomado del exterior: $\dot{Q}_L = \dot{Q}_H - \dot{W}_C = 16.5 - 2.5 = 14.0\,\mathrm{kW}$ (tomados del aire exterior a 2°C).
>
> **(c) Comparación con resistencia eléctrica:**
>
> Una resistencia de $2.5\,\mathrm{kW}$ entregaría exactamente $2.5\,\mathrm{kW}$ de calor.
>
> La bomba de calor entrega $16.5\,\mathrm{kW}$ — **6.6 veces más** por el mismo consumo eléctrico.
>
> **(d) Comparación con Carnot:**
>
> $\text{COP}_{HP,\rm Carnot} = T_H/(T_H-T_L) = (273.15+24)/(24-2) = 297.15/22 = 13.5$.
>
> Eficiencia relativa: $\text{COP}_{HP}/\text{COP}_{HP,\rm Carnot} = 6.60/13.5 = 48.9\%$.
>
> | Equipo | $\dot{Q}_H$ [kW] | COP |
> |:---|:---:|:---:|
> | Resistencia eléctrica (2.5 kW) | 2.5 | 1.0 |
> | Bomba de calor (este ejemplo) | **16.5** | **6.6** |
> | Límite de Carnot | 33.7 | 13.5 |
>
> $$\boxed{\text{COP}_{HP} = 6.60,\quad \dot{Q}_H = 16.5\,\mathrm{kW}.}$$ $\blacksquare$

> [!info]
> En la práctica, el $\text{COP}_{HP}$ de las bombas de calor aire-aire varía entre 2 y 5 en condiciones reales (temperatura exterior variable, pérdidas mecánicas). Los equipos geotérmicos (fuente fría: suelo a $\approx12°\mathrm{C}$ constante) alcanzan $\text{COP}_{HP} = 4{-}6$ de forma más estable porque la diferencia $T_H - T_L$ es menor y más constante.

> [!referencia]
> Borgnakke & Sonntag, §11.7; Çengel & Boles, §11-3; Moran & Shapiro, §10.2.
