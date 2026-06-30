---
title: Torres de Enfriamiento
order: 3
tags:
  - termodinamica
  - psicrometria
  - torres-enfriamiento
  - transferencia-calor
draft: false
aliases:
  - Torres de Enfriamiento
  - Cooling Tower
  - Torre de Enfriamiento
---

# Torres de Enfriamiento

> [!definicion]
> Una **torre de enfriamiento** es un dispositivo de **contacto directo** aire–agua: el agua caliente se enfría al ponerse en contacto con una corriente de aire, evaporándose parcialmente. A diferencia de un intercambiador de calor convencional (donde los fluidos no se mezclan), aquí el vapor de agua **pasa del agua al aire** — el proceso es simultáneamente transferencia de calor y de masa.
>
> *¿Por qué es eficiente?* El mecanismo de enfriamiento no es solo convección sensible (el aire absorbe calor) sino principalmente **evaporación**: cada kg de agua que se evapora lleva consigo $\approx 2400\,\mathrm{kJ}$ de calor latente, lo que produce un enfriamiento mucho más intenso que el intercambio sensible. El **límite termodinámico** del enfriamiento es la temperatura de bulbo húmedo del aire entrante $T_{bh,1}$: nunca se puede enfriar el agua por debajo de $T_{bh,1}$, incluso con una torre de altura infinita.
>
> *Aplicación principal:* rechazar el calor del condensador en plantas de potencia (ciclo Rankine) y sistemas de refrigeración industrial, donde se necesita enfriar grandes caudales de agua de forma económica.

![[torre_enfriamiento_esquema.svg|420]]
*Esquema de torre de enfriamiento. El agua caliente ($\dot{m}_3$, $T_3$) cae desde arriba; el aire húmedo frío ($\dot{m}_a$, $T_1$, $\omega_1$) asciende. El agua fría ($\dot{m}_4$, $T_4$) se recoge abajo. La diferencia $\dot{m}_3 - \dot{m}_4$ es el agua evaporada, repuesta por agua de maquillaje.*

---

## Parámetros de rendimiento

> [!proposicion]
> Dos parámetros caracterizan el rendimiento de la torre:
>
> **Rango** = diferencia de temperatura del agua:
> $$\text{Rango} = T_3 - T_4 \quad [°\mathrm{C}].$$
>
> **Aproximación** = distancia al límite termodinámico:
> $$\text{Aproximación} = T_4 - T_{bh,1} \quad [°\mathrm{C}].$$
>
> Una aproximación de 5°C es excelente (torre eficiente); valores > 10°C indican torre subóptima. El costo de reducir la aproximación crece rápidamente porque la fuerza impulsora de transferencia de masa es proporcional a $(T_4 - T_{bh,1})$.

---

## Balances de masa y energía

> [!proposicion]
> Sistema: volumen de control que incluye toda la torre, en régimen estacionario.
>
> **Balance de masa de aire seco** (el aire seco no cambia de fase):
> $$\dot{m}_a = \text{cte}.$$
>
> **Balance de masa de agua** (parte del agua líquida se evapora y pasa al aire):
> $$\dot{m}_4 = \dot{m}_3 - \dot{m}_a(\omega_2 - \omega_1).$$
>
> **Agua de maquillaje** (para reponer el agua evaporada y mantener el nivel del estanque):
> $$\boxed{\dot{m}_{\rm maq} = \dot{m}_a(\omega_2 - \omega_1)}.$$
>
> **Razón de flujos** (del balance de energía):
> $$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(h_{a2}-h_{a1}) - (\omega_2-\omega_1)\,h_f(T_4)}{h_f(T_3) - h_f(T_4)}.$$

> [!demostracion]
> **Hipótesis:** VC estacionario, adiabático al exterior ($\dot{Q}=0$, sin intercambio de calor con el ambiente), sin trabajo de eje, sin cambios de EC ni EP.
>
> **Paso 1 — Balance de masa de agua (líquida + vapor).** Entra: $\dot{m}_3$ (agua líquida) $+ \dot{m}_a\,\omega_1$ (vapor en el aire). Sale: $\dot{m}_4$ (agua líquida) $+ \dot{m}_a\,\omega_2$ (vapor en el aire que sale). Igualando:
> $$\dot{m}_3 + \dot{m}_a\,\omega_1 = \dot{m}_4 + \dot{m}_a\,\omega_2 \implies \dot{m}_4 = \dot{m}_3 - \dot{m}_a(\omega_2-\omega_1).$$
>
> **Paso 2 — Balance de energía.** Primera ley del VC ($\dot{Q}=0$, $\dot{W}=0$):
> $$\dot{m}_a\,h_{a1} + \dot{m}_3\,h_f(T_3) = \dot{m}_a\,h_{a2} + \dot{m}_4\,h_f(T_4).$$
>
> **Paso 3 — Sustituir $\dot{m}_4$:**
> $$\dot{m}_a\,h_{a1} + \dot{m}_3\,h_f(T_3) = \dot{m}_a\,h_{a2} + [\dot{m}_3 - \dot{m}_a(\omega_2-\omega_1)]\,h_f(T_4).$$
>
> **Paso 4 — Reorganizar para aislar $\dot{m}_3$:**
> $$\dot{m}_3[h_f(T_3)-h_f(T_4)] = \dot{m}_a[(h_{a2}-h_{a1}) - (\omega_2-\omega_1)\,h_f(T_4)].$$
>
> **Paso 5 — Despejar la razón de flujos:**
> $$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(h_{a2}-h_{a1}) - (\omega_2-\omega_1)\,h_f(T_4)}{h_f(T_3)-h_f(T_4)}. \qquad \blacksquare$$
>
> *Interpretación del numerador:* $(h_{a2}-h_{a1})$ es el calor que absorbió el aire (latente + sensible); el término $(\omega_2-\omega_1)h_f(T_4)$ es la entalpía del agua que pasó del líquido al vapor y ya no está en el agua de salida (corrección menor).

---

## Ejemplo: torre de enfriamiento de una central térmica

> [!ejemplo]
> Una planta de potencia rechaza $\dot{Q}_{\rm cond} = 120\,\mathrm{MW}$ en su condensador. El agua de enfriamiento entra a la torre a $T_3=40\,°\mathrm{C}$ y sale a $T_4=24\,°\mathrm{C}$. El aire ambiente entra a $T_1=20\,°\mathrm{C}$, $\phi_1=40\%$, y sale saturado a $T_2=34\,°\mathrm{C}$, $\phi_2=100\%$. $P=101.325\,\mathrm{kPa}$.
>
> Determinar: (a) flujo de agua caliente $\dot{m}_3$; (b) flujo de aire seco $\dot{m}_a$; (c) agua de maquillaje $\dot{m}_{\rm maq}$; (d) aproximación de la torre.

> [!solucion]
> **Tablas de agua y saturación:** $P_{\rm sat}(20) = 2.338\,\mathrm{kPa}$; $P_{\rm sat}(34) = 5.325\,\mathrm{kPa}$. $h_f(24) \approx 100.6\,\mathrm{kJ/kg}$; $h_f(40) = 167.5\,\mathrm{kJ/kg}$.
>
> **Estado 1 del aire** ($T_1=20\,°\mathrm{C}$, $\phi_1=40\%$): $P_{v,1} = 0.40\times2.338 = 0.935\,\mathrm{kPa}$. $\omega_1 = 0.622\times0.935/(101.325-0.935) = 0.622\times0.935/100.39 = 0.005797\,\mathrm{kg/kg}$. $h_{a1} = (1.005+1.86\times0.005797)\times20+2501\times0.005797 = 1.01579\times20+14.498 = 20.32+14.50 = 34.82\,\mathrm{kJ/kg}$.
>
> **Estado 2 del aire** ($T_2=34\,°\mathrm{C}$, $\phi_2=100\%$): $P_{v,2} = P_{\rm sat}(34) = 5.325\,\mathrm{kPa}$. $\omega_2 = 0.622\times5.325/(101.325-5.325) = 0.622\times5.325/96.00 = 0.03449\,\mathrm{kg/kg}$. $h_{a2} = (1.005+1.86\times0.03449)\times34+2501\times0.03449 = 1.06915\times34+86.23 = 36.35+86.23 = 122.6\,\mathrm{kJ/kg}$.
>
> **(a) Flujo de agua caliente.** El condensador aporta $\dot{Q}_{\rm cond}$ al agua que circula:
> $$\dot{m}_3 = \frac{\dot{Q}_{\rm cond}}{h_f(T_3)-h_f(T_4)} = \frac{120\times10^3\,\mathrm{kW}}{167.5-100.6} = \frac{120000}{66.9} = 1793\,\mathrm{kg/s}.$$
>
> **(b) Flujo de aire seco.** De la razón de flujos:
> $$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(122.6-34.82)-(0.03449-0.005797)\times100.6}{66.9} = \frac{87.78-0.02870\times100.6}{66.9} = \frac{87.78-2.887}{66.9} = \frac{84.89}{66.9} = 1.269.$$
> $$\dot{m}_a = 1793/1.269 = 1413\,\mathrm{kg\,a.s./s}.$$
>
> **(c) Agua de maquillaje:**
> $$\dot{m}_{\rm maq} = 1413\times(0.03449-0.005797) = 1413\times0.02869 = 40.5\,\mathrm{kg/s} = 146\,\mathrm{t/h}.$$
> Es el 2.26% del caudal total de agua — pérdida que se repone continuamente.
>
> **(d) Aproximación.** Con $T_1=20\,°\mathrm{C}$, $\phi_1=40\%$: de carta psicrométrica, $T_{bh,1} \approx 13.4\,°\mathrm{C}$.
> $$\text{Aproximación} = T_4 - T_{bh,1} = 24 - 13.4 = 10.6\,°\mathrm{C}.$$
> Una torre de alto rendimiento lograría 5°C; $10.6$°C indica diseño convencional.
>
> $\boxed{\dot{m}_3 = 1793\,\mathrm{kg/s},\quad \dot{m}_a = 1413\,\mathrm{kg/s},\quad \dot{m}_{\rm maq} = 146\,\mathrm{t/h}.}$ $\blacksquare$

> [!referencia]
> Çengel & Boles, §14-8; Moran & Shapiro, §12.7; Borgnakke & Sonntag, §12.6.
