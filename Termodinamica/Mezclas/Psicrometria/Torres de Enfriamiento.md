---
title: Torres de Enfriamiento
tags:
  - termodinamica
  - teoria
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
> Una **torre de enfriamiento** es un dispositivo de contacto directo aire–agua en el que agua caliente se enfría mediante evaporación parcial al ponerse en contacto con una corriente de aire. A diferencia de un intercambiador convencional, los fluidos **se mezclan**: el vapor de agua evaporado pasa al aire. El proceso es simultáneamente transferencia de masa y de energía. Son el método estándar para rechazar el calor del condensador en plantas de potencia (ciclo Rankine) y en sistemas de refrigeración industriales.

> [!info]
> **Contexto.** La torre de enfriamiento es el enlace entre la [[../index | sección de Mezclas]] y los [[../../Conservacion/Volumenes de Control/Balance de Energia VC | balances de volumen de control]]: aplica simultáneamente balance de masa de agua, balance de masa de aire seco y balance de energía, todo sobre aire húmedo. El ejemplo canónico de análisis psicrométrico en ingeniería.

---

## Esquema y variables

El agua caliente entra por la parte superior ($\dot{m}_3$, $T_3$) y gotea contra una corriente de aire húmedo que asciende. El aire entra frío y húmedo por abajo (estado 1: $\dot{m}_{a}$, $T_1$, $\omega_1$) y sale caliente y más húmedo por arriba (estado 2: $T_2$, $\omega_2\ge\omega_1$). El agua fría sale por el fondo ($\dot{m}_4$, $T_4$).

Una fracción del agua se **evapora**: la masa de agua líquida que sale es menor que la que entra. Esta pérdida se repone con **agua de maquillaje** ($\dot{m}_{\rm maq}$).

![[torre_enfriamiento_esquema.svg|420]]
*Esquema de una torre de enfriamiento de tiro natural. El agua caliente (3) cae en gotas; el aire húmedo (1) asciende por convección natural o forzada; el agua fría (4) se recoge en el estanque inferior. La diferencia $m_3-m_4$ es el agua evaporada, repuesta por el agua de maquillaje.*

**Parámetros de rendimiento:**
$$\text{Rango} = T_3-T_4 \qquad [\text{enfriamiento de la torre}]$$
$$\text{Aproximación} = T_4-T_{bh,1} \qquad [\text{distancia al límite termodinámico}]$$

El límite inferior de $T_4$ es $T_{bh,1}$ (temperatura de bulbo húmedo del aire entrante), alcanzado solo en una torre ideal con área de contacto infinita.

---

## Balances de masa y energía

Sistema: volumen de control que incluye la torre completa, en **régimen estacionario**.

**Balance de masa de aire seco** (el aire seco no cambia de fase):
$$\dot{m}_a = \text{cte} \quad\text{(kg a.s./s, conservado)}.$$

**Balance de masa de agua total:**
$$\dot{m}_3 + \dot{m}_a\,\omega_1 + \dot{m}_{\rm maq} = \dot{m}_4 + \dot{m}_a\,\omega_2.$$

Si la torre es adiabática al exterior y no se añade agua de maquillaje durante el análisis estacionario, el balance de vapor de agua es:
$$\dot{m}_4 = \dot{m}_3 - \dot{m}_a(\omega_2-\omega_1).$$

**Agua de maquillaje** (para reponer el agua evaporada):
$$\boxed{\dot{m}_{\rm maq} = \dot{m}_a(\omega_2-\omega_1).}$$

**Balance de energía** (adiabático al exterior, $\dot{W}=0$):
$$\dot{m}_a\,h_{a1} + \dot{m}_3\,h_3 = \dot{m}_a\,h_{a2} + \dot{m}_4\,h_4$$

donde $h_{a}=h_{\rm aire+vapor}$ es la entalpía del aire húmedo por kg de aire seco, y $h_3$, $h_4$ son entalpías del agua líquida (≈ $h_f(T)$ desde tablas).

Sustituyendo $\dot{m}_4 = \dot{m}_3 - \dot{m}_a(\omega_2-\omega_1)$:
$$\dot{m}_a(h_{a2}-h_{a1}) = \dot{m}_3\,h_3 - \dot{m}_4\,h_4 = \dot{m}_3\,h_3 - [\dot{m}_3-\dot{m}_a(\omega_2-\omega_1)]\,h_4$$
$$\dot{m}_a(h_{a2}-h_{a1}) = \dot{m}_3(h_3-h_4) + \dot{m}_a(\omega_2-\omega_1)h_4.$$

Despejando la razón de flujo $\dot{m}_3/\dot{m}_a$:

> [!proposicion] Razón de flujos en la torre de enfriamiento
> $$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(h_{a2}-h_{a1})-(\omega_2-\omega_1)h_4}{h_3-h_4}.$$

> [!demostracion]
> Del balance de energía:
> $$\dot{m}_a(h_{a2}-h_{a1}) = \dot{m}_3(h_3-h_4) + \dot{m}_a(\omega_2-\omega_1)h_4.$$
> Despejando:
> $$\dot{m}_3(h_3-h_4) = \dot{m}_a[(h_{a2}-h_{a1})-(\omega_2-\omega_1)h_4].$$
> $$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(h_{a2}-h_{a1})-(\omega_2-\omega_1)h_4}{h_3-h_4}. \qquad \blacksquare$$

---

## Ejemplo: torre de enfriamiento para condensador de planta de potencia

> [!ejemplo]
> Una planta de potencia de 50 MW rechaza calor en su condensador a razón de $\dot{Q}_{\rm cond}=120\,\mathrm{MW}$. Este calor lo absorbe el agua de enfriamiento que circula por la torre. El agua caliente entra a la torre a $T_3=40\,°\mathrm{C}$ y debe salir a $T_4=24\,°\mathrm{C}$ (rango $= 16\,°\mathrm{C}$). El aire ambiente entra a $T_1=20\,°\mathrm{C}$, $\phi_1=40\%$, y sale saturado a $T_2=34\,°\mathrm{C}$, $\phi_2=100\%$. $P=101.325\,\mathrm{kPa}$.
>
> Determinar: (a) el flujo de agua caliente $\dot{m}_3$, (b) el flujo de aire seco $\dot{m}_a$, (c) el flujo de agua de maquillaje $\dot{m}_{\rm maq}$, (d) la aproximación de la torre.

> [!solucion]
> **Datos de tablas de saturación:**
>
> $P_{\rm sat}(20\,°\mathrm{C})=2.338\,\mathrm{kPa}$; $P_{\rm sat}(34\,°\mathrm{C})=5.325\,\mathrm{kPa}$.
> $h_f(24\,°\mathrm{C})\approx100.6\,\mathrm{kJ/kg}$; $h_f(40\,°\mathrm{C})=167.5\,\mathrm{kJ/kg}$.
> $h_{\rm fg}(34\,°\mathrm{C})\approx2422\,\mathrm{kJ/kg}$.
>
> **Estado 1 del aire:** $P_{v,1}=0.40\times2.338=0.935\,\mathrm{kPa}$.
> $$\omega_1=0.622\times\frac{0.935}{101.325-0.935}=0.622\times\frac{0.935}{100.39}=0.005797\,\mathrm{kg/kg\,a.s.}$$
> $$h_{a1}=(1.005+1.86\times0.005797)\times20+2501\times0.005797=(1.005+0.01078)\times20+14.498=1.01578\times20+14.498=20.316+14.498=34.81\,\mathrm{kJ/kg\,a.s.}$$
>
> **Estado 2 del aire:** saturado a $T_2=34\,°\mathrm{C}$; $P_{v,2}=P_{\rm sat}(34)=5.325\,\mathrm{kPa}$.
> $$\omega_2=0.622\times\frac{5.325}{101.325-5.325}=0.622\times\frac{5.325}{96.00}=0.03449\,\mathrm{kg/kg\,a.s.}$$
> $$h_{a2}=(1.005+1.86\times0.03449)\times34+2501\times0.03449=(1.005+0.06415)\times34+86.23=1.06915\times34+86.23=36.351+86.23=122.58\,\mathrm{kJ/kg\,a.s.}$$
>
> **Parte (a) — Flujo de agua caliente.**
> El condensador rechaza $\dot{Q}_{\rm cond}=120\,\mathrm{MW}$ al agua de enfriamiento:
> $$\dot{m}_3=\frac{\dot{Q}_{\rm cond}}{h_3-h_4}=\frac{120\times10^3\,\mathrm{kW}}{h_f(40)-h_f(24)}=\frac{120000}{167.5-100.6}=\frac{120000}{66.9}=1793\,\mathrm{kg/s}.$$
>
> **Parte (b) — Flujo de aire seco.**
> De la razón de flujos:
> $$\frac{\dot{m}_3}{\dot{m}_a}=\frac{(h_{a2}-h_{a1})-(\omega_2-\omega_1)h_4}{h_3-h_4}=\frac{(122.58-34.81)-(0.03449-0.005797)\times100.6}{66.9}$$
> $$=\frac{87.77-0.02870\times100.6}{66.9}=\frac{87.77-2.887}{66.9}=\frac{84.88}{66.9}=1.2688\,\mathrm{kg\,agua/kg\,a.s.}$$
> $$\dot{m}_a=\frac{\dot{m}_3}{1.2688}=\frac{1793}{1.2688}=1413\,\mathrm{kg\,a.s./s}.$$
>
> **Parte (c) — Agua de maquillaje.**
> $$\dot{m}_{\rm maq}=\dot{m}_a(\omega_2-\omega_1)=1413\times(0.03449-0.005797)=1413\times0.02869=40.56\,\mathrm{kg/s}=146\,\mathrm{t/h}.$$
> Esta es el agua que se evapora y debe reponerse continuamente. Representa el $40.56/1793=2.26\%$ del caudal total de agua.
>
> **Parte (d) — Aproximación.**
> Temperatura de bulbo húmedo del aire entrante: con $T_1=20\,°\mathrm{C}$, $\phi_1=40\%$, se tiene $T_{bh,1}\approx13.4\,°\mathrm{C}$ (leído de la carta psicrométrica o calculado iterativamente).
> $$\text{Aproximación}=T_4-T_{bh,1}=24-13.4=10.6\,°\mathrm{C}.$$
> Una aproximación de $10.6\,°\mathrm{C}$ indica una torre de rendimiento razonable; torres bien diseñadas alcanzan $3$–$5\,°\mathrm{C}$. $\blacksquare$

> [!referencia]
> Çengel & Boles, *Termodinámica*, §14-8; Moran & Shapiro §12.7; Borgnakke & Sonntag §12.6. Diseño detallado: Merkel equation, NTU method (Perry's Chemical Engineers' Handbook, sec. 12).
